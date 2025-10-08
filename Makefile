
SRC			=	src/main.py
# DATAFILE	=	data.csv

all:
	@python3 $(SRC)  -l 0.001 -i 3000

push:
	@echo -n "enter the commit text: "
	@git add . && read commit && git commit -m "$$commit" && git push

env:
	@python3 -m venv env && source ./env/bin/activate.fish && pip3 install requirements.txt

.PHONY: env