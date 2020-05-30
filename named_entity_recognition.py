text = 'Seshadri told Navjyot about the lockdown yesterday.Their college is in Mumbai.The University will release circular today.'

lines = text.split('.')

words = []

for line in range(len(lines)):
    words.append(lines[line].split(" "))



Person = ['seshadri', 'navjyot', 'Anushka']
Time = ['today', 'tomorrow', 'yesterday', 'morning', 'evening', 'afternoon', 'night']
Location = ['India', 'mumbai', 'Thane']
Orgn = ['college', 'university']

NER = []

for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j].casefold() in Person:
            NER.append((words[i][j], 'Person'))

        elif words[i][j].casefold() in Time:
            NER.append((words[i][j], 'Time'))

        elif words[i][j].casefold() in Location:
            NER.append((words[i][j], 'Location'))

        elif words[i][j].casefold() in Orgn:
            NER.append((words[i][j], 'Orgn'))

        else:
            continue
        

print(NER)
