# A bot-in-development to say hi to new users
# Needs: Mastodon.py
# App scopes: read:notifications write:statuses

from mastodon import Mastodon, StreamListener
from datetime import datetime
from time import sleep
import os, asyncio

if os.environ['MASTO_TOKEN'] == "setme":
  print("You have to set $MASTO_TOKEN to run this container")
  print("Run the container with:")
  print("docker run -e MASTO_TOKEN=YOUR_TOKEN_HERE mastobot:latest")
  exit()

instance = 'https://mastodon.nl'

masto = Mastodon(
  access_token = os.environ['MASTO_TOKEN'],
  api_base_url = instance
)

global text1
global text2

text1 = "Hoi @"
text2 = """, welkom op mastodon.nl

De beheerders en het supportteam zijn blij dat je er bent. Om je op weg te helpen vind je hier in het kort wat handige info.

1. Over deze server: https://mastodon.nl/about
2. Eerste hulp bij Mastodon: https://www.forceflow.be/2022/11/01/eerste-hulp-bij-mastodon/

Voor vragen kun je ook terecht bij het supportteam: @support@mastodon.nl

Happy tooting!

#welkomsttoot"""


class Listener(StreamListener):

  def on_notification(self, noti):
    if noti["type"] == "admin.sign_up":
      noti_id=str(noti['id'])
      user_id=str(noti['account']['id'])
      user_name=noti['account']['username']
      toot(noti_id, user_id, user_name)


def toot(noti_id, user_id, user_name):
  text = text1 + user_name + text2
  toot=masto.status_post(text, visibility="direct")
  toot_id=str(toot['id'])
  log = '{"time": "' + str(int(datetime.utcnow().timestamp() * 1000)) + '", "notification_id": ' + noti_id + '", "user_id": ' + user_id + '", "user_name": ' + user_name + '", "toot_id": ' + toot_id + '"}'
  print(log)

listener = Listener()

print('{"time": "' + str(int(datetime.utcnow().timestamp() * 1000)) + '", "startup": "True"}')
masto.stream_user(listener, run_async=True, reconnect_async=True, reconnect_async_wait_sec=2)

async def heartbeat():
  while True:
    print('{"time": "' + str(int(datetime.utcnow().timestamp() * 1000)) + '", "heartbeat": "True"}')
    sleep(3600)

asyncio.run(heartbeat())
