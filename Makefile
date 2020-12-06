.DEFAULT_GOAL := help
.PHONY: help build devserve watch

help: ## this help dialog
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build:
	./build.py

devserve:
	python3 -m http.server 8000 -d output

watch:
	modd
