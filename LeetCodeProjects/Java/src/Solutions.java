import java.util.*;
import java.util.stream.Collector;
import java.util.stream.Collectors;


public class Solutions {
    /**
     * 1081. Smallest Subsequence of Distinct Characters
     * Given a string s, return the lexicographically smallest subsequence
     * of s that contains all the distinct characters of s exactly once.
     */
    public String smallestSubsequence(String s) {
        // store the last index for each character
        int[] lastIndexForChar = new int[26];
        for (int i = 0; i < s.length(); i++)
            lastIndexForChar[s.charAt(i) - 'a'] = i;

        Stack<Integer> stack = new Stack<Integer>(); // working stack
        boolean[] charSeen = new boolean[26]; // the value of the i's index will be true if the char i is in the stack

        // the main loop
        for (int i = 0; i < s.length(); i++) {
            int c = s.charAt(i) - 'a';
            // if the current char is already in the stack continue
            if (charSeen[c]) continue;
            // else, if the stack isn't empty and the stack top is grater then the current chat and
            // its appears later in the string, pop the top and posh the current character
            while (!stack.empty() && stack.peek() > c && i < lastIndexForChar[stack.peek()])
                charSeen[stack.pop()] = false;
            stack.push(c);
            charSeen[c] = true;
        }

        // build the result string from the stack and reverse it
        StringBuffer stringBuffer = new StringBuffer();
        while (!stack.empty()) stringBuffer.append((char) (stack.pop() + 'a'));

        return stringBuffer.reverse().toString();
    }

    /**
     * 1005. Maximize Sum Of Array After K Negations
     * Given an integer array nums and an integer k, modify the array in the following way:
     * <p>
     * choose an index i and replace nums[i] with -nums[i].
     * You should apply this process exactly k times. You may choose the same index i multiple times.
     * <p>
     * Return the largest possible sum of the array after modifying it in this way.
     */
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);

        // replace negatives to positives
        int i = 0;
        while (k > 0 && i < nums.length) {
            if (nums[i] >= 0) break;
            nums[i] = -nums[i];
            k--;
            i++;
        }
        int m = 0;
        if (k % 2 == 1) { // all element in nums are positive and k is odd, so the smallest should be negative
            m = -2 * Arrays.stream(nums).min().getAsInt();
        }
        return m + Arrays.stream(nums).sum();
    }

    /**
     * 1002. Find Common Characters
     * Given a string array words, return an array of all characters that show up in all strings within the words
     * (including duplicates). You may return the answer in any order.
     */
    // Solution 1
    public List<String> commonChars(String[] words) {
        int[][] arr = new int[words.length][26];

        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < words[i].length(); j++) {
                arr[i][words[i].charAt(j) - 'a']++;
            }
        }

        List<String> characters = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            int num = arr[0][i];
            for (int j = 1; j < words.length; j++) {
                num = Math.min(num, arr[j][i]);
            }
            for (int j = 0; j < num; j++)
                characters.add(Character.toString(i + 'a'));
        }
        return characters;
    }


