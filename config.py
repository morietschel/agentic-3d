# config.py

# Scene description
SCENE_DESCRIPTION = ' a pair of eyeglasses with one round lens and one square lens'

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

# Max iterations
MAX_ITERATIONS = 10

# Rendering settings
IMAGE_SIZE = (800, 600)    # Width, Height in pixels

# Camera settings
CAMERA_POSITION = [25.40, 4.02, 46.29]    # x, y, z position of the camera
CAMERA_LOOK_AT = [0, 0, 0]     # x, y, z point the camera looks at
CAMERA_ANGLE = 90              # Camera angle in degrees