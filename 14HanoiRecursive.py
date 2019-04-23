'''
Name: Omri Daniel
Date: 11/5/2018
Desc: Tower of Hanoi Recursive Method
'''
class Stack:
    def __init__(self,name):
        self.items = []
        self.name=name
        self.move=-1

    def __str__(self): 	return str(self.item)

    def push(self, items): self.items.append(items)

    def pop(self): return self.items.pop()

    def peek(self): return self.items[len(self.items)-1]

    def size(self): return len(self.items)
    
def printTowers():
	pegA.move+=1
	tList=[]
	towers=[pegA,pegB,pegC]
	print('\nMove:',pegA.move)											#print num of moves
	for j in range(1,len(towers)+1):
		print(('Tower '+str(j)+':').center(rings*3),end='')				#print labels of towers
	print()																#print new line to allows pegs proper printing

	for r in range(rings):												
		tList.append([])												#create 2-d list
		for i in range(len(towers)):
			if towers[i].size()<=r: tList[r].append('|'.center(rings*3))#if theres not enough rings print the pole
			elif towers[i].size()>r: tList[r].append(('#'*((((towers[i].items[r])*2))+1)).center(rings*3))#if theres rings print them

	for row in reversed(tList):											#reverse list of rings in each tower to print proper rings
		print(''.join(row))												
	print('[]'*rings*5)													#print the bottum block

def moveRing(ring, a, b, c):											#main recursion
	if ring > 0: 														
		moveRing(ring - 1, a, c, b) 									#move tower of size ring-1 to tower b
		if a:															#check if only one ring left to move
			ring = a.pop()												#move disk from tower a peg to tower c peg
			c.push(ring)
			printTowers()												
			print('Moved ring from',a.name,'tower to',c.name,'tower.') 	
		moveRing(ring - 1, b, a, c)										#move tower of size ring-1 from tower b to tower a

pegA=Stack('first')														
pegB=Stack('second')
pegC=Stack('third')

while True:																#While loop for integer 1-6 so doesnt crash/take long 
	try:
		rings=int(input('Please enter an integer(1-6) number for the amount of rings: '))
		if 0<rings<7: break
	except: pass

for r in range(rings,0,-1): pegA.push(r)								#Set up the stack with proper amount of rings and prints them
printTowers()
print('Starting towers with all rings on first tower.')

moveRing(pegA.size(),pegA,pegB,pegC)									#Main Game
print('Tower of Hanoi completed.')										#End game output