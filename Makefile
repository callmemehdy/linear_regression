
SRC		=	main.py

all:
	python3 $(SRC)

push:
	git add . && read commit && git commit -m "$$commit" && git push