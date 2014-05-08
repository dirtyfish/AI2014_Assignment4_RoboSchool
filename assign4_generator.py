#assign4_generator.py


randomset = [0,1,1,1,2,3,4,5,6]
instructions= ['UP','LEFT','DOWN','RIGHT','TURN LEFT','TURN RIGHT']

#for python 2x
def printf(str, *args):
    print(str % args),


def searchrange(levels):
 for x in range(1<<levels):
  #print " ",x," ",
  xx=x
  count=0
  result=[]
  for y in range(levels,0,-1):
    yy=xx>>y-1
    yy%=2
    count+=yy
    #print yy,
    result.append(yy)
  #print count,
  if count==levels/2:
  	yield result

def splitlist(getlist,sortlist):
 	result=[[],[]]
 	for x in range(len(getlist)):
 		result[sortlist[x]].append(getlist[x])
 	return result



count=0
for x in searchrange(8):
	count+=1
	print count,x, splitlist(range(8),x)


