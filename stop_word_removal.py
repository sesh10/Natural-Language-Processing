para = "Mera name Seshadri hai. What is your kaam? What are you eating? Navjyot called you a lot of times."

words = para.split()

uni_word = []
punct = [',', '.', ';', ':', '?', '!']

for a in words:
    if a[-1] in punct:
        if a[:-1] not in uni_word:
            uni_word.append(a[:-1])
            uni_word.append(a[-1])
    elif a not in uni_word:
        uni_word.append(a)

filtered = []

print(uni_word)

slangs = ["mujhe", "tujhe", "mein", "tu", "tera", "mera", "kaam", "dekh", "aaj", "kal", "hai"]

for x in uni_word:
    if x in punct:
        continue
    if x.casefold() not in slangs:
        filtered.append(x)

print(filtered)

arra = []

stop_words = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they",
              "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "a",
              "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more",
              "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before"]

for word in filtered:
    if word not in stop_words:
        arra.append(word)

print(arra)

word_dict = ['come', 'you', 'go', 'work', 'feel', 'eat', 'call', 'time']

stems = []

for word in arra:
    if word.endswith("ing"):
        if word[:-3] in word_dict:
            stems.append(word[:-3])
        elif word[:-3]+'e' in word_dict:
            stems.append(word[:-3]+'e')
    elif word.endswith("es"):
        if word[:-2] in word_dict:
            stems.append(word[:-2])
    elif word.endswith("ed"):
        if word[:-2] in word_dict:
            stems.append(word[:-2])
    elif word.endswith("s"):
        if word[:-1] in word_dict:
            stems.append(word[:-1])
    elif word.endswith("r"):
        if word[:-1] in word_dict:
            stems.append(word[:-1])
    else:
        stems.append(word)


print(stems)


    
    
        
