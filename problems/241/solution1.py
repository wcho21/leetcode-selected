# Accepted: 36ms (70.96%), 16.68MB (57.68%)

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def tokenize(expression: str) -> Tuple[List[int], List[str]]:
            digitBuf = []
            nums = []
            operators = []

            for char in expression:
                if char not in "+-*":
                    digitBuf.append(char)
                    continue

                if len(digitBuf) > 0:
                    nums.append(int("".join(digitBuf)))
                    digitBuf = []

                operators.append(char)

            nums.append(int("".join(digitBuf)))

            return nums, operators

        nums, operators = tokenize(expression)

        # recursion over intervals on nums
        def evaluate(beg: int = 0, end: int = len(nums)) -> List[int]:
            assert end > beg

            if end - beg == 1:
                return [nums[beg]]

            if end - beg == 2:
                return [applyOperator(operators[beg], nums[beg], nums[beg+1])]

            evaluated: List[int] = []
            for i in range(beg+1, end):
                lower = evaluate(beg, i)
                upper = evaluate(i, end)
                operator = operators[i-1]

                evaluated.extend(joinByOperator(operator, lower, upper))

            return evaluated

        def joinByOperator(operator: str, operands1: List[int], operands2: List[int]) -> List[int]:
            evaluated: List[int] = []
            for operand1 in operands1:
                for operand2 in operands2:
                    evaluated.append(applyOperator(operator, operand1, operand2))
            return evaluated

        def applyOperator(operator: str, operand1: int, operand2: int) -> int:
            if operator == "*":
                return operand1 * operand2
            if operator == "+":
                return operand1 + operand2
            if operator == "-":
                return operand1 - operand2
            raise Exception(f"bad operator '{operator}'")

        return evaluate()
