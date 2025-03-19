def triangular_arbitrage(exchange_rates):
    usd_to_eur = exchange_rates['usd_to_eur']
    eur_to_gbp = exchange_rates['eur_to_gbp']
    gbp_to_usd = exchange_rates['gbp_to_usd']

    initial_amount = 1  # Start with 1 USD
    result = initial_amount * usd_to_eur * eur_to_gbp * gbp_to_usd

    if result > initial_amount:
        print(f"Arbitrage Opportunity: ${initial_amount} → ${result:.2f}")
    else:
        print("No arbitrage opportunity.")

