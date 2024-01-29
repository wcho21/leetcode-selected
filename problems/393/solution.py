# Accepted: 90ms (92.70%), 17.49MB (44.53%)

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # continue if valid; otherwise early return false
        i = 0
        while i < len(data):
            # continue if valid one-byte prefix
            if (data[i] >> 7) & 0b1 == 0:
                i += 1
                continue

            # return false if invalid second byte
            if i+1 >= len(data) or ((data[i+1] >> 6) & 0b11) != 0b10:
                return False

            # continue if valid two-byte prefix
            if ((data[i] >> 5) & 0b111) == 0b110:
                i += 2
                continue

            # return false if invalid third byte
            if i+2 >= len(data) or ((data[i+2] >> 6) & 0b11) != 0b10:
                return False

            # continue if valid three-byte prefix
            if ((data[i] >> 4) & 0b1111) == 0b1110:
                i += 3
                continue

            # return false if invalid fourth byte
            if i+3 >= len(data) or ((data[i+3] >> 6) & 0b11) != 0b10:
                return False

            # continue if valid four-byte prefix
            if ((data[i] >> 3) & 0b11111) == 0b11110:
                i += 4
                continue

            return False

        return True
