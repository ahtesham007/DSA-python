def solve(s):
    mpp = {}
    left = 0
    right = 0
    n = len(s)
    length = 0
    while right < n:
        if s[right] in mpp:
            left = max(mpp[s[right]] + 1, left)
        mpp[s[right]] = right

        length = max(length, right - left + 1)
        right += 1
    return length


def lengthOfLongestSubstring(s: str) -> int:

        if not s:
            return 0
        elif len(s)==1:
            return 1
        
        sub_str = ''
        m_len = 0

        for char in s:
            if char in sub_str:
                sub_str = sub_str[sub_str.index(char)+1:]
            
            sub_str += char
            m_len = max(m_len, len(sub_str))
        
        return m_len

print(solve('abcabcbb'))