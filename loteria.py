import random

def mega():
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
  print("\n\nNúmeros da mega-sena:\n",numeros)
  print("\n\n")


def lotofacil():
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
  print("\n\nNúmeros da lotofácil:\n",numeros)
  print("\n\n")


def quina():
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
  print("\n\nNúmeros da quina:\n",numeros)
  print("\n\n")

def main():
  while(True):
    escolha= int(input("1. Mega Sena\n2. Lotofácil\n3. Quina\nDigite o jogo desejado: "))
    if escolha ==1:
      mega()
    elif escolha ==2:
      lotofacil()
    elif escolha ==3:
      quina()
    else:
      print("Valor incorreto! Escolha número entre 1 e 3\n")

main()

