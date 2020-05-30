para = "Mera name Seshadri hai. What is your kaam? Can you meet me tomorrow? So nice meeting you!"

words = para.split()

uni_word = []
punct = [',', ':', ';', '.', '?', '!']

for a in words:
    if a[-1] in punct:
        if a[:-1] not in uni_word:
            uni_word.append(a[:-1])
            uni_word.append(a[-1])
    else:
        uni_word.append(a)

filtered = []

print("Tokens: ",uni_word)              #tokenization

slangs = ["mujhe", "tujhe", "mein", "tu", "tera", "mera", "kaam", "dekh", "aaj", "kal", "hai"]


for x in uni_word:
    if x in punct:
        continue
    if x.casefold() not in slangs:
        filtered.append(x)
    

print(filtered)             #Filtration
