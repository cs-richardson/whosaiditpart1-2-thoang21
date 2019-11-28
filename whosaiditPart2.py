"""
Tung Hoang - 11/28/19

This program will go through the transcript of Hamlet and Pride and Prejudice.
After that it will create a dictionary where the every word is counted to see
how many times the author repeats a word

https://www.w3schools.com/python/python_dictionaries.asp
"""

# This function takes a word and returns the same word with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()


# This function takes a filename and generates a dictionary whose keys are
# the unique words in the file and whose values are the counts for those words.
def get_counts(filename):
    result_dict = {}
    total = 0

    file = open(filename)
    for line in file:
        line = line.strip()
        
        for word in line.split():
            word = normalize(word)

            if word in result_dict:
                if word == '':
                    continue
                result_dict[word] += 1  
            else:
                result_dict[word] = 1

            total += 1

    result_dict["_total"] = total
    return result_dict

# Get the counts for the both of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride-and-prejudice.txt")

# Check the contents of the dictionaries
for key in shakespeare_counts:
    print (key + ": " + str(shakespeare_counts[key]))

print ("-----")

for key in austen_counts:
    print (key + ": " + str(austen_counts[key]))
 
 