//    // Solution 2
//    int[] arr = new int[26];
//    count(arr, words[0]);
//
//    for (int i = 1; i < words.length; i++) {
//        int[] newArr = new int[26];
//        count(newArr, words[i]);
//
//        for (int j = 0; j < 26; j++)
//            arr[j] = Math.min(arr[j], newArr[j]);
//    }
//
//    List<String> characters = new ArrayList<>();
//    for (int i = 0; i < 26; i++)
//        for (int j = 0; j < arr[i]; j++)
//            characters.add(Character.toString(i + 'a'));
//
//    return characters;
//}
//
//    private void count(int[] newArr, String words) {
//        for (char c : words.toCharArray())
//            newArr[c - 'a']++;
//    }

    /**
     * 88. Merge Sorted Array
     * You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
     * representing the number of elements in nums1 and nums2 respectively.
     * Merge nums1 and nums2 into a single array sorted in non-decreasing order.
     * The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
     * To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that
     * should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
     */
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] num1Tmp = Arrays.copyOfRange(nums1, 0, m);

        int ind1 = 0;
        int ind2 = 0;
        while (ind1 < m && ind2 < n) {
            if (num1Tmp[ind1] < nums2[ind2]) {
                nums1[ind1 + ind2] = num1Tmp[ind1];
                ind1++;
            } else {
                nums1[ind1 + ind2] = nums2[ind2];
                ind2++;
            }
        }

        if (ind1 < m) System.arraycopy(num1Tmp, ind1, nums1, ind1 + n, m - ind1);

        if (ind2 < n) System.arraycopy(nums2, ind2, nums1, ind2 + m, n - ind2);
    }

    /**
     * 27. Remove Element
     * Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
     * The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
     * Consider the number of elements in nums which are not equal to val be k, to get accepted,
     * you need to do the following things:
     * Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
     * The remaining elements of nums are not important as well as the size of nums.
     * - Return k.
     */
    public int removeElement(int[] nums, int val) {
        int k = 0;
        int ind = 0;
        for (int i = 0; i < nums.length; i++)
            if (nums[i] != val) {
                nums[ind] = nums[i];
                ind++;
                k++;
            }
        return k;
    }

    /**
     * 26. Remove Duplicates from Sorted Array
     * Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
     * element appears only once. The relative order of the elements should be kept the same.
     * Then return the number of unique elements in nums.
     */
    public int removeDuplicates(int[] nums) {
        int k = 1;
        int ind = 1;
        int prv = nums[0];
        for (int i = 1; i < nums.length; i++)
            if (nums[i] != prv) {
                nums[ind] = nums[i];
                prv = nums[i];
                ind++;
                k++;
            }
        return k;
    }

    /**
     * 80. Remove Duplicates from Sorted Array II
     * Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that
     * each unique element appears at most twice. The relative order of the elements should be kept the same.
     * Since it is impossible to change the length of the array in some languages, you must instead have the
     * result be placed in the first part of the array nums. More formally, if there are k elements after
     * removing the duplicates, then the first k elements of nums should hold the final result. It does not matter
     * what you leave beyond the first k elements.
     * <p>
     * Return k after placing the final result in the first k slots of nums.
     * Do not allocate extra space for another array.
     * You must do this by modifying the input array in-place with O(1) extra memory.
     */
    public int removeDuplicates2(int[] nums) {
        if (nums.length <= 2) return nums.length;

        int k = 2;
        int ind = 2;
        int prv1 = nums[0];
        int prv2 = nums[1];
        for (int i = 2; i < nums.length; i++)
            if (nums[i] != prv1) {
                nums[ind] = nums[i];
                prv1 = prv2;
                prv2 = nums[i];
                ind++;
                k++;
            }
        return k;
    }

    /**
     * 169. Majority Element
     * Given an array nums of size n, return the majority element.
     * The majority element is the element that appears more than ⌊n / 2⌋ times.
     * You may assume that the majority element always exists in the array.
     * Constraint: O(n) time and O(1) space.
     */
    public int majorityElement(int[] nums) {
        int count = 0;
        int res = 0;

        for (int num : nums) {
            if (count == 0) res = num;

            if (num == res) count++;
            else count--;
        }

        return res;
    }

    /**
     * 274. H-Index
     * Given an array of integers citations where citations[i] is the number of citations a researcher received
     * for their ith paper, return the researcher's h-index.
     * According to the definition of h-index on Wikipedia:
     * The h-index is defined as the maximum value of h such that the given researcher has published at least
     * h papers that have each been cited at least h times.
     */
    public int hIndex(int[] citations) {
        Arrays.sort(citations);

        int i = citations.length;
        int ind = citations.length - 1;
        int counter = 0;
        while (i >= 0) {
            while (ind >= 0 && citations[ind] >= i) {
                counter++;
                ind--;
            }

            if (counter >= i) break;
            i--;
        }
        return i;
    }

    /**
     * 238. Product of Array Except Self
     * Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
     * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
     * You must write an algorithm that runs in O(n) time and without using the division operation.
     */
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];

        // forward
        int prev = 1;
        for (int i = 0; i < nums.length; i++) {
            res[i] = prev;
            prev *= nums[i];
        }

        // backward
        prev = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= prev;
            prev *= nums[i];
        }

        return res;
    }

    /**
     * 189. Rotate Array
     * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
     */
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        // reverse the array
        reversePortion(0, nums.length, nums);

        // reverse each portion of the reversed array
        reversePortion(0, k, nums);
        reversePortion(k, nums.length, nums);
    }

    private static void reversePortion(int start, int end, int[] nums) {
        for (int i = start; i < (end + start) / 2; i++) {
            int tmp = nums[i];
            nums[i] = nums[end + start - i - 1];
            nums[end + start - i - 1] = tmp;
        }
    }

    /**
     * 122. Best Time to Buy and Sell Stock II
     * You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
     * On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
     * However, you can buy it then immediately sell it on the same day.
     * Find and return the maximum profit you can achieve.
     */
    public int maxProfit(int[] prices) {
        int profit = 0;
        int left = 0, right = 1;
        int tmpProfit = 0;
        while (right < prices.length && left <= right) {
            if (tmpProfit > prices[right] - prices[left]) {
                profit += tmpProfit;
                tmpProfit = 0;
                left = right;
                right++;
                continue;
            }
            tmpProfit = Math.max(tmpProfit, prices[right] - prices[left]);
            right++;
        }
        profit += tmpProfit;
        return profit;
    }

    /**
     * 45. Jump Game II
     * You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
     * Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
     * if you are at nums[i], you can jump to any nums[i + j] where:
     * 0 <= j <= nums[i] and
     * i + j < n
     * Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
     */
