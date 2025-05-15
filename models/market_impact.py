import numpy as np

def almgren_chriss_impact(order_size, volatility, avg_daily_volume, sigma, eta):
    """
    Calculate expected market impact using Almgren-Chriss model.
    order_size: quantity to trade
    volatility: asset volatility
    avg_daily_volume: average daily traded volume
    sigma: volatility parameter
    eta: market impact parameter
    """
    permanent_impact = eta * (order_size / avg_daily_volume)
    temporary_impact = sigma * np.sqrt(order_size / avg_daily_volume)
    return permanent_impact + temporary_impact