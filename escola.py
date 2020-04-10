from professor import Professor
from estudante import Estudante
op=99
aluno=[]
professor=[]
sd=[]
s=[]
pa=[]
men=[]
while op!=0:
    op=int(input("Escolha uma das opçoes:\n 1 - Deseja cadastrar um novo estudante\n2 - Deseja cadastrar um novo Professor \n3 - Mostrar informação \n4 - Mostrar mensalidades\n5 - Mostrar dias de trabalho\n6 - Adicional de peculiaridade "))
    if op == 1:
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
            

    elif op == 2:
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
        salaryn=p.additional_health_hazard(salary,course)
        pa.append(salaryn)
    elif op == 3:
        opc=int(input("Digite qual opção que deseja ver :\n1- Para estudantes\n2-Para professores\nEscolhe logo porra: "))
        if opc==1:
            a.Show_info(name,phone,email,ar,course,aluno)
        elif opc==2:      
            p.Show_info(name,phone,email,course,salary,sd,professor)
    elif op == 4:
        print(men)
        

    elif op == 5:
        print(s)

    elif op == 6:
        print(pa)