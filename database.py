import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pesu_sports"
)
c = mydb.cursor()


def add_user(new_user,new_pass):
    c.execute('INSERT INTO users(user,password) values(%s,%s)',(new_user,new_pass))
    mydb.commit()

def view_users():
    c.execute('SELECT * FROM users')
    data=c.fetchall()
    return data


def add_data(ename,sd,ed,ven,sp,io,desc,e):
    c.execute('INSERT INTO event VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(ename,sd,ed,ven,sp,io,desc,e))
    mydb.commit()

def view_events():
    c.execute('SELECT * FROM event')
    data=c.fetchall()
    return data

def add_team_details(a,b,c2):
    c.execute('INSERT INTO enter_team VALUES (%s,%s,%s)',(a,b,c2))
    mydb.commit()

def view_team():
    c.execute('SELECT * FROM enter_team INNER JOIN event ON event.event_id=enter_team.event_id')
    data=c.fetchall()
    return data

def add_results(x,y,z,a,b):
    c.execute('INSERT INTO results VALUES (%s,%s,%s,%s,%s)',(x,y,z,a,b))
    mydb.commit()

def view_results():
    c.execute('SELECT * FROM results')
    data=c.fetchall()
    return data

def view_entry():
    c.execute('SELECT * FROM entry')
    data=c.fetchall()
    return data

def add_entry(m,n,o,p):
    c.execute('INSERT INTO entry(SRN,in_out,sport,guard_name) VALUES(%s,%s,%s,%s)',(m,n,o,p))
    mydb.commit()

def add_coach_details(a,b,d,e):
    c.execute('INSERT INTO coach VALUES(%s,%s,%s,%s)',(a,b,d,e))
    mydb.commit()

def show_coach_details():
    c.execute('SELECT * FROM coach')
    data=c.fetchall()
    return data 

def delete_data(eid):
    c.execute('DELETE FROM event WHERE event_id="{}"'.format(eid))
    mydb.commit()

def update_venue(eid,new_venue):
    c.execute('UPDATE event SET venue=%s WHERE event_id=%s',(new_venue,eid))
    mydb.commit()

def update_date(eid,sd,ed):
    c.execute('UPDATE event SET start_date=%s,end_date=%s WHERE event_id=%s',(sd,ed,eid))
    mydb.commit()

#def create_procedure():
   # c.execute('CREATE function find_no_teams(eid int) begin declare final result; select count(*) into final from enter_team where event_id=eid')

def count_teams(eid):
    c.execute('SELECT find_teams({})'.format(eid))
    data=c.fetchall()
    return data

#create_procedure()
def query(q):
    c.execute(q)
    return c.fetchall()
    