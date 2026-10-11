# ASM Dev 2 — ESGI

## Présentation
Projet réalisé dans le cadre du cours Asm dev 2.

## Membres du groupe
- Alix Mathiot-Bousseliou
- Quentin Sautreuil

## Environnement
- Linux Mint
- NASM
- GCC
- Git

## Organisation
- Sources
- Documentation
- Tests

## Compilation et vérification

Le projet comprend un programme de démonstration permettant d'observer la structure d'un exécutable ELF sous Linux.

### Prérequis

- GCC
- `file`
- `readelf`
- Bash

### Lancer les vérifications

Depuis la racine du dépôt :

```bash
bash tests/verify_elf.sh
```

Le script compile `tests/fixtures/hello.c`, affiche les informations du binaire avec `file` et `readelf`, puis exécute le programme de démonstration.

La sortie attendue du programme est :

```text
Hello ELF
```

### Documentation

Le document `docs/analyse-elf.md` présente les principales caractéristiques ELF observées et explique les différences entre les segments, les sections et les notes GNU.

