import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import AddUser, Batch
from recombee_api_client.exceptions import APIException

# --- CONFIG ---
DB_ID = 'exxmple-top-100-books'
TOKEN = 'Lc2xgXTGrgmPkvdHcHwd1xhfRdBSujuIkhCzRCStW2BHBWjRWGnrSKsjBSY92h4x'

client = RecombeeClient(DB_ID, TOKEN, region=Region.EU_WEST)

# Read people.csv
df = pd.read_csv('people.csv', encoding='utf-8-sig')

# Remove rows with empty SP ID
df = df.dropna(subset=['SP ID'])
df = df[df['SP ID'].str.strip() != '']

print(f"Sending {len(df)} user IDs...\n")

# Create a list of AddUser requests
user_ids = [str(row['SP ID']).strip() for _, row in df.iterrows()]

# Send user IDs using Batch
requests = [AddUser(user_id) for user_id in user_ids]

try:
    response = client.send(Batch(requests))
    print(f"All IDs sent successfully!")
    print(f"\nUsers added:")
    for user_id in user_ids:
        print(f"  - {user_id}")
    print(f"\nTotal: {len(user_ids)} users")
except APIException as e:
    print(f"Error sending IDs: {e}")

