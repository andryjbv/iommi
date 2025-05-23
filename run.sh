#!/bin/bash
### COMMON SETUP; DO NOT MODIFY ###
set -e

# Redirect output
exec > /workspace/stdout.txt 2> /workspace/stderr.txt

export DJANGO_SETTINGS_MODULE=tests.settings

# --- CONFIGURE THIS SECTION ---
run_all_tests() {
  echo "Running all tests..."
  cd /workspace/app
  python -m pytest -v tests/ || true
}

run_selected_tests() {
  local test_files=("$@")
  echo "Running selected tests: ${test_files[@]}"
  cd /workspace/app
  python -m pytest -v "${test_files[@]}" || true
}
# --- END CONFIGURATION SECTION ---

### COMMON EXECUTION; DO NOT MODIFY ###

if [ $# -eq 0 ]; then
  run_all_tests
  exit 0
fi

if [[ "$1" == *","* ]]; then
  IFS=',' read -r -a TEST_FILES <<< "$1"
else
  TEST_FILES=("$@")
fi

run_selected_tests "${TEST_FILES[@]}"
exit 0
