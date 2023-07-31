#!/bin/sh

set -e

# Go to root folder
cd $(dirname $0)/..

NAME="GPA-Calculator"
PROJECT_DIR="${PWD}/gpa_calculator"
MODULE_NAME="client/app.py"
PORT=8501

echo "Starting ${NAME} client..."

streamlit run ${PROJECT_DIR}/${MODULE_NAME} --server.port ${PORT}
