with open('dados.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        lista = linha.split()
        notas = lista[-1:-5:-1]
        print('-' * 50)
        print(f'/n Notas: {notas}')
        soma = 0
        for n in notas:
            soma += float(n)
        media = soma / 4
        print(f'{media:.2f}')
