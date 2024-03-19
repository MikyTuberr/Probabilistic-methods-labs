class Permutations:
    @staticmethod
    def generate(data: list) -> list:
        stack = [(data, [])] 
        
        result = []
        while stack:
            current_data, current_permutation = stack.pop()  
            if len(current_data) == 1:
                result.append(current_permutation + current_data) 
            else:
                for i in range(len(current_data)):
                    next_element = current_data[i]
                    next_permutation = current_permutation + [next_element]
                    next_data = current_data[:i] + current_data[i+1:]
                    stack.append((next_data, next_permutation))  
                    
        return result