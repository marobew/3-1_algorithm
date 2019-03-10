import time
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

start = time.time()

# 10부터 50까지 10개씩 증가하여 출력하기
for i in range(10, 51, 10):
    print("fib(%d) ="%i, fib(i))

print("실행시간 : %s 초"%(time.time()-start))