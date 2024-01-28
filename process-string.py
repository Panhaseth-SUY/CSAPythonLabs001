# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

string = input("Enter a String : ")
repeat = ""
for i in range(len(string)): 
    repeat += string[i]*2
print(repeat)



# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, 
#  including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

string = input("Enter a range of letters (e.g., a-z): ")
start, end = string.split('-')
result = ""
while start <= end: 
    result += start
    start = chr(ord(start) + 1)
print(result.upper() if string.isupper() else result)  




