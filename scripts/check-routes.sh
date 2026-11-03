#!/usr/bin/env bash
# Comprova que totes les rutes del build responen 200 contra una URL donada.
# Ús: npm run build && scripts/check-routes.sh https://www.latorre2.com
#
# Les pàgines es demanen sense barra final (/carta), que és com les enllaça el
# web. No segueix redireccions: una ruta que redirigeix compta com a error.
# També avisa si alguna resposta porta Set-Cookie (el web no n'ha de posar cap).
set -euo pipefail

base="${1:?Cal una URL base, p. ex. https://www.latorre2.com}"
base="${base%/}"
dist="$(cd "$(dirname "$0")/.." && pwd)/dist"
[ -d "$dist" ] || { echo "No hi ha dist/: fes npm run build abans"; exit 2; }

fails=0
check() {
  local path="$1" want="$2" headers code
  headers="$(curl -s -o /dev/null -D - "$base$path")"
  code="$(printf '%s' "$headers" | awk 'toupper($1) ~ /^HTTP/ {c=$2} END {print c}')"
  if [ "$code" != "$want" ]; then
    echo "FAIL $code (volia $want) $path"; fails=$((fails + 1))
  else
    echo "ok   $code $path"
  fi
  if printf '%s' "$headers" | grep -qi '^set-cookie:'; then
    echo "FAIL Set-Cookie a $path"; fails=$((fails + 1))
  fi
}

while IFS= read -r file; do
  path="/${file#./}"
  case "$path" in
    /index.html) path="/" ;;
    */index.html) path="${path%/index.html}" ;;
  esac
  check "$path" 200
done < <(cd "$dist" && find . -type f | sort)

check /aquesta-ruta-no-existeix 404

echo
if [ "$fails" -gt 0 ]; then echo "$fails errors contra $base"; exit 1; fi
echo "Totes les rutes OK contra $base"