//    public int jump(int[] nums) {
//        for (int i = 1; i < nums.length; i++)
//            nums[i] = Math.max(nums[i - 1], nums[i] + i); // choose to use the last jump or not
//
//        int result = 0, ind = 0;
//        while (ind < nums.length - 1) {
//            result++;
//            ind = nums[ind];
//        }
//        return result;
//    }
    public int jump(int[] nums) {
        int n = nums.length;
        int[] numJumpsToEnd = new int[n];

        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] + i >= n - 1) {
                numJumpsToEnd[i] = 1;
                continue;
            }
            if (nums[i] == 0) {
                numJumpsToEnd[i] = n;
                continue;
            }
            int minSteps = n;
            for (int j = i + 1; j < n - 1 && j - i <= nums[i]; j++)
                minSteps = Math.min(minSteps, numJumpsToEnd[j]);
            numJumpsToEnd[i] = 1 + minSteps;
        }
        return numJumpsToEnd[0];
    }

    /**
     * 134. Gas Station
     * There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
     * You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
     * You begin the journey with an empty tank at one of the gas stations.
     * Given two integer arrays gas and cost, return the starting gas station's index if you can travel around
     * the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
     */
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // could do this instead the second loop to guarantee a solution:
        //
        // if (Arrays.stream(gas).sum() < Arrays.stream(cost).sum()) return -1;

        // first loop
        int startInd = 0, ind = 0, sum = 0;
        while (ind < gas.length) {
            sum += gas[ind] - cost[ind];
            ind++;
            if (sum < 0) {
                startInd = ind;
                sum = 0;
            }
        }
        if (startInd == gas.length) return -1;

        // second loop
        sum = 0;
        ind = startInd;
        int len = 0;
        while (len < gas.length) {
            sum += gas[ind] - cost[ind];
            if (sum < 0) return -1;
            ind = (ind + 1) % gas.length;
            len++;
        }
        return startInd;
    }

    /**
     * 135. Candy
     * There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
     * You are giving candies to these children subjected to the following requirements:
     * Each child must have at least one candy.
     * Children with a higher rating get more candies than their neighbors.
     * Return the minimum number of candies you need to have to distribute the candies to the children.
     */
    public int candy(int[] ratings) {
        int[] numCandies = new int[ratings.length];
        // forward
        for (int i = 0; i < ratings.length; i++) {
            numCandies[i] = 1;
            if (i > 0 && ratings[i] > ratings[i - 1]) numCandies[i] = numCandies[i - 1] + 1;
        }

        // backward
        for (int i = ratings.length - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) numCandies[i] = Math.max(numCandies[i + 1] + 1, numCandies[i]);
        }

        return Arrays.stream(numCandies).sum();
    }

    /**
     * 42. Trapping Rain Water
     * Given n non-negative integers representing an elevation map where the width of each bar is 1,
     * compute how much water it can trap after raining.
     */
    public int trap(int[] height) {
        int sum = 0;
        int left = 0, right = height.length - 1;
        int maxL = height[left], maxR = height[right];
        while (left < right) {

            if (maxL < maxR) {
                left++;
                maxL = Math.max(maxL, height[left]);
                sum += maxL - height[left];

            } else {
                right--;
                maxR = Math.max(maxR, height[right]);
                sum += maxR - height[right];
            }
        }
        return sum;
    }

    /**
     * 12. Integer to Roman
     * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
     * Symbol       Value
     * I             1
     * V             5
     * X             10
     * L             50
     * C             100
     * D             500
     * M             1000
     * For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
     * which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
     * Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
     * Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
     * I can be placed before V (5) and X (10) to make 4 and 9.
     * X can be placed before L (50) and C (100) to make 40 and 90.
     * C can be placed before D (500) and M (1000) to make 400 and 900.
     * Given an integer, convert it to a roman numeral.
     */
    public String intToRoman(int num) {
        String[] keySet = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] valSet = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

        StringBuilder res = new StringBuilder();
        for (int i = 0; i < valSet.length; i++)
            while (num >= valSet[i]) {
                res.append(keySet[i]);
                num -= valSet[i];
            }
        return String.valueOf(res);
    }

    /**
     * 14. Longest Common Prefix
     * Write a function to find the longest common prefix string amongst an array of strings.
     * If there is no common prefix, return an empty string "".
     */
    public String longestCommonPrefix(String[] strs) {
        String str = strs[0];
        for (String item : strs) {
            int i = 0;
            for (; i < Math.min(str.length(), item.length()); i++)
                if (str.charAt(i) != item.charAt(i)) break;
            str = str.substring(0, i);
        }
        return str;
//        Arrays.sort(strs);
//        String first = strs[0], last = strs[strs.length - 1];
//        StringBuilder str = new StringBuilder();
//
//        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
//            if (first.charAt(i) == last.charAt(i))
//                str.append(first.charAt(i));
//            else break;
//        }
//
//        return String.valueOf(str);
    }

    /**
     * 58. Length of Last Word
     * Given a string s consisting of words and spaces, return the length of the last word in the string.
     * A word is a maximal substring consisting of non-space characters only.
     */
    public int lengthOfLastWord(String s) {
        int res = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') if (res != 0) break;
            else continue;
            res++;
        }
        return res;
