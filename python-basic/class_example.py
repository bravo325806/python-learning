

class Employee():
    def __init__(self,first_name,last_name,payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.email = first_name + '_' + last_name + '@example.com'
    def info(self):
        print('{} {}'.format(self.first_name,self.last_name))
        print('email: {}'.format(self.email))

staff1 = Employee('brown','jack',22000)

# same
Employee.info(staff1)
staff1.info()