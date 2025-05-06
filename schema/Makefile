
.PHONY: all clean install test docs

SRC_DIR = src/fga_schema
SCHEMA_DIR = $(SRC_DIR)/schema
BUILD_DIR = project
EXAMPLES_DIR = examples
DOCS_DIR = docs

all: install gen-docs gen-schema

install:
	pip install -e .

test:
	pytest

clean:
	rm -rf $(BUILD_DIR)/jsonschema/*
	rm -rf $(BUILD_DIR)/shex/*
	rm -rf $(BUILD_DIR)/owl/*
	rm -rf $(DOCS_DIR)

gen-schema: gen-json gen-shex gen-owl

gen-json:
	mkdir -p $(BUILD_DIR)/jsonschema
	gen-json-schema -d $(SCHEMA_DIR)/core.yaml > $(BUILD_DIR)/jsonschema/fga_schema.json

gen-shex:
	mkdir -p $(BUILD_DIR)/shex
	gen-shex -d $(SCHEMA_DIR)/core.yaml > $(BUILD_DIR)/shex/fga_schema.shex

gen-owl:
	mkdir -p $(BUILD_DIR)/owl
	gen-owl -d $(SCHEMA_DIR)/core.yaml > $(BUILD_DIR)/owl/fga_schema.owl

gen-docs:
	mkdir -p $(DOCS_DIR)
	gen-doc -d $(SCHEMA_DIR)/core.yaml -o $(DOCS_DIR)

gen-examples:
	mkdir -p $(EXAMPLES_DIR)/data
	gen-linkml $(SCHEMA_DIR)/core.yaml \
	  --output-formats yaml \
	  --output $(EXAMPLES_DIR)/data/example.yaml

validate:
	linkml-validate -s $(SCHEMA_DIR)/core.yaml $(EXAMPLES_DIR)/data/*.yaml
