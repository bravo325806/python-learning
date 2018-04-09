import psycopg2
from flask import jsonify
class PostgreDbProcess:

    def __init__(self, post_data ):
        self.post_data = post_data
        self.id = str(10)
        self.name = str(post_data['name'])
        self.email = str(post_data['email'])
        self.birthday = str(post_data['birthday'])
        self.register_time =  str(post_data['register_time'])
        self.dbtable = str(post_data['table'])
        self.dbcolumns = str(post_data['columns'])

        self.values = self.id+",'"+self.name+"','"+self.email+"','" +self.birthday+"','" + self.register_time+"'"
        self.statement = 'INSERT INTO ' + self.dbtable + '('+self.dbcolumns+')'+' VALUES (' + self.values + ')'
        #  
    def insert(self):
        print(self.statement)
        # print(self.columns)
        # print("'"+str(self.id)+"','"+self.name+"','"+self.birthday+"','"+self.register_time+"'")
        print(self.statement)
        db_connection = psycopg2.connect(dbname= 'email', user= 'plusone')
        mark = db_connection.cursor()
        mark.execute(self.statement)
        db_connection.commit()

# post_data = {
#   "birthday": "2011-10-21", 
#   "columns": "id, name, email, birthday, register_time", 
#   "email": "my1@emxample.com", 
#   "name": "apple", 
#   "phone": "0912923232", 
#   "table": "users",
#   "register_time":"2018-10-11"
# }
# insert_data = PostgreDbProcess(post_data)
# insert_data.insert()
