# 🚀 Crypto Trading Bot - Binance Futures Testnet

A sophisticated Python-based cryptocurrency trading bot with both CLI and web interfaces, designed for Binance Futures Testnet trading. Built with modern web technologies and professional-grade architecture.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.46.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🎯 Core Features
- **Dual Interface**: Both CLI and modern web interface (Streamlit)
- **Multiple Order Types**: Market, Limit, and Stop-Market orders
- **Binance Integration**: Official python-binance library integration
- **Testnet Safe**: Uses Binance Futures Testnet for risk-free testing
- **Real-time Trading**: Execute trades instantly with live market data
- **Comprehensive Logging**: All trades and errors logged with timestamps

### 🛡️ Security & Risk Management
- **Environment Variables**: Secure API credential management
- **Testnet Only**: No real money at risk during development/testing
- **Input Validation**: Robust parameter validation and error handling
- **Exception Handling**: Graceful error management and recovery

### 🎨 User Experience
- **Intuitive Web UI**: Clean, responsive Streamlit interface
- **Real-time Feedback**: Instant order confirmation and status updates
- **JSON Response Display**: Complete order details visualization
- **Multi-platform Support**: Works on Windows, macOS, and Linux

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.8+ |
| **Streamlit** | Web interface framework | 1.46.0 |
| **python-binance** | Binance API integration | 1.0.29 |
| **python-dotenv** | Environment variable management | 1.1.0 |
| **Binance Futures API** | Trading execution | REST API |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Binance Futures Testnet account
- API credentials (Key & Secret)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/crypto-trading-bot.git
cd crypto-trading-bot
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Environment Setup
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your credentials
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_secret_key_here
```

## ⚙️ Configuration

### Getting Binance Testnet Credentials

1. **Visit Binance Testnet**: https://testnet.binancefuture.com/
2. **Create Account**: Register for a testnet account
3. **Generate API Keys**: 
   - Go to API Management
   - Create new API key
   - Enable Futures Trading
   - Save your API Key and Secret

### Environment Variables
Create a `.env` file in the project root:

```env
# Binance Futures Testnet API Credentials
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```

## 🚀 Usage

### Web Interface (Recommended)
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

### Command Line Interface
```bash
python main.py
```

### Example Trading Sessions

#### Market Order Example
```
Symbol: BTCUSDT
Order Side: BUY
Order Type: MARKET
Quantity: 0.001
```

#### Limit Order Example
```
Symbol: ETHUSDT
Order Side: SELL
Order Type: LIMIT
Quantity: 0.01
Limit Price: 3000
```

#### Stop Market Order Example
```
Symbol: BTCUSDT
Order Side: SELL
Order Type: STOP_MARKET
Quantity: 0.001
Stop Price: 25000
```

## 📊 API Documentation

### BasicBot Class

```python
class BasicBot:
    def __init__(self):
        """Initialize bot with Binance Testnet configuration"""
        pass
    
    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Place trading order on Binance Futures Testnet
        
        Args:
            symbol (str): Trading pair (e.g., 'BTCUSDT')
            side (str): 'BUY' or 'SELL'
            order_type (str): 'MARKET', 'LIMIT', or 'STOP_MARKET'
            quantity (float): Order quantity
            price (str, optional): Limit price for LIMIT orders
            stop_price (str, optional): Stop price for STOP_MARKET orders
            
        Returns:
            dict: Order response from Binance API
        """
        pass
```

### Supported Order Types

| Order Type | Description | Required Parameters |
|------------|-------------|-------------------|
| **MARKET** | Execute immediately at current market price | symbol, side, quantity |
| **LIMIT** | Execute only when price reaches specified level | symbol, side, quantity, price |
| **STOP_MARKET** | Trigger market order when stop price is reached | symbol, side, quantity, stop_price |

## 📸 Screenshots

### Web Interface
![Trading Interface](screenshots/web-interface.png)
*Modern Streamlit web interface with real-time trading capabilities*

### Order Execution
![Order Success](screenshots/order-success.png)
*Successful order placement with JSON response display*

### CLI Interface
![CLI Interface](screenshots/cli-interface.png)
*Command-line interface for programmatic trading*

## 📁 Project Structure

```
crypto_trading_bot_with_streamlit/
├── 📄 app.py                 # Streamlit web interface
├── 📄 main.py                # Core trading logic & CLI
├── 📄 requirements.txt       # Python dependencies
├── 📄 .env.example          # Environment template
├── 📄 .env                  # API credentials (private)
├── 📄 README.md             # Project documentation
├── 📄 .gitignore            # Git ignore file
├── 📁 screenshots/          # UI screenshots
└── 📄 trading_bot.log       # Trade execution logs
```

## 🔧 Advanced Configuration

### Custom API Endpoints
```python
# Modify in main.py for different environments
self.client.API_URL = "https://testnet.binancefuture.com/fapi"  # Testnet
# self.client.API_URL = "https://fapi.binance.com"  # Mainnet (DANGER!)
```

### Logging Configuration
```python
# Customize logging in main.py
logging.basicConfig(
    filename='trading_bot.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## 🧪 Testing

### Test Cases
Run these test scenarios to verify functionality:

1. **Connection Test**: Verify API connectivity
2. **Market Order Test**: Place small market order
3. **Limit Order Test**: Place limit order with realistic price
4. **Error Handling Test**: Test with invalid parameters
5. **UI Responsiveness**: Test web interface interactions

### Sample Test Commands
```bash
# Test market order
python -c "from main import BasicBot; bot = BasicBot(); print(bot.place_order('BTCUSDT', 'BUY', 'MARKET', 0.001))"
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

### Development Guidelines
- Follow PEP 8 Python style guide
- Add comprehensive comments
- Include error handling
- Test on Testnet only
- Update documentation

## 📈 Roadmap

### Upcoming Features
- [ ] OCO (One-Cancels-Other) orders
- [ ] TWAP (Time-Weighted Average Price) strategy
- [ ] Grid trading algorithm
- [ ] Portfolio management dashboard
- [ ] WebSocket real-time data
- [ ] Docker containerization
- [ ] Unit test coverage
- [ ] CI/CD pipeline

## ⚠️ Disclaimers

- **For Educational Use**: This bot is designed for learning and testing
- **Testnet Only**: Always use testnet for development and testing
- **No Financial Advice**: This software doesn't provide investment advice
- **Use at Own Risk**: Trading cryptocurrencies involves risk of loss

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/crypto-trading-bot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/crypto-trading-bot/discussions)
- **Email**: your.email@example.com

## 🙏 Acknowledgments

- [Binance API Documentation](https://binance-docs.github.io/apidocs/futures/en/)
- [python-binance Library](https://python-binance.readthedocs.io/)
- [Streamlit Framework](https://streamlit.io/)
- [Python Community](https://www.python.org/community/)

---

⭐ **Star this repository if it helped you!**

Made with ❤️ for the crypto trading community
