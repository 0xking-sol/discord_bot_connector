import discord
import random
import responses
from CEXs import currency_list


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

        if len(message.embeds) == 1:
            embed = message.embeds[0]
            embed.title = embed.title.lower()
            embed.description = embed.description.lower()
            message_currency = embed.title.split(" on ")[-1].split("\n")[0]
            message_currency = message_currency.upper()
            print(f'{username} said: "{embed.title}" ({channel})')

            if message_currency in currency_list:
                index = currency_list.index(message_currency)
            else:
                index = 0
                currency_list[index] = '- coin not on binance'

            if "twap" in embed.title:
                if "buying" in embed.description:
                    await message.channel.send('twap buy activated, opening a long on ' + currency_list[index])
                if "selling" in embed.description:
                    await message.channel.send('twap sell activated, opening a short on ' + currency_list[index])

            if "market sell" in embed.title:
                await message.channel.send('market sold, opening a long on ' + currency_list[index])

            if "market buy" in embed.title:
                await message.channel.send('market bought, opening a short on ' + currency_list[index])

            if "test notification" in embed.title:
                await message.channel.send('test doubly approved')

            if len(user_message) > 0 and user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=True)
            else:
                await send_message(message, user_message, is_private=False)

        else:
            print(f'{username} said: "{user_message}" ({channel})')

    client.run(TOKEN)
