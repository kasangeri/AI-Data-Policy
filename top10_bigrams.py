import nltk

words = nltk.corpus.gutenberg.words("shakespeare-macbeth.txt")

bigram = {}

for i in range(len(words)-1):
	if words[i].isalnum() and words[i+1].isalnum():
		string = words[i].lower() + " " + words[i+1].lower()
		try:
			bigram[string]+=1
		except:
			bigram[string]=1

bigram = sorted(bigram.items(), key=lambda x: x[1], reverse=True)

print("Total number of words: ", len(words))
print("Total number of distinct bigrams: ", len(bigram))
print("Top 10 bigrams in the text are : \n", bigram[:10])


