import random
x = random.randint(0,100)

t = 1
resposta = int (input("Estou a pensar num número entre 0 e 100. Adivinhe esse número."))

while resposta != x :
    if resposta > x :
        resposta = int (input("O número que pensei é menor. Tente novamente."))
    if resposta < x :
        resposta = int (input("O número que pensei é maior. Tente novamente."))
    t = t + 1

print(f"Acertou! Necessitou de {t} tentativas.")