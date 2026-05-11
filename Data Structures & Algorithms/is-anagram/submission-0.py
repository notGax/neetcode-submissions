class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]]=1
            else:
                store[s[i]]+=1
        for i in range(len(t)):
            if t[i] not in store:
                return False
            else:
                store[t[i]]-=1
                if store[t[i]]<0:
                    return False
        return True