import sys
import asyncio
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from websocket_client import OrderBookWebSocket
from models.slippage import SlippageModel
from models.market_impact import almgren_chriss_impact
from utils.fees import calculate_fee

class TradeSimulatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.slippage_model = SlippageModel()
        self.orderbook_data = None

    def init_ui(self):
        layout = QHBoxLayout()
        # Left panel: Inputs
        left_panel = QVBoxLayout()
        left_panel.addWidget(QLabel("Exchange:"))
        self.exchange_input = QComboBox()
        self.exchange_input.addItems(["OKX"])
        left_panel.addWidget(self.exchange_input)

        left_panel.addWidget(QLabel("Spot Asset:"))
        self.asset_input = QLineEdit("BTC-USDT-SWAP")
        left_panel.addWidget(self.asset_input)

        left_panel.addWidget(QLabel("Order Type:"))
        self.order_type_input = QComboBox()
        self.order_type_input.addItems(["market"])
        left_panel.addWidget(self.order_type_input)

        left_panel.addWidget(QLabel("Quantity (USD):"))
        self.quantity_input = QLineEdit("100")
        left_panel.addWidget(self.quantity_input)

        left_panel.addWidget(QLabel("Volatility:"))
        self.volatility_input = QLineEdit("0.01")
        left_panel.addWidget(self.volatility_input)

        left_panel.addWidget(QLabel("Fee Tier:"))
        self.fee_input = QLineEdit("0.001")
        left_panel.addWidget(self.fee_input)

        self.start_button = QPushButton("Start Simulation")
        self.start_button.clicked.connect(self.start_simulation)
        left_panel.addWidget(self.start_button)

        layout.addLayout(left_panel)

        # Right panel: Outputs
        right_panel = QVBoxLayout()
        self.slippage_label = QLabel("Expected Slippage: ")
        right_panel.addWidget(self.slippage_label)
        self.fee_label = QLabel("Expected Fees: ")
        right_panel.addWidget(self.fee_label)
        self.impact_label = QLabel("Expected Market Impact: ")
        right_panel.addWidget(self.impact_label)
        self.net_cost_label = QLabel("Net Cost: ")
        right_panel.addWidget(self.net_cost_label)
        self.maker_taker_label = QLabel("Maker/Taker Proportion: ")
        right_panel.addWidget(self.maker_taker_label)
        self.latency_label = QLabel("Internal Latency: ")
        right_panel.addWidget(self.latency_label)

        layout.addLayout(right_panel)
        self.setLayout(layout)
        self.setWindowTitle("GoQuant Trade Simulator")

    def start_simulation(self):
        url = "wss://ws.gomarket-cpp.goquant.io/ws/l2-orderbook/okx/BTC-USDT-SWAP"
        threading.Thread(target=lambda: asyncio.run(self.run_ws(url)), daemon=True).start()

    async def run_ws(self, url):
        async def on_tick(data, latency):
            self.orderbook_data = data
            # Dummy values for demonstration
            slippage = 0.1
            fee = calculate_fee(float(self.quantity_input.text()), float(data['bids'][0][0]), float(self.fee_input.text()))
            impact = almgren_chriss_impact(float(self.quantity_input.text()), float(self.volatility_input.text()), 1000000, 0.01, 0.01)
            net_cost = slippage + fee + impact
            maker_taker = 0.5
            self.slippage_label.setText(f"Expected Slippage: {slippage:.4f}")
            self.fee_label.setText(f"Expected Fees: {fee:.4f}")
            self.impact_label.setText(f"Expected Market Impact: {impact:.4f}")
            self.net_cost_label.setText(f"Net Cost: {net_cost:.4f}")
            self.maker_taker_label.setText(f"Maker/Taker Proportion: {maker_taker:.2f}")
            self.latency_label.setText(f"Internal Latency: {latency*1000:.2f} ms")
        await OrderBookWebSocket(url, self.asset_input.text(), on_tick).connect()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TradeSimulatorUI()
    window.show()
    sys.exit(app.exec_())