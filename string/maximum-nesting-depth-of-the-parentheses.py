class Solution:
    def maxDepth(self, s: str) -> int:
        st = []
        mlen = 0
        for c in s:
            if c =="(":
                st.append("(")
                mlen = max(mlen,len(st))
            elif c == ")":
                st.pop()
            else:
                continue
        return mlen