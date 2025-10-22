from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import AddUserProperty, Batch

# --- CONFIG ---
DB_ID = 'exxmple-top-100-books'
TOKEN = 'Lc2xgXTGrgmPkvdHcHwd1xhfRdBSujuIkhCzRCStW2BHBWjRWGnrSKsjBSY92h4x'

client = RecombeeClient(DB_ID, TOKEN, region=Region.EU_WEST)

# Define user properties (property names and types)
properties = {
    'name': 'string',            # User name
    'age': 'int',                # Age 
    'location': 'string',        # Location
    'email': 'string'            # Email 
}

requests = [AddUserProperty(name, typ) for name, typ in properties.items()]

response = client.send(Batch(requests))
print("User properties added successfully:")
for name, typ in properties.items():
    print(f"  - {name}: {typ}")

