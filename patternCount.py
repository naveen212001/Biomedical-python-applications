


from asyncore import read 

#Below code helps to select between datasets : 1 for dataset_1 and 2 for dataset_2
print("Select the dataset :")
selection = 0 #set selection to 0 initially
selection = input("'1' for dataset_1 AND '2' for dataset_2 :" )
#If selection value is 1 then dataset_1 is passed as argument for open
if selection == '1' :
    with open("dataset_1.txt") as text:
        lines = text.read()
        first = lines.split('\n', 1)[0]
#If selection value is 2 then dataset_3 is passed as argument for open
else:
    with open("dataset_2.txt") as text:
        lines = text.read() 
        first = lines.split('\n', 1)[0] #Code used to get first line

#Function to compute repeated sequence to a dictionary
def RepeatedSeq(seq,k): 
  n = len(seq) #total length of sequence
  seqTable = {} #initialize dictionary to add count as well as patterns
  #This loop helps to iterate through the seq and 
  # extract individual kmers and their respective count
  for i in range(n-k):
    pattern = seq[i:i+k] #first pattern will be from 0 t0 11
    seqTable.setdefault(pattern,0) #set first 'value' to 0
    #count increment
    if seqTable[pattern] >= 1:
      seqTable[pattern] = seqTable[pattern] + 1
    else:
      seqTable[pattern] = 1
  return seqTable #Return dictionary containing 'patterns' : 'counts'

k = 12 #set the value of K(not necessary)
patterns = [] #Empty array
dict = RepeatedSeq(first,k) #Function call and save retuen value to dictionary
allValues = dict.values() #Take only values part of the dictionary
maxVal = max(allValues)  #Find the maximum count
#Iterate through the dictionary and append patterns having highest count(maxVal)
for j in dict.keys(): 
   if dict.get(j) == maxVal:
      patterns.append(j)
print("The patterns are:")
#Loop through the pattern array and print the contents
for i in patterns: 
    print(i) 
print("Number of repeatations",maxVal) #Print maximum count


