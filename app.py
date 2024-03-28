from random import randint

while True:
    input("Para iniciar, pressione Enter...")
    print("Iniciando...\n")
    print("*** Bem-vindo ao adivinhe o número! ***")

    num = randint(1, 100)

    while True:
        guess_num_str = input("Escolha um número de 1 a 100 (ou 's' para sair): ").strip()

        if guess_num_str.lower() == 's':
            print("Jogo encerrado.")
            exit()  # Encerra o jogo se o usuário digitar 's'

        if guess_num_str:  # Verifica se a entrada não está vazia
            try:
                guess_num = int(guess_num_str)
            except ValueError:
                print("Por favor, digite um número válido.")
                continue

            if guess_num < num:
                print("Um pouco mais.")
            elif guess_num > num:
                print("Um pouco menos.")
            else:
                print("Parabéns!!! Você acertou o número!")
                break
        else:
            print("Por favor, digite um número de 1 a 100.")

    while True:
        play_again = input("Deseja jogar novamente? [S]im [N]ao: ").strip().upper()

        if play_again not in ['S', 'N']:
            print("Por favor, digite apenas 'S' ou 'N'.")
        else:
            break  # Sai do loop interno se a entrada estiver correta

    if play_again != 'S':
        print("Jogo encerrado.")
        break
