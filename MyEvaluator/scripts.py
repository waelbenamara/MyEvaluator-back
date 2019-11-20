import csv 
def identify_user(email):
	with open('people.csv', 'r') as csvFile:
	    reader = csv.reader(csvFile)
	    for row in reader:
	        print(row)
	        if email == row[0]:
	        	return row[1]
	        else :
	        	print('notfound')	
	csvFile.close()



