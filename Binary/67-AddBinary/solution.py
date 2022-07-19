class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry = "", 0
        index_a, index_b = len(a)-1, len(b)-1
        while index_a >= 0 or index_b >= 0:
            tempt = carry
            if index_a >= 0:
                tempt += int(a[index_a])
            if index_b >= 0:
                tempt += int(b[index_b])

            index_a, index_b = index_a-1, index_b-1
            carry = 1 if tempt > 1 else 0
            result += str(tempt % 2)

        if carry != 0:
            result += str(carry)
        return result[::-1]
