# Trade Opportunities API

A FastAPI service that analyzes market data and provides trade opportunity insights for specific sectors in India.

## Features
- **FastAPI**: Asynchronous web framework for high performance.
- **In-memory Rate Limiting**: Limit API requests per client IP to prevent abuse.
- **API Key Authentication**: Simple token-based security via headers.
- **Data Collection**: Integrated DuckDuckGo search to pull current market news.
- **AI Analysis**: Gemini API integration to structure and analyze the collected data into a markdown report.

## Requirements
- Python 3.9+
- Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

## Setup Instructions

1. **Clone/Navigate to the project directory**
   ```bash
   cd appscrip_task
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\\Scripts\\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory and copy the contents from `.env.example`:
   ```env
   API_KEY=my_secure_api_key_123
   GEMINI_API_KEY=your_gemini_api_key_here
   RATE_LIMIT_REQUESTS=5
   RATE_LIMIT_SECONDS=60
   ```
   *Replace `your_gemini_api_key_here` with your actual Gemini API Key.*

5. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

Once the server is running, the interactive API documentation will be available at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Endpoint: Analyze Sector

`GET /analyze/{sector}`

#### Headers
- `X-API-Key`: Your configured `API_KEY` (e.g., `my_secure_api_key_123`)

#### Example Request
```bash
curl -X 'GET' \\
  'http://127.0.0.1:8000/analyze/pharmaceuticals' \\
  -H 'accept: application/json' \\
  -H 'X-API-Key: my_secure_api_key_123'
```

#### Expected Response
The response will be a structured markdown string that you can easily save into a `.md` file.

```markdown
# Market Analysis Report: Pharmaceuticals Sector (India)

## 1. Executive Summary
...

## 2. Key Market Trends
...

## 3. Trade Opportunities
...

## 4. Risks & Challenges
...

## 5. Conclusion
...
```
