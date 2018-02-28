from __future__ import division #To get floating point values after division
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
hab_index = [] #Habitat Index to define the 0.5 Threshold
gb=[]
hsi=[] #Habitat Suitability Index Considered
hsi_temp=[] #Temporary storage for HSI Computation

avg=0 #To compute the Population Index based on mean
elem=0 #Total number of elements in dataset
imax=500 #Maximum Immigration (User-Defined)
emax=600 #Maximum Emmigration (User-Defined)
t=1.5 #Iteration Times

#Importing the values from a csv file
with open('test.csv') as csvfile:
    readTest = csv.reader(csvfile, delimiter=',')
    for row in readTest:  #Dataset row allocation
    	cols=(len(row)) #To find the dataset column length

    	'''
    	Passes the HSI attributes to compute the Habitat Suitability Index to 
    	the mean value using the dataset range , thus reducing the main features
    	in the dataset into a single value using feature selection technique
    	'''
    	for j in range(4,9): #Will vary according to the dataset
    		hsi_value=row[j]	
    		hsi.append(hsi_value)
    		hsi = list(map(int, hsi))

    		hsi_temp.append(hsi_value)
    		hsi_temp=list(map(int, hsi_temp))
    		hsi_temp=hsi_temp+hsi

    	#Change row numbers for any of these according to the dataset value
    	habitat_value=row[1]
    	immig_value=row[3]
    	emmig_value=row[2]
    	hab_index_value = row[2]
    	gb_value = row[2]

    	#Conversion of Objects into String Lists
    	habitat.append(habitat_value)
    	immig.append(immig_value)
    	emmig.append(emmig_value)
    	hab_index.append(hab_index_value)
    	gb.append(gb_value)

    	#Conversion of String lists into Integer Lists
    	habitat = list(map(int, habitat))
    	immig = list(map(int, immig))
    	emmig = list(map(int, emmig))
    	hab_index=list(map(int,hab_index))
    	gb=list(map(int,gb))

for i in range(0,len(habitat)-1): #ranking the habitats
	for j in range(i+1,len(habitat)):
		if habitat[i] > habitat[j]:
			(habitat[i],habitat[j])=(habitat[j],habitat[i])

print ("\n\nRanking done with respect to population\n\n")

N=len(habitat) #Total number of habitats considered

elem=(cols*N)
print("Features of the Dataset")
print("Records,Features,Total Elements")
print(N),
print(cols),
print(elem)

for i in xrange(0,N):	#To compute and pass final HSI value
	hsi[i]=hsi_temp[i]//6

#To check ranking 
print("\n\n") #For spacing of output
for i in range(0,N):
	print (habitat[i]),

#Setting up the immigration and emmigration rates based on the list
j=1
print("\n\n Immigration | Emmigration\n\n")
for i in range(0,N):
	immig[i]=imax-((imax*(j))//N) #immig is the immigration rate
	emmig[i]=(emax*(j))//N #emmig is the emmigration rate
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
temp=0
for i in range(0,N):
	temp=temp+habitat[i]
avg=(temp//N)

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

#Reducing the Population to an index to compute good/bad habitat using the threshold 0.5
for i in range(0,N):
	hab_index[i]=habitat[i]/avg #avg is used to obtain a mean proportion for population index threshold
	if hab_index[i]>= 0.5:
		gb[i]=1
	else:
		gb[i]=0

#To print a new Dataset after reduction of dimensions
with open("feature_reduced.csv", 'wb') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(['Population','Population Index','HSI','Immigration','Emmigration','(1-good)(0-bad)'])
	rows = zip(habitat,hab_index,hsi,immig,emmig,gb)
	for row in rows:
		wr.writerow(row)
