import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
ontos = int(1000)

print("Seus pontos:", pontos)
print("Qual nível de dificudade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
   total_de_tentativas = 20
elif(nivel == 2):
   total_de_tentativas = 10
else:
   (nivel == 3)
   total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1):
   print("Tentativa {} de {}".format(rodada, total_de_tentativas))
   chute_str = input("Digite um número entre 1 e 100:")
   print("Você digitou: ", chute_str)
   chute = int(chute_str)

   acertou = chute == numero_secreto
   maior = chute > numero_secreto
   menor = chute < numero_secreto

   if (acertou):
      print("Você acertou")
   else:
      if(maior):
         print("Você errou! O seu chute foi maior do que o número secreto.")
      elif(menor):
         print("Você errou! O seu chute foi menor do que o número secreto.")
         pontos_perdidos = abs(numero_secreto - chute)
         pontos = pontos_perdidos - pontos_perdidos

   print("Fim do jogo")
