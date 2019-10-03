


#read csv file
f = open('Absenteeism_at_work.csv', 'r')

#split file by lines by reading the data from the file into a list
listOfLines = f.read().splitlines()

#print(listOfLines) #print all the lines in the datafile
print(listOfLines[0]) #print first line of data
print(listOfLines[1]) #prints second line of data file
print(listOfLines[len(listOfLines)-1]) #prints last line of data

#ID;Reason for absence;Month of absence;Day of the week;Seasons;Transportation expense;Distance from Residence to Work;Service time;Age;Work load Average/day ;Hit target;Disciplinary failure;Education;Son;Social drinker;Social smoker;Pet;Weight;Height;Body mass index;Absenteeism time in hours #First Line
#11;26;7;3;1;289;36;13;33;239.554;97;0;1;2;1;0;1;90;172;30;4 #Second line
#35;0;0;6;3;179;45;14;53;271.219;95;0;1;1;0;0;1;77;175;25;0 #Last line'''

#split line by semi colon, convert into list
listf = listOfLines[1]
lineValue =listf.split(';') 
#prints data in list form, allowing to extract data from the list.
#in this case, line 1 is extracted to print.
print(lineValue)

#in the list, we can also extract specific elements.
#for example, we will extract the 'Age'(the 8th element in the list) and 'Absenteeism time in hours'(the last element in the list, 40th item)
#idno = lineValue[0]
age = lineValue[8]
hours = lineValue[len(lineValue)-1]
print(age,hours)

f.close()