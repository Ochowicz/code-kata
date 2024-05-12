# You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.
#
# Define a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.
def six_toast(num):
    return 6 - num if num < 6 else num - 6