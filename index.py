

peso=float(input("Digite seu peso em kg : "))
altura=float(input('Digite sua altura em metros :'))

imc= (peso * (altura *altura))/10

print(imc)

if (imc <18.5):
    print(f"Abaixo do peso")

elif (imc<25):
    print(f'Normal') 

elif (imc<30 ):
    print(f'Sobrepeso') 

elif (imc<35):
    print(f'Obesidade grau 1')  

elif (imc<40):
    print(f'Obesidade grau 2')

else:
    print(f'Obesidade grau 3')  

                  