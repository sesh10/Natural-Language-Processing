sentence = "sesha loves to code.he lives in mulund.Park the bus.he is a good little boy"

line = sentence.split('.')

NN = ['sesha', 'mulund', 'park', 'bus', 'boy']

PRP = ['he']

VB = ['loves', 'code', 'lives', 'park']

IN = ['in']

TO = ['to']

DT = ['the']

JJ = ['good', 'little']

tags = []

c = 0
d = 0

ans = []

for i in range(len(line)):
    w = line[i].split(" ") 
    w.append('$')
    for j in range(len(w)-1):
        if w[j].casefold() in NN:
            if w[j+1].casefold() in DT:
                if j == 0:
                    tags.append((w[j], 'VB, B_VP'))
            else:
                if j == 0:
                    tags.append((w[j], 'NN, B_NP'))
                else:
                    tags.append((w[j], 'NN, I_NP'))
        elif w[j] in VB:
            if w[j-1] in DT or w[j-1] in TO:
                tags.append((w[j], 'VB, I_VP'))
            else:
                tags.append((w[j], 'VB, B_VP'))

        elif w[j] in IN:
            if w[j-1] in VB:
                tags.append((w[j], 'IN, B_NP'))
        elif w[j] in TO:
            if w[j-1] in VB and w[j+1] in VB:
                tags.append((w[j], 'TO, B_VP'))
            else:
                tags.append((w[j], 'TO, I_VP'))
        elif w[j] in PRP:
            tags.append((w[j], 'PRP, B_NP'))
        elif w[j] in DT:
            tags.append((w[j], 'DT'))
        elif w[j] in JJ:
            if w[j+1] in JJ:
                tags.append((w[j], 'JJ, B_NP'))
            elif w[j+1] in VB:
                if w[j-1] in JJ:
                    tags.append((w[j], 'JJ, I_VP'))
                else:
                    tags.append((w[j], 'JJ, B_VP'))
            elif w[j+1] in NN:
                if w[j-1] in JJ:
                    tags.append((w[j], 'JJ, I_NP'))
                else:
                    tags.append((w[j], 'JJ, B_NP'))
            elif w[j-1] in JJ and w[j+1] in VB:
                tags.append((w[j], 'JJ, I_VP'))
            elif w[j-1] in JJ and w[j+1] in NN:
                tags.append((w[j], 'JJ, I_NP'))
    
    for j in range(len(w)-1):
        if c == 1:
            c = 0
            continue
        
        if w[j].casefold() in NN:
            if w[j+1] not in DT:
                ans.append((w[j],'NP'))
            else:
                ans.append((w[j],'VP'))
        elif w[j].casefold() in VB:
            ans.append((w[j],'VP'))
        elif w[j].casefold() in DT:
            if w[j+1].casefold() in VB:
                c = 1
                ans.append((w[j] +' '+ w[j+1],'VP'))
            elif w[j+1].casefold() in NN:
                c = 1
                ans.append((w[j] +' '+ w[j+1],'NP'))
                
        elif w[j].casefold() in IN or w[j].casefold() in TO:
            if w[j+1].casefold() in VB:
                c = 1
                ans.append((w[j] +' '+ w[j+1],'VP'))
            elif w[j+1].casefold() in NN:
                c = 1
                ans.append((w[j] +' '+ w[j+1],'NP'))
        elif w[j].casefold() in PRP:
            ans.append((w[j],'NP'))
        elif w[j].casefold() in JJ:
            if w[j+1].casefold() in JJ:
                d = 1
                s = w[j] + ' ' + w[j+1]
            elif w[j+1].casefold() in NN:
                d = 0
                ans.append((s +' '+ w[j+1],'NP'))
                break

print(tags)

print(ans)
