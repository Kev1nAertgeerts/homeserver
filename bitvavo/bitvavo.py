from python_bitvavo_api.bitvavo import Bitvavo
from cryptography.fernet import Fernet

class MyBitvavo:
    def __init__(self, model_keys):
        self._login(model_keys)

    def _login(self, model_keys):
        total_key = ""
        total_secret = ""
        for i in model_keys:
            bitv = Encryption()
            key_part = bitv.decrypt(i.key, i.crypto_gr_key).decode()
            secret_part = bitv.decrypt(i.sec, i.crypto_gr_key).decode()
            total_key = total_key+key_part
            total_secret = total_secret+secret_part
        self.engine = Bitvavo({
            'APIKEY': total_key,
            'APISECRET': total_secret
        })

    def get_portefeuille(self):
        all_balance = self.engine.balance({})
        selected_balance = []
        for i in all_balance:
            if i["available"] != "0" or i["inOrder"] != "0" or i["symbol"] == "EUR":
                selected_balance.append(i)
        return selected_balance

    def buy_crypto(self):
        pass

    def sell_crypto(self):
        pass

    def get_prices(self, price_list):
        all_prices = self.engine.tickerPrice({})
        selected_prices = []
        for i in all_prices:
            if i["market"] in price_list:
                selected_prices.append(i)
        return selected_prices


class Encryption:
    def __init__(self):
        pass

    def _generate_key(self):
        return Fernet.generate_key()
    
    def encrypt(self, data, key):
        return Fernet(key).encrypt(data)
    
    def decrypt(self, data, key):
        return Fernet(key).decrypt(data)