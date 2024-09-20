def main():
    #get the list of itens
    itens = get_itens()
    
    #print itens
    print_itens(itens)

def print_itens(itens: list[str]):
    n = 1
    for iten in itens:
        print(f"{n} {iten.upper()}")
        n += 1


def get_itens():
    itens = []
    while True:
        try:
            itens.append(
                input("")
            )
        except EOFError:
            return itens



if __name__ == '__main__':
    main()