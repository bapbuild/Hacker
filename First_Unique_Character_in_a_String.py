# import collections
#
#
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         """
#         :type s: str
#         :rtype: int
#         """
#         # build hash map : character and how often it appears
#         count = collections.Counter(s)
#
#         # find the index
#         for idx, ch in enumerate(s):
#             if count[ch] == 1:
#                 return idx
#         return -1


inp = input().strip()

dict={}

for x in inp:
    if x in dict.keys():
        dict[x]+=1
    else:
        dict[x]=1

for d,y in dict.items():
    if dict[d]==1:
        print(d)
#        print
        break