trainingSample=[]
count=0
with open('trainingDataSet.txt','r') as f:

    for line in f:
    	contents = line.rstrip('\n').split("\t")
    	trainingSample.append(contents)
    	n=len(contents)
    	
    	count=count+1
w=[]
h_w=[]
for i in range(n):
	print('Enter w',i)
	w.append(input())
learn_rate=input("Enter Learning Rate");
Err = 1.0000 ;
J=0


for i in range(count):	
	h=float(w[0])
	for j in range(n-1):
		h=h+(float(w[j+1])*float(trainingSample[i][j]))
	h_w.append(h)


temp1=0

while(Err!=0):
	temp = 0
	for j in range(count):
		temp=temp + (float(trainingSample[j][n-1])-h_w[j])
	temp = (float(learn_rate)*temp) + float(w[0])
	w[0] = temp
	for j in range(count):
		h=float(w[0])
		for i in range(n-1):
			h=h+(float(w[i+1])*float(trainingSample[j][i]))
		h_w[j]=h
		temp = 0
		for i in range(n-1):
			temp=(float(trainingSample[j][i])*(float(trainingSample[j][n-1])-h_w[j]))
			w[i+1] = (float(learn_rate)*(temp)) + float(w[i+1])
	for i in range(n-1):
		temp1=temp1 + ((h_w[n-1]-float(trainingSample[i][n-1]))*(h_w[n-1]-float(trainingSample[i][n-1])))
	temp1=temp1/(count*2)
	if(temp1 >=  J  ):
		Err = temp1 - J
	else:
		Err = J - temp1
	J = temp1 
	for i in range(count):
		h=float(w[0])
		for j in range(n-1):
			h=h+(w[j+1]*float(trainingSample[i][j]))
		h_w[i]=h

print(w)

fp=open('testingDataPredicted.txt','w')
with open('testingDataSet.txt','r') as f:
	for line in f:
		contents = line.rstrip('\n').split("\t")
		h=w[0]
		for i in range(n-1):
			h=h+(w[i+1]*float(contents[i]))
		fp.write(str(h)+"\n")
fp.close()





