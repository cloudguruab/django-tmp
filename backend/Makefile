.DEFAULT_GOAL := build
SHELL := /bin/bash
# ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
LOOPAPI := $(HOME)/loop
export LOOPAPI

# LINTS
test-lint:
	pre-commit install
	pre-commit run --all-files


# BUILD
build-run:
	docker compose up -d
