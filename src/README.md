# Module d'analyse ELF

## Rôle

Le module `analyse_elf.py` analyse l'en-tête d'un fichier ELF en lecture seule. Il permet d'identifier les principales caractéristiques du fichier sans l'exécuter ni le modifier.

## Informations analysées

- Classe ELF : ELF32 ou ELF64.
- Encodage : little endian ou big endian.
- Type de fichier ELF.
- Architecture cible.
- Point d'entrée.
- Taille de l'en-tête.
- Taille et nombre d'entrées de la table des en-têtes de programme.

Le module vérifie également plusieurs champs de l'en-tête et détecte certaines incohérences structurelles.

## Utilisation

Depuis la racine du dépôt :

```bash
python3 src/analyse_elf.py tests/fixtures/hello
```

Le programme affiche un rapport décrivant les caractéristiques détectées.

Pour afficher l'aide :

```bash
python3 src/analyse_elf.py --help
```

## Gestion des erreurs

Le programme signale les fichiers illisibles, les signatures invalides, les en-têtes incomplets et certaines incohérences de structure.

## Limites

Ce module ne constitue pas un analyseur ELF complet. Il ne valide pas toutes les structures du format et ne détermine pas si un fichier est malveillant. Les informations affichées doivent être interprétées dans le contexte du fichier analysé.
