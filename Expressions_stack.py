# list1 = ['2', '+', '(', '3', '-', '2', ')','{','}']
list1 = list(input("Enter a expression"))
print(list1)
stack1 = []
for i in list1:
    print(stack1)
    stack1.append(i)
print("Push in Stack=> ", stack1)

a = 0
b = 0
c = 0
d = 0
for j in list1:
    temp = stack1.pop()
    if (temp == "("):
        a += 1
    elif (temp == "{"):
        c += 1
    elif (temp == "}"):
        d += 1
    elif (temp == ")"):
        b += 1

print(a, b, c, d)

if (a == b and c == d):
    print("Valid statement")
else:
    print("invalid statement")
