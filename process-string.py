# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

text = input("Enter a string: ")
repeated_text = "".join(char * 2 for char in text)
print("Repeated string:", repeated_text)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

str_ = input("Enter a range of letters (e.g., a-z): ")
start, end = str_.split("-")
result = ''.join(chr(i) for i in range(ord(start[0]), ord(end[0]) + 1))
print(result.upper() if str_.isupper() else result) 

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# user_range = input("Enter a range of letters (e.g., a-z): ")


