import random

#print each element of row_original to see the hangman board
#row_original=[["|-----------------"],["|"," "," "," "," "," "," "," ","|"],["|"," "," "," "," "," "," "," ","O"],["|"," "," "," "," "," ","/"," ","|"," ","\\"],["|"," "," "," "," "," "," "," ","|"],["|"," "," "," "," "," "," ","/"," ","\\"],["|"]]

#Each element of the board is stored in two dimensional list
row=[["|-----------------"],["|"," "," "," "," "," "," "," "," "],["|"," "," "," "," "," "," "," "," "],["|"," "," "," "," "," "," "," "," "," "," "],["|"," "," "," "," "," "," "," "," "],["|"," "," "," "," "," "," "," "," "," "],["|"]]
position=[]
win_status=0
i=0

#Two lists holding the position of row[] which are to be changed with grid_val[x] if wrong guess is done
grid_x=[1,2,3,3,3,4,5,5]
grid_y=[8,8,6,8,10,8,7,9]
grid_val=["|","O","/","|","\\","|","/","\\"]

#Method to draw the board
def draw_board():
	i=0
	j=0
	while i<7:
		while j<len(row[i]):
			print row[i][j],
			j+=1
		print '\n'
		j=0
		i+=1

#A random word is chosen from these words
#words=["apple","government","unusal","apple","muzzlers","jackboot"]
words=open("words.txt").readlines()
index=random.randint(0,212)

#Printing a ___ (underscore) for each letter of the word
for x in range(len(words[index])):
	position.append(-1)
	print " __ ",

print '\n'


#Game starts!
while win_status==0:
	letter=raw_input("Guess a letter -> ")

	#If the actual word doesn't contain the guessed letter, the hangmang board is altered for redrawing
	if letter not in words[index]:
		row[grid_x[i]][grid_y[i]]=grid_val[i]
		i=i+1
		draw_board()
		print '\n\n\n\n'


	#if 'apple' is the word and you input 'p' then position[] will look like
	#[-1,0,0,-1,-1]
	for x in range(len(words[index])):
		if words[index][x]!=letter and position[x]!=0:
			position[x]=-1
		else:
			position[x]=0

	#Printing the word with correctly guessed portion non-hidden
	for x in range(len(words[index])):
		if position[x]==-1:
			print " __ ",
		else:
			print words[index][x],
	print '\n'

	#Check if user has correctly guessed the word
	#win_status=1 breaks the loop
	#condition len(set(position))==1 and position[0]!=-1 checks if every entry in position[] is same
	#or not. If every entry is same and it is not -1 you are declared a winner.
	#For example- if you have guessed every letter in the word the position[] list will look like-
	#[0,0,0,...,0]
	if len(set(position))==1 and position[0]!=-1:
		print "You have won the game!\n"
		win_status=1

	#Checks if hangman is hung or not!
	if i==8:
		print "You have lost the game."
		print "The word was- " + words[index]
		win_status=1



	