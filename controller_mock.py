from wrapper_mock import Markit
from model_2_mock import model

while(True):
	print("Here are your options:")
	print("1.Click on 1 to get ticker symbol of the company you want to know about")
	print("2. Click on 2 to get relevant info before buying stock")
	print("3. CLick on 3 if you want to buy and sell stock or view your portfolio")
	print("4. Click on 4 if you are visiting for the first time and you want to make your account")
	print("5. Click 5 to quit")

	x=int(input("?"))

	if x==1:
		company=input("Enter name of company: ")
		print(Markit.company_search(company))

		X=int(input("Enter index of exchange to get corresponding symbol(seems pretty dumb right...)"))
		

		ticker=Markit.company_search(company)[X]['Symbol']
		print("**********************")
		print("                       ")
		print("Ticker Symbol: "+ticker)
		print("                       ")

		print("***********************")

	elif x==2:
		symbol=input("Enter symbol of stock: ")
		print(Markit.get_quote(symbol))
	


	elif x==3:
		userid=input("Enter userid")
		password=input("Enter password")
		if model.check_userid(userid):
			if model.check_pass(password):
				print("Login successful!")

				opt=int(input("Click 4 to buy ,5 to sell stock and 6 to view their portfolio"))
				if opt==4:
					print("you entered 4")
					symbol=input("Enter symbol of stock")
					print("your symbol is "+symbol)
					vol=input("Enter vol you want to buy")
					print("your vol is "+vol)
					model.Buy(userid,vol,symbol)
				elif opt==5:
					symbol=input("Enter symbol of stock")
					vol=input("Enter vol you want to sell")
					model.Sell(userid,vol,symbol)

				elif opt==6:
					model.View_Profile(userid)
	

		else:
			print("I'm  hurt")
			break
	elif x==4:
		userid=input("Enter userid")
		password=input("Enter password")
		model.create_account(userid,password)

	elif x==5:
		print("Bye")
		break
	








