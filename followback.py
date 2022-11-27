import os
from mastodon import Mastodon

mode = "addtolist"
# mode = "unfollow"
instance = 'https://mastodon.nl'

masto = Mastodon(
  access_token = os.environ['MASTO_TOKEN'],
  api_base_url = instance
)

donotunfollowListID = 1048
doesnotfollowmeListID = 1097

followsme=[]
ifollow=[]
donotunfollow = []
doesnotfollowme = []

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
      # print("Followed ", user['username'])
    except:
      # print("Could not follow ", user['username'])
      pass

for i in masto.list_accounts(donotunfollowListID):
  donotunfollow.append(i['id'])

for i in masto.list_accounts(doesnotfollowmeListID):
  masto.list_accounts_delete(doesnotfollowmeListID, i['id'])

tounfollow=[x for x in ifollow if x not in followsme]
for user in allfollowing:
  if user['id'] not in donotunfollow and user['id'] in tounfollow:
    try:
      if mode == "addtolist":
        masto.list_accounts_add(doesnotfollowmeListID, user['id'])
        # print("User ", user['username'], " added to list")
      elif mode == "unfollow":
        masto.account_unfollow(user['id'])
        # print("Unfollowed user ", user['username'], ".")
    except:
      # print("User ", user['username'], " could not be processed")
      pass
