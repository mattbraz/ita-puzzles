from __future__ import division

"""
Combining nine 9s with any number of the operators +, -, *, /, (, ), what is the smallest positive integer that cannot be expressed?

Hints:
 The answer isn't zero. You can express zero like this: (9 - 9) * (9 + 9 + 9 + 9 + 9 + 9 + 9) Also, zero isn't a positive integer.
 The answer isn't one. You can express one like this: 9 - (9 * 9 - 9)/9 + 9 - 9 + 9 - 9
 It's not a trick question.
 Be sure to handle parentheses correctly.

Notes:
 You cannot exponentiate.
 You cannot concatenate (for example, put two 9s together to make 99).
 The - operator can be used in either its binary or unary form.
 Assume base 10.

"""

results = {1: [9,-9]}

def solve(n):
    if n in results:
        return results[n]
    new = set()
    for c in range(1,n):
        left = solve(c)
        right = solve(n-c)
        for a in left:
            for b in right:
                new.add(a+b)
                new.add(a-b)
                new.add(a*b)
                if b != 0:
                    new.add(a/b)
                
    results[n] = new
    return new

if __name__ == "__main__":
    n = 9
    solve(n);
    for x in range(1,n+1):
        i = 1
        while i in results[x]:
            i += 1
        print x,i
    
    
    