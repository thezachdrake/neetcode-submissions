class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score: list[int] = []
        for idx,op in enumerate(operations):
            match op:
              case "+":
                two_back: int = int(score[-1])
                one_back: int = int(score[-2])
                score.append((two_back + one_back))
              case "C":
                score.pop()
              case "D":
                score.append(score[-1] * 2)
              case _:
                score.append(int(op))
        return sum(score)

