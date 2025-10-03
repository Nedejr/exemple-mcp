from langchain_core.tools import tool

import yfinance as yf


@tool
def current_stock_price(ticker: str) -> float:
    """Retorna o preço atual de uma ação."""
    data = yf.Ticker(ticker)
    return data.fast_info.get("lastPrice")


@tool
def get_historical_stock_price(ticker: str, period: str = "1mo") -> dict:
    """Retorna dados históricos de uma ação.
    period: str: Período para o qual os dados históricos são necessários. Exemplo: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist.to_dict()


@tool
def get_company_info(ticker: str) -> dict:
    """Retorna informações da empresa."""
    data = yf.Ticker(ticker)
    return data.info
