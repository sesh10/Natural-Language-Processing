rules = {
 'root' : {
 'y' : 'ies', #sng -> plural
 'e' : 'ed', # pres -> past
 'ed' : 'e',
 'll' : 'lt',
 'en' : 'an'
 },
 'cnt' : {
   'plural' : ['ies', 's'],
   'sng' : ['e']
 },
 'person' : {
   'first' : ['I', 'me', 'We'],
   'second' : ['You', 'him'],
   'third' : ['They', 'them']
 },
 'category' : {
   'noun' : ['Raj','cities'],
   'verb' : ['bake','baked','smelt','smell']
 }
}
text = input('Enter your text: ')
tokens = text.split()
morphological = []
 
for t in tokens:
  
 c_rules = rules['cnt']
 for rule in c_rules:
   if t.endswith(tuple(c_rules[rule])):
     print(t, rule)
 
 p_rules = rules['person']
 for rule in p_rules:
   if t in p_rules[rule]:
     print(t, rule)
 cat_rules = rules['category']
 for rule in cat_rules:
   if t in cat_rules[rule]:
     print(t, rule)
     if t.endswith('ed'):
         c = 1   
     else:
         c = 0
         
 tnew = t
 m_rules = rules['root']
 for rule in m_rules:
   if t.endswith(m_rules[rule]):
     tnew = t.replace(m_rules[rule], rule) 
 morphological.append(tnew)
    
if c == 1:
 print("Past Tense")
 print("In present: ", morphological)
else:
 print("Present Tense")
 print("In past: ", morphological)

print(" ".join(str(word) for word in morphological))
