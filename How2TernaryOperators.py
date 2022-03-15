num4 = 4

num3 = 3

string1 = "words"

print("string1 is a string") if type(string1) is str else print("string1 is not a string")

print("num3 is a string") if type(num3) is str else print("num3 is not a string")

def isEven(int):
    if int%2 == 0:
        return True
    else:
        return False

print("3 is an even number") if isEven(num3) else print("3 is not an even number")

print("4 is an even number") if isEven(num4) else print("4 is not an even number")
