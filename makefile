init:
  pip install -r requirements.txt

foo:
	python sample.py

.PHONY: init foo
