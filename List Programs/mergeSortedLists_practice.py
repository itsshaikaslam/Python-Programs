
def sortList(list1):
	for i in range(0,len(list1)):
		for j in range(i+1,len(list1)):
			if list1[i] > list1[j]:
				temp = list1[i]
				list1[i] = list1[j]
				list1[j] = temp
	return list1

def mergeSortedLists(l1,l2):
	i=0
	j=0
	l3=[]
	while i < len(l1) and j < len(l2):
		if l1[i] < l2[j]:
			l3.append(l1[i])
			i+=1
		else:
			l3.append(l2[j])
			j+=1
	if i < len(l1):
		l3.extend(l1[i:])
	if j < len(l2):
		l3.extend(l2[j:])
	return l3

def main():
	l1=input("Enter list :")
	l2=input("Enter list :")
	
	l1=sortList(l1)
	l2=sortList(l2)
	
	l3=mergeSortedLists(l1,l2)
	print(l3)

if __name__=="__main__":
	main()
