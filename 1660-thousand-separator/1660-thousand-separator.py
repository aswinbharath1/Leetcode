class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return str(n)
        else:
            t=n
            n=list(str(n))
            if t<999999 : 
                n.insert(-3,'.')
                n=''.join(n)
                return str(n)
            elif t<999999999: 
                n.insert(-3,'.')           
                n.insert(-7,'.')
                n=''.join(n)
                return str(n)
            else:
                n.insert(-3,'.')           
                n.insert(-7,'.')
                n.insert(-11,'.')
                n=''.join(n)
                return str(n)