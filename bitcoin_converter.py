# bitcoin_converter.py
# This program converts Bitcoin to US Dollars (USD)
#
# Carina Sylvester
#

print("As of 01/14/2021 at 13:33hrs, bitcoin is currently trading at $39,384.85 per bitcoin. ")

def bitcoin_to_dollar():
    bitcoinAmount = float(input("Enter the bitcoin amount: "))
    dollarAmount = bitcoinAmount * 39384.85
    print("That is worth $" + str(dollarAmount))

bitcoin_to_dollar()