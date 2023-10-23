# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
nume1= int(input("digite um número:"))
nume2= int(input("digite o segundo número:"))
nume3= int(input("digite o terceiro número:"))
if (nume1 > nume2 and nume1 > nume3):
    print(f"O número {nume1} é o maior entre os 3.")
    if nume2 < nume3:
        print(f"O número {nume2} é o menor número entre os 3")
    else:
        print(f"O número {nume3} é o menor número entre os 3")
elif (nume2 > nume1 and nume2 > nume3):
    print(f"O número {nume2} é o maior entre os 3.")
    if nume1 < nume3:
        print(f"O número {nume1} é o menor número entre os 3")
    else:
        print(f"O número {nume3} é o menor número entre os 3")
elif (nume3 > nume1 and nume3 > nume2):
    print(f"O número {nume3} é o maior entre os 3.")
    if nume1 < nume2:
        print(f"O número {nume1} é o número menor entre os 3")
    else:
        print(f"O número {nume2} é o número entre os 3")
        