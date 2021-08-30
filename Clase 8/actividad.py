file1 = "discharge_s_6893.txt"
file2 = "discharge_s_14237.txt"
file3 =  "discharge_s_19989.txt"

file = open (file1)
allData = file.readlines ()

substring = allData[6]
pos1 = substring.index('[')
pos2 = substring.index(']')
print(allData [6] [pos1+3 : pos2 -2])
