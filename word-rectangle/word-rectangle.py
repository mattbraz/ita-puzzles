"""
Write a program to find the largest possible rectangle of letters such that every row forms a word (reading left to right) and every column forms a word (reading top to bottom).
Words should appear in this dictionary: WORD.LST (1.66MB).
Heuristic solutions that may not always produce a provably optimal rectangle will be accepted: seek a reasonable tradeoff of efficiency and optimality.

---

My solution finds square shaped word rectangles only.  The examples below have have symmetry and will be identical when transposed.  These are easier to find, pass symmetrical=True to find only squares like these.

B I T
I C E
T E N

C A R D
A R E A
R E A R
D A R T

Word squares that form different words across and down are known as "double word squares". Examples are:

T O O
U R N
B E E	

A D M I T S
D E A D E N
S E R E N E
O P I A T E
R E N T E R
B R E E D S

To find such squares (in addition to symmetrical ones), pass symmetrical=False.
This will increase the search space and theus be slower to find solutions.

"""

class WordRectangle:

    def __init__(self, filepath, size=5, symmetrical=True):
        self.size = size
        self.symmetrical = symmetrical
        self.max = size*size
        self.words = []
        self.root_trie = {}
        self.tmap = {}

        self._read_words(filepath)
        self._build_root_trie()
        self._build_transpose_map()
        self._reset()

    def _reset(self):
        self.candidate = [None] * self.max
        self.across = [self.root_trie] * self.max
        self.down = [self.root_trie] * self.max
        self.nfound = 0

    def _read_words(self, filepath):
        words = []
        with open(filepath) as f:
            for line in f:
                words.append(line.strip())
        self.words = [w for w in words if len(w) == self.size]

    # Builds a root_trie that is suitable only for words of equal length.
    def _build_root_trie(self):
        for w in self.words:
            t = self.root_trie
            for c in w:
                t = t.setdefault(c, {})

    # Maps an index in the lower left half to its counterpart in the upper right.
    def _build_transpose_map(self):
        for i in range(self.size):
            for j in range(i):
                self.tmap[i*self.size+j] = j*self.size+i

    def display(self):
        for i in range(self.size*self.size):
            print(self.candidate[i]+" ", end='')
            if i % self.size == self.size - 1: print()

    def solve(self):
        self._solve(0);

    def _solve(self, idx):
        if self.symmetrical:
            while idx in self.tmap:
                self.candidate[idx] = self.candidate[self.tmap[idx]]
                self.across[idx+1] = self.across[idx][self.candidate[idx]]
                idx += 1

        if idx == self.max:
            self.nfound += 1
            print(f"Found {self.nfound}:")
            self.display()
            return

        for c in self.across[idx]:
            if c not in self.down[idx]: continue

            self.candidate[idx] = c

            if idx < self.max - self.size:
                self.down[idx+self.size] = self.down[idx][c]
            if (idx+1) % self.size:
                self.across[idx+1] = self.across[idx][c]

            self._solve(idx+1)


if __name__ == "__main__":

    filepath = "./words.txt"
    size = 7
    symmetrical = True
    wr = WordRectangle(filepath, size, symmetrical)
    wr.solve()

