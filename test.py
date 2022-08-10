token="N5b0MXU4EwlJFEHKv04e0rdZHpFGhK33B6z6nGQ2"
from groupy.client import Client
client = Client.from_token(token)
for group in client.groups.list_all():
    #print(group.name)
    g = 'Kensington Player Pool'
    if (group.name == g):
        for message in group.messages.list_all(): 
            print(message.text)
