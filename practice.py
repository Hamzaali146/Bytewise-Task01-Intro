# a = int(input("Enter Operand one: "))
# b = int(input("Enter Operand two: "))

# def add(a:int,b:int):
#     return a+b
    
# print(add(a,b))

# a=5
# b=2
# print(a%b)

# typpee= input("write to check type: ")

# def typechecker(x = None):
#     return type(x)
    
# print(typechecker(typpee))

# to calculate average:

# ope1 = int(input("please: "))
# ope2 = int(input("please: "))
# def aveg(x=0,y=0):
#     return (x+y)/2
# print(aveg(ope1,ope2))
    

# my_list = [1, 2, 3, 2]
# my_list.remove(2)  # my_list becomes [1, 3, 2]
# print(my_list)

my_list = [3, 1, 2]
my_list.sort(reverse=True)  # my_list becomes [1, 2, 3]
print(my_list*3)
b,c,d = my_list
a = my_list.copy()
print(a)
print(c)
def transform_string(s: str) -> str:
    # Step 1: Reverse the string
    s = s[::-1]
    
    # Step 2: Remove all vowels
    vowels = 'aeiou'
    s = ''.join([char for char in s if char not in vowels])
    
    # Step 3: Replace each consonant with its next consonant
    def next_consonant(c):
        consonants = 'bcdfghjklmnpqrstvwxyz'
        index = consonants.index(c)
        return consonants[(index + 1) % len(consonants)]
    
    transformed_string = ''.join(next_consonant(char) for char in s)
    
    return transformed_string

# Example Usage
print(transform_string("hello"))       # Output: "mmj"
print(transform_string("hamza")) # Output: "hpnnsqh"

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example Usage
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False

