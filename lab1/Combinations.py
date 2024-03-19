class Combinations:
    @staticmethod
    def generate(elements: list, K: int) -> list:
        subsets = []

        def backtrack(start, current):
            if len(current) == K:
                subsets.append(current[:])  
                return
            for i in range(start, len(elements)):
                current.append(elements[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return subsets
