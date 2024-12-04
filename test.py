import main
from config import UFO_LIST

def success_rate_one_object():
    num_successes = 0
    for i in range(10):
        if main.main():
            num_successes += 1
    
    return f"Success rate over 10 iterations: {num_successes / 10}"

def success_rate_on_UFOs():
    num_successes = 0
    for i in range(50):
        if main.main(UFO_LIST[i]):
            num_successes += 1
    
    return f"Success rate on UFO_LIST: {num_successes / 50}"

#print(success_rate_one_object())
print(success_rate_on_UFOs())