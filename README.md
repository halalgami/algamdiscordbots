Just a small collection of discord bots i made for my own benefit.

Special thanks to:
https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-discord-connection

for the inspiration and guidance.

main.py currently contains the meme bot, which fetches the freshest memes from the following RSS feeds:

    https://www.funnyordie.com/rss/index.xml
    http://9gagrss.com/feed/
    https://memebase.cheezburger.com/rss
    https://www.reddit.com/r/memes/.rss?format=xml
    https://www.reddit.com/r/animemes/.rss?format=xml
    http://www.theonion.com/feeds/rss
    http://rss.moddb.com/groups/warhammer-40k-fans-group/images/feed/rss.xml
    https://www.reddit.com/r/Warhammer40kmemes/.rss?format=xml


You can start by running

`pip install -U discord.py`

Create a file name `.env` in the same directory as main.py and don't forget to install

`pip install -U python-dotenv`

to store the discord bot token in the following format:

`DISCORD_TOKEN=YOUR_TOKEN_HERE`
