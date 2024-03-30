class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        len_s = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                break
            len_s += 1

        return len_s


if __name__ == "__main__":
    obj = Solution()
    s = input()
    print(obj.lengthOfLastWord(s))
