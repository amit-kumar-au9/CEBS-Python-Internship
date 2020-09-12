import mysql.connector as MySQL

def main():
	try:
		conn = MySQL.connect(host="localhost",user="root",passwd="")
		print("Connection Created");

		cursor = conn.cursor()
		dataBase = "cebs_training";
		
		sql = "create database "+dataBase;
		cursor.execute(sql)
		conn.close()

		conn = MySQL.connect(host="localhost",user="root",passwd="",database = dataBase)
		cursor = conn.cursor()
		sql = "create table user(uid integer,name varchar(30),email varchar(30),phone varchar(15))"
		cursor.execute(sql)

		conn.commit()
	except Exception as e:
		print("OOPS Connection Error :",e)


if __name__ == "__main__":
	main()