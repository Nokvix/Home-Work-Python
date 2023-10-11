def process_data():
    print("1. Ключи: {data_keys}\n"
          "Значения: {data_values}".format(data_keys=data.keys(), data_values=data.values()))
    data["ETH"]["total_diff"] = 100
    print("2. {0}".format(data["ETH"]))
    data["tokens"][0]["fst_token_info"]["name"] = "doge"
    print("3. {0}".format(data["tokens"][0]["fst_token_info"]["name"]))
    total_out = 0
    for i_token in data["tokens"]:
        total_out += i_token.pop("total_out")
    data["ETH"]["total_out"] = total_out
    print("4. Удалены total_out {0}\n"
          "Присвоена сумма значений total_out {1}".format(data["tokens"], data["ETH"]))
    for i_token in data["tokens"]:
        if "sec_token_info" in i_token:
            token_price = i_token["sec_token_info"].pop("price")
            i_token["sec_token_info"]["total_price"] = token_price
    print("5. {0}".format([i_token for i_token in data["tokens"] if "sec_token_info" in i_token]))


data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
process_data()
