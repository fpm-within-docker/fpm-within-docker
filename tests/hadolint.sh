#!/usr/bin/env bash

# modified from https://github.com/caarlos0/shell-ci-build

set -eo pipefail
test -n "${DEBUG:-}" && set -x

HADOLINT_OPTIONS="--ignore DL3008"

WORKDIR="/build"

success() {
  printf "\r%s [ \033[00;32mOK\033[0m ]\n" "$script"
}

fail() {
  printf "\r%s [\033[0;31mFAIL\033[0m]\n" "$1"
}

check() {
  local script="$1"
  local OUTPUT

  if OUTPUT="$(hadolint $HADOLINT_OPTIONS "$script")"; then
    success "$script"
    RETURN=0
  else
    fail "$script"
    echo "$OUTPUT"
    RETURN=1
  fi
  echo; echo
  return $RETURN
}

find_scripts() {
  git ls-tree -r HEAD | grep -E 'Dockerfile$' | awk '{print $4}'
}

cd $WORKDIR || exit 1
echo "Linting all Dockerfile files..."
find_scripts | {
  # shellcheck disable=SC2030
  EXIT=0
  while read -r script; do
    if ! check "$script"; then
      EXIT=1
    fi
  done
  exit $EXIT
}

# shellcheck disable=SC2031
exit $EXIT
