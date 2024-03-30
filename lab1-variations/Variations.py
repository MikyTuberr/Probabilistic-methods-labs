class Variations:
    @staticmethod
    def generate_no_repeats(data: list, K: int) -> list:
        stack = [(data, [])]
        result = []
        while stack:
            curr_data, curr_var = stack.pop()
            if len(curr_var) == K:
                result.append(curr_var)
            else:
                iter = len(curr_data)
                if iter >= K:
                    for i in range(iter):
                        next_data = curr_data[:i] + curr_data[i+1:]
                        next_per = curr_var + [curr_data[i]]
                        stack.append((next_data, next_per))
        return result


    @staticmethod
    def generate_repeats(data: list, K: int) -> list:
        stack = [(data, [])]
        result = []
        while stack:
            curr_data, curr_var = stack.pop()
            if len(curr_var) == K:
                curr_var = sorted(curr_var)
                if not curr_var in result:
                    result.append(curr_var)
            else:
                iter = len(curr_data)
                if iter >= K:
                    for i in range(iter):
                        next_data = curr_data[i]
                        next_var = curr_var + [next_data]
                        stack.append((curr_data, next_var))
        return result
