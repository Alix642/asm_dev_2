# ASM Dev 2 — Analyse du format ELF

## 1. Présentation du projet

Ce projet est réalisé dans le cadre du cours **Asm Dev 2 à l'ESGI**. Il porte sur l'observation et l'analyse structurelle des fichiers exécutables au format ELF (*Executable and Linkable Format*), utilisé notamment sous Linux.

Le dépôt contient un analyseur développé en Python qui examine certains champs de l'en-tête ELF en lecture seule, ainsi qu'un programme de démonstration en C permettant d'observer la structure d'un exécutable Linux.

Les objectifs sont de :
- comprendre les principales informations présentes dans un en-tête ELF ;
- identifier le type de fichier, l'architecture et le point d'entrée ;
- observer les segments et les notes ELF à l'aide des outils système ;
- vérifier le comportement de l'analyseur grâce à des tests automatisés ;
- documenter les résultats et les limites de l'analyse.

## 2. Membres du groupe

- Alix Mathiot-Bousseliou
- Quentin Sautreuil

## 3. Environnement technique

Le projet est développé et testé sous Linux Mint.

| Outil | Utilisation |
|---|---|
| Python 3 | Développement de l'analyseur et tests unitaires |
| GCC | Compilation du programme de démonstration en C |
| `file` | Identification du type de fichier |
| `readelf` | Inspection détaillée des structures ELF |
| Bash | Exécution du script de vérification |
| Git | Gestion des versions du projet |
| NASM | Environnement d'assembleur du cours |

## 4. Organisation du dépôt

```text
asm_dev_2/
├── docs/
│   ├── README.md
│   └── analyse-elf.md
├── src/
│   ├── README.md
│   └── analyse_elf.py
├── tests/
│   ├── README.md
│   ├── fixtures/
│   │   └── hello.c
│   ├── test_analyse_elf.py
│   └── verify_elf.sh
├── .gitignore
└── README.md
```

Le binaire de démonstration `tests/fixtures/hello` est généré par le script de vérification ; il n'est pas nécessaire de le compiler manuellement.

## 5. Utilisation de l'analyseur

Depuis la racine du dépôt, lancer l'analyse d'un fichier ELF :

```bash
python3 src/analyse_elf.py tests/fixtures/hello
```

Pour afficher les options disponibles :

```bash
python3 src/analyse_elf.py --help
```

L'analyseur affiche notamment :
- la classe ELF (ELF32 ou ELF64) ;
- l'encodage des données ;
- le type de fichier ;
- l'architecture cible ;
- le point d'entrée ;
- la taille de l'en-tête ;
- la taille et le nombre d'entrées de la table des en-têtes de programme.

Le fichier analysé doit exister. Pour cette démonstration, le binaire est généré à l'étape de vérification décrite ci-dessous.

## 6. Compilation et vérification

### Prérequis

Installer ou disposer des outils suivants :
- Python 3 ;
- GCC ;
- `file` ;
- `readelf` ;
- Bash.

### Lancer la vérification complète

Depuis la racine du dépôt :

```bash
bash tests/verify_elf.sh
```

Le script compile le programme de démonstration, affiche son type et ses principales structures ELF avec `file` et `readelf`, puis exécute le programme.

La sortie attendue de ce dernier est :

```text
Hello ELF
```

### Exécuter les tests unitaires

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Les tests couvrent l'analyse d'un fichier valide et plusieurs cas d'erreur, dont les fichiers absents, les en-têtes incomplets et les incohérences de certaines structures.

### Vérifier la syntaxe Python

```bash
python3 -m py_compile src/analyse_elf.py tests/test_analyse_elf.py
```

## 7. Documentation complémentaire

- [`docs/analyse-elf.md`](docs/analyse-elf.md) : compte rendu technique de l'analyse ELF, des segments, des sections et des notes GNU.
- [`docs/README.md`](docs/README.md) : index de la documentation technique.
- [`src/README.md`](src/README.md) : fonctionnement et utilisation de l'analyseur.
- [`tests/README.md`](tests/README.md) : procédures de test et interprétation des résultats.

## 8. Limites et précautions d'interprétation

L'analyseur est un outil pédagogique qui examine une partie de la structure ELF. Il ne valide pas l'intégralité du format et ne constitue pas un outil de détection de logiciels malveillants.

Les résultats dépendent du fichier étudié et de son environnement de compilation. Le point d'entrée, le nombre de segments et d'autres valeurs peuvent varier entre deux compilations.

L'analyseur travaille en lecture seule : il ne modifie pas le fichier examiné et ne l'exécute pas. Le script de démonstration, quant à lui, compile et exécute uniquement le programme de test fourni dans ce dépôt.
