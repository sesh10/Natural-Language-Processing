test_list = ["this is a cat this cat is smart smart cats are naughty"]
print ("The original list is : " + str(test_list))
test_list = [i for j in test_list for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]
print ("The formed bigrams are : " + str(test_list))
count=0
new_list=[]

for i in test_list:
	if count==0:
		i="eos "+str(i)+" eos"
	else:
		i=str(i)+" (eos)"
	new_list.append(i)
	count+=1
word_list=[]

for i in new_list:
	x=i.split()
	word_list.extend(x)

print("Word list: ",word_list)
print("New list: ",new_list)
res = [(x, i.split()[j + 1]) for i in new_list for j, x in enumerate(i.split()) if j < len(i.split()) - 1]
print ("The formed bigrams are : " + str(res))

def prob_calc(a,b):
	prob=(res.count((b,a))+1)/(word_list.count(b)+len(set(word_list)))
	return prob

wordset=list(set(word_list))
print("\t",end="")

for i in wordset:
	print(" ",i, end="")
print()

for i in wordset:
	print(i,":\t", end="")
	for j in wordset:
		ans=prob_calc(j,i)
		print("%.3f "%ans,end="")
	print()