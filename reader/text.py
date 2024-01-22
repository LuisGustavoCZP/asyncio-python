def read_text(path):
    with open(path, "r", encoding="utf8") as arquivo:
        return arquivo.read()