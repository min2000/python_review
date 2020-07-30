#소수 찾기

def isPrime(num):
    if num==1:
        return False
    
    elif num==2:
        return True
    
    else:
        if num%2==0:
            return False
        
        for i in range(3, int(num**0.5)+1, 2):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)

'''
for i in range(3, int(num**0.5)+1, 2)

'''
