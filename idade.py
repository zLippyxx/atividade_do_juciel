idade=input("Qual a sua idade? ")
idade=int(idade)
valida_maior=idade>=18

if valida_maior:
    print("Já pode ser preso")
else:
    print("Não pode ser preso")