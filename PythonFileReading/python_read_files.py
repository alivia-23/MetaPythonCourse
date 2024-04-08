with open('sample.txt', 'r') as file:
    #print(file.read()) # prints entire contents of the file
    #print(file.read(44)) # prints first 44 characters of the file
    #print(file.readline()) # prints only the very first line
    #print(file.readlines()) # prints entire contents in square brackets


    for x in file:
        print(x)
