class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        priority = {
            "electronics": 0, 
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid_coupons = []

        for c, b, a in zip(code, businessLine, isActive):
            if not a: continue
            if not c: continue
            if b not in priority: continue

            is_valid = True
            for char in c:
                if not (char.isalnum() or char == '_'):
                    is_valid = False
                    break

            if is_valid:
                valid_coupons.append((b, c))

        valid_coupons.sort(key=lambda x: (priority[x[0]], x[1]))

        return [x[1] for x in valid_coupons]

