def fibonacci(num, memory = {0:0, 1:1}):
    if num not in memory:
        memory[num] =fibonacci(num-1, memory) + fibonacci(num-2, memory)
    return memory[num]

