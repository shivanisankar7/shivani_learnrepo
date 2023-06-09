import json

# Step 2: Read the JSON data into a dictionary
with open('ex5.json', 'r') as file:
    ex5 = json.load(file)

# Step 3: Modify the dictionary to add a new batter
for item in ex5:
    if item['name'] == 'Old Fashioned':
        item['batters']['batter'].append({"id": "1005", "type": "Coffee"})

# Step 4: Write the updated dictionary back to the file
with open('ex5.json', 'w') as file:
    json.dump(ex5, file, indent=4)
