# Accepted: 34ms (76.88%), 17.20MB (38.80%)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # consider only 12 least significant bits.
        # the leftmost bit will behave as a sign bit
        MASK = 0xFFF

        a &= MASK
        b &= MASK

        while True:
            carry = ((a & b) << 1) & MASK
            added = a ^ b

            if carry == 0:
                # if leftmost bit is set to 1, invert the varable to make negative
                return added if added <= (MASK>>1) else ~(added^MASK)

            a = carry
            b = added
