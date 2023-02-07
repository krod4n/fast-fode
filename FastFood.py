print('1 - Hambúrguer - R$10,00')
print('2 - Batata - R$5,00')
print('3 - Refri - R$4,00')
print('4 - Sorvete - R$2,00')

opcao = int(input('Digite o nº da opção desejada: '))

quantidade = int(input('Digite a quantidade desejada: '))

nome = input('Digite seu nome: ')

if opcao == 1:
    print('Hambúrguer sendo preparado para ', nome)
    print('Tempo de espera de 15 minutos')
    total = quantidade * 10
    print('Total: R$', total)
if opcao == 2:
    print('Batata sendo preparado para ', nome)
    print('Tempo de espera de 15 minutos')
    total = quantidade * 5
    print('Total: R$', total)
if opcao == 3:
    print('Sorvete sendo preparado para: ', nome)
    print('Tempo de espera de 15 minutos')
    total = quantidade * 4
    print('Total: R$', total)
if opcao == 4:
    print('Hambúrguer sendo preparado para ', nome)
    print('Tempo de espera de 15 minutos')
    total = quantidade * 2
    print('Total: R$', total)