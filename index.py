'''

The following code is the direct implementation of the working of
Bigeography Based Optimization Algorithm

'''
import numpy as np #For future use
import random as rd #To generate random numbers 
import csv #To retrieve data from the csv file

#Lists Initialization
habitat=[] #Population in every habitat #change immig,emmig no of entries accordingly
immig = [] 
emmig = [] 

imax=500 #Maximum Immigration (User-Defined)
emax=600 #Maximum Emmigration (User-Defined)
hsi=[] #Habitat Suitability Index Considered
t=1.5 #Iteration Times

#Importing the values from a csv file
with open('test.csv') as csvfile:
    readTest = csv.reader(csvfile, delimiter=',')
    for row in readTest: #Dataset row allocation

    	#Change row numbers for any of these according to the dataset value
	    hsi_value=row[0] 
	    habitat_value=row[1]
	    immig_value=row[5]
	    emmig_value=row[4]
	
	    #Conversion of Objects into String Lists
	    hsi.append(hsi_value)
	    habitat.append(habitat_value)
	    immig.append(immig_value)
	    emmig.append(emmig_value)

	    #Conversion of String lists into Integer Lists
	    hsi = list(map(int, hsi))
	    habitat = list(map(int, habitat))
	    immig = list(map(int, immig))
	    emmig = list(map(int, emmig))

for i in range(0,len(habitat)-1): #ranking the habitats
	for j in range(i+1,len(habitat)):
		if habitat[i] > habitat[j]:
			(habitat[i],habitat[j])=(habitat[j],habitat[i])

print ("\n\nRanking done with respect to population\n\n")

N=len(habitat) #Total number of habitats considered
print("The total number of habitats in the given dataset is :"),
print(N)

#To check ranking 
print("\n\n") #For spacing of output
for i in range(0,N):
	print (habitat[i]),

#Setting up the immigration and emmigration rates based on the list
j=1
print("\n\n Immigration | Emmigration\n\n")
for i in range(0,N):
	immig[i]=imax-((imax*(j))/N) #immig is the immigration rate
	emmig[i]=(emax*(j))/N #emmig is the emmigration rate
	j=j+1
for i in range(0,N):
	print (immig[i],emmig[i]), #To print the rates on terminal

while t < N: #N*N*N is to depict for the maximum number of iterations
	for i in range(0,N):
		if habitat[i]!=0:
			if immig[i]!=0: #To select a random emmigration rate and to replace it in immigration rate
				habitat[i]=emmig[rd.randint(0,N-1)]
			else:
				break
		else:
			break
	break
t+=1 # To increase the time gradually

print("\n\nThe Migration state is updated and the population is updated again\n\n")

for i in range(0,N):
	print (habitat[i]),

print("\n\n\nThe Feature Reduced Dataset 'feature_reduced.csv' has been generated in the project folder\n\n\n")
'''
print ("\n\nRanking done II time with respect to population\n\n")
for i in range(0,len(habitat)-1): #ranking the habitats before mutation
	for j in range(i+1,len(habitat)):
		if habitat[i] > habitat[j]:
			(habitat[i],habitat[j])=(habitat[j],habitat[i])

for i in range(0,N): #Printing after the II ranking of Habitats before mutations
	print(habitat[i]),
'''

#To print a new Dataset after reduction of dimensions
with open("feature_reduced.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(['Population','HSI','Immigration','Emmigration'])
	rows = zip(habitat,hsi,immig,emmig)
	for row in rows:
		wr.writerow(row)

#Need to Finish
#1. Good or Bad Habitat Column
#2. HSI Formula based calculation
#3. Printing the globally best habitat