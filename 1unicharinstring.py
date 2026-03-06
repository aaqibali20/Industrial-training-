class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for val in s:
            if val in m:
                m[val] += 1
            else:
                m[val] = 1

        for i, val in enumerate(s):
            if m[val] == 1:
                return i

        return -1


s = input("Enter string: ")

obj = Solution()
print(obj.firstUniqChar(s))