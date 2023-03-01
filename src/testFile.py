# import string
#
#
# def isPangram(str1, alphabet=string.ascii_lowercase):
#     for character in alphabet:
#         if character not in str1:
#             return False
#     return True
#
#
# print(isPangram("the brown fox"))
# print(isPangram("abcdefghijklmnopqrstuvwxyz"))

# def unique_list(lst):
#     a = set(lst)
#     print(a)
#
#
#
# unique_list([1,1,1,11,2,2,3,4,3,3,3,3,4,4,4,4,5,5,5,])
#
# def multiply(numbers):
#     result = 1
#     for item in numbers:
#         result *= item
#
#     return result
#     pass
#
# print(multiply([1, 2, 3, -4]))
#

class Dog:

    def __init__(self, breed):

        self.breed = breed


my_dog = Dog(breed="Lab")

print(my_dog.breed)