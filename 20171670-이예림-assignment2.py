num=0

while num!=-1:
    num=int(input('Enter a number: '))
    if num<0 and num!=-1 :
        print('retry!')
    if num>=0  :
        sum=1
        for a in range (1,num+1) :
            sum=sum*a
        print('%d! = '%num, sum)
            
        
