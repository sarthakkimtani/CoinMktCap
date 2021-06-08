import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


class APIError(Exception):
    def __init__(self, r):
        super().__init__(repr(r))
        self.res = r


class CoinMarketCap:

    def __init__(self, api_key=None):
        self.__base_api_url = "https://pro-api.coinmarketcap.com/v1/"
        self.__sandbox_api_url = "https://sandbox-api.coinmarketcap.com/v1/"
        self.__sandbox_key = "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c"
        self.__session = Session()

        self.api_key = api_key if api_key is not None else self.__sandbox_key
        self.__headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }

    def __get_api_url(self):
        url = self.__sandbox_api_url if self.api_key == self.__sandbox_key else self.__base_api_url
        return url

    def __request(self, endpoint, **kwargs):
        url = f"{self.__get_api_url()}{endpoint}"
        self.__session.headers.update(self.__headers)
        try:
            res = self.__session.get(url, params=kwargs, timeout=30)
            data = json.loads(res.text)
            if res.status_code != 200:
                raise APIError(data["status"]["error_message"])
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as err_msg:
            print(err_msg)

    def close(self):
        self.__session.close()

    def cryptocurrency_map(self, **kwargs):
        # Returns a mapping of all cryptocurrencies
        return self.__request("cryptocurrency/map", **kwargs)

    def cryptocurrency_info(self, **kwargs):
        # Returns all static metadata available for one or more cryptocurrencies
        return self.__request("cryptocurrency/info", **kwargs)

    def cryptocurrency_latest_listings(self, **kwargs):
        # Returns a paginated list of all active cryptocurrencies with latest market data
        return self.__request("cryptocurrency/listings/latest", **kwargs)

    def cryptocurrency_historical_listings(self, **kwargs):
        # Returns a ranked and sorted list of all cryptocurrencies for a historical UTC date
        return self.__request("cryptocurrency/listings/historical", **kwargs)

    def cryptocurrency_latest_quotes(self, **kwargs):
        # Returns the latest market quote for 1 or more cryptocurrencies
        return self.__request("cryptocurrency/quotes/latest", **kwargs)

    def cryptocurrency_historical_quotes(self, **kwargs):
        # Returns an interval of historic market quotes for any cryptocurrency
        return self.__request("cryptocurrency/quotes/historical", **kwargs)

    def cryptocurrency_market_pairs(self, **kwargs):
        # Lists all active market pairs that CoinMarketCap tracks for a given cryptocurrency
        return self.__request("cryptocurrency/market-pairs/latest", **kwargs)

    def cryptocurrency_latest_ohlcv(self, **kwargs):
        # Returns the latest OHLCV (Open, High, Low, Close, Volume)
        return self.__request("cryptocurrency/ohlcv/latest", **kwargs)

    def cryptocurrency_historical_ohlcv(self, **kwargs):
        # Returns historical OHLCV (Open, High, Low, Close, Volume)
        return self.__request("cryptocurrency/ohlcv/historical", **kwargs)

    def exchange_map(self, **kwargs):
        # Returns a paginated list of all active cryptocurrency exchanges
        return self.__request("exchange/map", **kwargs)

    def exchange_info(self, **kwargs):
        # Returns all static metadata for one or more exchanges
        return self.__request("exchange/info", **kwargs)

    def exchange_latest_listings(self, **kwargs):
        # Returns a paginated list of all cryptocurrency exchanges including the latest aggregate market data
        return self.__request("exchange/listings/latest", **kwargs)

    def exchange_historical_listings(self, **kwargs):
        # Returns an interval of historic market quotes for any exchange
        return self.__request("exchange/listings/historical", **kwargs)

    def exchange_latest_quotes(self, **kwargs):
        # Returns the latest aggregate market data for 1 or more exchanges
        return self.__request("exchange/quotes/latest", **kwargs)

    def exchange_historical_quotes(self, **kwargs):
        # Returns an interval of historic quotes for any exchange based on time and interval parameters
        return self.__request("exchange/quotes/historical", **kwargs)

    def exchange_market_pairs(self, **kwargs):
        # Returns all active market pairs that CoinMarketCap tracks for a given exchange
        return self.__request("exchange/market-pairs/latest", **kwargs)

    def global_metrics_latest(self, **kwargs):
        # Returns the latest global cryptocurrency market metrics
        return self.__request("global-metrics/quotes/latest", **kwargs)

    def global_metrics_historical(self, **kwargs):
        # Returns an interval of historical global cryptocurrency market metrics
        return self.__request("global-metrics/quotes/historical", **kwargs)

    def price_conversion_tool(self, **kwargs):
        # Convert an amount of one cryptocurrency or fiat currency into one or more different currencies
        return self.__request("tools/price-conversion", **kwargs)

    def blockchain_latest(self, **kwargs):
        # Returns the latest blockchain statistics data for 1 or more blockchains
        return self.__request("blockchain/statistics/latest", **kwargs)

    def fiat_map(self, **kwargs):
        # Returns a mapping of all supported fiat currencies
        return self.__request("fiat/map", **kwargs)

    def key_info(self, **kwargs):
        # Returns API key details and usage stats
        return self.__request("key/info", **kwargs)
