import psycopg2
from flask import jsonify


class PostgreDbProcess:
    
    # connect to email DB
    db_connection = psycopg2.connect(dbname= 'email', user= 'plusone')
    mark = db_connection.cursor()
    
    def __init__(self, post_data):
        self.post_data = post_data
    def insert(self):
        
        # val 
        PostgreDbProcess.id = str(11)
        PostgreDbProcess.dbtable = str(self.post_data['table'])
        PostgreDbProcess.dbcolumns = str(self.post_data['columns'])
        PostgreDbProcess.name = str(self.post_data['name'])
        PostgreDbProcess.email = str(self.post_data['email'] + 'plusmail.example.com')
        PostgreDbProcess.birthday = str(self.post_data['birthday'])
        PostgreDbProcess.register_time =  str(self.post_data['register_time'])

        # sql 
        self.values = self.id+",'"+self.name+"','"+self.email+"','" +self.birthday+"','" + self.register_time+"'"
        self.statement = 'INSERT INTO ' + self.dbtable + '('+self.dbcolumns+')'+' VALUES (' + self.values + ')'
   
        # insert data to DB
        PostgreDbProcess.mark.execute(self.statement)
        PostgreDbProcess.db_connection.commit()

    def delete_user(self):
        PostgreDbProcess.user_id = self.post_data
        self.statement = 'DELETE FROM users Where id = ' + PostgreDbProcess.user_id +';'
        print(self.statement)
        
        # commit to db
        PostgreDbProcess.mark.execute(self.statement)
        PostgreDbProcess.db_connection.commit()
