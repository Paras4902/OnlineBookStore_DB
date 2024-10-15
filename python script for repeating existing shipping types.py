import random

# Generate a list of 107 IDs
ids = list(['Expedited Shipping','Flat Rate Shipping','Freight Shipping','International Shipping','Local Delivery or Pickup','Multiple Addresses','Overnight Shipping',
            'Priority Mail','Same-Day Delivery','Standard Ground Shipping'])

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
