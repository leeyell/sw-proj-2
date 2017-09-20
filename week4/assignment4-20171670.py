#factorial 구하기.

def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)

#factorial 을 이용하여 조합의 수 구하기. (n개 중, r개를 선택하는 방법의 수 = n!/r!*(n-r)!)

def nCr1(n, r):
    return fac(n)/(fac(r)*fac(n-r))

#재귀함수를 이용하여 조합의 수 구하기.

def nCr2(n, r):
    if r == 0 and (n >= r):
        return 1
    elif n == 0 and (n < r):
        return 0
    else:
        return nCr2(n-1, r) + nCr2(n-1, r-1)

a = int(input("팩토리얼을 구할 하나의 양의 정수를 입력 : "))
n = int(input("n개 중 r개를 선택할 경우, n에 들어갈 양의 정수 : "))
r = int(input("n개 중 r개를 선택할 경우, r에 들어갈 정수 (음수 제외): "))

print("%d! = "%a, fac(a))
print(nCr1(n, r))
print(nCr2(n, r))