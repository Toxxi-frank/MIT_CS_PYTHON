# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print
#
# Longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'

str = s[0]
final = ''

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        str += s[i+1]
    else:
        if len(final) < len(str):
            final = str
        str = s[i+1]
if len(final) < len(str):
    final = str
print(final)

