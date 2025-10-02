
SRC			=	main.py
DATAFILE	=	data.csv

all:
	python3 $(SRC) $(DATAFILE)

push:
	@echo -n "enter the commit text: "
	@git add . && read commit && git commit -m "$$commit" && git push

