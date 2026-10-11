# Documentation technique

## Présentation

Ce répertoire regroupe la documentation technique du projet ASM Dev 2. Il présente le format ELF, les observations réalisées sur un exécutable de démonstration et les limites de l'analyseur développé.

## Documents

### `analyse-elf.md`

Compte rendu de l'analyse d'un exécutable ELF sous Linux. Ce document présente notamment :

- la structure générale d'un fichier ELF ;
- les principales informations de l'en-tête ;
- le rôle des segments, notamment `PT_LOAD`, `PT_INTERP`, `PT_DYNAMIC` et `PT_NOTE` ;
- les notes GNU observées avec `readelf` ;
- les commandes utilisées pour inspecter le binaire ;
- les limites de l'analyse réalisée.

### Documentation du code source

Le fichier [`../src/README.md`](../src/README.md) décrit le fonctionnement, l'utilisation et les limites du module `analyse_elf.py`.

### Documentation des tests

Le fichier [`../tests/README.md`](../tests/README.md) explique comment lancer les tests unitaires et le script de vérification.

## Reproductibilité

Les commandes et observations sont réalisées dans un environnement Linux avec les outils présentés dans les documents. Les valeurs telles que le point d'entrée, le nombre de segments ou l'identifiant de construction peuvent varier selon la compilation et l'environnement.

## Limites

L'analyse porte sur des caractéristiques structurelles du format ELF. Elle ne constitue ni une validation exhaustive du format ni une détection de logiciels malveillants.
