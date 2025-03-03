# Define the currency exchange rates in a dictionary
currency_rates = {
    'PHP': 54.81472580697,
    'EUR': 0.85,
    'JPY': 110.25,
    'GBP': 0.75,
    # Add more currencies as needed
}

# Function to convert USD to a target currency
def convert_currency(amount, target_currency):
    if target_currency in currency_rates:
        exchange_rate = currency_rates[target_currency]
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return "Currency not found."

# Example usage
dollar_amount = float(input("How much dollar do you have? "))
target_currency = input("What currency you want to have? ").upper()

converted_amount = convert_currency(dollar_amount, target_currency)

if isinstance(converted_amount, str):
    print(converted_amount)
else:
    print(f"Dollar: {dollar_amount} USD")
    print(f"{target_currency}: {converted_amount}")
