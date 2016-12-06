ITA Puzzles
===

ITA Software hiring puzzle solutions in python.

Add-A-Gram
---
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


Nine 9s
---
Combining nine 9s with any number of the operators +, -, *, /, (, ), what is the smallest positive integer that cannot be expressed?

Hints:

1) The answer isn't zero. You can express zero like this:
      (9 - 9) * (9 + 9 + 9 + 9 + 9 + 9 + 9)
    Also, zero isn't a positive integer.

2) The answer isn't one. You can express one like this:
       9 - (9 * 9 - 9)/9 + 9 - 9 + 9 - 9

3) It's not a trick question.

4) Be sure to handle parentheses correctly.

Notes:
* You cannot exponentiate.
* You cannot concatenate (for example, put two 9s together to make 99).
* The - operator can be used in either its binary or unary form.
* Assume base 10.

# Lucky Sevens

Write a program to compute the sum of all the integers between 1 and 1011 both divisible by seven and, when the decimal digits are reversed, are still divisible by seven.

# Sling Blade Runner

"How long a chain of overlapping movie titles, like Sling Blade Runner, can you find?"

Use the following listing of movie titles: MOVIES.LST. Multi-word overlaps, as in "License to Kill a Mockingbird," are allowed. The same title may not be used more than once in a solution. Heuristic solutions that may not always produce the greatest number of titles will be accepted: seek a reasonable tradeoff of efficiency and optimality.
 
Data provided by MovieLens at the University of Minnesota.
