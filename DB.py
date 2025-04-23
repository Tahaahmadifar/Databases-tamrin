import psycopg2
from psycopg2 import connect

connection_to_db = psycopg2.connect(host="Localhost", database='taha1', user='postgres', password='ta0509ha')
connection = connection_to_db.cursor()

lst = [(1,"taha","ahmadi"), (2,"arad","afkar"), (3,"mahan","bazogh"), (4,"mohammadmahdi","lotfi")]
for id, name, family in lst:
    connection.execute("insert into db(id, name, family) values(%s, %s, %s)", (id, name, family))
    connection_to_db.commit()

found = False
var_name = input("please enter name:")
var_family = input("please enter family:")
connection.execute("select * from db")
connection_to_db.commit()
var_search = connection.fetchall()
for i in var_search:
    if var_name == i[1] and var_family == i[2]:
        found = True
if found:
    print("a user with these characteristice exists")
else:
    print("there is no user with these characteristice exists")
