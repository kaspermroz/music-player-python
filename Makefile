reqs:
	pip3 install -r requirements.txt

lint:
	pylint --rcfile=.pylintrc src

run:
	python3 main.py

test:
	pytest