import psycopg2
def insert(table, columns, values):
    db_connection = psycopg2.connect(dbname= 'mydb', user= 'plusone')
    mark = db_connection.cursor()
    #  INSERT INTO <table> (columns) VALUES (values) ; 
    statement = 'INSERT INTO ' + table + ' (' + columns + ') VALUES (' + values + ')'
    mark.execute(statement)
    db_connection.commit()

table = 'users'
fields = "id, birthday, phone, name, email"
values = " 4, '2006-07-16','0987115421','alex','alex@example.com' "
insert(table, fields, values) 