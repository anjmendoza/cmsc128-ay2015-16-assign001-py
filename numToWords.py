#!/usr/bin/env python
#Mendoza, Ma. Angelica E.
#2013-20378
#AB-3L
#Programming Assignment #1
#Enables the user to input a number from 0 to 1 million and returns the word equivalent of it
# SOurce: #http://stackoverflow.com/questions/8982163/how-do-i-tell-python-to-convert-integers-into-words

#variable declarations
case1 = {0:'zero',1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6:'six', \
            7:'seven', 8:'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'\
            ,13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17:'seventeen'\
            ,18: 'eighteen', 19: 'nineteen'}
case2 = {1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
case3 = [' hundred', ' thousand', ' million']

#function that passes an integer and prints the word equivalent of it
def numToWords(integer):
	#temporary variable
	temp = 0
	#if-else statements to control the flow of the program
	#if the number entered by the user is less than 0, it is invalid
	if integer < 0:
		print "Wrong Input"
	#if the number entered by the user is greater than 0 but less than 20
	elif integer >= 0 and integer < 20: # 1-19
		#calls the array and passes the integer to search its value
		print case1[integer]
	#if the number entered by the user is greater than 20 but less than 100
	elif integer >= 20 and integer < 100:  # 20 -99
		 temp = integer%10
		 if temp > 0:
		 	print case2[integer/10] + " - " + case1[temp]	#21, 22,etc
		 else:
		 	print case2[integer/10]							#30, 40, 50
	elif integer >= 100 and integer < 1000: # 100 -999
		temp = integer % 100
		if temp > 0 and temp < 20:
			print case1[integer/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
		elif temp >=20 and temp < 100:
			if (temp%10) > 0:
				print case1[integer/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
		 	else:
		 		print case1[integer/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
		else:
		 	print case1[integer/100] + case3[0]		#100, 200, 3000
	elif integer >= 1000 and integer < 10000:	#1000-9999
		temp = integer % 1000
		if temp > 0 and temp < 20:
			print case1[integer/1000] + case3[1]+ " " + case1[temp]				#1009, 1008, 1007
		elif temp >=20 and temp < 100:
			if (temp%10) > 0:
				print case1[integer/1000] + case3[1]+ " " + case2[temp/10] + " - " + case1[temp%10]		#1021, 1022, 1023
		 	else:
		 		print case1[integer/1000] + case3[1]+ " " + case2[temp/10]		#1020,1030, etc
		elif temp >=100 and temp < 1000:
			if (temp%100) > 0 and (temp%100) < 20:
				print case1[integer/1000] + case3[1]+ " " + case1[temp/100] + case3[0] + " " + case1[temp%100] #1101, 1102, 103
			elif (temp%100) >=20 and (temp%100)<100:
				if((temp%100)%10) > 0:
					print case1[integer/1000] + case3[1]+ " " + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10] + " - " + case1[(temp%100)%10]
				else:
		 			print case1[integer/1000] + case3[1]+ " " + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10]
		else:
		 	print case1[integer/1000] + case3[1]
	elif integer >= 10000 and integer < 100000:
		temp  = integer % 10000
		print(temp)
		if temp > 0 and temp < 10:
			print case2[integer/10000] + case3[1] + " " + case1[temp]
		elif temp >= 20 and temp < 100:
			if (temp%10) > 0:
				print case2[integer/10000] + case3[1]+ " " + case2[temp/10] + " - " + case1[temp%10]		#1021, 1022, 1023
		 	else:
		 		print case2[integer/10000] + case3[1]+ " " + case2[temp/10]
		elif temp >=100 and temp < 1000:
			if (temp%100) > 0 and (temp%100) < 20:
				print case2[integer/10000] + case3[1]+ " " + case1[temp/100] + case3[0] + " " + case1[temp%100] #1101, 1102, 103
			elif (temp%100) >=20 and (temp%100)<100:
				if((temp%100)%10) > 0:
					print case2[integer/10000] + case3[1]+ " " + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10] + " - " + case1[(temp%100)%10]
				else:
		 			print case2[integer/10000] + case3[1]+ " " + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10]
		elif temp >= 1000 and temp < 10000:
			temp = integer % 1000
			if temp > 0 and temp < 10:
				if(integer/1000 >= 20):
					print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1] + " " + case1[temp]
				else:
					print case1[integer/1000] + case3[1] + " " + case1[temp]
			elif temp >= 20 and temp < 100:
				if (temp%10) > 0:
					if(integer/1000>=20):
						print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1] + " " + case2[temp/10] + " - " + case1[temp%10]		#1021, 1022, 1023
			 		else: 
			 			print case1[integer/1000] + case3[1] + " " + case2[temp/10] + " - " + case1[temp%10]		#1021, 1022, 1023
			 	else:
			 		if(integer/1000>=20):
			 			print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1] + " " + case2[temp/10]
			 		else:
			 			print case1[integer/1000] + case3[1] + " " + case2[temp/10]
			elif temp >=100 and temp < 1000:
				if (temp%100) > 0 and (temp%100) < 20:
					if(integer/1000>=20):
						print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1] + " " + case1[temp/100] + case3[0] + " " + case1[temp%100] #1101, 1102, 103
					else:
						print case1[integer/1000] + case3[1] + " " + case1[temp/100] + case3[0] + " " + case1[temp%100] #1101, 1102, 103
				elif (temp%100) >=20 and (temp%100)<100:
					if((temp%100)%10) > 0:
						if(integer/1000>=20):
							print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1] + " "  + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10] + " - " + case1[(temp%100)%10]
						else:
							print case1[integer/1000] + case3[1] + " "  + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10] + " - " + case1[(temp%100)%10]
					else:
						if(integer/1000>=20):
			 				print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1] + " " + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10]
						else:
							print case1[integer/1000] + case3[1] + " " + case1[temp/100] + case3[0] + " " + case2[(temp%100)/10]
			else:
				if(integer/1000>=20):
					print case2[integer/10000] + " " +  case1[(integer/1000)%10] + case3[1]
				else:
					print case1[integer/1000] + case3[1] 
		else:
			if(integer/1000<=20):
				print case2[integer/10000] + case3[1]
			else:
				print case1[integer/1000] + case3[1]
	elif integer >=100000 and integer < 1000000:
		temp1 = (integer/1000)%100
		temp = (integer%100000) % 100
		if temp1 > 0 and temp1 < 20:
			if temp > 0 and temp < 20:
				if((integer%1000)/100 > 0): 
					print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
				else:
					print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] +  " " + case1[temp]
			elif temp >=20 and temp < 100:
				if (temp%10) > 0:
					if((integer%1000)/100 > 0): 
						print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 		else:
			 			print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] +  " " + case2[temp/10] + " - " + case1[temp%10] 
			 	else:
			 		if((integer%1000)/100 > 0): 
			 			print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
					else:
						print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case2[temp/10]			#130, 140, 150
			else:
				if((integer%1000)/100 >0):
			 		print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 	else:
			 		print case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1]
		elif temp1 >=20 and temp1 < 100:
			if (temp1%10) > 0:
				#print case1[integer/100] + case3[0]+ " " + case2[temp1/10] + " - " + case1[temp1%10] 	#121, 122, 123
				if temp > 0 and temp < 20:
					if((integer%1000)/100 >0):
						print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
					else:
						print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] +  " " + case1[temp]	
				elif temp >=20 and temp < 100:
					if (temp%10) > 0:
						if((integer%1000)/100 >0):
							print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 			else:
			 				print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " +  case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 		else:
			 			if((integer%1000)/100 >0):
			 				print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1]  + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
						else:
							print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1]  + " " + case2[temp/10]			#130, 140, 150
				else:
					if((integer%1000)/100 >0):
			 			print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 		else:
			 			print case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] 	
		 	else:
		 		if temp > 0 and temp < 20:
					print case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
				elif temp >=20 and temp < 100:
					if (temp%10) > 0:
						print case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 		else:
			 			print case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1]  + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
				else:
					if((integer%1000)/100 >0):
			 			print case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 		else:
			 			print case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] 	
		else:
			if temp > 0 and temp < 20:
				if ((integer%1000)/100) > 0:
					print case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
				else:
					print case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[temp]
			elif temp >=20 and temp < 100:
				if ((integer%1000)/100) > 0:
					if (temp%10) > 0:
						print case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
					else:
				 		print ccase1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
				else:
					if (temp%10) > 0:
						print case1[integer/100000] + case3[0] + " " + case3[1] + " " +  case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
					else:
				 		print case1[integer/100000] + case3[0] + " " + case3[1] + " " +  case2[temp/10]			#130, 140, 150
			else:
				if((integer%1000)/100 >0):
					print case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 	else:
			 		print case1[integer/100000] + case3[0] + " " + case3[1]	
	


	elif integer >= 1000000 and integer < 10000000:
		million=integer/1000000
		integer=integer-(1000000*million)
		temp1 = (integer/1000)%100
		temp = (integer%100000) % 100
		if temp1 > 0 and temp1 < 20:
			if temp > 0 and temp < 20:
				if((integer%1000)/100 > 0): 
					print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
				else:
					print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] +  " " + case1[temp]
			elif temp >=20 and temp < 100:
				if (temp%10) > 0:
					if((integer%1000)/100 > 0): 
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 		else:
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] +  " " + case2[temp/10] + " - " + case1[temp%10] 
			 	else:
			 		if((integer%1000)/100 > 0): 
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
					else:
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case2[temp/10]			#130, 140, 150
			else:
				if((integer%1000)/100 >0):
			 		print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 	else:
			 		print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case1[temp1]+ case3[1]
		elif temp1 >=20 and temp1 < 100:
			if (temp1%10) > 0:
				#print case1[integer/100] + case3[0]+ " " + case2[temp1/10] + " - " + case1[temp1%10] 	#121, 122, 123
				if temp > 0 and temp < 20:
					if((integer%1000)/100 >0):
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
					else:
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] +  " " + case1[temp]	
				elif temp >=20 and temp < 100:
					if (temp%10) > 0:
						if((integer%1000)/100 >0):
							print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 			else:
			 				print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " +  case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 		else:
			 			if((integer%1000)/100 >0):
			 				print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1]  + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
						else:
							print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1]  + " " + case2[temp/10]			#130, 140, 150
				else:
					if((integer%1000)/100 >0):
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 		else:
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10]+  " - " + case1[temp1%10] + " " + case3[1] 	
		 	else:
		 		if temp > 0 and temp < 20:
					print case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
				elif temp >=20 and temp < 100:
					if (temp%10) > 0:
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
			 		else:
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1]  + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
				else:
					if((integer%1000)/100 >0):
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 		else:
			 			print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0]+ " " + case2[temp1/10] + " " + case3[1] 	
		else:
			if temp > 0 and temp < 20:
				if ((integer%1000)/100) > 0:
					print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case1[temp]		#109, 108, 107
				else:
					print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[temp]
			elif temp >=20 and temp < 100:
				if ((integer%1000)/100) > 0:
					if (temp%10) > 0:
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
					else:
				 		print case1[million] + " " + case3[2] + " " + ccase1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]+ " " + case2[temp/10]			#130, 140, 150
				else:
					if (temp%10) > 0:
						print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1] + " " +  case2[temp/10] + " - " + case1[temp%10] 	#121, 122, 123
					else:
				 		print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1] + " " +  case2[temp/10]			#130, 140, 150
			else:
				if((integer%1000)/100 >0):
					print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1] + " " + case1[(integer%1000)/100] + case3[0]		#100, 200, 3000
			 	else:
			 		print case1[million] + " " + case3[2] + " " + case1[integer/100000] + case3[0] + " " + case3[1]	
	else:
		print "Number is too large"
			 					
user_input= int(input("Enter the number: "))
print (user_input)
numToWords(user_input)