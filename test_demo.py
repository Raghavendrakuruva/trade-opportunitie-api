import sys
import os
sys.path.append(os.getcwd())
from app.services.search import fetch_market_data
from app.services.analyzer import analyze_sector_data

def demonstrate_api():
    sector = "pharmaceuticals"
    print(f"1. User requested analysis for: {sector}")
    
    print(f"2. Fetching real-time market data from DuckDuckGo...")
    data = fetch_market_data(sector)
    
    print(f"3. Validating Gemini API Key and sending data to model...")
    report = analyze_sector_data(sector, data)
    
    print(f"\n======== GENERATED MARKDOWN REPORT ========\n")
    print(report)

if __name__ == "__main__":
    demonstrate_api()
