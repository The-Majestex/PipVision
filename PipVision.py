print("PipVision starting.........")
import yfinance as yf
# I am getting EURUSD Forex pair 
data = yf.download("EURUSD=X", period="1d", interval="15m")
print("EUR/USD 15m data:")
print(data.tail()) 

