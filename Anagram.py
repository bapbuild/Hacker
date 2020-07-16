#############Simple Anagram########################
# inp1 = input().strip()
# inp2 = input().strip()
#
# print(sorted(inp1)== sorted(inp2))

###########################complicated############


def isAnagram(s,t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict = {}
        tict = {}
        count = 0
        for c in s:
            keys = dict.keys()
            if c in keys:
                dict[c] += 1
            else:
                dict[c] = 1
        for d in t:
            keys = tict.keys()
            if d in keys:
                tict[d] += 1
            else:
                tict[d] = 1
        print(dict)
        print(tict)
        if dict == tict:
            return True
        else:
            return False

print(isAnagram('anagram','margana'))