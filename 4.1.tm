; Example from Morphett
; This example program checks if the input string is a binary palindrome.
; Input: a string of 0's and 1's, eg '1001001'

; State 0: read the leftmost symbol
0 0 _ r 1
0 1 _ r 2
0 _ _ * halt-accept

; State 1, 2: find the rightmost symbol
1 _ _ l 3
1 * * r 1

2 _ _ l 4
2 * * r 2

; State 3, 4: check if the rightmost symbol matches the most recently read left-hand symbol
3 0 _ l 5
3 _ _ * halt-accept
3 * * * halt-reject

4 1 _ l 5
4 _ _ * halt-accept
4 * * * halt-reject

; State 5, 4: return to left end of remaining input
5 _ _ * halt-accept
5 * * l 6
6 * * l 6
6 _ _ r 0  ; Back to the beginning
