# x = int(input())
# y = int(input())
#
# x*=60
# print(x+y)
#
# x = int(input())
# print(int(x / 60))
# print(int(x % 60))

X = int(input()) #минут для сна
H = int(input())
M = int(input())
X1 = H * 60 + M
X2 = X1 + X
print(int(X2/60))
print(int(X2%60))