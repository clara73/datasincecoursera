import os
import time
#loop begin
i=0

#parelle array 
Times=[]
returnvalues=[]

 
#def average (runtimesArray, returnvaluesArray):
# average takes 2 parameters (an array of run times and an array of return values)
def average(runtimesArray,returnvaluesArray):
	for value in returnvaluesArray:
		if value !=0:
			position = returnvalue.index(value)
			runtimesArray.pop(position)
	if len(runtimesArray)==len(returnvaluesArray):
		sum(runtimesArray)
		return sum(runtimesArray)/len(runtimesArray)

# consistency check
# make sure runtimesArray length == returnvaluesArray length

# loop through each pair and if returnvalues[i] != 0 then skip that one
# if returnvalues[i] == 0 then include runtimesArray[i] in the average

######## END average



while i<2:
        start = time.clock()
        # TODO justin: get clara a container that takes parameters
        #              and that can fail
        returnvalue = os.system("docker run hello-world")
        returnvalues.append(returnvalue)
        elapsed = (time.clock()-start)
        Times.append(elapsed)
        i+=1
print Times,returnvalues,average(Times,returnvalues)
#loop end

