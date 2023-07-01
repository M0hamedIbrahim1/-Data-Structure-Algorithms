# link : https://leetcode.com/problems/fair-distribution-of-cookies/description/
# author : Mohamed Ibrahim


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        result = float('inf')

        def recurse(i, children):
            if i == len(cookies):
                nonlocal result
                result = min(result, max(children))
                return

            cookie_size = cookies[i]
            for child in range(min(i + 1, k)):
                children[child] += cookie_size
                recurse(i + 1, children)
                children[child] -= cookie_size

        recurse(0, children)

        return result
