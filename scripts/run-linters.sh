#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

APP_MODULES="gpa_calculator"
TEST_MODULES="tests"

BLACK_ARGS="--check"
ISORT_ARGS="--check-only"

# Call this script with --fix to have it fix the files
if [ "$1" = "--fix" ]; 
    then
        echo "Files will be formatted"
        BLACK_ARGS=""
        ISORT_ARGS=""
fi


# BLACK
echo "======Black formatting checks======"
poetry run black ${BLACK_ARGS} ${APP_MODULES} ${TEST_MODULES} && echo "black successful"


# ISORT
echo "====Isort import sorting checks===="
poetry run isort ${ISORT_ARGS} ${APP_MODULES}  && echo "isort successful"


# FLAKE8
echo "=======Flake8 linting checks======="
# flake8 is silent when it's successful, so make some noise
poetry run flake8 ${APP_MODULES}  && echo "flake8 successful"
