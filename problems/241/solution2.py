# Accepted: 70ms (6.44%), 16.51MB (88.60%)

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def evaluate(expression: str) -> List[int]:
            if expression.isdigit():
                return [int(expression)]

            # get evaluated expressions using built-in eval function
            evaluated: List[int] = [] 
            for i, char in enumerate(expression):
                if char not in "*+-":
                    continue

                lower = evaluate(expression[:i])
                upper = evaluate(expression[i+1:])

                for n1 in lower:
                    for n2 in upper:
                        evaluated.append(eval(f"{n1}{char}{n2}"))

            return evaluated

        return evaluate(expression)
