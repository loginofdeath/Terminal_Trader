from wrapper_mock import Markit
import sqlite3
import pandas as pd

class ORM(object):
	@classmethod
	def buy(self,user,vol,stock_symbol):
		import sqlite3

		connection = sqlite3.connect('trading.db')
		cursor = connection.cursor()
		cursor.execute("SELECT balance FROM users WHERE username ='{}'".format(user))
		bal=cursor.fetchone()
		bal=bal[0]
		original_price_per_stock=Markit.get_quote(stock_symbol)['LastPrice']
		print("original price per stock "+str(original_price_per_stock))
		investment=original_price_per_stock*float(vol)
		print("This is the investment "+str(investment))
		print("This is the balance "+str(bal))
		stock=Markit.get_quote(stock_symbol)['Name']
		print("Stock name "+stock)

		if investment>bal:
			print("You are too greedy!")
		else:
			bal_left=bal-investment

			#cursor.execute("UPDATE users SET balance={} WHERE username='{}'".format(bal_left,user))
			cursor.execute("INSERT INTO portfolio('username','stock_name','stock_symbol','last_price','volume','portfolio_value') VALUES('{}','{}','{}','{}','{}','{}')".format(user,stock,stock_symbol,original_price_per_stock,vol,investment))
			#cursor.execute("INSERT INTO portfolio(username, stock_name, stock_symbol, last_price, volume, portfolio_value) VALUES(?,?,?,?,?,?)", (user,stock_name,stock_symbol,original_price_per_stock,vol,investment))
		connection.commit()
		cursor.close()
		connection.close()

	@classmethod
	def sell(self,user,vol,stock_symbol):
		connection = sqlite3.connect('trading.db')
		cursor = connection.cursor()
		cursor.execute("SELECT stock_name FROM portfolio WHERE username='{}' AND stock_symbol='{}'".format(user,stock_symbol))
		test_stock=cursor.fetchone()
		if test_stock is None:
			print("You dont have that stock!")
		else:
			cursor.execute("SELECT volume FROM portfolio WHERE username='{}' AND stock_symbol='{}'".format(user,stock_symbol))
			test_vol=cursor.fetchone()
			test_vol=int((test_vol[0]))
			print("vol: "+vol)
			print("test_vol: "+str(test_vol))

			if test_vol<int(vol):
				print("You are being naughty ")
			else:
				original_price_per_stock=Markit.get_quote(stock_symbol)['LastPrice']
				money=original_price_per_stock*test_vol
				cursor.execute("SELECT balance FROM users WHERE username ='{}'".format(user))
				bal=cursor.fetchone()
				bal=bal[0]
				bal_new=bal+money
				vol_new=test_vol-int(vol)
				cursor.execute("UPDATE users SET balance={} WHERE username='{}'".format(bal_new,user))
				cursor.execute("UPDATE portfolio SET last_price={},volume={},portfolio_value= {} WHERE username='{}'".format(original_price_per_stock,vol_new,money,user)) 
				connection.commit()
				cursor.close()
				connection.close()
	@classmethod
	def create(self,username,password):
		connection = sqlite3.connect('trading.db')
		cursor = connection.cursor()
		cursor.execute("INSERT INTO users('username','password','balance') VALUES('{}','{}',100000)".format(username,password))
		connection.commit()
		cursor.close()
		connection.close()
	@classmethod
	def checkUserID(self,username):
		connection = sqlite3.connect('trading.db')
		cursor = connection.cursor()
		#print("hey")
		cursor.execute("SELECT * FROM users WHERE username='{}'".format(username))
		#print("hey")
		if cursor.fetchone() is not None:
			#print("hey its true")
			return True

		else:
			return False

	@classmethod
	def checkPass(self,password):
		connection = sqlite3.connect('trading.db')
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM users WHERE password='{}'".format(password))
		if cursor.fetchone() is not None:
			return True

		else:
			return False

	@classmethod
	def view_profile(self,userid):
		connection = sqlite3.connect('trading.db')
		cursor = connection.cursor()
		cursor.execute("DELETE FROM portfolio WHERE volume=0")
		connection.commit()


		sql="SELECT * FROM portfolio WHERE username='{}'".format(userid)
		print()
		print("***********************************************************")
		df = pd.read_sql_query(sql,connection)
		print (df)
		print()
		print("***********************************************************")

		cursor.close()
		connection.close()



















