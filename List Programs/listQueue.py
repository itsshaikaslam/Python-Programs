#Write a program to implement Queue using list

import sys
def EnQueue(l1,data):
	l1.append(data)
def DeQueue(l1):
	return l1.pop(0)
def IsFull(l1):
	return len(l1)==10
def IsEmpty(l1):
	return len(l1)==0
	
def menu():
	print("************************************************************")
	print("+++QUEUE IMPLEMENTATION USING LIST+++")
	print("1.EnQueue\n2.DeQueue\n3.IsFull\n4.IsEmpty\n5.Exit")
	choice=input("Enter your choice :")
	return choice

def SimulateMain():
	l1=[]
	choice=menu()
	while(1):
		if choice == 1:
			if not IsFull(l1):
				print("Maximum queue limit is 10..!!")
				data=input("Enter data to enqueue :")
				EnQueue(l1,data)
			else:
				print("Queue is full")
		elif choice == 2:
			if not IsEmpty(l1):
				data=DeQueue(l1)
				print("Dequeued data is :{}".format(data))
			else:
				print("Queue is empty.")
		elif choice == 3:
			print("Checking IsFull condition :{}".format(IsFull(l1)))
		elif choice == 4:
			print("Checking IsEmpty condition :{}".format(IsEmpty(l1)))
		elif choice == 5:
			sys.exit()
		else:
			print("You entered invalid choice.")
		choice=menu()

def main():
	
	SimulateMain()

if __name__=="__main__":
	main()
