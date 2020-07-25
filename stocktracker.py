import stockquotes
kroger = stockquotes.Stock('SLB')
krogerPrice = kroger.current_price
print (krogerPrice)

bitcoin = stockquotes.Stock('BTC-USD')
bitcoinPrice = bitcoin.current_price
print (bitcoinPrice)