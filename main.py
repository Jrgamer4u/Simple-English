import json
import random
import time
import os
import keep_alive

from requests_oauthlib import OAuth1Session

ndb = open('database/n.json')
vdb = open('database/v.json')
ddb = open('database/d.json')

ndb_dict = json.load(ndb)
vdb_dict = json.load(vdb)
ddb_dict = json.load(ddb)

consumer_key = os.environ['consumer_key']
client_secret = os.environ['client_secret']
resource_owner_key = os.environ['resource_owner_key']
resource_owner_secret = os.environ['resource_owner_secret']

keep_alive.keep_alive()

time.sleep(30)

while True:
    payload = {
        "text":
        ndb_dict[str(random.randrange(1, 601))] + " " +
        vdb_dict[str(random.randrange(1, 18))] + " " +
        ddb_dict[str(random.randrange(1, 18))] + " " +
        ndb_dict[str(random.randrange(1, 601))]
    }

    oauth = OAuth1Session(
        consumer_key,
        client_secret,
        resource_owner_key,
        resource_owner_secret,
    )

    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception("Request returned an error: {} {}".format(
            response.status_code, response.text))

    print("Response code: {}".format(response.status_code))

    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    time.sleep(30)
