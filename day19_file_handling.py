# File Handling
# So far we have seen different Python data types. We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt).

# File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.

# # Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()