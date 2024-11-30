a = input()
b = list(a)

print(b)
def sum(b):
    for i in range(len(b)):
        f = int(b[i])+int(b[i+1])
        j = f+int(b[i+1])
        print(j)
sum(b)