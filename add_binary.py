# def add(a: str, b: str) -> tuple[str, bool]:
#     # Lengthly way to add
#     if a == '1' and b == '1':
#         return ('0', True)
#     if (a == '1' and b == '0') or (a == '0' and b == '1'):
#         return ('1', False)
#     return ('0', False)


def add(a: str, b: str) -> tuple[str, bool]:
    # ord("0") is 48
    # ord("1") is 49
    s = ord(a) + ord(b)
    # 1 + 1
    if s == 98:
        return ('0', True)
    # 1 + 0 or 0 + 1
    if s == 97:
        return ('1', False)
    
    # We can only have 0 + 0 here
    return ('0', False)


def pad(a: str, num_zeros: int) -> str:
    return "0" * num_zeros + a


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # To avoid annoying operations with lists of different lengths, pad shorter array with zeros
        if len(a) < len(b):
            a = pad(a, len(b) - len(a))
        elif len(a) > len(b):
            b = pad(b, len(a) - len(b))
        
        # Make sure we have one more digit than largest string
        s = ['0'] * (len(a) + 1)
        for i in range(len(a) - 1, -1, -1):
            digit, should_transfer = add(a[i], b[i])
            s[i + 1], should_transfer_1 = add(s[i + 1], digit)
            # If we overflow, place 1 to next digit to the left
            # Because we allocated one more digit, we won't have index out of range error
            if should_transfer or should_transfer_1:
                s[i] = '1'

        return ''.join(s) if s[0] != '0' else ''.join(s[1:])


s = Solution()
assert s.addBinary("111", "11") == "1010"

print("All good")
