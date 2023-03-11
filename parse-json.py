import time
import json 

# startIndex = input("What integer index would you like to START at: ")
# endIndex = input("What integer index would you like to END at: ")

startIndex = '1000000'
endIndex = '3000000'

startT = time.time()
with open("minitraj.json", "r") as file:
    data = json.load(file)


written = open("indexed.dat", "a")
written.truncate(0)

startWriting = False

for key, value in data.items():
    if key == startIndex: 
        startWriting = True
    if key == endIndex and startWriting:
        written.write("\n")
        written.write("\n".join(i for i in value))
        startWriting = False
        break
    if startWriting: 
        if key != startIndex and key != endIndex: written.write("\n")
        written.write("\n".join(i for i in value))



written.close()
execT = (time.time() - startT)
print(f"\nExecution time in seconds: " + str(execT) + "\n") 