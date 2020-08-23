
# function named "split_sentence", takes an argument named "sentence"
def split_sentence(sentence):
#splits the sentence
    split1 = sentence.split()
    return split1

# sets variable = to input sentence
sentence = raw_input('\n' + 'Please type any sentence of your choice:' + '\n')
print "I will now split your sentence"

# displays each word in the split sentence
for word in split_sentence(sentence):
    print "\n" +  "\t" + word + "\n"

print "Done! Your sentence is now split!"
print '\n' + "-------------------" + "-------------------"
print "Now I wll organize your sentence by the length of each word:"
# creates new list
newlist = []
# if a word isnt in the list, append it to the list
for word in split_sentence(sentence):
    if word not in newlist:
        newlist.append(word)
# sorts the list by length of each word
        lenlist = sorted(newlist, key = len)
#prints the list
print lenlist
# prints a dotted line in the command prompt
print '\n' + "-------------------" + "-------------------"
print "Let's add this list of words to a new file."
# variable named "filename" is set equal to the user picked filename
filename = raw_input("What would you like this new file to be called?:" + '\n')
# adds a '.txt' to the user picked filename
new_file = filename + '.txt'
# creats a new file under the user picked name and sets it in write mode
g = open(new_file, 'w+')
# data that is outputted in the function split_sentence is set = to variable "ofile"
ofile = lenlist
# coverts the function output to a string, writes it to "f"
g.write(str(ofile))
g.close()
g = open(new_file, 'r')
g.seek(0)
file_contents = g.read()


print "I have now added the list into your new text file."
print "Here is your new file:" + '\n'
print filename + ':' + '\n'
# prints the file to the command prompt
print file_contents
print '\n' + "-------------------" + "-------------------"
print "Now we add another sentence to this file"
new_sentence = raw_input('What sentence do you want to add to your new file?:' + '\n')

new_split_sentence = split_sentence(new_sentence)

print "Ok, lets split that sentence"

for word in split_sentence(new_sentence):
    newlist.append(word)
    print '\n' + '\t' + word + '\n'

alphalist = sorted(newlist)

g.close()
g = open(new_file, 'w')
g.write(str(alphalist))
g.close()
g = open(new_file, 'r')
g.seek(0)
appended_file = g.read()

print "I have added it to your file and organized it in alphabetical order"
print "Here is your new file:" + '\n'
print filename +':' + '\n'
print appended_file
print "-------------------" + "-------------------"
print "-------------------" + "-------------------"
print "-------------------" + "-------------------"
print "-------------------" + "-------------------"
print 'Goodbye.'
g.close()




# 1: split the sentence after taking user input DONE
# 2: print the split sentence with line numbers DONE
# 3: organize the words by the length of each word DONE
# 4: add the list to a new file DONE
# 5: ask what the file should be called DONE
# 6: write to the new file DONE
# 7: add another sentence to the file
# 8: split and reorganize in alphabetical order, and print.
# 9: close the file.
