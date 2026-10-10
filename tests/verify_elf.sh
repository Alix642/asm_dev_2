
#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/tests/fixtures/hello.c"
BINARY="$ROOT/tests/fixtures/hello"

echo "=== Compilation ==="
gcc -Wall -Wextra -Werror "$SOURCE" -o "$BINARY"

echo
echo "=== Type du fichier ==="
file "$BINARY"

echo
echo "=== En-tête ELF ==="
readelf -h "$BINARY"

echo
echo "=== Segments ELF ==="
readelf -l "$BINARY"

echo
echo "=== Notes ELF ==="
readelf -n "$BINARY"

echo
echo "=== Exécution du programme de test ==="
"$BINARY"
