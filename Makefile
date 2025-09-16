
SRC		=	main.py

all:
	python3 $(SRC)

push:
	@echo -n "enter the commit text: "
	@git add . && read commit && git commit -m "$$commit" && git push

