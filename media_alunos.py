# media_alunos.py

# Recebe as notas dos alunos
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média aritmética
media = (nota1 + nota2 + nota3) / 3

# Exibe o resultado
print(f"Média do aluno: {media:.2f}")

# Verifica se o aluno foi aprovado ou reprovado
if media > 6:
    print("Aprovado")
else:
    print("Reprovado")