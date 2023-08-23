MAIOR_IDADE = 18
IDADE_ESPECIAL= 17

idade= int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print ("Está apto a tirar a carteira de habilitação.")

if idade < MAIOR_IDADE:
    print("Não está apto a tirar a carteira de habilitação.")




if idade >= MAIOR_IDADE:
    print ("Está apto a tirar a carteira de habilitação.")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer aulas práticas")    

else:
    print("Não está apto a tirar a carteira de habilitação.")