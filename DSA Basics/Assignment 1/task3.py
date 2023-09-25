# 3. Write a program to check if two strings are a rotation of each other?

def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False
    
    temp = str1 + str1
    
    if str2 in temp:
        return True
    
    return False

# Example 
string1 = "hello"
string2 = "lohel"

if are_rotations(string1, string2):
    print(f"{string1} and {string2} are rotations of each other")
else:
    print(f"{string1} and {string2} are not rotations of each other")
