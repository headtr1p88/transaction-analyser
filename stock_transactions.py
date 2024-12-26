import locale

locale.setlocale(locale.LC_ALL, 'en_US')

def analyse_transactions(filename, stockname):
    
    total_value = 0
    total_shares = 0
    avg_purchase = 0
    purchase_history = ''

    with open(filename) as file:
        next(file)

        for line in file:
            date, stock, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)

            if stock == stockname:
                total_value += amount * price
                total_shares += amount
                purchase_history += f'You purchased {amount} {stock} shares at a price of {locale.currency(price)}\n'
    
    avg_purchase = total_value / total_shares
    return f'{purchase_history}You purchased {total_shares} {stockname} shares at an average price of {locale.currency(avg_purchase)} valued at {locale.currency(total_value, grouping = True)}' 

result = analyse_transactions('stock_transactions.txt', 'NVDA')
print(result)