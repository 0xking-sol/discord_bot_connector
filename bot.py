import discord
import random
import responses
import ccxt
from CEXs import currency_list, symbols, binance
import time


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if response:
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
            message_description = embed.description.lower()
            message_currency_pair = ''
            print(f'{username} said: "{embed.title}" ({channel})')

            # use the symbol trading pair (FLOW/BUSD) that is in the embed
            # and take this, and use it to search through symbols
            # it can then easily be used to get the price with ticker method
            for word in message_description.split():
                if '/' in word:
                    message_currency_pair = word.strip()
                    message_currency_pair = message_currency_pair.upper()
                    print(message_currency_pair)
                    break

            def price(message_currency_pair):
                currency_price = 'unknown, pair not on Binance'
                if message_currency_pair is not None and message_currency_pair in symbols:
                    ticker = binance.fetch_ticker(message_currency_pair)
                    print(ticker)
                    currency_price = str(ticker['last'])
                return currency_price

            if "twap" in embed.title:
                if "buying" in embed.description:
                    await message.channel.send('twap buy activated, opening a long on ' + message_currency_pair + ". Current Price is " + price(message_currency_pair))
                    time.sleep(10)
                    await message.channel.send('price is now ' + price(message_currency_pair))
                if "selling" in embed.description:
                    await message.channel.send('twap sell activated, opening a short on ' + message_currency_pair + ". Current Price is " + price(message_currency_pair))
                    time.sleep(10)
                    await message.channel.send(
                        'price is now ' + price(message_currency_pair))

            if "market sell" in embed.title:
                await message.channel.send('market sold, opening a long on ' + message_currency_pair + ". Current Price is " + price(message_currency_pair))
                time.sleep(10)
                await message.channel.send('price is now ' + price(message_currency_pair))

            if "market buy" in embed.title:
                await message.channel.send('market bought, opening a short on ' + message_currency_pair + ". Current Price is " + price(message_currency_pair))
                time.sleep(10)
                await message.channel.send('price is now ' + price(message_currency_pair))

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
