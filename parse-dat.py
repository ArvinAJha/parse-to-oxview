import time

# startIndex = input("What integer index would you like to START at: ")
# endIndex = input("What integer index would you like to END at: ")

startIndex = 1_000_000
endIndex = 3_000_000

startT = time.time()

file = open("minitraj.dat")
written = open("indexed.dat", "a")
written.truncate(0)

startWriting = False

line = file.readline()

while(line):
    
    if(line.startswith("t = ")):
        if (line[4::] == f"{startIndex}\n"):
            startWriting = True
        if (line[4::] == f"{endIndex}\n"): 
            startWriting = False
            break

    if(startWriting): written.write(line)
    
    line = file.readline()

while(line):
    written.write(line)
    line = file.readline()
    if(line.startswith("t = ")): break


written.close()
execT = (time.time() - startT)
print(f"\nExecution time in seconds: " + str(execT) + "\n")