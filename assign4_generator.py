#assign4_generator.py



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

count=0
for x in searchrange(8):
	count+=1
	print count,x
