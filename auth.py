import os
from mastodon import Mastodon

instance = 'https://mastodon.nl'

masto = Mastodon(
  access_token = os.environ['MASTO_TOKEN'],
  api_base_url = instance
)
