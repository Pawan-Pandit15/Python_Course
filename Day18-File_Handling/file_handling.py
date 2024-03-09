# File Handling
# How to Read a Text, and Write into it using python Code.


# Function -
# open("file_name","mode")

# Mode -
# 'r' for reading (default).
# 'w' for writing (creates a new file or truncates an existing one).
# 'a' for appending.
# 'b' for binary mode.  zoom.exe - binary   # binary mode read file 'rb',write 'wb', append 'ab'
# '+' for updating (reading and writing).
# 'r+' for read and write
# 'w+' for write and read
# 'a+' for write and read

# Read and Write content
# Read a File
# Reading Entire Content: content = file_object.read()
# line = file_object.readline() for a single line.
# lines = file_object.readlines() for all lines in a list.

# Close the file

# if not mention read and write mode in code then automatic read mode open
# if you want to open txt file but that file is different location so that time you enter path (location) then open file
# (file=open("d\\.........txt","w")


#-------------------------------------------------------------------

# WRITE A FILE ( CREATE A FILE )

# t="Hello pawan"
# file=open("myfile.txt","w")
# file.write(t)
# print("file created")
# file.close()



# READING A FILE

# file = open("myfile.txt","r")
# text = file.read()
# print(text)
# file.close()



# WRITE A LIST INTO FILE

# l=["pawan","basant","kajal","annu"]
# file=open("myfile2.txt","w")
# file.writelines(l)
# print("file created")
# file.close()



# READ A LIST FROM FILE

# file=open("myfile2.txt","r")
# f1=file.readlines()
# print(f1)
# file.close()



# #  APPENDING THE VALUE INTO FILE
#
# a="mamta and aayushi"
# file=open("myfile2.txt","a")
# file.write(a)
# print("append sucessfull")
# file.close()