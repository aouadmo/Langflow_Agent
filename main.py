from langflow import load_flow_from_json

# Load the flow
flow = load_flow_from_json('flow.json')

# Use the flow as a chain
response = flow("Your input prompt here")
print(response)
