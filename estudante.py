from pessoa import Pessoa
class Estudante(Pessoa):
   
   def __init__(self,name,email,phone,ar,course):
      self.ar=ar
      self.course=course
      super().__init__(name,phone,email)

   def Show_info(self,name,email,phone,ar,course,aluno):
         print(aluno)
   def monthly_payment(self,course):
      self.course=course
      if self.course ==1:
         cur="a mensalidade do curso de engenharia é: R$2000,00"
      elif self.course==2:
        cur="a mensalidade do curso de Direito é: R$1500,00"
      elif self.course==3:
         cur="a mensalidade do curso de Pedagogia é: R$500,00"
      return cur

