import json

# Dictionary of Indian states and capitals
indian_states = {
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Kerala": "Thiruvananthapuram",
    "Rajasthan": "Jaipur"
}

# Write the dictionary to a JSON file
with open('indian_states.json', 'w') as json_file:
    json.dump(indian_states, json_file)

print("Dictionary written to indian_states.json")
