import plotly
import yfinance as yf
import plotly.express as px

def plot_ts(ticker:str
) -> plotly.graph_objs._figure.Figure:
    """
    Plots the time series of the closing prices for a given stock ticker.

    This function retrieves historical stock data for a given ticker symbol (assumed
    to be listed on the B3 exchange in Brazil) using the `yfinance` library. It then
    processes the data by rounding the 'Open', 'High', 'Low', and 'Close' prices to 
    two decimal places and drops the 'Adj Close' and 'Volume' columns. Finally, it 
    creates an interactive line plot of the 'Close' prices over time using Plotly.

    Args:
        ticker (str): The stock ticker symbol (e.g., 'PETR4' for Petrobras).

    Returns:
        plotly.graph_objs._figure.Figure: A Plotly figure object representing the 
        closing prices over time.

    Example:
        fig = plot_ts('PETR4')
        fig.show()
    """


    ticker_sa = ticker + '.SA'
    data = yf.download(ticker_sa) \
        .reset_index() \
        .assign(
            Open = lambda x: round(x['Open'], 2),
            High = lambda x: round(x['High'], 2),
            Low = lambda x: round(x['Low'], 2),
            Close = lambda x: round(x['Close'], 2)
        ) \
        .drop(['Adj Close',	'Volume'], axis = 1)

    fig = px.line(data,
        x = 'Date', y = 'Close',
        title = f'Preço de fechamento de {ticker} '
    )

    return fig