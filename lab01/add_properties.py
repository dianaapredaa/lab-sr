from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import AddItemProperty, Batch

DB_ID = 'exxmple-top-100-books'
TOKEN = 'Lc2xgXTGrgmPkvdHcHwd1xhfRdBSujuIkhCzRCStW2BHBWjRWGnrSKsjBSY92h4x'

client = RecombeeClient(DB_ID, TOKEN, region=Region.EU_WEST)

properties = {
    'author_name': 'string',
    'book_title': 'string',
    'pages': 'int',
    'publishing_year': 'int'
}

requests = [AddItemProperty(name, typ) for name, typ in properties.items()]

response = client.send(Batch(requests))
print("Proprietăți adăugate cu succes:")
