import os
from mastodon import Mastodon

instance = 'https://mastodon.nl'

masto = Mastodon(
  access_token = os.environ['MASTO_TOKEN'],
  api_base_url = instance
)

followsme=[]
ifollow=[]

followers = masto.account_followers(masto.me()['id'])
allfollowers=masto.fetch_remaining(followers)
for i in allfollowers:
  followsme.append(i['id'])

following = masto.account_following(masto.me()['id'])
allfollowing=masto.fetch_remaining(following)
for i in allfollowing:
  ifollow.append(i['id'])

tofollow=[x for x in followsme if x not in ifollow]
for user in allfollowers:
  if user['statuses_count'] > 10 and "missing.png" not in user['avatar'] and user['id'] in tofollow:
    try:
      result=masto.account_follow(user['id'])
      print("Followed ", user['username'])
    except:
      print("Could not follow ", user['username'])