//        String[] str = s.split(" ");
//        return str[str.length - 1].length();
    }

    /**
     * 151. Reverse Words in a String
     * Given an input string s, reverse the order of the words.
     * A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
     * Return a string of the words in reverse order concatenated by a single space.
     * Note that s may contain leading or trailing spaces or multiple spaces between two words.
     * The returned string should only have a single space separating the words. Do not include any extra spaces.
     */
    public String reverseWords(String s) {
        // O(1) space except the str result
        StringBuilder str = new StringBuilder();
        int left = s.length() - 1, right = s.length() - 1;
        int i = s.length() - 1;
        while (i >= 0) {
            while (i >= 0 && s.charAt(i) == ' ') {
                right = i - 1;
                i--;
            }
            left = right;
            while (i >= 0 && s.charAt(i) != ' ') {
                left--;
                i--;
            }

            for (int j = left + 1; j <= right; j++)
                str.append(s.charAt(j));
            str.append(" ");
        }
        return String.valueOf(str).trim();

//        // using array:
//        String[] strArr = s.trim().split("\\s+");
//        StringBuilder str = new StringBuilder();
//        for (int i = strArr.length - 1; i > 0; i--)
//            str.append(strArr[i]).append(" ");
//        return str + strArr[0];
    }
    // another possible solution is to reverse the whole String and then to reverse every word

    /**
     * 6. Zigzag Conversion
     * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
     * (you may want to display this pattern in a fixed font for better legibility)
     * P   A   H   N
     * A P L S I I G
     * Y   I   R
     * And then read line by line: "PAHNAPLSIIGYIR"
     * Write the code that will take a string and make this conversion given a number of rows:
     * string convert(string s, int numRows);
     */
    public String convert(String s, int numRows) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            int ind = i;

            while (ind < s.length()) {
                str.append(s.charAt(ind));
                ind += Math.max(1, 2 * numRows - 2 - ind % Math.max(numRows - 1, 1) * 2);
            }
        }
        return String.valueOf(str);
    }

    /**
     * 28. Find the Index of the First Occurrence in a String
     * Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
     * or -1 if needle is not part of haystack.
     */
    public int strStr(String haystack, String needle) {
        int start = 0, ind = 0, needleInd = 0;
        while (ind < haystack.length() && needleInd < needle.length()) {
            if (haystack.charAt(ind) == needle.charAt(needleInd)) {
                ind++;
                needleInd++;
                continue;
            }
            needleInd = 0;
            start++;
            ind = start;
        }
        if (needleInd != needle.length()) return -1;
        return start;
    }

    /**
     * 68. Text Justification
     * Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
     * You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
     * Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
     * Extra spaces between words should be distributed as evenly as possible.
     * If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
     * For the last line of text, it should be left-justified, and no extra space is inserted between words.
     * Note:
     * A word is defined as a character sequence consisting of non-space characters only.
     * Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
     * The input array words contains at least one word.
     */
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int ind = 0;
        int currWidth = 0, currNumWords = 0;
        while (ind < words.length) {
            StringBuilder s = new StringBuilder();
            while (ind < words.length && currWidth + currNumWords + words[ind].length() <= maxWidth) {
                currWidth += words[ind].length();
                currNumWords++;
                ind++;
            }
            int totalSpaces = maxWidth - currWidth;
            if (currNumWords == 1 || ind == words.length) {
                for (int i = 0; i < currNumWords - 1; i++)
                    s.append(words[ind - currNumWords + i]).append(" ");
                s.append(words[ind - 1]);
                s.append(" ".repeat(totalSpaces - currNumWords + 1));

            } else {
                int numSpaces = (maxWidth - currWidth) / Math.max(1, currNumWords - 1);

                totalSpaces -= numSpaces * (currNumWords - 1);

                for (int i = 0; i < currNumWords - 1; i++) {
                    s.append(words[ind - currNumWords + i]).append(" ".repeat(Math.max(1, numSpaces)));
                    if (totalSpaces > 0) {
                        s.append(" ");
                        totalSpaces--;
                    }
                }
                s.append(words[ind - 1]);

            }
            result.add(String.valueOf(s));
            currWidth = 0;
            currNumWords = 0;

        }
        return result;
    }

    /**
     * 125. Valid Palindrome
     * A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
     * it reads the same forward and backward. Alphanumeric characters include letters and numbers.
     * Given a string s, return true if it is a palindrome, or false otherwise.
     */
    public boolean isPalindrome(String s) {
//        String str = s.toLowerCase().replaceAll("[^a-z,0-9]", "");
//        for (int i = 0; i < str.length() / 2; i++)
//            if (str.charAt(i) != str.charAt(str.length() - 1 - i)) return false;
//        return true;
        int left = 0, right = s.length() - 1;
        while (left < right) {
            char leftChar = Character.toLowerCase(s.charAt(left));
            char rightChar = Character.toLowerCase(s.charAt(right));

            if (!Character.isLetterOrDigit(leftChar)) {
                left++;
                continue;
            }
            if (!Character.isLetterOrDigit(rightChar)) {
                right--;
                continue;
            }

            if (leftChar != rightChar) return false;

            left++;
            right--;
        }
        return true;
    }

    /**
     * 392. Is Subsequence
     * Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
     * A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
     * of the characters without disturbing the relative positions of the remaining characters.
     * (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
     */
    public boolean isSubsequence(String s, String t) {
        int sInd = 0, tInd = 0;
        while (sInd < s.length() && tInd < t.length()) {
            if (s.charAt(sInd) == t.charAt(tInd)) sInd++;
            tInd++;
        }
        return sInd == s.length();
    }

    /**
     * 167. Two Sum II - Input Array Is Sorted
     * Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
     * find two numbers such that they add up to a specific target number.
     * Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
     * Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
     * The tests are generated such that there is exactly one solution. You may not use the same element twice.
     * Your solution must use only constant extra space.
     */
    public int[] twoSum(int[] numbers, int target) {
        int leftIndex = 0, rightIndex = numbers.length - 1;
        while (leftIndex < rightIndex) {
            int result = numbers[leftIndex] + numbers[rightIndex];
            if (result == target) break;
            else if (result < target) leftIndex++;
            else rightIndex--;
        }

        return new int[]{leftIndex + 1, rightIndex + 1};
    }

    /**
     * 11. Container With Most Water
     * You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
     * Find two lines that together with the x-axis form a container, such that the container contains the most water.
     * Return the maximum amount of water a container can store.
     * Notice that you may not slant the container.
     */
    public int maxArea(int[] height) {
        int maxLeft = 0, maxRight = height.length - 1;
        int total = 0;
        while (maxLeft < maxRight) {
            total = Math.max(total, Math.min(height[maxLeft], height[maxRight]) * (maxRight - maxLeft));
            if (height[maxLeft] < height[maxRight]) maxLeft++;
            else maxRight--;
        }
        return total;
    }

    /**
     * 15. 3Sum
     * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
     * Notice that the solution set must not contain duplicate triplets.
     */
    public List<List<Integer>> threeSum(int[] nums) {
        nums = Arrays.stream(nums).sorted().toArray();
        List<List<Integer>> list = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i - 1] == nums[i]) continue;
            int j = i + 1, k = nums.length - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    list.add(Arrays.asList(nums[i], nums[j], nums[k]));

                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (k > j && nums[k] == nums[k - 1]) k--;
                }
                if (sum < 0) j++;
                else k--;
            }
        }
        return list;
    }

    /**
     * 209. Minimum Size Subarray Sum
     * Given an array of positive integers nums and a positive integer target, return the minimal length of a
     * subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
     */
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, sum = 0;
        int minLength = nums.length + 1;
        for (int right = 0; right < nums.length; right++) {
            sum += nums[right];
            while (sum >= target) {
                minLength = Math.min(minLength, right - left + 1);
                sum -= nums[left];
                left++;
            }
        }
        if (minLength == nums.length + 1) return 0;
        return minLength;
    }

    /**
     * 3. Longest Substring Without Repeating Characters
     * Given a string s, find the length of the longest substring without repeating characters.
     */
    public int lengthOfLongestSubstring(String s) {
        int left = 0, maxSize = 0;
        Set<Character> set = new HashSet<>();
        for (int right = 0; right < s.length(); right++) {
            while (set.contains(s.charAt(right))) {
                set.remove(s.charAt(left));
                left++;
            }
            set.add(s.charAt(right));
            maxSize = Math.max(maxSize, set.size());
        }
        return maxSize;
    }

    /**
     * 30. Substring with Concatenation of All Words
     * You are given a string s and an array of strings words. All the strings of words are of the same length.
     * A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
     * For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings.
     * "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
     * Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
     */
    public List<Integer> findSubstring(String s, String[] words) {
        int numWords = words.length, wordLen = words[0].length();
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            if (map.containsKey(word)) map.put(word, map.get(word) + 1);
            else map.put(word, 1);
        }

        List<Integer> result = new ArrayList<>();
        Map<String, Integer> tmpMap = new HashMap<>();
        for (int i = 0; i + wordLen * numWords <= s.length(); i++) {
            for (int j = i; j < i + wordLen * numWords; j += wordLen) {
                String word = s.substring(j, j + wordLen);
                if (tmpMap.containsKey(word)) tmpMap.put(word, tmpMap.get(word) + 1);
                else tmpMap.put(word, 1);
            }
            boolean addIndex = true;
            for (String key : map.keySet()) {
                if (!tmpMap.containsKey(key) || !Objects.equals(tmpMap.get(key), map.get(key))) {
                    addIndex = false;
                    break;
                }
            }
            if (addIndex) result.add(i);
            tmpMap.clear();
        }
        return result;
    }


