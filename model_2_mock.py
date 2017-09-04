from wrapper_mock import Markit
import sqlite3
from ORM_mock import ORM
class model(object):
	
	@classmethod
	def Buy(self,user,vol,stock_symbol):
		ORM.buy(user,vol,stock_symbol)
		
		# import sqlite3

		# connection = sqlite3.connect('trading.db')
		# cursor = connection.cursor()
		# cursor.execute("SELECT balance FROM users WHERE username ='{}'".format(user))
		# bal=cursor.fetchone()
		# bal=bal[0]
		# original_price_per_stock=Markit.get_quote(stock_symbol)['LastPrice']
		# print("original price per stock "+str(original_price_per_stock))
		# investment=original_price_per_stock*float(vol)
		# print("This is the investment "+str(investment))
		# print("This is the balance "+str(bal))
		# stock=Markit.get_quote(stock_symbol)['Name']
		# print("Stock name "+stock)

		# if investment>bal:
		# 	print("You are too greedy!")
		# else:
		# 	bal_left=bal-investment

		# 	cursor.execute("UPDATE users SET balance={} WHERE username='{}'".format(bal_left,user))
		# 	cursor.execute("INSERT INTO portfolio('username','stock_name','stock_symbol','last_price','volume','portfolio_value') VALUES('{}','{}','{}','{}','{}','{}')".format(user,stock,stock_symbol,original_price_per_stock,vol,investment))
		# 	#cursor.execute("INSERT INTO portfolio(username, stock_name, stock_symbol, last_price, volume, portfolio_value) VALUES(?,?,?,?,?,?)", (user,stock_name,stock_symbol,original_price_per_stock,vol,investment))
		# connection.commit()
		# cursor.close()
		# connection.close()

	@classmethod
	def Sell(self,user,vol,stock_symbol):
		ORM.sell(user,vol,stock_symbol)
		# connection = sqlite3.connect('trading.db')
		# cursor = connection.cursor()
		# cursor.execute("SELECT stock_name FROM users WHERE username={} AND stock_symbol={}".format(user,stock_symbol))
		# test_stock=cursor.fetchone()
		# if test_stock is None:
		# 	print("You dont have that stock!")
		# else:
		# 	cursor.execute("SELECT volume FROM users WHERE username={} AND stock_symbol={}".format(user,stock_symbol))
		# 	test_vol=cursor.fetchone()
		# 	test_vol=(test_vol[0])

		# 	if test_vol<vol:
		# 		print("You are full of shit")
		# 	else:
		# 		original_price_per_stock=Markit.get_quote(stock_symbol)['LastPrice']
		# 		money=original_price_per_stock*test_vol
		# 		cursor.execute("SELECT balance FROM users WHERE username ={}".format(user))
		# 		bal=cursor.fetchone()
		# 		bal=bal[0]
		# 		bal_new=bal+money
		# 		vol_new=test_vol-vol
		# 		cursor.execute("UPDATE users SET balance=bal_new WHERE username={}".format(user))
		# 		cursor.execute("UPDATE portfolio SET 'last_price'=original_price_per_stock,'volume'=vol_new,'portfolio_value'= money WHERE username={}".format(user)) 
		# 		connection.commit()
		# 		cursor.close()
		# 		connection.close()

	@classmethod
	def create_account(self,username,password):
		ORM.create(username,password)
		# connection = sqlite3.connect('trading.db')
		# cursor = connection.cursor()
		# cursor.execute("INSERT INTO users('username','password','balance') VALUES('{}','{}',100000)".format(username,password))
		# connection.commit()
		# cursor.close()
		# connection.close()

	@classmethod
	def check_userid(self,username):
		return ORM.checkUserID(username)
		# connection = sqlite3.connect('trading.db')
		# cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE username='{}'".format(username))
		# if cursor.fetchone() is not None:
		# 	return True

		# else:
		# 	return False
	@classmethod
	def check_pass(self,password):
		return ORM.checkPass(password)
		# connection = sqlite3.connect('trading.db')
		# cursor = connection.cursor()
		# cursor.execute("SELECT * FROM users WHERE password='{}'".format(password))
		# if cursor.fetchone() is not None:
		# 	return True

		# else:
		# 	return False
	@classmethod
	def View_Profile(self,userid):
		ORM.view_profile(userid)







	

