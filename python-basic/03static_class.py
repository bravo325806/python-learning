

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
        print(self.first_name,self.last_name)
        print('email: {}'.format(self.email))
    def pay_raise(self):
        self.payment = int(self.payment * Employee.raise_amount) #or self.raise_amount

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# create Employee
staff1 = Employee('brown','jack',22000)
staff2 = Employee('hello','kitty',22000)

import datetime
day = datetime.date(2018,4,8)
print(Employee.is_work_day(day))