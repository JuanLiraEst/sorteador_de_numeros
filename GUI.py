from tkinter import *
import random

from matplotlib.pyplot import margins
#Criando janela
window = Tk()

canvas = Canvas(
    window,
    height=3000,
    width=3000,
    bg='lightgray'
    )
    
canvas.pack()
canvas.create_rectangle(
    10, 350, 790, 550,
    outline="black",
    fill="#E9E8EB")

#titulo
window.title("Loteria")

window.geometry('800x600')

header = Label(window, text="Sorteador de números",font=("Arial",25), bg="lightgray")
subtitle = Label(window, text="Lotofácil, Quina e Mega-Sena",font=("Arial",20), bg="lightgray")
resultado = Label(window, text="Selecione o jogo desejado",font=("Arial",16), bg="#E9E8EB")
#posição relativa pra manter a responsividade
#mas tbm é possível declarar x=100, y=200 por exemplo
#a referência (anchor) é o centro

header.place(x=400, y=50, anchor =CENTER)
subtitle.place(x=400, y=100, anchor =CENTER)
resultado.place(x=400, y=450, anchor=CENTER)

def mega():
  canvas.pack()
  canvas.create_rectangle(
    10, 350, 790, 550,
    outline="black",
    fill="#128752")
  numeros = []
  x = 0
  while x<6:
    sorteado = random.randint(1,60)
    if sorteado not in numeros:
      numeros.append(sorteado)
      x+=1   
    else:
      x= x     
  numeros.sort() #ordenar
  
  jogo="     "
  espaco = "     "
  y=0
  while y<6:
    jogo = jogo + str(numeros[y])+espaco
    y+=1
  resultado['text'] = jogo


def lotofacil():
  canvas.pack()
  canvas.create_rectangle(
    10, 350, 790, 550,
    outline="black",
    fill="#BD22FF")
  numeros = []
  x = 0
  while x<15:
    sorteado = random.randint(1,25)
    if sorteado not in numeros:
      numeros.append(sorteado)
      x+=1   
    else:
      x= x   
  numeros.sort() #ordenar
  
  jogo="    "
  espaco = "    "
  y=0
  while y<15:
    jogo = jogo + str(numeros[y])+espaco
    y+=1
  resultado['text'] = jogo


def quina():
  canvas.pack()
  canvas.create_rectangle(
    10, 350, 790, 550,
    outline="black",
    fill="#873EF5")
  numeros = []
  x = 0
  while x<5:
    sorteado = random.randint(1,80)
    if sorteado not in numeros:
      numeros.append(sorteado)
      x+=1   
    else:
      x= x    
  numeros.sort() #ordenar

  jogo="     "
  espaco = "     "
  y=0
  while y<5:
    jogo = jogo + str(numeros[y])+espaco
    y+=1
  resultado['text'] = jogo

#BOTÕES
btnMega = Button(window, text="Mega-Sena", command=mega ,bg="#128752", font=("Arial",20), fg="white", cursor="plus")
btnMega.place(x=200,y=220, anchor=CENTER)

btnQuina = Button(window, text="Quina", command=quina, bg="#873EF5",font=("Arial",20), fg="white", cursor="plus")
btnQuina.place(x=400,y=220, anchor=CENTER)

btnLoto = Button(window, text="Lotofácil", command=lotofacil, bg="#BD22FF", font=("Arial",20), fg="white", cursor="plus")
btnLoto.place(x=600,y=220, anchor=CENTER)

#manter a janela aberta
window.mainloop()

