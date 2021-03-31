import os 

def math():
    questoes = ['Quanto é 1 mais 1 ?', 'Qual é a mass do sol?']
    alter = ['1', '2', '3']
    gabarito = ['a','a','b']
    ponto = 0
    print(questoes[0])
    print('--------------------------------')
    print('Escolha a alternativa:') 
    escolha = input(f'[A] - {alter[0]} {os.linesep}[B] - {alter[1]} {os.linesep}[C] - {alter[2]} {os.linesep}')
    if escolha == gabarito[0]:
        print("\033[1;32;40m Resposta certa !!")
        ponto += 1
