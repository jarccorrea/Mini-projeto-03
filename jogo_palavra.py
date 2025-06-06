palavra_secreta = 'carta'
letras_acertadas = ''
contagem = 0

while True:
    letra_digitada = input('Digite uma letra: ')

    if len(letra_digitada) > 1 or letra_digitada == ' ' or letra_digitada == '':
        print ('Digite apenas uma letra.')
        continue

    contagem += 1

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)
    print(contagem)

    if palavra_formada == palavra_secreta:
        print('Parabéns!! Você conseguiu!')
        print(f'Em apenas {contagem} tentativas!')
        print(f'A Palavra era {palavra_secreta}.')
        letras_acertadas = ''
        contagem = 0
        print ()
        break
