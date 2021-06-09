# CoinMarketCap API

[![License](https://img.shields.io/github/license/sarthakkimtani/CoinMktCap)](https://github.com/sarthakkimtani/CoinMktCap/blob/main/LICENSE)

Unofficial Python wrapper around the CoinMarketCap API

 - Read the [official Documentation](https://coinmarketcap.com/api/documentation/v1/)
 
## Installation

PyPI

Use the following command to install:

 - `pip install CoinMktCap`

Source Code

 - ```bash
    git clone https://github.com/sarthakkimtani/CoinMktCap.git
    cd CoinMktCap
    python setup.py install
    ```
 
## Example

```python
  from CoinMktCap import CoinMarketCap
  
  market = CoinMarketCap("API_KEY")
  eth = market.cryptocurrency_info(symbol="ETH")
  
  something(eth.data)
  ```
 
 ## Methods
 
 Pass the required parameters for each endpoint. Refer the [docs](https://coinmarketcap.com/api/documentation/v1/)
 
| Method | Definition | Endpoint |
|-|-|-|
| [cryptocurrency_map](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap) | Map of all currencies | /cryptocurrency/map |
| [cryptocurrency_info](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyInfo) | Info of specified currency | /cryptocurrency/info/ |
| [cryptocurrency_latest_listings](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest) | Active cryptocurrencies with latest market data | /cryptocurrency/listings/latest |
| [cryptocurrency_historical_listings](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsHistorical) | Cryptocurrencies for a historical UTC date | /cryptocurrency/listings/historical |
| [cryptocurrency_latest_quotes](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesLatest) | Latest market quote for 1 or more cryptocurrencies | /cryptocurrency/quotes/latest |
| [cryptocurrency_historical_quotes](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyQuotesHistorical) | Historic market quotes for any cryptocurrency | /cryptocurrency/quotes/historical |
| [cryptocurrency_market_pairs](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMarketpairsLatest) | Active market pairs for given cryptocurrency | /cryptocurrrency/market-pairs/latest |
| [cryptocurrency_latest_ohlcv](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvLatest) | Latest OHLCV (Open, High, Low, Close, Volume) | /cryptocurrency/ohlcv/latest |
| [cryptocurrency_historical_ohlcv](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyOhlcvHistorical) | Historical OHLCV (Open, High, Low, Close, Volume) | /cryptocurrency/ohlcv/historical |
| [exchange_map](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMap) | List of all active cryptocurrency exchanges | /exchange/map |
| [exchange_info](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeInfo) | Static metadata for one or more exchanges | /exchange/info |
| [exchange_latest_listings](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsLatest) | List of all cryptocurrency exchanges | /exchange/listings/latest |
| [exchange_historical_listings](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeListingsHistorical) | Historic market quotes for any exchange | /exchange/listings/historical |
| [exchange_latest_quotes](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesLatest) | Latest aggregate market data for 1 or more exchanges | /exchange/quotes/latest |
| [exchange_historical_quotes](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeQuotesHistorical) | Historic quotes for any exchange | /exchange/quotes/historical |
| [exchange_market_pairs](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ExchangeMarketpairsLatest) | Market pairs for a given exchange | /exchange/market-pairs/latest |
| [global_metrics_latest](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesLatest) | Latest global cryptocurrency market metrics | /global-metrics/quotes/latest |
| [global_metrics_historical](https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical) | Historical global cryptocurrency market metrics | global-metrics/quotes/historical |
| [price_conversion_tool](https://coinmarketcap.com/api/documentation/v1/#operation/getV1ToolsPriceconversion) | Convert an amount of one cryptocurrency or fiat currency | tools/price-conversion |
| [blockchain_latest](https://coinmarketcap.com/api/documentation/v1/#operation/getV1BlockchainStatisticsLatest) | Latest blockchain statistics | blockchain/statistics/latest |
| [fiat_map](https://coinmarketcap.com/api/documentation/v1/#operation/getV1FiatMap) | Mapping of all supported fiat currencies | fiat/map |
| [key_info](https://coinmarketcap.com/api/documentation/v1/#operation/getV1KeyInfo) | API key details | key/info |


## Properties

- `data` (__dict__): will give you the result.
- `status` (__dict__): the status object always included for both successful calls and failures.
- `timesamp` (__str__): current time on the server when the call was executed.
- `error_code` (__str | None__): In case of an error has been raised, this property will give you the status error code.
- `error_message` (__str | None__): In case of an error has been raised, this property will give details about error.

## License
[MIT License](https://github.com/sarthakkimtani/CoinMktCap/blob/main/LICENSE)
