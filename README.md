# Jogo de Adivinhação de Palavra

Este repositório contém um simples jogo de adivinhação de palavra em Python. O objetivo é que o usuário tente descobrir uma palavra secreta (“carta”) digitando letras, recebendo feedback sobre quais letras já acertou até completar a palavra.

---

## 📄 Descrição

O jogo funciona da seguinte forma:

1. Há uma variável `palavra_secreta` definida como `'carta'`.
2. O programa entra em um laço `while True`, solicitando ao usuário que digite **apenas uma letra** por tentativa.
3. Se o usuário digitar mais de um caractere, um espaço em branco ou nada, o programa exibe uma mensagem de erro e pede uma nova entrada.
4. A cada tentativa válida, incrementa-se um contador (`contagem`).
5. Se a letra digitada estiver na palavra secreta, ela é adicionada à string `letras_acertadas`.
6. O programa reconstrói a “palavra formada” usando `*` para cada letra ainda não adivin­hada e exibe no terminal.
7. O jogo continua até que todas as letras tenham sido descobertas. Ao acertar a palavra completa, exibe-se uma mensagem de parabéns, informa-se o número total de tentativas e encerra o laço.

---
