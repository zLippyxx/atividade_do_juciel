numero=input("Qual é o seu número? ")
numero=int(numero)
valida_pos=numero>0
valida_neg=numero<0

if valida_pos:
    print("Seu número é positivo")

elif valida_neg:
    print("Seu número é negativo")
else:
    print("Seu número é igual a zero")