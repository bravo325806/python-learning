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

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def new_employee_from_str(cls,new_employee_str):
        first_name, last_name, payment =  new_employee_str.split('-')
        return cls(first_name, last_name, payment)

# create Employee
staff1 = Employee('brown','jack',22000)
staff2 = Employee('hello','kitty',22000)

staff1.raise_amount = 1.5
Employee.set_raise_amount(1)
print('staff1:',staff1.raise_amount) # 1.5
print('staff2:',staff2.raise_amount) # 1

# new employee string
new_employee_str1 = 'kerry-moomy-23000'
new_employee_1 = Employee.new_employee_from_str(new_employee_str1)
print(new_employee_1.__dict__)

new_employee_str2 = 'apple-pie-24000'
new_employee_2 = Employee.new_employee_from_str(new_employee_str2)
print(new_employee_2.__dict__)

print(Employee.staff_num)