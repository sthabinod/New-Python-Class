# mostly csv, txt



# first argument file
# second argument mode 
# mode - r reads file
    #  - w writes in file
f = open('my_files/sjfjsdfjksd.txt','a')
# read_file  = my_file.write("Hello\n")

f.write("New file ....\n")

# my_file.write("Hello Welcome to ITTN!\n")
# my_file.seek(0)
# print(my_file.readlines())

# escapse sequence

f.close()











# # Open the file in write mode with reading capabilities
# with open("my_files/file.txt", "w+") as file:
#     # Write new data to the file
#     file.write("First line\n")
#     file.write("Second line\n")
    
#     # Move the file cursor to the beginning
#     file.seek(0)
    
#     # Read the contents of the file
#     contents = file.read()
    
#     # Print the contents
#     print(contents)