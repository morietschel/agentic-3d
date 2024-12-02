# success rate (out of 10 tries)
import main

def success_rate():
    num_successes = 0
    for i in range(2):
        if main.main():
            num_successes += 1
    
    return f"Success rate over 2 iterations: {num_successes / 2}"

print(success_rate())