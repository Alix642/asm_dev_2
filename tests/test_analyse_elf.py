import tempfile
import unittest
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


if __name__ == "__main__":
    unittest.main()
