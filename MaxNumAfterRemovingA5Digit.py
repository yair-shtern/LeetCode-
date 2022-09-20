# For Example given 15958 return 1958
# given -5859 return -589

class Solution(object):
    def removeOneFive(self, n):
        max_num = float("-inf")
        str_num = str(n)
        for i, c in enumerate(str_num):
            if c == '-':
                continue
            if c == '5':
                new_num = int(str_num[:i] + str_num[i + 1:])
                max_num = max(new_num, max_num)
        return max_num


if __name__ == '__main__':
    print(Solution().removeOneFive(15958) == 1958)
    print(Solution().removeOneFive(-5859) == -589)
    print(Solution().removeOneFive(50000) == 0)
    print(Solution().removeOneFive(10005) == 1000)
