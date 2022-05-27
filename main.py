# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


filename = "./story.txt" 

def read_file_content(filename):
    # [assignment] Add your code here 

    with open(filename, "r") as f:
        text = f.read()
        return text

print(read_file_content(filename))

############################################################

def count_words():
    str = read_file_content(filename)

    # [assignment] Add your code here
    counts = dict()
    words = str.split()

    # Loop through each line of the file
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


# Print the number of occurrences of word
print(count_words())


    