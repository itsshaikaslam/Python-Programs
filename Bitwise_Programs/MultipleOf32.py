#Write a program to accept a number from user and check if it is multiple of 32 or not without using any arithmetic operator
def isMultipleOf32(num):
	if num & 31==0:
		return 1
	else:
		return 0
def main():
	num=input("Enter the number :")
	if isMultipleOf32(num)==1:
		print("{} is multiple of 32".format(num))
	else:
		print("{} is NOT multiple of 32".format(num))
if __name__=="__main__":
	main()
	
