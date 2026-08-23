class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        tfreq = {}

        for char in t:
            tfreq[char] = tfreq.get(char, 0) + 1

        sfreq = {}

        l = 0
        have = 0
        need = len(tfreq)

        min_len = float("inf")
        start = 0

        for r in range(len(s)):

            char = s[r]
            sfreq[char] = sfreq.get(char, 0) + 1

            if char in tfreq and sfreq[char] == tfreq[char]:
                have += 1

            while have == need:

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                left_char = s[l]
                sfreq[left_char] -= 1

                if left_char in tfreq and sfreq[left_char] < tfreq[left_char]:
                    have -= 1

                l += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]