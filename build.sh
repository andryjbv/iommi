#!/bin/sh
# Common Setup, DO NOT MODIFY
cd /app
set -e

# COMPLETE THE FOLLOWING SECTIONS
###############################################
# PROJECT DEPENDENCIES AND CONFIGURATION
###############################################
# Install project dependencies if needed based on relevant config/lock files in the repo.
# Note that we are developing the project, even if dependencies have been installed before, we need to install again to accommodate the changes we made.
python -m pip install --upgrade pip
# install runtime and test dependencies
python -m pip install -r requirements.txt -r test_requirements.txt
# install the package in editable mode
python -m pip install -e .
# Configure project and environment variables
export DJANGO_SETTINGS_MODULE=tests.settings

###############################################
# BUILD
###############################################
echo "================= 0909 BUILD START 0909 ================="
# No additional build steps required for this project

echo "================= 0909 BUILD END 0909 ================="

