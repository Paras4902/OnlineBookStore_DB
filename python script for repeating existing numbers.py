import random

# Generate a list of 107 IDs
ids = list([5072,5713,6354,6995,7636,8277,8918,9559,10200,10841,11482,12123,12764,13405,14046,14687,15328,15969,16610,17251,
            17892,18533,19174,19815,20456,21097,21738,22379,23020,23661,24302,24943,25584,26225,26866,27507,28148,28789,29430,
            30071,30712,31353,31994,32635,33276,33917,34558,35199,35840,36481,37122,37763,38404,39045,39686,40327,40968,41609,
            42250,42891,43532,44173,44814,45455,46096,46737,47378,48019,48660,49301,49942,50583,51224,51865,52506,53147,53788,
            54429,55070,55711,56352,56993,57634,58275,58916,59557,60198,60839,61480,62121,62762,63403,64044,64685,65326,65967,
            66608,67249,67890,68531,69172,69813,70454,71095,71736,72377,73018
])

# Create an empty list to store the repeated IDs
repeated_ids = []

# Calculate the total number of repetitions needed
total_repetitions = 8500

# Distribute the repetitions randomly among the IDs
while len(repeated_ids) < total_repetitions:
    id = random.choice(ids)
    repeated_ids.append(id)

# Shuffle the list to ensure randomness
random.shuffle(repeated_ids)

# Print each ID on a new line
for id in repeated_ids:
    print(id)
