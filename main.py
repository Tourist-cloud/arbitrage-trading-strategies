#!/usr/bin/env python3
from strategies.triangular_arbitrage import triangular_arbitrage

if __name__ == "__main__":
    rates = {
        'usd_to_eur': 0.85,
        'eur_to_gbp': 0.9,
        'gbp_to_usd': 1.5
    }

    triangular_arbitrage(rates)


