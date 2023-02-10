import discord
import random
import responses
import CEXs


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# do we want to send in channel or as private message


def run_discord_bot():
    TOKEN = 'MTA3Mjg5NTQwMTE2Mzc3MTk3Ng.GZ7fyG.aduVf2J1YVIwn9OXotfzp7uPjx1C2A6fOt3t3g'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if len(message.embeds) == 1:
            embed = message.embeds[0]
            embed.title = embed.title.lower()
            embed.description = embed.description.lower()
            if "twap" in embed.title:
                if "buying" in embed.description:
                    #if currency in embed.title:
                    await message.channel.send('twap buy activated, opening a long on ' + currency)
                if "selling" in embed.description:
                    #if currency in embed.title:
                    await message.channel.send('twap sell activated, opening a short on ' + currency)

            if "market sell" in embed.title:
                if currency in embed.title:
                    await message.channel.send('market sold, opening a long on ' + currency)

            if "market buy" in embed.title:
                if currency in embed.title:
                    await message.channel.send('market bought, opening a short on ' + currency)

            if "test notification" in embed.title:
                await message.channel.send('test doubly approved')

            # this won't work until i split the dictionary into a string - maybe it will work now?
            #for currency in currencies:
            #currency = str(currency)
             #   if currency in embed.title:
              #      await message.channel.send('relevant currency is ' + currency)

        if user_message[0] not in range:
            return
        else:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
