import pandas as pd
import random
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetUserValues
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

print(f"Loading {len(df)} users...\n")

for _, row in df.iterrows():
    user_id = str(row['SP ID']).strip()
    name = str(row['Sales person']).strip()
    age = random.randint(7, 65)  # Generate random age between 7 and 65
    location = str(row['Location']).strip() if pd.notna(row['Location']) else ''
    
    # Generate email from name (lowercase, replace spaces with dots, remove special chars)
    email_name = name.lower().replace(' ', '.').replace("'", "").replace("-", "")
    email = f"{email_name}@company.com"
    
    values = {
        'name': name,
        'age': age,
        'location': location,
        'email': email
    }

    try:
        client.send(SetUserValues(user_id, values, cascade_create=True))
        print(f"✓ User {user_id} ({name}) uploaded successfully")
    except APIException as e:
        print(f"✗ Error uploading user {user_id}: {e}")

print(f"\n{'='*60}")
print(f"All users uploaded successfully!")
print(f"Total users: {len(df)}")
print(f"{'='*60}")

