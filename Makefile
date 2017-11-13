all: build
	gpg -a --detach-sign dist/*
build: clean
	python3 setup.py sdist
clean:
	rm -rf dist tomaatti.egg-info
