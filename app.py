# Projeto Exemplo: Calculadora de Média do Aluno

def calcular_media(nota1, nota2):
    return (nota1 + nota2) /2

print("===Sistema de Notas do Aluno===")
n1 = float(input("\nDigite a primeira nota: "))
n2 = float(input("\nDigite a segunda nota: "))

media = calcular_media(n1, n2)

print(f"\nA media final é: {media:.2f}")

if media >= 7.0:
    print("\nStatus: APROVADO!")

elif media >= 5:
    print("\nStatus: Você ficou de recuperação")
    
else:
    print("\nStatus: REPROVADO.")