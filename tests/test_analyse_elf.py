import tempfile
import unittest
import struct
from pathlib import Path

from src.analyse_elf import ELFError, analyser_en_tete


RACINE = Path(__file__).resolve().parents[1]
BINAIRE_TEST = RACINE / "tests" / "fixtures" / "hello"


class TestAnalyseELF(unittest.TestCase):

    def test_analyse_binaire_elf(self):
        if not BINAIRE_TEST.exists():
            self.skipTest("Lancer d'abord tests/verify_elf.sh")

        rapport = analyser_en_tete(BINAIRE_TEST)

        self.assertEqual(rapport["classe"], "ELF64")
        self.assertEqual(rapport["encodage"], "Little endian")
        self.assertEqual(rapport["architecture"], "AMD x86-64")
        self.assertEqual(rapport["nombre_entrees_programme"], 13)

    def test_fichier_non_elf(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "texte.txt"
            chemin.write_text("Ceci n'est pas un fichier ELF.")

            with self.assertRaisesRegex(ELFError, "Signature ELF invalide"):
                analyser_en_tete(chemin)

    def test_fichier_trop_court(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "vide"
            chemin.write_bytes(b"\x7fELF")

            with self.assertRaisesRegex(ELFError, "trop court"):
                analyser_en_tete(chemin)

    def test_entete_incomplet(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "incomplet"
            chemin.write_bytes(b"\x7fELF\x02\x01" + b"\x00" * 10)

            with self.assertRaisesRegex(ELFError, "incomplet"):
                analyser_en_tete(chemin)

    def test_fichier_absent(self):
        chemin = Path("/chemin/inexistant/analyse_elf_test")

        with self.assertRaisesRegex(ELFError, "Impossible de lire"):
            analyser_en_tete(chemin)


    def test_version_identification_invalide(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "version_invalide"
            donnees = bytearray(64)
            donnees[:7] = b"\x7fELF\x02\x01\x02"
            chemin.write_bytes(donnees)

            with self.assertRaisesRegex(ELFError, "Version ELF d'identification"):
                analyser_en_tete(chemin)

    def test_table_programme_tronquee(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "table_tronquee"
            donnees = bytearray(64)
            donnees[:7] = b"\x7fELF\x02\x01\x01"

            # En-tête ELF64 minimal, little endian.
            struct.pack_into(
                "<HHIQQQIHHHHHH",
                donnees,
                16,
                2,      # ET_EXEC
                62,     # x86-64
                1,      # Version
                0x400000,
                64,     # Début de la table des programmes
                0,      # Pas de table de sections
                0,
                64,     # Taille de l'en-tête ELF
                56,     # Taille d'une entrée de programme
                1,      # Une entrée annoncée
                0,
                0,
                0,
            )
            chemin.write_bytes(donnees)

            with self.assertRaisesRegex(ELFError, "tronquée"):
                analyser_en_tete(chemin)

    def test_taille_entree_programme_invalide(self):
        with tempfile.TemporaryDirectory() as dossier:
            chemin = Path(dossier) / "entree_invalide"
            donnees = bytearray(120)
            donnees[:7] = b"\x7fELF\x02\x01\x01"

            struct.pack_into(
                "<HHIQQQIHHHHHH",
                donnees,
                16,
                2,      # ET_EXEC
                62,     # x86-64
                1,
                0x400000,
                64,
                0,
                0,
                64,
                1,      # Taille invalide : 1 octet
                1,
                0,
                0,
                0,
            )
            chemin.write_bytes(donnees)

            with self.assertRaisesRegex(ELFError, "trop petite"):
                analyser_en_tete(chemin)



if __name__ == "__main__":
    unittest.main()
