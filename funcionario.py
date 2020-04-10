from pessoa import Pessoa
import datetime
class Funcionario(Pessoa):
    def __init__(self,name,phone,email,salary,sd):
        self.salary=salary
        self.sd=sd
        super().__init__(name,phone,email)
    
    def work_days(self,sd,s):
        datapadrao = datetime.date(sd[0], sd[1], sd[2])
        hoje = datetime.date.today()

        if datapadrao > hoje:
            delta = datapadrao - hoje
            
        elif datapadrao <= hoje:
        
            delta = hoje - datapadrao
            
        
        
        return delta