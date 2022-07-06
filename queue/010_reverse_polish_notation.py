def apply(l, op, r):
    match op:
        case '+':
            return l + r
        case '-':
            return l - r
        case '*':
            return l * r
        case _:
            return int(l / r)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        operators = '+-*/'
        for i in range(len(tokens)):
            token = tokens[i]
            if token in operators:
                right = q.pop()
                left = q.pop()
                res = apply(left, token, right)
                q.append(res)
            else:
                q.append(int(token))

        return q[0]