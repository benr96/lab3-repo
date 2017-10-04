
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.189.212.110'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''drop table students''')
    cur.execute('''CREATE TABLE students (studentName VARCHAR(255), email VARCHAR(255), studentID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(studentID))''')
    cur.execute('''insert into students(studentName, email) values("student1","student1@mydit.ie")''')
    cur.execute('''insert into students(studentName, email) values("student2","student2@mydit.ie")''')
    cur.execute('''insert into students(studentName, email) values("student3","student3@mydit.ie")''')
    cur.execute('''update students set studentName = "Bob" where studentName = "student1"''')
    cur.execute('''delete from students where studentName = "student2"''')
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return str(rv)      #Return the data in a string format

@app.route("/html")
def hello2():
	return('<html><body><h1>HELLO WORLD</h1></body></html>')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

