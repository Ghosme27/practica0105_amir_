peso_payaso=112
peso_muñecas=75
payasos=int(input('Cuantos payasos se envian:'))
muñecas=int(input('Cuantas muñecas se envian:'))
paquete=peso_payaso * payasos + peso_muñecas * muñecas
print('El peso total del paquete es de',paquete,'g')