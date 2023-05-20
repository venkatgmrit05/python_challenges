
def isin(market_identifiers: list, x: str):

    isin_result: bool = False
    for mi in market_identifiers:
        # print(mi, x , mi in str(x).lower())
        if mi in str(x).lower():
            isin_result = True
            return (isin_result)
    return isin_result


def get_market(x, market_mapping_dict):
    identified_market = None
    try:
        for market, market_identifiers in market_mapping_dict.items():
            if isin(market_identifiers, x):
                identified_market = market
                break

        return identified_market
    except Exception as e:
        print(f'err: {e}')
        return 0


def convert_currency(
        currency: float,
        from_to: tuple,
        exchange_map: dict):
    return exchange_map[from_to]*currency
