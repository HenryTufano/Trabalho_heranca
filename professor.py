from funcionario import Funcionario
class Professor(Funcionario):
    def __init__(self,name,phone,email,course,salary,sd):
        self.name=name
        self.phone=phone
        self.email=email
        self.course=course
        self.salary=salary
        self.sd=sd
        super().__init__(name,phone,email,salary,sd)

    def additional_health_hazard(self,salary,course):
        if self.course ==1:
            salary=self.salary+(self.salary*0.3)
        
        elif self.course ==2:
            salary=self.salary+(self.salary*0.05)
    
        elif self.course==3:
            salary=self.salary+(self.salary*0.15)

        return salary 
    def Show_info(self,name,phone,email,course,salary,sd,professor):
        print(professor)