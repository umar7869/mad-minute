#importing all needed functions
#TABS ONLY
import math
import random
import time
import threading
import pickle
import os
from colorama import Fore
#introductory paragraph/text
#This also includes all of the difficulty settings and which setting you want to select
#introducing varibles for scorboard later

def SavingUmarsIQ():
	UmarsIQ=[0,0,0]
	save_highScore(UmarsIQ)
	
def intro():
	#initializing highscore

	highscore=[]
	
	print("WELCOME TO THE RADDEST MADDEST MATH MINUTE")
	
	print("This program allows you to pick a difficulty and answer various math questions in less than one minute.")
	print(Fore.LIGHTRED_EX+"PLEASE DO NOT USE DECIMALS AS IT WILL COUNT AS INCORRECT")
	
	#ALL DIFFICULTIES
	#1 second intervals to allow user to read
	time.sleep(.5)

	print("HERE ARE YOUR OPTIONS: ")

	time.sleep(.5)
	print()

	print(Fore.CYAN+"PEACEFUL")

	print("The easiest setting that has addition and subtraction to a total sum of 40 or a total difference of 0.")
	
	print()
	time.sleep(.5)
	print(Fore.GREEN+"EASY")

	print("This setting has addition to a total sum of 50, subtraction with a minimum difference of 0 and multiplication and devision up to 5.")

	print()
	
	time.sleep(.5)

	print(Fore.LIGHTYELLOW_EX+"MEDIUM")

	print("This setting has addition to a total sum of 60, subtraction with a minimum difference of 0 and multiplication and devision up to 7.")

	print()
	
	time.sleep(.5)

	print(Fore.LIGHTMAGENTA_EX+"HARD")

	print("This setting has addition to a total sum of 80, subtraction with a minimum difference of 0 and multiplication and devision up to 10.")

	print()
	
	time.sleep(.5)

	print(Fore.RED+"GENUIS")

	print("This setting has addition to a total sum of 100, subtraction with a minimum difference of 0 and multiplication and devision up to 12.")
	
	print()

	#initializing difficulties settings
	#Dio= difficulty
	
	print(Fore.WHITE+"(P/E/M/H/G)")
	print()
	
	

	
	
#converting each latter into its difficulty along with timer and generating questions

