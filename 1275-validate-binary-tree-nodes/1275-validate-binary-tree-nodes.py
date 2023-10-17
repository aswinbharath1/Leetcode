class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # construct a binary tree
        s = [0]
        visited = defaultdict(bool)
        
        for i in range(n):
            if leftChild[i] == s[0] or rightChild[i] == s[0]:
                s[0] = i
                       
        while s:
            node = s.pop(0)
                
            if visited[node]: 
                return False
            
            n -= 1
            visited[node] = True
            
            if leftChild[node] != -1:
                s.append(leftChild[node])
            if rightChild[node] != -1:
                s.append(rightChild[node])
        
        return n == 0
        