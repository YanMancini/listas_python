## Lista de Tarefas
import os 

tarefa=[]
choose=1
i=0
feita1=" Feita👌"

os.system("cls")

while choose!=0:

    os.system("cls")

    i=0

    print("          Tarefas\n==========================")
    for taref in tarefa: 
        print(i," -",taref)
        i=i+1
    print("==========================")

    choose=int(input("O que deseja fazer?\n1-Incluir tarefa na lista\n2-Marcar tarefa na lista\n3-Remover tarefa na lista\n4-Limpar lista\n"))
    if choose==1:
        tarefa.append(input("Que tarefa deseja adicionar?\n"))
    elif choose==2:
        feita=int(input("qual a posição da tarefa que deseja marcar?"))
        tarefa[feita]=tarefa[feita]+feita1
    elif choose==3:
        tarefa.pop(int(input("Qual tarefa que deseja remover?")))
    elif choose==4:
        tarefa.clear()
    else:
        print("Digite uma opção valida!")