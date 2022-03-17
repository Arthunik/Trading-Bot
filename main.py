import os
import discord
import requests
import json

#simple bot reply to specific msg
client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
def get_coinrank():
  url = "https://api.coinranking.com/v2/stats"
  api = os.environ['RAPID_API']
  querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl"}
  header = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': '"'+api+'"'
  }
  response = requests.request("GET", url, headers=header, params=querystring)
  json_data = json.loads(response.text)
  print(json_data['data']['totalMarkets'])
  message = "TotalCoin: "+str(json_data['data']['totalCoins']) + " TotalMarket: " + str(json_data['data']['totalMarkets'])
  return(message)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  #if msg from bot do nothing else reply
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send("HELLO!")
  if message.content.startswith('$quote'):
    await message.channel.send(get_quote())
  if message.content.startswith('$coin'):
    await message.channel.send(get_coinrank())


#run the bot
token = os.environ['TOKEN']
client.run(token)

