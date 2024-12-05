import main
from config import UFO_LIST, SCENE_DESCRIPTION
from api_utils import test_api_call
from collections import defaultdict

# Instead, loop through all generations and if there is at least one success, then can count that as a success overall
# Can also keep track of which iteration it got the first success on

# How many iterations were successful

# Get both 'T' or 'F' for whether generation was successful, but also ask model to give generation a score 1-10 of how good it is
def test_one_object():
    num_successes = 0
    successes_overall = 0
    ratings = defaultdict(list)
    first_success = {}

    for i in range(10):
        success = False
        main.main(SCENE_DESCRIPTION)

        for j in range(10):
            # API call to check if generation was successful, to rate generation on scale of 1-10
            # If successful, add to num_sucesses
            output = test_api_call(SCENE_DESCRIPTION, f"renders/scene{j}.png")
            match = output['match']

            # Add rating for each generation to ratings dictionary
            ratings[f"iteration{i}"].append(output['rating'])

            if match:
                num_successes += 1
                if not success:
                    first_success[f"iteration{i}"] = j + 1
                    success = True

        if num_successes >= 1:
            successes_overall += 1
    
    # Rough for now, can be changed
    return {"Success rate": successes_overall / 10, "Ratings": ratings, "Generations until first success": first_success}


# NOT FIXED YET
def test_UFOs():
    num_successes = 0
    for i in range(50):
        if main.main(UFO_LIST[i]):
            num_successes += 1
    
    return f"Success rate on UFO_LIST: {num_successes / 50}"

print(test_one_object())
#print(test_UFOs())