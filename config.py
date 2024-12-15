# config.py

# give ability to choose which LLM, how many runs (outer for loop), and which object to render (DONE)

# LLM choices
LLM_CHOICES = {'gpt-4o': 'gpt-4o-2024-08-06', 'gpt-4o-mini': 'gpt-4o-mini-2024-07-18'}

# Scene description
SCENE_DESCRIPTION = " a mug with a handle"

# Objects to test
OBJECTS_LIST = [" a chair", " a table", " a pyramid", " a bowl", " a bottle", \
           " a vase", " a candle with a wick", " a mug with a handle", " a desk lamp", " a wine glass", \
           " a car", "a spiral staircase", " a cathedral", " a pair of eye glasses", " a wrist watch"]

OBJECTS_DICT = {"Easy": [" a chair", " a table", " a pyramid", " a bowl", " a bottle"],
                "Medium": [" a vase", " a candle with a wick", " a mug with a handle", " a desk lamp", " a wine glass"],
                "Hard": [" a car", "a spiral staircase", " a cathedral", " a pair of eye glasses", " a wrist watch"]}

# Scene descriptions for testing - Unconventionally Feasible Objects - 50 objects
UFO_LIST = [' a chair with two legs', ' a chair with three legs', \
        ' a chair with five legs', ' a chair with six legs', ' a chair with seven legs', \
        ' a chair with one armrest', ' a chair with three armrests', ' a chair with two backrests', \
        ' a chair with three backrests', ' a stool with two legs', ' a stool with three legs', \
        ' a stool with five legs', ' a stool with six legs', ' a stool with seven legs', \
        ' a stool with one armrest', ' a stool with three armrests', ' a stool with two backrests', \
        ' a stool with three backrests', ' a desk with two legs', ' a desk with three legs', \
        ' a desk with five legs', ' a desk with six legs', ' a desk with seven legs', \
        ' a table with two legs', ' a table with three legs', ' a table with five legs', \
        ' a table with six legs', ' a table with seven legs', ' a pair of eyeglasses with one round lens and one square lens', \
        ' a pair of eyeglasses with one round lens and one triangle lens', ' a pair of eyeglasses with one square lens and one triangle lens', \
        ' a pair of eyeglasses with three lenses', ' a pair of eyeglasses with four lenses', ' a pair of eyeglasses with five lenses', \
        ' a sofa with one leg', ' a sofa with two legs', ' a sofa with three legs', ' a sofa with five legs',  \
        ' a sofa with legs that are longer than its backrest', ' a sofa with armrests that are longer than its backrest', \
        ' a lamp with two legs', ' a lamp with four legs', ' a lamp with five legs', ' a bottle whose lid is twice as wide as its mouth', \
        ' a bottle with a lid that is three times wider than its mouth', ' a bottle with a lid that is four times wider than its mouth', \
        ' a mug with two handles', ' a mug with three handles', ' a mug with four handles', ' a mug with five handles']

UFO_DICT = {1: 'a chair with two legs',
                2: 'a chair with three legs',
                3: 'a chair with five legs',
                4: 'a chair with six legs',
                5: 'a chair with seven legs',
                6: 'a chair with one armrest',
                7: 'a chair with three armrests',
                8: 'a chair with two backrests',
                9: 'a chair with three backrests',
                10: 'a stool with two legs',
                11: 'a stool with three legs',
                12: 'a stool with five legs',
                13: 'a stool with six legs',
                14: 'a stool with seven legs',
                15: 'a stool with one armrest',
                16: 'a stool with three armrests',
                17: 'a stool with two backrests',
                18: 'a stool with three backrests',
                19: 'a desk with two legs',
                20: 'a desk with three legs',
                21: 'a desk with five legs',
                22: 'a desk with six legs',
                23: 'a desk with seven legs',
                24: 'a table with two legs',
                25: 'a table with three legs',
                26: 'a table with five legs',
                27: 'a table with six legs',
                28: 'a table with seven legs',
                29: 'a pair of eyeglasses with one round lens and one square lens',
                30: 'a pair of eyeglasses with one round lens and one triangle lens',
                31: 'a pair of eyeglasses with one square lens and one triangle lens',
                32: 'a pair of eyeglasses with three lenses',
                33: 'a pair of eyeglasses with four lenses',
                34: 'a pair of eyeglasses with five lenses',
                35: 'a sofa with one leg',
                36: 'a sofa with two legs',
                37: 'a sofa with three legs',
                38: 'a sofa with five legs',
                39: 'a sofa with legs that are longer than its backrest',
                40: 'a sofa with armrests that are longer than its backrest',
                41: 'a lamp with two legs',
                42: 'a lamp with four legs',
                43: 'a lamp with five legs',
                44: 'a bottle whose lid is twice as wide as its mouth',
                45: 'a bottle with a lid that is three times wider than its mouth',
                46: 'a bottle with a lid that is four times wider than its mouth',
                47: 'a mug with two handles',
                48: 'a mug with three handles',
                49: 'a mug with four handles',
                50: 'a mug with five handles'}

# Num versions
NUM_VERSIONS = 10

# Num replications
NUM_REPLICATIONS = 3

# Rendering settings
IMAGE_SIZE = (800, 600)    # Width, Height in pixels

# Camera settings
CAMERA_POSITION = [25.40, 4.02, 46.29]    # x, y, z position of the camera
CAMERA_LOOK_AT = [0, 0, 0]     # x, y, z point the camera looks at
CAMERA_ANGLE = 90              # Camera angle in degrees