//        int numWords = words.length, wordLen = words[0].length();
//        Map<String, Integer> map = new HashMap<>();
//        for (String word : words) {
//            if (map.containsKey(word))
//                map.put(word, map.get(word) + 1);
//            else map.put(word, 1);
//        }
//
//        List<Integer> result = new ArrayList<>();
//        for (int i = 0; i < s.length() - wordLen * numWords + 1; i++) {
//            Map<String, Integer> tmpMap = new HashMap<>();
//            int j = i;
//            while (j < i + wordLen * numWords) {
//                String word = s.substring(j, j + wordLen);
//
//                if (!map.containsKey(word)) break;
//
//                if (tmpMap.containsKey(word))
//                    tmpMap.put(word, tmpMap.get(word) + 1);
//                else tmpMap.put(word, 1);
//
//                if (tmpMap.get(word)> map.get(word)) break;
//
//                j += wordLen;
//            }
//            if (j == i + wordLen * numWords)
//                result.add(i);
//        }
//        return result;
//    }

    /**
     * 76. Minimum Window Substring
     * Given two strings s and t of lengths m and n respectively, return the minimum window
     * substring of s such that every character in t (including duplicates) is included in the window.
     * If there is no such substring, return the empty string "".
     * The testcases will be generated such that the answer is unique.
     */
    public String minWindow(String s, String t) {
        Map<Character, Integer> tMap = new HashMap<>();
        for (int i = 0; i < t.length(); i++)
            tMap.put(t.charAt(i), tMap.getOrDefault(t.charAt(i), 0) + 1);

        char c;
        int[] res = {-1, -1};
        int minWindow = Integer.MAX_VALUE;
        int count = 0, target = tMap.size(), l = 0;
        Map<Character, Integer> map = new HashMap<>();

        for (int r = 0; r < s.length(); r++) {
            c = s.charAt(r);
            map.put(c, map.getOrDefault(c, 0) + 1);


            if (Objects.equals(map.get(c), tMap.getOrDefault(c, 0))) count++;

            while (count == target) {
                if (r - l + 1 < minWindow) {
                    res[0] = l;
                    res[1] = r + 1;
                    minWindow = r - l + 1;
                }
                c = s.charAt(l);
                map.put(c, map.get(c) - 1);
                if (map.get(c) < tMap.getOrDefault(c, 0)) count--;

                l++;
            }
        }
        return minWindow == Integer.MAX_VALUE ? "" : s.substring(res[0], res[1]);
    }

    /**
     * 36. Valid Sudoku
     * Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
     * Each row must contain the digits 1-9 without repetition.
     * Each column must contain the digits 1-9 without repetition.
     * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
     * Note:
     * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
     * Only the filled cells need to be validated according to the mentioned rules.
     */
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            if (!isValidRow(board, i) || !isValidColumn(board, i) || !isValidSubgrid(board, i)) return false;
        }
        return true;
    }

    private static boolean isValidRow(char[][] board, int row) {
        Set<Character> seen = new HashSet<>();
        for (Character c : board[row]) {
            if (Character.isDigit(c)) if (seen.contains(c)) return false;
            else seen.add(c);
        }
        return true;
    }

    private static boolean isValidColumn(char[][] board, int col) {
        Set<Character> seen = new HashSet<>();
        for (int row = 0; row < 9; row++) {
            char c = board[row][col];
            if (Character.isDigit(c)) if (seen.contains(c)) return false;
            else seen.add(c);
        }
        return true;
    }

    private static boolean isValidSubgrid(char[][] board, int i) {
        int rowStart = (i / 3) * 3;
        int colStart = (i % 3) * 3;
        Set<Character> seen = new HashSet<>();
        for (int row = rowStart; row < rowStart + 3; row++) {
            for (int col = colStart; col < colStart + 3; col++) {
                char c = board[row][col];
                if (Character.isDigit(c)) if (seen.contains(c)) return false;
                else seen.add(c);
            }
        }
        return true;
    }

    /**
     * 54. Spiral Matrix
     * Given an m x n matrix, return all elements of the matrix in spiral order.
     */

    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<>();
        int startRow = 0, endRow = matrix.length;
        int startCol = 0, endCol = matrix[0].length;

        while (startRow < endRow && startCol < endCol) {
            // go right
            for (int i = startCol; i < endCol; i++) {
                list.add(matrix[startRow][i]);
            }
            startRow++;

            // go down
            for (int i = startRow; i < endRow; i++) {
                list.add(matrix[i][endCol - 1]);
            }
            endCol--;

            // if possible - go left
            if (startRow < endRow) {
                for (int i = endCol - 1; i >= startCol; i--)
                    list.add(matrix[endRow - 1][i]);
                endRow--;
            }

            // if possible - go up
            if (startCol < endCol) {
                for (int i = endRow - 1; i >= startRow; i--)
                    list.add(matrix[i][startCol]);
                startCol++;
            }
        }
        return list;
    }

    /**
     * 48. Rotate Image
     * You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
     * You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
     * DO NOT allocate another 2D matrix and do the rotation.
     */
    public void rotate(int[][] matrix) {
        int n = matrix.length - 1;
        // reverse rows
        for (int row = 0; row <= n; row++)
            for (int col = 0; col <= n / 2; col++) {
                int tmp = matrix[row][col];
                matrix[row][col] = matrix[row][n - col];
                matrix[row][n - col] = tmp;
            }

        // swap diagonals
        for (int row = 0; row < n; row++)
            for (int col = 0; col < n - row; col++) {
                int tmp = matrix[row][col];
                matrix[row][col] = matrix[n - col][n - row];
                matrix[n - col][n - row] = tmp;
            }
    }

    /**
     * 73. Set Matrix Zeroes
     * Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
     * You must do it in place.
     */
    public void setZeroes(int[][] matrix) {
        int firstRow = 1;
        for (int i = 0; i < matrix.length; i++)
            for (int j = 0; j < matrix[0].length; j++)
                if (matrix[i][j] == 0) {
                    if (i == 0) firstRow = 0;
                    else matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }

        for (int i = 1; i < matrix.length; i++)
            if (matrix[i][0] == 0) Arrays.fill(matrix[i], 0);

        for (int j = 0; j < matrix[0].length; j++)
            if (matrix[0][j] == 0) for (int i = 0; i < matrix.length; i++)
                matrix[i][j] = 0;

        if (firstRow == 0) Arrays.fill(matrix[0], 0);
    }

    /**
     * 289. Game of Life
     * According to Wikipedia's article: "The Game of Life, also known simply as Life,
     * is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
     * The board is made up of an m x n grid of cells, where each cell has an initial state:
     * live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
     * using the following four rules (taken from the above Wikipedia article):
     * Any live cell with fewer than two live neighbors dies as if caused by under-population.
     * Any live cell with two or three live neighbors lives on to the next generation.
     * Any live cell with more than three live neighbors dies, as if by over-population.
     * Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
     * The next state is created by applying the above rules simultaneously to every cell in the current state,
     * where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
     */
    public void gameOfLife(int[][] board) {
        // | Original | New | State |
        // |    0     |  0  |   0   |
        // |    1     |  0  |   1   |
        // |    0     |  1  |   2   |
        // |    1     |  1  |   3   |
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++) {
                int numNeighbors = countNeighbors(board, i, j);
                if (board[i][j] == 0) {
                    if (numNeighbors == 3) board[i][j] = 2; // State 2 else, remained State 0
                } else { // Original is 1
                    if (numNeighbors == 2 || numNeighbors == 3) board[i][j] = 3; // State 3 else, remained State 1
                }
            }
        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                if (board[i][j] == 1) board[i][j] = 0;
                else if (board[i][j] == 2 || board[i][j] == 3) board[i][j] = 1;
    }

    private int countNeighbors(int[][] board, int i, int j) {
        int count = 0;
        for (int k = i - 1; k <= i + 1; k++) {
            for (int l = j - 1; l <= j + 1; l++) {
                if ((k == i && l == j) || k < 0 || l < 0 || k >= board.length || l >= board[0].length) continue;
                else count += board[k][l] % 2 == 0 ? 0 : 1;
            }
        }
        return count;
    }

    /**
     * 383. Ransom Note
     * Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
     * Each letter in magazine can only be used once in ransomNote.
     */
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] charArray = new int[26];
        for (char c : magazine.toCharArray())
            charArray[c - 'a']++;

        for (char c : ransomNote.toCharArray())
            if (charArray[c - 'a']-- == 0) return false;

        return true;
    }

    /**
     * 205. Isomorphic Strings
     * Given two strings s and t, determine if they are isomorphic.
     * Two strings s and t are isomorphic if the characters in s can be replaced to get t.
     * All occurrences of a character must be replaced with another character while preserving the order of characters.
     * No two characters may map to the same character, but a character may map to itself.
     */
    public boolean isIsomorphic(String s, String t) {
        if (s.length() < t.length()) return false;
        Map<Character, Character> tToS = new HashMap<>();
        Map<Character, Character> sToT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char sChar = s.charAt(i), tChar = t.charAt(i);
            if (sToT.getOrDefault(sChar, tChar) != tChar || tToS.getOrDefault(tChar, sChar) != sChar) return false;

            sToT.put(sChar, tChar);
            tToS.put(tChar, sChar);
        }
        return true;
    }

    /**
     * 290. Word Pattern
     * Given a pattern and a string s, find if s follows the same pattern.
     * Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
     */
    public boolean wordPattern(String pattern, String s) {
        String[] sArray = s.split(" ");
        if (pattern.length() != sArray.length) return false;

        Map<Character, String> patternToS = new HashMap<>();
        Map<String, Character> sToPattern = new HashMap<>();
        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String str = sArray[i];
            if (!Objects.equals(patternToS.getOrDefault(c, str), str) || !Objects.equals(sToPattern.getOrDefault(str, c), c))
                return false;
            patternToS.put(c, str);
            sToPattern.put(str, c);
        }
        return true;
    }

    /**
     * 242. Valid Anagram
     * Given two strings s and t, return true if t is an anagram of s, and false otherwise.
     * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
     */
    public boolean isAnagram(String s, String t) {
        int[] sArr = new int[26];
        int[] tArr = new int[26];
        for (char c : s.toCharArray())
            sArr[c - 'a']++;
        for (char c : t.toCharArray())
            tArr[c - 'a']++;

        for (int i = 0; i < 26; i++)
            if (sArr[i] != tArr[i]) return false;

        return true;
    }

    /**
     * 49. Group Anagrams
     * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
     * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
     * typically using all the original letters exactly once.
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            char[] arr = str.toCharArray();
            Arrays.sort(arr);
            String sorted = new String(arr);
            if (!map.containsKey(sorted)) map.put(sorted, new ArrayList<>());
            map.get(sorted).add(str);
        }
        return new ArrayList<>(map.values());
    }

    /**
     * 1. Two SumGiven an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
     * You may assume that each input would have exactly one solution, and you may not use the same element twice.
     * You can return the answer in any order.
     */
    public int[] twoSumI(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) return new int[]{map.get(target - nums[i]), i};
            map.put(nums[i], i);
        }
        return null;
    }

    /**
     * 202. Happy Number
     * Write an algorithm to determine if a number n is happy.
     * A happy number is a number defined by the following process:
     * Starting with any positive integer, replace the number by the sum of the squares of its digits.
     * Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
     * Those numbers for which this process ends in 1 are happy.
     * Return true if n is a happy number, and false if not.
     */
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        while (!set.contains(n)) {
            if (n == 1) return true;

            set.add(n);
            n = numOfSquares(n);
        }
        return false;
    }

    private int numOfSquares(int n) {
        int num = 0;
        while (n > 0) {
            num += (int) Math.pow((n % 10), 2);
            n /= 10;
        }
        return num;
    }

    /**
     * 219. Contains Duplicate II
     * Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
     * such that nums[i] == nums[j] and abs(i - j) <= k.
     */
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i]))
                return true;
            set.add(nums[i]);
            if (i >= k)
                set.remove(nums[i - k]);
        }
        return false;
    }

    /**
     * 128. Longest Consecutive Sequence
     * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
     * You must write an algorithm that runs in O(n) time.
     */
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums)
            set.add(i);

        int longest = 0;
        for (int item : set) {
            if (set.contains(item - 1))
                continue;

            int jump = 0;
            while (set.contains(item + jump))
                jump++;

            longest = Math.max(longest, jump);
        }
        return longest;
    }

    /**
     * 228. Summary Ranges
     * You are given a sorted unique integer array nums.
     * A range [a,b] is the set of all integers from a to b (inclusive).
     * Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
     * That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
     * Each range [a,b] in the list should be output as:
     * "a->b" if a != b
     * "a" if a == b
     */
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        int left = 0;
        while (left < nums.length) {
            StringBuilder str = new StringBuilder().append(nums[left]);
            int right = left;
            while (right + 1 < nums.length && nums[right + 1] == nums[right] + 1)
                right++;
            if (right > left)
                str.append("->").append(nums[right]);
            result.add(str.toString());
            left = right + 1;
        }
        return result;
    }

    /**
     * 56. Merge Intervals
     * Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
     * and return an array of the non-overlapping intervals that cover all the intervals in the input.
     */
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<List<Integer>> list = new ArrayList<>();
        for (int[] interval : intervals) {
            if (list.isEmpty() || list.get(list.size() - 1).get(1) < interval[0])
                list.add(Arrays.asList(interval[0], interval[1]));

            else {
                list.get(list.size() - 1).set(1, Math.max(list.get(list.size() - 1).get(1), interval[1]));
            }
        }
        int[][] result = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            result[i][0] = list.get(i).get(0);
            result[i][1] = list.get(i).get(1);
        }

        return result;
    }

    /**
     * 57. Insert Interval
     * You are given an array of non-overlapping intervals intervals where
     * intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
     * You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
     * Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
     * does not have any overlapping intervals (merge overlapping intervals if necessary).
     * Return intervals after the insertion.
     */
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> list = new ArrayList<>();
        int i = 0;
        while (i < intervals.length && intervals[i][1] < newInterval[0]) {
            list.add(intervals[i]);
            i++;
        }

        int start = newInterval[0], end = newInterval[1];
        while (i < intervals.length && end >= intervals[i][0]) {
            start = Math.min(start, intervals[i][0]);
            end = Math.max(end, intervals[i][1]);
            i++;

        }
        list.add(new int[]{start, end});

        while (i < intervals.length && newInterval[1] < intervals[i][0]) {
            list.add(intervals[i]);
            i++;
        }

        intervals = list.toArray(new int[list.size()][2]);
        return intervals;
    }


    /**
     * 452. Minimum Number of Arrows to Burst Balloons
     * There are some spherical balloons taped onto a flat wall that represents the XY-plane.
     * The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
     * denotes a balloon whose horizontal diameter stretches between xstart and xend.
     * You do not know the exact y-coordinates of the balloons.
     * Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
     * A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot.
     * A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
     * Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
     */
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int numArrows = 1;
        int end = points[0][1];
        for (int[] point : points) {
            if (point[0] <= end) {
                end = Math.min(end, point[1]);
            } else {
                numArrows++;
                end = point[1];
            }
        }
        return numArrows;
    }

    /**
     * 20. Valid Parentheses
     * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
     * An input string is valid if:
     * Open brackets must be closed by the same type of brackets.
     * Open brackets must be closed in the correct order.
     * Every close bracket has a corresponding open bracket of the same type.
     */
    public boolean isValid(String s) {
        Map<Character, Character> map = Map.of('{', '}', '[', ']', '(', ')');
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c))
                stack.push(c);
            else { // its closing brackets
                if (stack.empty())
                    return false;
                // stack not empty
                char key = stack.pop();
                if (map.get(key) != c)
                    return false;
            }
        }
        return stack.empty();
    }

    /**
     * 71. Simplify Path
     * Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
     * convert it to the simplified canonical path.
     * In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level,
     * and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem,
     * any other format of periods such as '...' are treated as file/directory names.
     * The canonical path should have the following format:
     * The path starts with a single slash '/'.
     * Any two directories are separated by a single slash '/'.
     * The path does not end with a trailing '/'.
     * The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
     * Return the simplified canonical path.
     */
    public String simplifyPath(String path) {

    }
}

