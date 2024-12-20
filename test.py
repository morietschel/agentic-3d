import main
from config import OBJECTS_LIST, SCENE_DESCRIPTION, NUM_REPLICATIONS, NUM_VERSIONS
from api_utils_openai import test_api_call
from collections import defaultdict
import pandas as pd

def test_one_object():
    num_successes = 0
    successes_overall = 0
    ratings = defaultdict(list)
    first_success = {}

    for i in range(1, NUM_REPLICATIONS + 1):
        success = False
        main.main(SCENE_DESCRIPTION)

        for j in range(1, NUM_VERSIONS + 1):
            output = test_api_call(SCENE_DESCRIPTION, f"renders/scene-version{j}.png")
            rating = output['rating']

            # Add rating for each generation to ratings dictionary
            ratings[f"iteration{i}"].append(rating)

            if rating >= 5:
                print(f"Version {j} MATCHED")
                num_successes += 1
                if not success:
                    first_success[f"iteration{i}"] = j
                    success = True
            else:
                print(f"Version {j} NOT MATCHED")

        if num_successes >= 1:
            successes_overall += 1
            print("Successes_overall:", successes_overall)
    
    return {"Success rate": successes_overall / NUM_REPLICATIONS, "Ratings": dict(ratings), "Generations until first success": first_success}

def test_objects():
    output_table = pd.DataFrame({"Object": [], "Mean Initial Quality Score": [], "Mean Final Quality Score": [], "Mean Max Quality Score": [], "Mean Overall Score Improvement": [], "Mean Iterations to First Success": [], "Mean Quality Score": []})

    for i in range(len(OBJECTS_LIST)): # go through all of the objects
        num_successes = 0
        successes_overall = 0
        ratings = defaultdict(list)
        first_success = {}

        for j in range(1, NUM_REPLICATIONS + 1):
            success = False
            main.main(OBJECTS_LIST[i])

            for k in range(1, NUM_VERSIONS + 1):
                output = test_api_call(OBJECTS_LIST[i], f"renders/scene-version{k}.png")
                rating = output['rating']

                # Add rating for each generation to ratings dictionary
                ratings[f"iteration{j}"].append(rating)

                if rating >= 5:
                    print(f"Version {k} MATCHED")
                    num_successes += 1
                    if not success:
                        first_success[f"iteration{j}"] = j
                        success = True
                else:
                    print(f"Version {k} NOT MATCHED")

            if num_successes >= 1:
                successes_overall += 1
                print("Successes_overall:", successes_overall)
            
            if not success:
                first_success[f"iteration{j}"] = 10

        ratings = dict(ratings)
        initial_quality_scores = 0
        final_quality_scores = 0
        score_improvements = 0
        mean_scores = 0
        max_quality_scores = 0
        for key in ratings.keys():
            initial_quality_scores += ratings[key][0]
            final_quality_scores += ratings[key][NUM_VERSIONS - 1]
            max_score = max(ratings[key])
            min_score = min(ratings[key])
            score_improvements += max_score - min_score
            max_quality_scores += max_score
            mean_scores += sum(ratings[key]) / NUM_VERSIONS

        print("Initial quality scores:", initial_quality_scores)
        mean_first_success = round(sum(first_success.values()) / NUM_REPLICATIONS, 3) if first_success else 0
        mean_initial_quality_score = round(initial_quality_scores / NUM_REPLICATIONS, 3)
        mean_final_quality_score = round(final_quality_scores / NUM_REPLICATIONS, 3)
        mean_max_quality_score = round(max_quality_scores / NUM_REPLICATIONS, 3)
        mean_score_improvement = round(score_improvements / NUM_REPLICATIONS, 3)
        overall_mean_score = round(mean_scores / NUM_REPLICATIONS, 3)

        new_row = pd.DataFrame({"Object": [OBJECTS_LIST[i]], "Mean Initial Quality Score": [mean_initial_quality_score], "Mean Final Quality Score": [mean_final_quality_score], "Mean Max Quality Score": [mean_max_quality_score], "Mean Overall Score Improvement": [mean_score_improvement], "Mean Iterations to First Success": [mean_first_success], "Mean Quality Score": [overall_mean_score]})
        output_table = pd.concat([output_table, new_row], ignore_index=True)
        print("Output Table")
        print(output_table)

        # Print so you can see the current table after each object
        output_table.to_csv(f"metrics_by_object{i}.csv")

    # Final save at the end
    numerical_cols = output_table.select_dtypes(include="number")
    column_averages = numerical_cols.mean().round(3)
    print("Column averages", column_averages)
    output_table.loc["Average"] = column_averages
    output_table.loc["Average", "Object"] = "N/A"
    output_table.to_csv("metrics_by_object.csv")

    # Get metrics by complexity level
    complexity_table = output_table.drop(columns=["Object", "Mean Initial Quality Score", "Mean Final Quality Score", "Mean Max Quality Score"])
    # Group indices into groups of 5
    num_rows = len(complexity_table)
    groups = [i // 5 for i in range(num_rows)]
    complexity_table["Group"] = groups
    # Group by 'Group' and compute the mean
    complexity_table = complexity_table.groupby("Group").mean().round(3)
    # Reset the index
    complexity_table.reset_index(drop=True, inplace=True)
    # Insert levels into the table
    levels = ["Easy", "Medium", "Hard"]
    complexity_table.insert(0, "Level", levels)
    # Output the table
    print(complexity_table)
    complexity_table.to_csv("metrics_by_complexity.csv", index=False)

    return output_table 

#print(test_one_object())
print(test_objects())