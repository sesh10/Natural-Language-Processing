sentence = "nitin loves to code. he lives in palava. Park the bus."

line = sentence.split('.')

nouns = ['nitin', 'palava', 'park', 'bus']

pronoun = ['he']

verb = ['loves', 'code', 'lives', 'park']

prep = ['to', 'in']

det = ['the']

tags = {}

for i in range(len(line)):
	w = line[i].split(" ") 
	for j in range(len(w)-1):
		if w[j] in nouns:
			if w[j+1] in det:
				tags[w[i]] = 'verb'
			tags[w[j]] = 'noun'
		elif w[j] in verb:
			tags[w[j]] = 'verb'

		elif w[j] in prep:
			tags[w[j]] = 'prep'
		elif w[j] in pronoun:
			tags[w[j]] = 'pronoun'
		elif w[j] in det:
			tags[w[j]] = 'det'

print(tags)	
