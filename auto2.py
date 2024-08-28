
estados = ['q0', 'q1', 'q2', 'q3']
estadoAtual = estados[0]

string = input("Digite a string:")

for index, letter in enumerate(string):
    if estadoAtual == estados[0]:
        if letter == '0':
            estadoAtual = estados[3]
            print(estadoAtual)
        elif letter == '1':
            estadoAtual = estados[1]
            print(estadoAtual)
        else:
            print("Simbolo nao existe na linguagem")
            exit()
    elif estadoAtual == estados[1]:
        if letter == '0':
            estadoAtual = estados[2]
            print(estadoAtual)
        elif letter == '1':
            estadoAtual = estados[0]
            print(estadoAtual)
        else:
            print("Simbolo nao existe na linguagem")
            exit()
    elif estadoAtual == estados[2]:
        if letter == '0':
            estadoAtual = estados[1]
            print(estadoAtual)
        elif letter == '1':
            estadoAtual = estados[3]
            print(estadoAtual)
        else:
            print("Simbolo nao existe na linguagem")
            exit()
    elif estadoAtual == estados[3]:
        if letter == '0':
            estadoAtual = estados[0]
            print(estadoAtual)
        elif letter == '1':
            estadoAtual = estados[2]
            print(estadoAtual)
        else:
            print("Simbolo nao existe na linguagem")
            exit()
    if index == (len(string) - 1):
        if estadoAtual == estados[0]:
            print("Palavra Aceita")
        else:
            print("Palavra nao aceita!")