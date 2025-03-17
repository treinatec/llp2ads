import turtle
import time
import random

# DEFINIÇÃO DAS VARIÁVEIS QUE REPRESENTAM OS JOGADORES
jogador_um = turtle.Turtle()
jogador_dois = turtle.Turtle()
jogador_tres = turtle.Turtle()

# DEFINIÇÃO DE PROPRIEDADES DO JOGADOR UM
jogador_um.color("red") # DEFINIÇÃO DA COR DO JOGADOR UM
jogador_um.shape("turtle") # DEFINIÇÃO DA FORMA DO JOGADOR UM
jogador_um.penup() 
jogador_um.goto(-600, 200) # DEFINIÇÃO DA POSIÇÃO DO JOGADOR UM

# DEFINIÇÃO DE PROPRIEDADES DO JOGADOR DOIS
jogador_dois.color("blue") # DEFINIÇÃO DA COR DO JOGADOR DOIS
jogador_dois.shape("turtle") # DEFINIÇÃO DA FORMA DO JOGADOR DOIS
jogador_dois.penup()
jogador_dois.goto(-600, 0) # DEFINIÇÃO DA POSIÇÃO DO JOGADOR DOIS

# DEFINIÇÃO DE PROPRIEDADES DO JOGADOR TRÊS
jogador_tres.color("green") # DEFINIÇÃO DA COR DO JOGADOR TRÊS
jogador_tres.shape("turtle") # DEFINIÇÃO DA FORMA DO JOGADOR TRÊS
jogador_tres.penup()
jogador_tres.goto(-600, -200) # DEFINIÇÃO DA POSIÇÃO DO JOGADOR TRÊS

# DEFINIÇÃO DO CÍRCULO DE CHEGADA DO JOGADOR UM
jogador_um.goto(600,200)
jogador_um.pendown()
jogador_um.circle(40)
jogador_um.penup()
jogador_um.goto(-600, 230)

# DEFINIÇÃO DO CÍRCULO DE CHEGADA DO JOGADOR DOIS
jogador_dois.goto(600,0)
jogador_dois.pendown()
jogador_dois.circle(40)
jogador_dois.penup()
jogador_dois.goto(-600, 30)

# DEFINIÇÃO DO CÍRCULO DE CHEGADA DO JOGADOR TRÊS
jogador_tres.goto(600,-200)
jogador_tres.pendown()
jogador_tres.circle(40)
jogador_tres.penup()
jogador_tres.goto(-600, -170)

dado = [1, 2, 3, 4, 5, 6]

# ENTRADA
turno_jogador = input("TURNO DO JOGADOR UM: Aperte <Enter> para rolar o dado!")
# PROCESSAMENTO E SAÍDA
dado_lancado = random.choice(dado)
print(f"DADO LANÇADO DO JOGADOR UM: {dado_lancado}")
# PROCESSAMENTO E SAÍDA
jogador_um.forward(20*dado_lancado)
print(f"JOGADOR UM ANDOU {20*dado_lancado} PASSOS")

turno_jogador = input("TURNO DO JOGADOR DOIS: Aperte <Enter> para rolar o dado!")
dado_lancado = random.choice(dado)
print(f"DADO LANÇADO DO JOGADOR DOIS: {dado_lancado}")
jogador_dois.forward(20*dado_lancado)
print(f"JOGADOR DOIS ANDOU {20*dado_lancado} PASSOS")

turno_jogador = input("TURNO DO JOGADOR TRÊS: Aperte <Enter> para rolar o dado!")
dado_lancado = random.choice(dado)
print(f"DADO LANÇADO DO JOGADOR TRÊS: {dado_lancado}")
jogador_tres.forward(20*dado_lancado)
print(f"JOGADOR TRÊS ANDOU {20*dado_lancado} PASSOS")

time.sleep(300)