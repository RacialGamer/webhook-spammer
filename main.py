from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep

print(""" _____                                           
/  ___|                                          
\ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
 `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
/\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
\____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
      | |                                        
      |_|                                        
""")
print("Made by https://github.com/racialgamer")
msg = input("Webhook Embed Message: ")
URL = input("Webhook URL: ")
amount = input("How many times to send: ")
seconds = input("How many seconds delay between messages: ")

amount = int(amount)
seconds = int(seconds)

webhook = DiscordWebhook(url=URL, avatar_url="https://avatars.githubusercontent.com/u/121128992?v=4", username="Webhook Spammer by RacialGamer", content="@everyone", rate_limit_retry=True)

embed = DiscordEmbed(title='Spammed',description=msg, color='880808')
embed.set_author(name='RacialGamer Spammer Bot (Link)', url='https://github.com/racialgamer', icon_url='https://avatars.githubusercontent.com/u/121128992?v=4')

webhook.add_embed(embed)

for i in range(amount):
 sleep(seconds)
 webhook.execute()