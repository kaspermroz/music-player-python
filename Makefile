reqs:
	pip3 install -r requirements.txt

lint:
	pylint src

run:
	python3 src/main.py