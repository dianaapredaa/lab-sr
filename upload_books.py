import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import (
    ListItems, DeleteItem, Batch, 
    AddItemProperty, DeleteItemProperty, SetItemValues
)
from recombee_api_client.exceptions import APIException

# --- CONFIG ---
DB_ID = 'exxmple-top-100-books'
TOKEN = 'Lc2xgXTGrgmPkvdHcHwd1xhfRdBSujuIkhCzRCStW2BHBWjRWGnrSKsjBSY92h4x'

client = RecombeeClient(DB_ID, TOKEN, region=Region.EU_WEST)

df = pd.read_csv('books.csv', encoding='utf-8-sig')

for _, row in df.iterrows():
    item_id = str(row['number']).zfill(4)
    values = {
        'author_name': str(row['author_name']),
        'book_title': str(row['book_title']),
        'pages': int(row['pages']),
        'publishing_year': int(row['publishing_year'])
    }

    try:
        client.send(SetItemValues(item_id, values, cascade_create=True))
    except APIException as e:
        print(f"Error uploading item {item_id}: {e}")

print("All books uploaded successfully.")
