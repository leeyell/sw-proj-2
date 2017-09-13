# 콜론 앞의 공백 삭제.
# 코드 설명 주석 추가.

#while 문 안에서 input 값을 받기 위해 num의 값을 초기화 해준다.
num=0

while num!=-1:
    num=int(input('Enter a number: '))
    #while 문 안에서 num의 값을 받았기 때문에 num == -1 일 때 'retry!'가 출력된 후에 종료되는 것을 방지.
    if num<0 and num!=-1:
        print('retry!')
    if num>=0:
        sum=1
        for a in range (1,num+1):
            sum=sum*a
        print('%d! = '%num, sum)