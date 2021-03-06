import time

def fib(n):
    lst = []
    for i in range(0, n):
        if i <= 1:
            lst.append(1)
        else:
            lst.append(lst[i-1] + lst[i-2])
    return lst[n-1]
start = time.time()

# 10부터 50까지 10개씩 증가하여 출력하기
for i in range(10, 51, 10):
    print("fib(%d) ="%i, fib(i))

print("실행시간 : %s 초"%(time.time()-start))