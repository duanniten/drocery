def main():
    #get the list of itens
    itens = get_itens()
    
    #print itens
    print_itens(itens)

def print_itens(itens: list[str]):
    itens_dict = {}
    for iten in itens:
        if iten in itens_dict.keys():
            itens_dict[iten] += 1
        else:
            itens_dict[iten] = 1
    for iten, n in itens_dict.items():
        print(f"{n} {iten}")

def get_itens():
    itens = []
    while True:
        try:
            itens.append(
                input("").upper()
            )
        except EOFError:
            return itens



if __name__ == '__main__':
    main()