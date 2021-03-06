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

* The answer isn't zero. You can express zero like this:
      (9 - 9) * (9 + 9 + 9 + 9 + 9 + 9 + 9)
    Also, zero isn't a positive integer.
* The answer isn't one. You can express one like this:
       9 - (9 * 9 - 9)/9 + 9 - 9 + 9 - 9
* It's not a trick question.
* Be sure to handle parentheses correctly.

Notes:
* You cannot exponentiate.
* You cannot concatenate (for example, put two 9s together to make 99).
* The - operator can be used in either its binary or unary form.
* Assume base 10.


Word Rectangle
---
Write a program to find the largest possible rectangle of letters such that every row forms a word (reading left to right) and every column forms a word (reading top to bottom). Words should appear in this dictionary: WORD.LST (1.66MB). Heuristic solutions that may not always produce a provably optimal rectangle will be accepted: seek a reasonable tradeoff of efficiency and optimality. 

Lucky Sevens
---

Write a program to compute the sum of all the integers between 1 and 10 ^ 11 both divisible by seven and, when the decimal digits are reversed, are still divisible by seven.

Sling Blade Runner
---

"How long a chain of overlapping movie titles, like Sling Blade Runner, can you find?"

Use the following listing of movie titles: MOVIES.LST. Multi-word overlaps, as in "License to Kill a Mockingbird," are allowed. The same title may not be used more than once in a solution. Heuristic solutions that may not always produce the greatest number of titles will be accepted: seek a reasonable tradeoff of efficiency and optimality.
 
Data provided by MovieLens at the University of Minnesota.

Strawberry Fields
---

Strawberries are growing in a rectangular field of length and width at most 50. You want to build greenhouses to enclose the strawberries. Greenhouses are rectangular, axis-aligned with the field (i.e., not diagonal), and may not overlap. The cost of each greenhouse is $10 plus $1 per unit of area covered.

Write a program that chooses the best number of greenhouses to build, and their locations, so as to enclose all the strawberries as cheaply as possible. Heuristic solutions that may not always produce the lowest possible cost will be accepted: seek a reasonable tradeoff of efficiency and optimality.

Your program must read a small integer 1 ≤ N ≤ 10 representing the maximum number of greenhouses to consider, and a matrix representation of the field, in which the '@' symbol represents a strawberry. Output must be a copy of the original matrix with letters used to represent greenhouses, preceded by the covering's cost. Here is an example input-output pair:

    Input	 	

    4
    ..@@@@@...............
    ..@@@@@@........@@@...
    .....@@@@@......@@@...
    .......@@@@@@@@@@@@...
    .........@@@@@........
    .........@@@@@........

    Output

    90
    ..AAAAAAAA............
    ..AAAAAAAA....CCCCC...
    ..AAAAAAAA....CCCCC...
    .......BBBBBBBCCCCC...
    .......BBBBBBB........
    .......BBBBBBB........

In this example, the solution cost of $90 is computed as (10+8*3) + (10+7*3) + (10+5*3).
 
Run your program on the 9 sample inputs found in this file and report the total cost of the 9 solutions found by your program, as well as each individual solution.

Queens & Knights
---

In 1850, Carl Friedrich Gauss and Franz Nauck showed that it is possible to place eight queens on a chessboard such that no queen attacks any other queen. The problem of enumerating the 92 different ways there are to place 8 queens in this manner has become a standard programming example, and people have shown that it can be solved using many different search techniques. Now consider a variant of this problem: you must place an equal number of knights and queens on a chessboard such that no piece attacks any other piece. What is the maximum number of pieces you can so place on the board, and how many different ways can you do it?

Tour the T
---

Given a T timetable, write a program to compute the quickest route that passes through every station on the Red, Blue, Green, and Orange Lines, ending at Kendall Square.

Your program should compute a route that visits all T stations at least once. A station has been visited if you stop there (to change to a different line) or pass through on a train. You may start at any station.

The supplied T timetable contains the definitive list of all T stations and the travel time between them. All trains in the timetable should be assumed to run in both directions. Assume that the expected wait time for a train at a given station is fixed:

* Red Line - 5 minutes
* Blue Line - 4 minutes
* Green Line - 3 minutes
* Orange Line - 2 minutes

For example, if part of your route includes changing from the Green Line to the Red Line at Park Street, you should assume that you will wait 5 minutes for the Red Line train to show up. You should also assume that the wait time is the same for all trains (e.g. you will wait 5 minutes for the Red Line to Braintree, Ashmont, or Alewife).

At the end of the line, you must get off the train and wait the appropriate amount of time for a train going in the opposite direction.

Include in your answer the total time to visit all stations, plus enough information to verify your solution. Sample output for a (suboptimal) route starting at Kendall Square might look like:

    0:00:00: Arrive Kendall/MIT
    0:05:00: Board Red Line Braintree
    0:07:00: Arrive Charles/MGH
    0:09:00: Arrive Park St
    0:12:00: Board Green Line B
    0:14:00: Arrive Government Center
    0:17:00: Board Green Line B
    ...

Of course, your code should not be in any way specific to the Boston subway topology, but generalize easily to other data files, representing, say, the New York subway.


Palindromic Pangram
---

A palindrome is a sequence of words like "lid off a daffodil" or "shallot ayatollahs" that uses the same letters reading backwards as forwards. The words need not form a meaningful or grammatical sentence.

A palindromic pangram is a multi-word palindrome that includes all 26 letters of the alphabet. Find the shortest sequence of words that is both a pangram and a palindrome. Use this dictionary: WORD.LST (1.66 MB).