/**
 * 380. Insert Delete GetRandom O(1)
 * Implement the RandomizedSet class:
 * RandomizedSet() Initializes the RandomizedSet object.
 * bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
 * bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
 * int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called).
 * Each element must have the same probability of being returned.
 * You must implement the functions of the class such that each function works in average O(1) time complexity.
 */


class RandomizedSet {

    Set<Integer> set;
    Random random;

    public RandomizedSet() {
        set = new HashSet<>();
        random = new Random();
    }

    public boolean insert(int val) {
        return set.add(val);

    }

    public boolean remove(int val) {
        return set.remove(val);

    }

    public int getRandom() {
        int rand = random.nextInt(set.size());
        int ret = 0;
        int i = 0;
        for (int item : set) {
            if (i == rand) {
                ret = item;
                break;
            }
            i++;
        }
        return ret;
    }
}

/**
 * 381. Insert Delete GetRandom O(1) - Duplicates allowed
 * RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset).
 * It should support inserting and removing specific elements and also reporting a random element.
 * Implement the RandomizedCollection class:
 * RandomizedCollection() Initializes the empty RandomizedCollection object.
 * bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
 * bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present,
 * false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
 * int getRandom() Returns a random element from the current multiset of elements.
 * The probability of each element being returned is linearly related to the number of the same values the multiset contains.
 * You must implement the functions of the class such that each function works on average O(1) time complexity.
 * Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection
 */
class RandomizedCollection {
    Map<Integer, Set<Integer>> map;
    List<Integer> list;
    Random random;

    public RandomizedCollection() {
        map = new HashMap<>();
        list = new ArrayList<>();
        random = new Random();
    }

    public boolean insert(int val) {
        boolean con = map.containsKey(val);
        if (!con) map.put(val, new HashSet<>());

        map.get(val).add(list.size());
        list.add(val);

        return !con;
    }

    public boolean remove(int val) {
        boolean con = map.containsKey(val);
        if (!con) return false;

        Set<Integer> set = map.get(val);
        int indToRemove = set.iterator().next();
        set.remove(indToRemove);
        if (set.isEmpty()) map.remove(val);

        if (indToRemove != list.size() - 1) {
            // swap the indexes
            int lastItem = list.get(list.size() - 1);
            list.set(indToRemove, lastItem);
            map.get(lastItem).remove(list.size() - 1);
            map.get(lastItem).add(indToRemove);
        }
        list.remove(list.size() - 1);
        return true;
    }

    public int getRandom() {
        return list.get(random.nextInt(list.size()));
    }
}



