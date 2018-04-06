

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

# create Employee
staff1 = Employee('brown','jack',22000)
staff2 = Employee('hello','kitty',22000)

# same
Employee.info(staff1)
staff1.info()
staff2.info()

# origin payment 
print(staff1.payment)
# raise
staff1.pay_raise()
print(staff1.payment)
# same
print(Employee.raise_amount)
print(staff1.raise_amount)

# we can change the raise_amount
staff1.raise_amount = 1.5
print('staff1:',staff1.raise_amount)
print('staff2:',staff2.raise_amount)

# __dict__
# print(staff1.__dict__)
# print(Employee.__dict__)

print(Employee.staff_num) # 2 :staff1 and staff2
