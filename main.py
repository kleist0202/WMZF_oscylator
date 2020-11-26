def load_from_file(file_name):
    d = {}
    with open(file_name, 'r') as f:
        next(f)
        for i in f:
            s = i.split()
            d[s[0]] = float(s[1])

    return d


if __name__ == "__main__":
    lepkosci = load_from_file("tabela-substancji-WMZF.txt")
    for key, value in lepkosci.items():
        print(key, value);
