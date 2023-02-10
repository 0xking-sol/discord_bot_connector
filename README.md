# discord_bot_connector

This Bot can be added to a Discord server and is capable of reading messages from other bots, even when they are in Embed format. 

Full documentation for embed class etc is here: https://discordpy.readthedocs.io/en/stable/api.html?highlight=embed#discord.Embed

Bot can be edited to choose responses, and is also capable of responding to private messages.


Currently building out compability with Binance API using the python-binance package. 

Example of Bot responding to an embedded message is below. 

<img width="600" alt="Screenshot 2023-02-10 at 12 31 01" src="https://user-images.githubusercontent.com/124360861/218093077-b1dc5650-fab2-4250-9656-de94f2152baf.png">



Decided to use ccxt as method. Will attempt to create my own wrapper for Binance API further down the line. API is set to read only regardless.
ccxt documentation is available here and easy to get up and running
https://docs.ccxt.com/en/latest/manual.html
