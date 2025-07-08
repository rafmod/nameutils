# nameutils - Identify family/given names and capitalize correctly
# https://raf.org/nameutils
# https://github.com/rafmod/nameutils
# https://codeberg.org/rafmod/nameutils
#
# Copyright (C) 2023-2025 raf <raf@raf.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <https://www.gnu.org/licenses/>.
#
# 20250708 raf <raf@raf.org>

help:
	@echo "make help        - Output this message (default)"
	@echo "make test        - Run the module tests"
	@echo "make check       - Same as make test"
	@echo "make cover       - Report test coverage"
	@echo "make coverage    - Same as make cover"
	@echo "make build       - test + Build the package for PyPI"
	@echo "make testrelease - build + Upload the package to TestPyPI"
	@echo "make release     - build + Upload the package to PyPI"
	@echo "make html        - Create nameutils.3py.html"
	@echo "make clean       - Delete generated files and directories"

test:
	tests/test_nameutils.py

check: test

cover:
	coverage run --branch tests/test_nameutils.py
	coverage report -m
	coverage html

coverage: cover

build: test
	rm -rf dist .build; \
	mkdir .build; \
	cp -pr LICENSE README.md pyproject.toml src tests .build; \
	rm -rf .build/src/*/__pycache__
	cd .build; \
	python3 -m build; \
	mv dist ..; \
	cd ..; \
	rm -rf .build

testrelease: build
	python3 -m twine upload --repository testpypi dist/*

release: build
	python3 -m twine upload dist/*

html:
	perl -ne 'BEGIN { $$in = 0 } $$in = !$$in, next if /^"""$$/; print if $$in' src/nameutils/__init__.py | rst2html.py --strict --title='nameutils(3py)' > nameutils.3py.html


clean:
	rm -rf dist .coverage htmlcov *.html

# vi:set ts=4 sw=4:
