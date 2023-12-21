import random
import time

def escolher_palavra():
    palavras_matematicas = ["derivada", "integral", "equacao", "matriz", "logaritmo"]
    return random.choice(palavras_matematicas)

def exibir_forca(erros):
    forca = [
        """
           -----
           |   |
               |
               |
               |
               |
        ----------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ----------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ----------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ----------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ----------
        """
    ]
    return forca[erros]

def jogar_jogo():
    palavra = escolher_palavra().upper()
    letras_descobertas = set()
    tentativas = 0
    max_tentativas = len(palavra) + 2
    erros = 0

    print("Bem-vindo ao Jogo da Forca com Palavras Matemáticas!")
    print("Adivinhe a palavra.")

    while True:
        palavra_atual = "".join(letra if letra in letras_descobertas else "_" for letra in palavra)
        print(exibir_forca(erros))
        print("Palavra: ", palavra_atual)
        print("Letras incorretas: ", ", ".join(set(palavra) - letras_descobertas))

        if palavra_atual == palavra:
            print("Parabéns! Você venceu!")
            break

        if erros == max_tentativas:
            print("Você perdeu! A palavra era:", palavra)
            break

        tentativa = input("Digite uma letra: ").upper()

        if tentativa.isalpha() and len(tentativa) == 1:
            if tentativa in letras_descobertas:
                print("Você já tentou essa letra. Tente novamente.")
            elif tentativa in palavra:
                letras_descobertas.add(tentativa)
                print("Letra correta!")
            else:
                erros += 1
                print("Letra incorreta. Tente novamente.")
        else:
            print("Por favor, digite uma única letra válida.")

        tentativas += 1

if __name__ == "__main__":
    temporizador = int(input("Digite o tempo máximo para o jogo (em segundos): "))
    print(f"Você tem {temporizador} segundos para adivinhar a palavra.")
    try:
        start_time = time.time()
        jogar_jogo()
    except KeyboardInterrupt:
        pass
    elapsed_time = time.time() - start_time

    if elapsed_time > temporizador:
        print(f"Tempo esgotado! Você demorou muito. A palavra era:")
        print(escolher_palavra().upper())
