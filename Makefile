#!/usr/bin/env bash

LIGHT_CYAN=\033[1;36m
NO_COLOR=\033[0m

.PHONY: docs

help:
	@echo "test - run tests"
	@echo "lint - lint the python code"
	@echo "format - format the python code"

# Run tests
test: 
	@echo "${LIGHT_CYAN}Running tests...${NO_COLOR}"
	pytest

# Lint python code
lint:
	@echo "${LIGHT_CYAN}Linting code...${NO_COLOR}"
	isort . --check-only
	black . --check
	flake8 .

# Format python code
format:
	@echo "${LIGHT_CYAN}Formatting code...${NO_COLOR}"
	isort .
	black .
