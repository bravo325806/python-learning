class Employee:
    staff_num = 0
    raise_amount = 1.8
    def __init__(self,first_name,last_name,payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.email = first_name + '_' + last_name + '@example.com'
        Employee.staff_num += 1

    def info(self):
        print('{} {}'.format(self.first_name,self.last_name))
        print('email: {}'.format(self.email))
    def pay_raise(self):
        self.payment = int(self.payment * Employee.raise_amount) #or self.raise_amount
        
class Developer(Employee):
    raise_amount = 2 # can't change!
    def __init__(self,first_name,last_name,payment,program_lang):
        super().__init__(first_name,last_name,payment)
        # same
        # Employee.__init__(self, first_name,last_name,payment) 
        self.program_lang = program_lang

class Manager(Employee):
    def __init__(self, first_name, last_name, payment, employees = None):
        super().__init__(first_name,last_name,payment)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
    def print_all_employees(self):
        for employee in self.employees:
            print('-->',employee.email)


# create Employee
dev_1 = Developer('brown','jack',22000,'Python')
dev_2 = Developer('hello','kitty',22000,'Java')
# print(dev_1.__dict__)
# print(help(Developer))
# dev_1.pay_raise()
# print(dev_1.payment)


# deverlop
print(dev_1.program_lang)
print(dev_2.program_lang)

# manager
manarger_1 = Manager('bob','johnson',32000,[dev_1])
print(manarger_1.email)
manarger_1.print_all_employees()
print('-----------------------')
manarger_1.add_emp(dev_2)
manarger_1.print_all_employees()
print('-----------------------')
manarger_1.remove_emp(dev_1)
manarger_1.print_all_employees()
print('-----------------------')

# instance 
print(isinstance(manarger_1, Manager))