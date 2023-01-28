file = open('Day - 6/01-writelines-readlines/whatever.txt', 'w') # create a new file on the specified destination
file.writelines(['One\n', 'Two\n', 'Three\n']) # overwrites the file over and over again with .writelines() method
file.close() # don't forget to close the file

file = open('Day - 6/01-writelines-readlines/whatever2.txt', 'w')
file.write("The quick brown fox jumps over the lazy dog")
file.close()

file = open('Day - 6/01-writelines-readlines/whatever.txt', 'r')
print(file.readlines()) # returns a list
file.close()

file = open('Day - 6/01-writelines-readlines/whatever.txt', 'r')
print(file.read()) # returns a string
file.close()