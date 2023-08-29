# Write your code here :-)
import pprint
message = 'From the output, you can see that the lowercase letter c appears 3 times, the space character appears 13 times, and the uppercase letter A appears 1 time. this program will work nomatter what string is inside the message variable, even if the string is milions of characters long!'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pformat(count)


