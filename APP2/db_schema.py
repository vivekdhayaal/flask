import sqlite3

def connect():
	con = sqlite3.connect('db1.db')
	cur = con.cursor()
	return con, cur

def insert_emp_record(data):
	err = ""
	inserted = ""
	con,cur = connect()
	try:
		query = "insert into employees values('%(empname)s','%(password)s','%(address)s')"%data
		cur.execute(query)
		inserted = True
	except Exception as err:
		pass
	finally:
		con.commit()
		cur.close()
		con.close()
	if inserted:
		return True
	else:
		return err


if __name__ == "__main__":
	con, cur = connect()
	query = "create table employees(empname varchar(20), password varchar(20), address varchar(200))"
	cur.execute(query)
