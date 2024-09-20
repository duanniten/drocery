def main():
    #get the list of itens
    itens = get_itens()
    
    #print itens
    print_itens(itens)

def print_itens(itens: list[str]):
    n = 0
    for iten in itens:
        print(f"{n} {iten.upper()}")


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