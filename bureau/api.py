# import frappe
# from openexchangerates import OpenExchangeRates

# def get_exchange_rates():
#     # Replace the API key with your own
#     client = OpenExchangeRates(api_key="6ffc9af5cce64aa58db12ebd12a645cf")

#     # Get the latest currency exchange rates
#     currency_list = client.latest()

#     # Loop through each currency in the Currency doctype
#     for currency in frappe.get_all("Currency", fields=["currency_name"]):
#         # Get the exchange rate for the currency
#         rate = currency_list.rates.get(currency.currency_name)
        
#         # Update the exchange rate field for the currency
#         frappe.db.set_value("exchange_rate", rate)

#     # Commit the changes
#     frappe.db.commit()

