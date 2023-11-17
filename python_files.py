with open('newfile.txt', 'w') as file:
    #file.write('This a new file created!')
    file.writelines(['This a new file created!', '\nThis is another line to be added'])

# write multiple lines in a file using writelines() function 
# a writelines() functions accepts a list