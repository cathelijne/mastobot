# mastobot
A tiny bot for my own use, to greet new users on mastodon.nl

You can run bot.py as is, or build the docker container. It's been running for a couple of weeks now, and though the output sometimes seems to crash, the bot keeps sending out the welcome messages.

To run, set MASTO_TOKEN in your environment, and change the "instance", "text1" and "text2" variables in the script (the user handle gets inserted between text1 and text2).

Also included are auth.py, which just authenticates with the mastodon server (I use it as a start script for interactive pyhton sessions) and followback.py, that I use to do some follower management. You don't need those for the bot, I just like to have those in my toolkit.
