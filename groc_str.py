items=[]
while True :
	print("---------------Welcome to ITI groceries---------------")
	op1=input("Owner enter 1 , Customer enter 2 , Exit enter 0: \n")
	if op1=='1':
		op2=input("add new items enter 1 , exit enter 0: \n")
		if op2 =='1':
			print("~~~~~~~~~adding new items~~~~~~~~~")
			item={}
			item['name']=input("item name : ")
			while True: 
				try:
					item['quantity'] = int(input("item quantity : "))
					break
				except 	ValueError:
					print("enter numbers")
			while True:
				try:
					item['price'] = int(input("price : "))
					break
				except 	ValueError:
					print("enter numbers")
			items.append(item)
			print("successfully added.")
		elif op2 =='0':
			print("------------exit-----------")
			break;
		else:
			print("invalid input")
	elif op1 == '2':
		op3=input("view items enter 1 , make a purchase 2 ,exit enter 0: \n")
		if op3 == '1':
			print("~~~~~~~~~~available items~~~~~~~~~")
			while len(items) !=0:
				print("available items .")
				for item in items:
					for key, value in item.items():
						print(key, ':', value)
				break
		elif op3 == '2':
			print("~~~~~~~~~~~~purchase~~~~~~~~")
			print(items)
			buy = input("enter name of product: ")
			for item in items:
				if buy.lower()==item['name'].lower():
					if item ['quantity']!=0:
						print('pay ', item['price'])
						item['quantity']-=1
					else:
						print("out of stock")
		elif op3 =='0':
			print("------------exit-----------")
			break;
		else:
			print("invalid input")
	elif op1 =='0':
			print("------------exit-----------")
			break;
	else:
		print("invalid input")		