def soljaboi():
	#variables
	global highscore
	highscore=[]

	netscore=0
	
	right=0
	
	wrong=0
	
	#initializing difficulties settings
	#Dio= difficulty
	global dio
	dio=input("PLEASE SELECT YOUR DIFFICULTY USING THE FIRST LETTER OF EACH DIFFICULTY: ")
	dio=dio.upper()

	#Timer
	
	from datetime import datetime, timedelta
	end_time=datetime.now()+ timedelta(seconds=60)
	while datetime.now()<end_time:
	
		#peaceful
	
		if dio=="P":
			number1=random.randint(1,20)
			
			number2=random.randint(1,20)
	
			operation=random.randint(1,2)
	
			#generating equation: Adddition
			if operation==1:
				
				compQ=number1+number2
				
				print (number1, "+", number2)
	
				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 0

				netscore= right-wrong

				print("You have a score of", netscore)
				
			#Generating equations: subtraction
				
			if operation == 2:
				compQ=number1-number2
				
				
				#This will make sure the result is not a negative number
				while number2>number1:
					number2=random.randint(1,20)
					compQ=number1-number2
					
					
				print (number1, "-", number2 )

				userC=str(input("Answer: "))

				if str(compQ) == str(userC):
					right += 1

				if str(compQ) != str(userC):
					wrong += 0

				netscore= right-wrong

				print("You have a score of", netscore, )

		#Easy

		elif dio == "E":
			#numbers generator/ operation
			number1= random.randint(1,25)
			number2= random.randint(1,25)
			number3= random.randint(1,5)
			number4= random.randint(1,5)

			operation = random.randint(1,4)

			#addition
			if operation == 1:
				compQ = number1 + number2

				print (number1, "+", number2)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 1

				netscore= right-wrong

				print("You have a score of", netscore, )


			if operation == 2:
				
				compQ=number1-number2

				#This will make sure the result is not a negative number
				while number2>number1:
					number2=random.randint(1,25)

				print (number1, "-", number2 )

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 1

				netscore= right-wrong

				print("You have a score of", netscore, )

			#Multiplication
			
			if operation ==3:
				compQ = number3 * number4

				print (number3, "x", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 1

				netscore= right-wrong

				print("You have a score of", netscore, )

			#Division
			if operation == 4:
				#making sure that the outcome is a whole number
				
				while number3%number4!=0:
					number3=random.randint(1,5)
					number4=random.randint(1,5)
					compQ = int(number3 / number4)

				
				print (number3, "/", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 1

				netscore= right-wrong

				print("You have a score of", netscore, ) 

		#MEDIUM

		elif dio == "M":
			number1= random. randint(1,30)
			number2= random. randint (1,30)
			number3= random. randint (1,7)
			number4 = random. randint (1,7)
			operation = random.randint(1,4)
			#addition
			if operation == 1:
				compQ = number1 + number2

				print (number1, "+", number2)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 2

				netscore= right-wrong

				print("You have a score of", netscore, )

			if operation == 2:
				while number2>number1:
					number2=random.randint(1,30)

				compQ=number1-number2

				#This will make sure the result is not a negative number
				
				print (number1, "-", number2 )

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 2

				netscore= right-wrong

				print("You have a score of", netscore, )

			#Multiplication
			
			if operation ==3:
				compQ = number3 * number4

				print (number3, "x", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 2

				netscore= right-wrong

				print("You have a score of", netscore, )

			#division
			if operation == 4:
				#making sure that the outcome is a whole number
				
				while number3%number4!=0:
					number3=random.randint(1,5)
					
				compQ = int(number3 / number4)


				print (number3, "/", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 2

				netscore= right-wrong

				print("You have a score of", netscore, ) 


		elif dio == "H":

			number1= random. randint(1,40)
			number2= random. randint (1,40)
			number3= random. randint (1,10)
			number4 = random. randint (1,10)
			operation = random.randint(1,4)
			#addition
			if operation == 1:
				compQ = number1 + number2

				print (number1, "+", number2)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 3

				netscore= right-wrong

				print("You have a score of", netscore, )

			if operation == 2:
				
				compQ=number1-number2

				#This will make sure the result is not a negative number
				while number2>number1:
					number2=random.randint(1,40)

				print (number1, "-", number2 )

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 3

				netscore= right-wrong

				print("You have a score of", netscore, )

			#Multiplication
			
			if operation ==3:
				compQ = number3 * number4

				print (number3, "x", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 3

				netscore= right-wrong

				print("You have a score of", netscore, )

			#division
			if operation == 4:
				#making sure that the outcome is a whole number
				
				while number3%number4!=0:
					number3=random.randint(1,10)
					number4=random.randint(1,10)
					compQ = int(number3 / number4)


				print (number3, "/", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 3

				netscore= right-wrong

				print("You have a score of", netscore, ) 

		elif dio == "G":
			number1= random. randint(1,50)
			number2= random. randint (1,50)
			number3= random. randint (1,12)
			number4 = random. randint (1,12)
			operation = random.randint(1,4)
			#addition
			if operation == 1:
				compQ = number1 + number2
				

				print (number1, "+", number2)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 5

				netscore= right-wrong

				print("You have a score of", netscore, )

			if operation == 2:
				while number2>number1:
					number2=random.randint(1,40)
				
				compQ=number1-number2
				

				#This will make sure the result is not a negative number


				print (number1, "-", number2 )

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 5

				netscore= right-wrong

				print("You have a score of", netscore, )

			#Multiplication
			
			if operation ==3:
				compQ = number3 * number4
				

				print (number3, "x", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 5

				netscore= right-wrong

				print("You have a score of", netscore, )

			#division
			if operation == 4:
				#making sure that the outcome is a whole number
				
				while number3%number4!=0:
					number3=random.randint(1,5)
					number4=random.randint(1,5)
				compQ = int(number3 / number4)
				
				


				print (number3, "/", number4)

				userC=str(input("Answer: "))

				if str(compQ) == userC:
					right += 1

				if str(compQ) != userC:
					wrong += 5 

				netscore= right-wrong

				print("You have a score of", netscore, ) 
		elif dio== "B":
			right += 100
			os.system("clear")
			print("YOU HAVE UNLOCKED BRICKNELL MODE")
			print("YOU HAVE BEEN GIVEN 100 STARTING POINTS")
			print("USE THEM WISELY AND SELECT A PROPER GAMEMODE")
			dio=(input(""))
			dio=dio.upper()
		elif dio== "CRANK":
			wrong += 1000
			os.system("clear")
			print("YOU HAVE UNLOCKED MATTHEW MODE")
			print("YOU HAVE BEEN GIVEN -1000 STARTING POINTS")
			print("USE THEM WISELY AND SELECT A PROPER GAMEMODE")
			dio=(input(""))
			dio=dio.upper()

		else:
			os.system("clear")
			print ("You have found an easter egg. Good job. Now select a proper difficulty as you are losing time as you read this")
			dio=(input(""))
			dio=dio.upper()


			
		
	os.system("clear")
	print("TIMES UP")
	highscore=load_highScore("highscore.pickle")
	highscore.append(netscore)
	save_highScore(highscore)
	
	sortedscore= sorted(load_highScore("highscore.pickle"))
	print("the current highsscores are ", sortedscore[-1],sortedscore[-2],sortedscore[-3])
def save_highScore(backout):
    try: #creates file under name "highscore.pickle"
        with open("highscore.pickle", "wb") as f:
            pickle.dump(backout, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex: 
        print("Error during pickling object (Possibly unsupported):", ex)

def load_highScore(blowing):
    try: #loads file if anything is in file
        with open(blowing, "rb") as f: 
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)



	

				







				

			


				
					
				

				
	
				
				

			
			

		#using if statment to regenerate subtraction equation if difference is below 0

intro()
soljaboi()

print("")

print(Fore.BLUE+"Please re-run code to try again.")

print(Fore.RED+"To reset highscores, please input 'SavingUmarsIQ()' right now.")
