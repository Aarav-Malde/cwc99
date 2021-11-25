def countwords():
    filename = input("Enter a file name to check the number of words in it ")
    n = 0
    f = open(filename)
    for line in f:
        words = line.split()
        n = n+ len(words)
    print(n)
    
countwords()