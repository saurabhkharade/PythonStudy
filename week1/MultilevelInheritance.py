class Founder:
    def founder(self):
        print('I am founder')
class CEO(Founder):
    def ceo(self):
        print('I am ceo')
class Employee(CEO):
    def employee(self):
        print('I am employee')

emp = Employee()
emp.employee()
emp.ceo()
emp.founder()