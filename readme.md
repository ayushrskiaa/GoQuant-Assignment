# GoQuant Trade Simulator

## Overview

This is my implementation of the GoQuant Trade Simulator. It's a Python app that connects to real-time crypto orderbook data (OKX, via WebSocket), simulates market orders, and estimates transaction costs and market impact. The UI is built with PyQt5, so you can input parameters and see outputs update live.

---

## Features

- Real-time L2 orderbook data from OKX (WebSocket)
- User interface for:
  - Exchange selection
  - Asset selection
  - Order type
  - Quantity (USD)
  - Volatility
  - Fee tier
- Outputs (update every tick):
  - Expected Slippage (regression model)
  - Expected Fees (rule-based)
  - Expected Market Impact (Almgren-Chriss model)
  - Net Cost (sum of above)
  - Maker/Taker Proportion (logistic regression)
  - Internal Latency (processing time per tick)
- Handles WebSocket disconnects and reconnects automatically
- Modular code for slippage, market impact, and maker/taker models

---

## Project Structure

```
GoQuant Assignment/
│
├── main.py                  # PyQt5 GUI and simulation logic
├── websocket_client.py      # Async WebSocket client with reconnect logic
├── models/
│   ├── slippage.py          # Linear regression for slippage estimation
│   ├── market_impact.py     # Almgren-Chriss market impact model
│   └── maker_taker.py       # Logistic regression for maker/taker prediction
├── utils/
│   ├── fees.py              # Fee calculation utility
│   └── latency.py           # Latency measurement decorator
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. (Optional) Activate VPN  
   OKX may require a VPN for access.

3. Run the app:
   ```sh
   python main.py
   ```

---

## Usage

- Fill in the left panel with your parameters (exchange, asset, order type, quantity, volatility, fee tier).
- Click "Start Simulation" to connect to the WebSocket and start the simulation.
- The right panel will show slippage, fees, market impact, net cost, maker/taker proportion, and latency, updating live.

---

## Models and Algorithms

- **Slippage:** Linear regression (`models/slippage.py`). For best results, train with historical data.
- **Market Impact:** Almgren-Chriss model (`models/market_impact.py`).
- **Fees:** Simple rule: `quantity * price * fee_rate` (`utils/fees.py`).
- **Maker/Taker Proportion:** Logistic regression (`models/maker_taker.py`).
- **Latency:** Measured per tick using `time.perf_counter()`.

---

## Error Handling & Reconnection

If the WebSocket connection drops (e.g., ping timeout, network issues), the client logs the error and tries to reconnect after a short delay.

---

## Performance Notes

- Uses async WebSocket for fast data processing.
- Async code runs in a thread so it doesn't block the PyQt5 UI.
- Minimal UI updates for low latency.

---

## Customization & Extension

- Add new models: put them in `models/` and import in `main.py`.
- Change endpoints: edit the WebSocket URL in `main.py`.
- Tune reconnection: adjust `reconnect_delay` in `websocket_client.py`.

---

## Troubleshooting

- **WebSocket errors:** Make sure your VPN is on and your network allows access to OKX.
- **No data:** Check the endpoint status and your internet connection.
- **Model errors:** Make sure all dependencies are installed and models are trained.

---

## License

This project is for educational and assessment purposes.

---
