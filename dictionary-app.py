import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0: #get_close_matches returns a list of keys similar to input.
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0]) #The first key in the list is the closest match
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)

#If the output is a list (a matched word), print it out
#If we don't check for the type, we might print out the strings' characters
# if they are returned.
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output) #print out strings from return statements.
