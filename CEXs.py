import os
import ccxt

# we are using CCXT library for this 

# import BINANCE READ ONLY API
read_binance_key = '<your key here>'
read_binance_secret = '<your secret here>'

# binance testnet documentation: https://www.binance.com/en/support/faq/how-to-test-my-functions-on-binance-testnet-ab78f9a1b8824cf0a106b4229c76496d
# need to use github and then use new API endpoint, maybe better to use CCXT guide on testnet

# from variable id
exchange_id = 'binance'
binance = ccxt.binance()
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': read_binance_key,
    'secret': read_binance_secret,
})

binance.load_markets()
currencies = binance.currencies
symbols = binance.symbols

# this loads all the symbols on binance into a dictionary (e.g {ETH, BTC, SOL... etc})


currency_list = []
for currency in currencies:
    currency_list.append(currency)
    
# this converts currency dictionary into a list of currencies so that you can iterate through them

# for digit in currency_list:
    # if digit.isalpha():

# Get account information


# import coinbase key and secret
cb_key = os.environ.get('COINBASE_KEY')
cb_secret = os.environ.get('COINBASE_SECRET')
