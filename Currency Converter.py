from forex_python.converter import CurrencyRates

def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()
    
    try:
        exchange_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except:
        return "Invalid currency code(s) or conversion not supported."

def main():
    print("Currency Converter")

    amount = float(input("Enter amount: "))
    from_currency = input("From Currency (3-letter code): ").upper()
    to_currency = input("To Currency (3-letter code): ").upper()

    result = currency_converter(amount, from_currency, to_currency)

    if isinstance(result, str):
        print(result)
    else:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
