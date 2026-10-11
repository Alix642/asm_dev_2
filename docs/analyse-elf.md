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

## Comprendre les informations ELF

### En-tête ELF

L'en-tête ELF identifie le format du fichier et fournit des informations générales :
- **Classe** : ELF32 ou ELF64, selon la taille des structures.
- **Encodage** : ordre des octets utilisé pour représenter les valeurs.
- **Type** : indique notamment si le fichier est un objet relogeable, un exécutable ou un objet partagé.
- **Machine** : architecture cible, par exemple x86-64.
- **Point d'entrée** : adresse virtuelle indiquée comme point de départ du programme.
- **En-têtes de programme** : décrivent les segments utilisés lors du chargement.

### Segments et sections

Les segments et les sections remplissent des rôles différents.

- **PT_LOAD** : décrit une région destinée à être chargée en mémoire. Ses permissions peuvent notamment indiquer la lecture, l'écriture ou l'exécution.
- **PT_NOTE** : décrit une zone contenant des notes et des métadonnées.
- **PT_INTERP** : indique le chemin de l'interpréteur dynamique lorsqu'il est présent.
- **PT_DYNAMIC** : contient des informations utiles à l'édition de liens dynamique.

Les sections, telles que `.text`, `.rodata` et `.data`, organisent le contenu du fichier. Plusieurs sections peuvent appartenir à un même segment.

### Notes GNU

Les notes observées dans le programme de test comprennent :
- `NT_GNU_PROPERTY_TYPE_0` : propriétés relatives à la plateforme et aux fonctionnalités prises en charge.
- `NT_GNU_BUILD_ID` : identifiant de construction du binaire.
- `NT_GNU_ABI_TAG` : informations de compatibilité avec l'environnement système.

### Limites de l'analyse

Les informations affichées décrivent le fichier analysé. Elles ne suffisent pas, à elles seules, à démontrer qu'un programme est sûr ou malveillant. Les résultats peuvent varier selon le compilateur, ses options et l'environnement de construction.

L'analyse du programme de démonstration est réalisée avec les outils `file` et `readelf`, sans modification du fichier analysé.
