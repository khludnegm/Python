
mode = input("For standard calculator press : 1\nFor programmer calculator press : 2\n")
while True:
	if mode == '1':
		number_1 = int(input("Enter first number: "))
		number_2 = int(input("Enter second number: "))
		print("available operations:\n"
		"1. Add "
		"2. Subtraction "
		"3. Multiply "
		"4. Division")
		select = int(input("Select operation from 1, 2, 3, 4 :"))
		
		if select == 1:
			sum=number_1+number_2
			print(number_1, "+", number_2, "=",sum)

		elif select == 2:
			sub=number_1-number_2
			print(number_1, "-", number_2, "=",sub)

		elif select == 3:
			multiply=number_1*number_2
			print(number_1, "*", number_2, "=",multiply)

		elif select == 4:
			divide=number_1/number_2
			print(number_1, "/", number_2, "=",divide)
		else:
			print("Invalid input")
		new=input("another operation? (yes/no)\n")
		if(new == "no"):
			break	
	
	elif mode == '2':
		select = input("available operations:\n"
		"1. number convertion "
		"2. bitwise operations")
		if select == "1":
			number= int(input("enter a decimal number\n"))
			convert = input("Convert the decimal number to:\n"
			"1.Binary "
			"2.Octal "
			"3.Hexadecimal")
			if convert == '1':
				print("binary of" , number, "is" , bin(number) )
			elif convert == '2':
				print("Octal of" , number, "is" , oct(number) )
			elif convert == '3':
				print("Hexadecimal of" , number, "is" , hex(number) )
			else:
				print("Invalid number")	
				
			new=input("another convertion? (yes/no)\n")
			if(new == "no"):
				break
		elif select == "2":
			num1 = int(input("enter first number\n"))
			num2 = int(input("enter second number\n"))
			choice = input("available Oprations :\n"
			"1.bitwise AND "
			"2.bitwise OR "
			"3.bitwise XOR "
			"4.Shift left "
			"5.Shift Right")
			if choice == '1':
				print(num1, "&", num2, "=", num1&num2, "\nwhich equal", bin(num1&num2), "in binary\n" )
			elif choice == '2':
				print(num1, "|", num2, "=",num1|num2, "\nwhich equal", bin(num1&num2), "in binary\n" )
			elif choice == '3':
				print(num1, "^", num2 ,"=" ,num1^num2, "\nwhich equal", bin(num1&num2), "in binary\n" )
			elif choice == '4':
				print(num1, "<<", num2 ,"=" ,num1<<num2, "\nwhich equal", bin(num1<<num2), "in binary\n" )
			elif choice == '5':
				print(num1, ">>", num2 ,"=" ,num1>>num2, "\nwhich equal", bin(num1>>num2), "in binary\n" )
			else:
				print("Invalid choice")
			new=input("another operation? (yes/no)\n")
			if(new == "no"):
				break
		else:
			print("Invalid number")
	else:
		print("Invalid number")