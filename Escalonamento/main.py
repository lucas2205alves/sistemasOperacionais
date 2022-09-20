
#O escalonamento de processos é uma das principais tarefas de um sistema operacional. O escalonamento pode ser realizado por diferentes políticas e critérios.

#Os escalonamentos podem ser feitos por ordem de criação, tamanho de trabalho estimado, prioridades, fatia de tempo entre outros critérios.

#A fim de investigar mais o mecanismo de escalonamento, desenvolva um simulador considerando os seguintes algoritmos não preemptivos.

#FIFO SJF Prioridade

#FIFO O que vem primeiro vai primeira
#SJF o menor vai primeiro
#Prioridades se baseia na prioridade

#Cada processo poderá possuir cargas de trabalho em CPU e em IO. Por exemplo:

#Processo 1 = { A, B, a, A , b, A}.

#Onde A e B representa uma carga de CPU com 1 e 2 unidades de tempos e a e b representam uma carga de IO com 1 e 2 unidades.

#O processo em execução.
#Os processos finalizados.
#O simulador pode ser desenvolvido com quaisquer linguagens de programação. O simulador deverá apresentar a cada passo:

#Os processos na fila de pronto Os processos na fila de espera

p1 = ["A", "a","b", "B", "b"]
pr1 =["A","a", "b", "B"]
pra1 =["A", "B","C", "D", "E"]
p2 = ["A", "b", "a", "A", "b"]
pr2 = ["A", "b", "a", "A" ]
e1 = []
e2 = []
print("FIFO")
print(" ")
for i in range(len(p1)): # Vai Iniciar o Processo 1
  p = p1[i] #A
  print(" ") 
  print("Iniciando o processo", p, "processo(s) pendentes", pr1)
  t = len(pr1)
  if t >= 1:
    del pr1[0]
  if i >= 0:
    print("Os processos prontos são", e1)
  e1.append(p)


  
print(" ")


for i in range(len(p2)): # Vai iniciar o processo 2 
  p = p2[i]
  print(" ")
  print("Iniciado processo", p, "processo(s) pendentes", pr2)
  t = len(pr2)
  if i >= 0:
    print("Os processos prontos são:", e2)
  e2.append(p)
  if t >= 1:
    del pr2[0]


print("")
print("SJF")
print("")
pr1 = ["A", "a", "B", "b", "A", "a"]
prc1 = ["A", "a", "B", "b", "A"]
pr2 = ["A", "B", "B", "B", "a"]
prc2 = ["A", "B", "B", "B"]
t1 = len(pr1)
t2 = len(pr2)
e1.clear()
e2.clear()

if t1 < t2: # Vai verificar se o processo 1 é menor que o processo 2 e vai iniciar,
  
  # Processo 1
  for i in range(t1): 
    p = pr1[i]
    print(" ") 
    print("Iniciado processo", p, "processo(s) pendentes", prc1)
    t = len(prc1)
    print("Os processos prontos são:", e1)
    e1.append(p)
    if t >= 1:
      del prc1[0]
  print("")
  # Processo 2
  for i in range(t2):
    p = pr2[i]
    print(" ") 
    print("Iniciado processo", p, "processo(s) pendentes", prc2)
    t = len(prc2)
    print("Os processos prontos são:", e2)
    e2.append(p)
    if t >= 1:
      del prc2[0]
    
if t2 < t1:
  # Processo 2
  
  for i in range(t2):
    p = pr2[i]
    print(" ") 
    print("Iniciado processo", p, "processo(s) pendentes", prc2)
    t = len(prc2)
    print("Os processos prontos são:", e2)
    e2.append(p)
    if t >= 1:
      del prc2[0]

  print("")
  # Processo 1
  for i in range(t1):
    p = pr1[i]
    print(" ") 
    print("Iniciado processo", p, "processo(s) pendentes", prc1)
    t = len(prc1)
    print("Os processos prontos são:", e1)
    e1.append(p)
    if t >= 1:
      del prc1[0]


print(" ")
print("Prioridade")
print(" ")

pri1 = [["A", "a", "B", "b", "A", "a"], ["P2"]]
pric1 = ["A", "a", "B", "b", "A"]
pri2 = [["A", "a", "A", "b", "A"],["P1"]]
pric2 = ["a", "A", "b", "A"]
e1.clear()
e2.clear()

print("Iniciando processo com prioridade 1")

if pri1[1][0] == "P1":
  for i in range(len(pri1[0])):
  
    p = pri1[0][i]
    print(" ") 
    print("Iniciando o processo", p, "processo(s) pendentes", pric1)
    t = len(pric1)
    if t >= 1:
      del pric1[0] #
    if i >= 1:
      print("Os processos prontos são", e1)
    e1.append(p)
  
  print(" ")
  print("Iniciando processo com processo 2")
  for i in range(len(pri2[0])):
    p = pri2[0][i]
    print(" ") 
    print("Iniciando o processo", p, "processo(s) pendentes", pric2)
    t = len(pric2)
    if t >= 1:
      del pric2[0]
    if i >= 1:
      print("Os processos prontos são", e2)
    e2.append(p)


else:
  print("Iniciando processo com processo 2")
  for i in range(len(pri2[0])):
      p = pri2[0][i]
      print(" ") 
      print("Iniciando o processo", p, "processo(s) pendentes", pric2)
      t = len(pric2)
      if t >= 1:
        del pric2[0]
      if i >= 1:
        print("Os processos prontos são", e2)
      e2.append(p)

  
  print(" ")
  print("Iniciando processo com processo 1")
  for i in range(len(pri1[0])):
      p = pri1[0][i]
      print(" ") 
      print("Iniciando o processo", p, "processo(s) pendentes", pric1)
      t = len(pric1)
      if t >= 1:
        del pric1[0] #
      if i >= 1:
        print("Os processos prontos são", e1)
      e1.append(p)


  








