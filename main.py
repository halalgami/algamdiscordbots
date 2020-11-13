from bs4 import BeautifulSoup
import os
import random
import discord
import keepmealive
import feedparser
import webbrowser
import json

from dotenv import load_dotenv

funnyordie = feedparser.parse("https://www.funnyordie.com/rss/index.xml")
ninegag = feedparser.parse("http://9gagrss.com/feed/")
memebase = feedparser.parse("https://memebase.cheezburger.com/rss")
redditmeme = feedparser.parse("https://www.reddit.com/r/memes/.rss?format=xml")
ranimes = feedparser.parse("https://www.reddit.com/r/animemes/.rss?format=xml")
theonion = feedparser.parse("http://www.theonion.com/feeds/rss")
warhammmerfortyk = feedparser.parse("http://rss.moddb.com/groups/warhammer-40k-fans-group/images/feed/rss.xml")
redditfortyk = feedparser.parse("https://www.reddit.com/r/Warhammer40kmemes/.rss?format=xml")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

keepmealive.keep_alive()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    #print("received:{}".format(message))    
    #print("received:{}".format(message.author.name))
    #print(" mentions:{}".format(message.mentions))
    #print(" client user:{}".format(client.user))
    #print("----------------------------") 
  
    # if message.author.name == 'ShogunX':
    #     print("got a message from :{}".format(message.author))
    #     response = 'Hello there! I KNOW YOU!!!!'
    #     await message.channel.send(response)
    
    if client.user in message.mentions:
        #print("got a message from :{}".format(message.author))
        
        if 'for the emperor!' in message.content or 'emperor grant me memes' in message.content or '40k' in message.content:
            random_item = random.choice(redditfortyk.entries)
            
            jsondata = random_item.content
            htmlcontent = jsondata[0]['value']            

            soup = BeautifulSoup(htmlcontent)
            thememecontainer = soup.find('span')
            thememe = thememecontainer.find('a')
            formatted_item = "Title: {} {}".format(random_item.title,thememe['href'])
            response = formatted_item
            await message.channel.send(response)

        elif '40k art' in message.content:
            listofentries = warhammmerfortyk.entries
            random_item = random.choice(listofentries)
            #formatted_item = "Title: {} {}".format(random_item.title,random_item.media_thumbnail)
            #formatted_item = "Title: {} {}".format(random_item.link,random_item.media_content[0]['url'])
            formatted_item = "{}".format(random_item.link)
            response = formatted_item
            await message.channel.send(response)
        elif 'memebase' in message.content:
            listofentries = memebase.entries
            random_item = random.choice(listofentries)
            formatted_item = "Title: {} {}".format(random_item.title,random_item.media_thumbnail[0]['url'])
            response = formatted_item
            await message.channel.send(response)
        
        elif 'reddit' in message.content:            
            random_item = random.choice(redditmeme.entries)
            
            jsondata = random_item.content
            htmlcontent = jsondata[0]['value']            

            soup = BeautifulSoup(htmlcontent)
            thememecontainer = soup.find('span')
            thememe = thememecontainer.find('a')
            formatted_item = "Title: {} {}".format(random_item.title,thememe['href'])
            response = formatted_item
            await message.channel.send(response)
        
        elif 'animemes' in message.content:            
            random_item = random.choice(ranimes.entries)
            #print("the item:{}".format(random_item))

            #print("the contents{}:".format(random_item.content))

            jsondata = random_item.content

            #print("the json contents{}:".format(jsondata))
            #print("actual content: {}".format(jsondata[0]['value']))
            htmlcontent = jsondata[0]['value']            

            soup = BeautifulSoup(htmlcontent)
            thememecontainer = soup.find('span')
            thememe = thememecontainer.find('a')
            formatted_item = "Title: {} {}".format(random_item.title,thememe['href'])
            response = formatted_item
            await message.channel.send(response)            
        
        elif 'onion' in message.content:            
            random_item = random.choice(theonion.entries)
            soup = BeautifulSoup(random_item.description)
            tehimage=soup.find('img')
            #formatted_item = "Title: {} {} <br/>{}".format(random_item.title,tehimage['src'],random_item.link)
            formatted_item = "Title: {} {}".format(random_item.title,random_item.link)
            response = formatted_item
            await message.channel.send(response)
        
        elif '9gag' in message.content:            
            random_item = random.choice(ninegag.entries)


            soup = BeautifulSoup(random_item.description)
            #print('description {}'.format(soup))

            if random_item.category == 'video':
              tehvid=soup.find('source')
              formatted_item = "Title: {} {}".format(random_item.title,tehvid['src'])
            elif random_item.category == 'static':
              tehimage=soup.find('img')
              #print('description {}'.format(soup))
              #print('the pic {}'.format(tehimage.src))
              formatted_item = "Title: {} {}".format(random_item.title,tehimage['src']) 
            else:           
              formatted_item = "Title: {} {}".format(random_item.title,random_item.description) 
            
            response = formatted_item
            await message.channel.send(response)
        
        elif 'funny or die' in message.content:            
            random_item = random.choice(funnyordie.entries)
            soup = BeautifulSoup(random_item.description)
            tehimage=soup.find('img')
            formatted_item = "Title: {} {}".format(random_item.title,tehimage['src'])
            response = formatted_item
            await message.channel.send(response)
        elif 'help':
            response = "For fresh memes type one of the following: 40k,40k art, memebase,reddit,animemes,onion,9gag,funny or die"
            await message.channel.send(response)
        else:
            response = "Hail to you {}! I live for memes!".format(message.author.name)
            await message.channel.send(response)


    if message.author == client.user:
        return

    

    
client.run(TOKEN)