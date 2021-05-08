#temp = open("AnyName.txt", 'r')
#text = temp.read(5)
#text = temp.readline()
#text = temp.readlines()
#temp.close()
#print(text[1])

with open('AnyName.txt') as f:
        for line in f:
            print(line)