class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        n= len(s)
        n= n//2
        l = s[ : n ]
        r = s[ n :  ]
        c=0
        for i in l:
            if i in a:
                c += 1
        for i in r :
            if i in a:
                c -= 1
        return c==0