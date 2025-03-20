import random

def get_number():
    chute = 0
    while not 1 <= chute <= 15:
        try:
            chute = int(input("Entre com um número entre 1 e 15: "))
        except ValueError:
            print("Entre com um valor válido!! Animal!")
    return chute


def check_number(chute, numero_certo):
    if chute == numero_certo:
        print("Parabéns, porrraaaa!!! Você acerto miserável!!")
        return True

    elif chute > numero_certo:
        print("Muito alto! Tente mais baixo")
        
    else:
        print("Muito baixo! Tente mais alto")
    
    return False


def main():
    numero_certo = random.randint(1,15)
    tentativas = 3

    for tentativa in range(1,tentativas+1):
        chute = get_number()
        if check_number(chute, numero_certo):
            break


if __name__ == "__main__":
    main()