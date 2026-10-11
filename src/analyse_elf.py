#!/usr/bin/env python3

import argparse
import struct
import sys
from pathlib import Path


ELF_MAGIC = b"\x7fELF"

CLASSES = {
    1: "ELF32",
    2: "ELF64",
}

ENCODINGS = {
    1: "Little endian",
    2: "Big endian",
}

FILE_TYPES = {
    0: "ET_NONE (aucun type)",
    1: "ET_REL (objet relogeable)",
    2: "ET_EXEC (exécutable)",
    3: "ET_DYN (objet partagé ou exécutable PIE)",
    4: "ET_CORE (fichier core)",
}

MACHINES = {
    3: "Intel 80386",
    40: "ARM",
    62: "AMD x86-64",
    183: "AArch64",
    243: "RISC-V",
}


class ELFError(Exception):
    """Erreur de lecture ou de validation d'un fichier ELF."""


def analyser_en_tete(chemin: Path) -> dict:
    """Lit et valide l'en-tête ELF sans exécuter le fichier."""

    try:
        with chemin.open("rb") as fichier:
            donnees = fichier.read(64)
    except OSError as erreur:
        raise ELFError(f"Impossible de lire le fichier : {erreur}") from erreur

    if len(donnees) < 16:
        raise ELFError("Fichier trop court pour contenir un en-tête ELF.")

    if donnees[:4] != ELF_MAGIC:
        raise ELFError("Signature ELF invalide.")

    classe = donnees[4]
    encodage = donnees[5]

    if classe not in CLASSES:
        raise ELFError(f"Classe ELF inconnue : {classe}.")

    if encodage not in ENCODINGS:
        raise ELFError(f"Encodage ELF inconnu : {encodage}.")

    taille_entete = 52 if classe == 1 else 64

    if len(donnees) < taille_entete:
        raise ELFError("En-tête ELF incomplet.")

    ordre = "<" if encodage == 1 else ">"

    if classe == 1:
        champs = struct.unpack_from(ordre + "HHIIIIIHHHHHH", donnees, 16)
    else:
        champs = struct.unpack_from(ordre + "HHIQQQIHHHHHH", donnees, 16)

    (
        type_fichier,
        machine,
        _version,
        point_entree,
        _debut_programmes,
        _debut_sections,
        _drapeaux,
        taille_header,
        taille_programme,
        nombre_programmes,
        _taille_section,
        _nombre_sections,
        _index_chaines,
    ) = champs

    if taille_header != taille_entete:
        raise ELFError("Taille d'en-tête incohérente avec la classe ELF.")

    return {
        "chemin": str(chemin),
        "classe": CLASSES[classe],
        "encodage": ENCODINGS[encodage],
        "type": FILE_TYPES.get(type_fichier, f"Inconnu ({type_fichier})"),
        "architecture": MACHINES.get(machine, f"Inconnue ({machine})"),
        "point_entree": point_entree,
        "taille_entete": taille_header,
        "taille_entree_programme": taille_programme,
        "nombre_entrees_programme": nombre_programmes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analyse en lecture seule l'en-tête d'un fichier ELF."
    )
    parser.add_argument("fichier", type=Path, help="Chemin du fichier à analyser")
    arguments = parser.parse_args()

    try:
        rapport = analyser_en_tete(arguments.fichier)
    except ELFError as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 1

    print("=== Rapport d'analyse ELF ===")
    print(f"Fichier : {rapport['chemin']}")
    print(f"Classe : {rapport['classe']}")
    print(f"Encodage : {rapport['encodage']}")
    print(f"Type : {rapport['type']}")
    print(f"Architecture : {rapport['architecture']}")
    print(f"Point d'entrée : 0x{rapport['point_entree']:x}")
    print(f"Taille de l'en-tête : {rapport['taille_entete']} octets")
    print(
        "Taille d'une entrée de programme : "
        f"{rapport['taille_entree_programme']} octets"
    )
    print(
        "Nombre d'entrées de programme : "
        f"{rapport['nombre_entrees_programme']}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
