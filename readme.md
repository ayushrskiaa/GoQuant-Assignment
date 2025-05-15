# GoQuant Trade Simulator

## Overview

The GoQuant Trade Simulator is a high-performance Python application that connects to real-time cryptocurrency orderbook data via WebSocket, simulates market orders, and estimates transaction costs and market impact. It features a PyQt5-based GUI for user input and real-time output display.

---

## Features

- **Real-time L2 orderbook ingestion** from OKX via WebSocket.
- **User interface** for parameter input (exchange, asset, order type, quantity, volatility, fee tier).
- **Output metrics:**  
  - Expected Slippage (regression model)
  - Expected Fees (rule-based)
  - Expected Market Impact (Almgren-Chriss model)
  - Net Cost (sum of above)
  - Maker/Taker Proportion (logistic regression)
  - Internal Latency (processing time per tick)
- **Robust error handling** and automatic WebSocket reconnection.
- **Extensible model architecture** for slippage, market impact, and maker/taker prediction.

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

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **(Optional) Activate VPN:**  
   Some exchanges (like OKX) may require a VPN for access.

3. **Run the application:**
   ```sh
   python main.py
   ```

---

## Usage

- **Input Parameters:**  
  Select exchange, asset, order type, quantity (USD), volatility, and fee tier in the left panel.
- **Start Simulation:**  
  Click "Start Simulation" to connect to the WebSocket and begin real-time simulation.
- **View Outputs:**  
  The right panel displays slippage, fees, market impact, net cost, maker/taker proportion, and latency, updated with each orderbook tick.

---

## Models and Algorithms

- **Slippage:**  
  Uses a linear regression model (`models/slippage.py`). Train with historical data for best results.
- **Market Impact:**  
  Implements the Almgren-Chriss model (`models/market_impact.py`) for estimating temporary and permanent price impact.
- **Fees:**  
  Calculated as `quantity * price * fee_rate` (`utils/fees.py`).
- **Maker/Taker Proportion:**  
  Logistic regression model (`models/maker_taker.py`).
- **Latency:**  
  Measured per tick using Python's `time.perf_counter()`.

---

## Error Handling & Reconnection

- The WebSocket client (`websocket_client.py`) automatically logs errors and attempts to reconnect after a delay if the connection drops (e.g., due to ping timeout or network issues).

---

## Performance Notes

- **Async WebSocket** ensures data is processed faster than it is received.
- **Threading** is used to run async code alongside the PyQt5 event loop.
- **Efficient data structures** and minimal UI updates for low latency.

---

## Customization & Extension

- **Add new models:**  
  Place new model files in the `models/` directory and import them in `main.py`.
- **Change endpoints:**  
  Update the WebSocket URL in `main.py` as needed.
- **Tune reconnection:**  
  Adjust `reconnect_delay` in `websocket_client.py`.

---

## Troubleshooting

- **WebSocket errors:**  
  Ensure your VPN is active and your network allows access to the exchange endpoint.
- **No data:**  
  Check endpoint status and your internet connection.
- **Model errors:**  
  Ensure all dependencies are installed and models are properly trained.

---

## License

This project is for educational and assessment purposes.

---

## Contact

For questions or submissions, email:  
- careers@goquant.io  
- CC: himanshu.vairagade@goquant.io

---