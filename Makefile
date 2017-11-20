all: sign
tests:
	python3 setup.py test
sign: build
	gpg -a --detach-sign dist/*.gz
	gpg -a --detach-sign dist/*.whl
	gpg -a --detach-sign dist/*.egg
build: clean
	python3 setup.py sdist bdist_wheel bdist_egg
clean:
	rm -rf dist tomaatti.egg-info build
upload: sign
	twine upload dist/*
install_local: clean
	mkdir -p ~/.local/lib/python3.6/site-packages
	python3 setup.py install --prefix=~/.local
	make clean
