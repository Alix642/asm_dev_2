# Analyse d'un exécutable ELF

## Environnement
- Système : Linux Mint
- Architecture : x86-64
- Compilateur : GCC
- Outil d'analyse : readelf

## Programme de test
Le fichier `tests/fixtures/hello.c` affiche `Hello ELF`.
Il a été compilé avec les options `-Wall -Wextra -Werror`.

## En-tête ELF
- Classe : ELF64
- Encodage : little endian
- Type : DYN (exécutable PIE)
- Point d'entrée observé : 0x1060
- Nombre d'en-têtes de programme : 13

## Segments observés
- PT_LOAD : décrit les zones chargées en mémoire.
- PT_NOTE : contient des métadonnées.
- PT_INTERP : indique l'interpréteur dynamique.
- PT_DYNAMIC : contient des informations pour l'édition de liens dynamique.

## Notes observées
- NT_GNU_PROPERTY_TYPE_0 : propriétés liées à la plateforme.
- NT_GNU_BUILD_ID : identifiant de construction.
- NT_GNU_ABI_TAG : étiquette de compatibilité ABI.

## Vérification
L'exécution du programme affiche `Hello ELF`.
L'analyse a été effectuée avec `file`, `readelf -h`, `readelf -l` et `readelf -n`.

## Limites
Les observations correspondent au binaire compilé dans cet environnement.
Les résultats peuvent varier selon le compilateur, ses options et la plateforme.
