# Tests et vérifications

## Objectif

Les tests vérifient le comportement de l'analyseur ELF face à un fichier valide et à différentes entrées incorrectes ou incomplètes. Ils permettent de détecter les régressions lors des modifications du code.

## Prérequis

- Python 3
- GCC
- `file`
- `readelf`
- Bash

## Tests automatisés de l'analyseur

Depuis la racine du dépôt, lancer :

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

La suite couvre notamment :

- l'analyse d'un exécutable ELF valide ;
- un en-tête incomplet ;
- un fichier inexistant ;
- un fichier qui n'est pas au format ELF ;
- un fichier trop court ;
- une table des en-têtes de programme tronquée ;
- une taille d'entrée de programme invalide ;
- une version d'identification ELF invalide.

## Vérification du programme de démonstration

Lancer le script suivant :

```bash
bash tests/verify_elf.sh
```

Ce script compile le programme de démonstration, examine le fichier produit avec `file` et `readelf`, puis exécute le programme.

La sortie attendue du programme de démonstration est :

```text
Hello ELF
```

## Compilation et syntaxe Python

Pour vérifier la syntaxe des fichiers Python :

```bash
python3 -m py_compile src/analyse_elf.py tests/test_analyse_elf.py
```

## Interprétation des résultats

Une suite de tests réussie indique que les comportements couverts par ces tests sont conformes aux attentes. Elle ne garantit pas que toutes les structures ELF possibles sont prises en charge.

Les tests sont à relancer après toute modification de l'analyseur.
