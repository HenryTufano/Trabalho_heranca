from professor import Professor
from estudante import Estudante
import os
op=99
ia=0
ip=0
aluno=[]
professor=[]
sd=[]
s=[]
pa=[]
men=[]
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
while op!=0:
    op=int(input("Escolha uma das opçoes:\n 1 - Deseja cadastrar um novo estudante\n2 - Deseja cadastrar um novo Professor \n3 - Mostrar informação \n4 - Mostrar mensalidades\n5 - Mostrar dias de trabalho\n6 - Adicional de peculiaridade\nEscolha a sua opção: "))
    if op == 1:
        if ia<2:
            clear()
            name=input('Digite o nome da pessoa :')
            phone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            ar = input("Digite o numero de matricula: ")
            course= int(input("Selecione a opção do curso: \n1-Engenharia\n 2-Direito\n 3-Pedagogia"))
            b=[name,email,phone,ar,course]
            aluno.append(b) 
            a=Estudante(name,phone,email,ar,course)    
            print('-'*15)
            m=a.monthly_payment(course)
            men.append(m)
            ia=ia+1
            print(ia)
        else:
            print("Alunos maximos cadastrados")
            
    elif op == 2:
        if ip<2:
            clear()
            name = input("Digite o nome da pessoa: ")
            phone = input("Digite o telefone: ")
            email = input("Digite o email: ")
            course= int(input("Digite o curso: "))
            salary = int(input("Digite o numero de salario: ")  )     
            print("Digite o dia de ingresso: ")
            ano=int(input("digite o ano"))
            mes=int(input("digite o mes"))
            dia=int(input("digite o dia"))
            sd=[ano,mes,dia]
            c=[name,email,phone,email,course,sd]
            professor.append(c)
            p=Professor(name,phone,email,course,salary,sd)
            delta=p.work_days(sd,s)
            s.append(delta)
            salar=p.additional_health_hazard(salary,course)
            pa.append(salar)
            ip=ip+1
        else:
            print("Professores maximos cadastrados")
            
    elif op == 3:
        clear()
        opc=int(input("Digite qual opção que deseja ver :\n1- Para estudantes\n2-Para professores\nEscolhe logo porra: "))
        if opc==1:
            clear()
            a.Show_info(name,phone,email,ar,course,aluno)
        elif opc==2:
            clear()     
            p.Show_info(name,phone,email,course,salary,sd,professor)

    elif op == 4:
        clear()
        print(men)
        
    elif op == 5:
        clear()
        print(s)

    elif op == 6:
        clear()
        print(pa)