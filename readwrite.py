def read(fname):
    with open("Files/" + fname, "rb") as f:
        data = f.read()
    return data


def write(fname, data):
    with open("Files/" + fname, "wb") as f:
        f.write(data)
