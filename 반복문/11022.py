a = int(input())
for i in range(1, a+1):
    A,B = map(int,input().split())
    print("Case #" + str(i) +": " + str(A) + " + " + str(B) + " = " + str(A+B))