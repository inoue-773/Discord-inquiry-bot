
# Discord Inquiry Bot


Automatically stores all the messages that have been sent to a specific Discord text channel and replies, indicating whether the message has already been sent to the same channel or not.

This bot is particularly useful when you need to log something that shouldn't be recorded multiple times. In my case, I use it for my business, as some of my products are limited to one per person. However, it's challenging to keep track of who has purchased the item among staff members. In such cases, this could be a game-changer, as all they need to do is send names, and this bot will take care of the rest.
## Requirements

- Discord bot (obviously)
Just go to https://discord.com/developers/applications and create one. Make sure not to upload your bot token on the internet. 

- A server
You can use your computer or you can rent one as well. I personally use https://railway.app/ to run this bot 24/7. (not affiliated)

- MongoDB Database
This bot uses MongoDB to store all the message. I personally use https://railway.app/ for this as well since I can manage and connect them easily. (not affiliated)

## Before you use

This bot uses message.content method provided in Discord.py, but to use it, you have to enable message content intent in Discord developer portal otherwise message.content becomes empty and your database will end up empty too.

### Enable message content intent

Simply head over to Discord developer portal and select your bot. Open "Bot" tab and scroll down to privileged gateway intent. You will see the section there.


##  Variables

To run this bot, you will need to manually change the values of 
`your-mongodb-link`, `your-discord-channel-id` and `your-discord-token`. Because I am lazy I have not created .env file so feel free to do so if you need. It will give this bot a little bit more flexibilities. Currently everything is hardcoded so if you need to change something you need to manually change the code itself.

- MongoDB link

This will need to access and store the data to MongoDB database. Make sure to give this bot a permission to both read and write.
The format is something like this:
```bash
  mongodb://USER_NAME:PASSWORD@MONGODB_SERVER_URL:PORT
  mongodb://testuser:imnotstupidenoughtosharepassword@exampleserver.com:0000
```

- Discord Channel ID
Just enable developer option of Discord and right click the channel that you want this bot to run.
```bash
11666357564388798538
```

- Discord Bot Token
Copy and paste it from Discord developer portal into the code.


## License

You can do whatever you want with this.

## Authors

- Me (5%)

- ChatGPT (95%)

I was basically useless.

