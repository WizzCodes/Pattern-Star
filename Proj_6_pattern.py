#Pattern star
#prog(A)
# a = int(input("How many number of lines you want to print"))
# b = bool(int(input("please add 0 for false")))
#
# def star(a, b):
#     if b == True:
#         c = 1
#         while c <= a:
#             print(c * "*")
#             c = c + 1
#     else:
#         while a > 0:
#             print(a * "*")
#             a = a - 1
#
# star(a, b)



#Prog(B)

print("Pattern Printing")
number = int(input("How many rows you want to print"))
print("Enter 1 or 0")
bool_val = input("1 for True or 0 for False")
if bool_val == "1":
    for i in range(0, number+1):
        print("*"*i)

if bool_val == "0":
    for i in range(number, 0, -1):
        print("*"*i)
