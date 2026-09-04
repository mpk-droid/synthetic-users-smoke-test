.PHONY: install run test lint docker-build docker-run

install:
	pip install -r requirements.txt

run:
	python -m demo_service.main

test:
	pytest tests/ -v

lint:
	ruff check src/

docker-build:
	docker build -t demo-service:local .

docker-run:
	docker run --rm -p 8080:8080 demo-service:local
