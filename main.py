

def sum_list(numbers):
    return sum(numbers)


def sort_list(numbers):
    return sorted(numbers)


def apply_function(func, numbers):
    return [func(x) for x in numbers]  


def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

if __name__ == "__main__":
   
    nums = [5, 2, 9, 1, 7]

    print("Lista original:", nums)

    
    print("Soma:", sum_list(nums))

   
    print("Ordenada:", sort_list(nums))

    
    print("Quadrados:", apply_function(lambda x: x**2, nums))

    
    times3 = multiplier(3)
    print("Multiplicados por 3:", apply_function(times3, nums))
