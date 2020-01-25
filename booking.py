import os
### prettytable is used to show booking information in tabular format...
from prettytable import PrettyTable

### booking is dictionary which is created to store values temporarily because i am not using any Database application to store data.
### booking dictionary has keys as facility and their values are booking information.

booking = {"Tennis_Court":[["","","","Available"]],"Club_House":[["","","","Available"]],"Badminton_Court":[["","","","Available"]]}

### input_time_date() function is created to take input(date,in_time,out_time) from user...
### input_time_date() function perform validation on user input and check for already booked slot...

def input_time_date(facility):
	date = input("\nEnter Date(yyyy-mm-dd) : ")
	if len(date)<10 or date[4]!="-" or date[7]!="-" or int(date[5:7])>12 or int(date[8:10])>31:
		print("\nINVALID DATE FORMAT.....")
		input()
		return []
	else:
		in_time = input("\nEnter In Time(hh:mm) : ")
		if len(in_time)<5 or int(in_time[:2])>23 or int(in_time[3:5])>59 or in_time[2]!=":":
			print("\nINVALID DATE FORMAT......")
			input()
			return []
		else:
			out_time = input("\nEnter Out Time(hh:mm) : ")
			if len(out_time)<5 or int(out_time[:2])>23 or int(out_time[3:5])>59 or out_time[2]!=":" or (int(in_time[:2])>int(out_time[:2])):
				print("\nINVALID DATE FORMAT......")
				input()
				return []
	

	ls = booking[facility]
	flag = -1
	for row in ls:
		if row[0]==date:
			if (int(in_time[:2])<int(row[1][:2])) and (int(out_time[:2])<int(row[1][:2])):
				flag = 1

			elif (int(in_time[:2])>int(row[2][:2])) and (int(out_time[:2])>int(row[2][:2])):
				flag = 1

			elif ((int(in_time[:2])<=int(row[1][:2])) and (int(out_time[:2])==int(row[1][:2]))):
				if int(out_time[3:5])<int(row[1][3:5]):
					flag = 1
				else:
					flag = 0
					break

			elif (int(in_time[:2])==int(row[2][:2])) and (int(out_time[:2])>=int(row[2][:2])):
				if int(in_time[3:5])>int(row[2][3:5]) :
					flag = 1
				else:
					flag = 0
					break

			else:
				flag = 0
				break
			
	if flag==1 or flag==-1:
		return [date,in_time,out_time,"Booked"]
	
	else:
		print("\n...Already Booked...")
		input()
		return []

### after selecting 1st option from main menu 2nd page is to book facility...
### available_facilities() is created for 2nd page...

def available_facilities():
	choice_for_booking = "0"
	while choice_for_booking!="4":
		os.system('clear')
		print("\n1. Tennis Court (Rs500/hour)...")
		print("2. Club House (Rs1000/hour)...")
		print("3. Badminton Court (Rs300/hour)...")
		print("4. Go Back to Main Menu...")
		print("======================================")
		choice_for_booking = input("\nSelect Facility which you want to Book(1/2/3) : ")


		# 1st option is for Tennis Court....

		if choice_for_booking=="1":
			choice_to_see_slots = input("\nWant to see Booked slots(y/n) : ")			
			if choice_to_see_slots=="y" or choice_to_see_slots=="Y":				
				for key,value in booking.items():					
					if key=="Tennis_Court":						
						t = PrettyTable(['Date','In Time','Out Time','Status'])						
						for itr in value:	
							if itr[3]=="Booked":
								t.add_row([itr[0],itr[1],itr[2],itr[3]])
				print(t)
				choice_to_continue = input("\nWant to Continue Booking(y/n) : ")
				if choice_to_continue=="y" or choice_to_continue=="Y":
					time_date = input_time_date("Tennis_Court")
					if len(time_date)!=0:
						booking["Tennis_Court"].append(time_date)
						print("\n...Your slot is Booked.....\n\nPayable amount is : Rs500/hour\n\nPress Enter to Continue...",end="")
						input()
					else:
						continue
				else:
					continue
			elif choice_to_see_slots=="n" or choice_to_see_slots=="N":
				print("\nContinue Booking....")
				time_date = input_time_date("Tennis_Court")
				
				if len(time_date)!=0:
					booking["Tennis_Court"].append(time_date)
					print("\n...Your slot is Booked.....\n\nPayable amount is : Rs500/hour\n\nPress Enter to Continue...",end="")
					input()
				
				else:
					continue

		# 2nd option is to book Club House...

		elif choice_for_booking=="2":
			choice_to_see_slots = input("\nWant to see Booked slots(y/n) : ")
			if choice_to_see_slots=="y" or choice_to_see_slots=="Y":
				for key,value in booking.items():
					if key=="Club_House":
						t = PrettyTable(['Date','In Time','Out Time','Status'])
						for itr in value:
							if itr[3]=="Booked":
								t.add_row([itr[0],itr[1],itr[2],itr[3]])
				print(t)
				choice_to_continue = input("\nWant to Continue Booking(y/n) : ")
				if choice_to_continue=="y" or choice_to_continue=="Y":
					time_date = input_time_date("Club_House")
					if len(time_date)!=0:
						booking["Club_House"].append(time_date)
						print("\n...Your slot is Booked.....\n\nPayable amount is : Rs1000/hour\n\nPress Enter to Continue...",end="")
						input()
					else:
						continue
				else:
					continue
			elif choice_to_see_slots=="n" or choice_to_see_slots=="N":
				print("\nContinue Booking....")
				time_date = input_time_date("Club_House")
				if len(time_date)!=0:
					booking["Club_House"].append(time_date)
					print("\n...Your slot is Booked.....\n\nPayable amount is : Rs1000/hour\n\nPress Enter to Continue...",end="")
					input()
				else:
					continue

		# 3rd option is to book Badminton Court...

		if choice_for_booking=="3":
			choice_to_see_slots = input("\nWant to see Booked slots(y/n) : ")
			if choice_to_see_slots=="y" or choice_to_see_slots=="Y":
				for key,value in booking.items():
					if key=="Badminton_Court":
						t = PrettyTable(['Date','In Time','Out Time','Status'])
						for itr in value:
							if itr[3]=="Booked":
								t.add_row([itr[0],itr[1],itr[2],itr[3]])
				print(t)
				choice_to_continue = input("\nWant to Continue Booking(y/n) : ")
				if choice_to_continue=="y" or choice_to_continue=="Y":
					time_date = input_time_date("Badminton_Court")
					if len(time_date)!=0:
						booking["Badminton_Court"].append(time_date)
						print("\n...Your slot is Booked.....\n\nPayable amount is : Rs300/hour\n\nPress Enter to Continue...",end="")
						input()
					else:
						continue
				else:
					continue
			elif choice_to_see_slots=="n" or choice_to_see_slots=="N":
				print("\nContinue Booking....")
				time_date = input_time_date("Badminton_Court")
				if len(time_date)!=0:
					booking["Badminton_Court"].append(time_date)
					print("\n...Your slot is Booked.....\n\nPayable amount is : Rs300/hour\n\nPress Enter to Continue...",end="")
					input()
				else:
					continue

choice_for_main = "0"
while choice_for_main!="2":
	os.system('clear')
	print("Welcome to Isha Mishty Greens Society...")
	print("\n1. Available Facilities...")
	print("2. Exit...")
	print("===============================")
	print("\nSelect your option(1/2) : ",end="")
	choice_for_main = input()
	if choice_for_main=="1":
		available_facilities()
	elif choice_for_main=="2":
			print("\nThank for visiting...",end="")
			input()
			