

def valid_anagram(s:str, t:str):

    if len(s) != len(t):
        return False

    hash_s = {}
    hash_t = {}

    for i in range(0,len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    return hash_s == hash_t

s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))