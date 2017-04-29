import sys
from collections import defaultdict

"""
An "add-a-gram" is a sequence of words formed by starting with a 3-letter word, adding a letter and rearranging to form a 4-letter word, and so on. For example, here are add-a-grams of the words "CREDENTIALS" and "ANACHRONISM":

ail + s =
sail + n =
nails + e =
aliens + t =
salient + r =
entrails + c =
clarinets + e =
interlaces + d =
CREDENTIALS (length 11)

mar + c =
cram + h =
march + s =
charms + o =
chromas + n =
monarchs + i =
harmonics + a =
maraschino + n =
ANACHRONISM (length 11)

Test your own credentials: given the dictionary found here, what is the longest add-a-gram?
"""

MIN = 3
MAX = 999
# An sword is a word with letters sorted alphabetically.
swords_by_len = defaultdict(list)
words_by_sword = defaultdict(list)

def parse_words(fp):
	with open(fp, "r") as file:
		for line in file:
			word = line.rstrip('\n')
			if len(word) > MAX:
				continue
			sword = "".join(sorted(word))
			swords_by_len[len(word)].append(sword)
			words_by_sword[sword].append(word)

# Check word2 has all the letters in word1 (any order).
def addable(word1, word2):
	ww = word2
	for l in word1:
		k = ww.find(l)
		if k == -1:
			return False
		ww = ww[:k] + ww[(k+1):]
	return True

# Iterate from MAX to MIN.  The first full chain we find is the longest.
def find_longest() :
	for i in range(MAX,MIN-1,-1):
		for sword in sorted(swords_by_len.get(i,[]), reverse=True):
			chain = find_chain(sword)
			if chain is not None: return chain

# If we can find a full chain from len(sword) to MIN, then return it.
def find_chain(sword, chain=None):
	if chain is None: chain = []
	chain.append(sword)
	for swn in swords_by_len.get(len(sword)-1,[]):
		if addable(swn, sword):
			if len(swn) < MIN:
				return chain
			return find_chain(swn, list(chain))
	return None

# Convert a list of swords into a list of words.
def wordify(chain):
	nchain = []
	for sword in chain:
		nchain.append(words_by_sword[sword][0])
	return nchain

#---------------------------------

if __name__ == "__main__":
	parse_words(sys.argv[1])
	chain = find_longest()
	print wordify(reversed(chain))
