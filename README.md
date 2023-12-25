# Senitment analysis

# Check the existing processes running on the port:
lsof -i:8000

# kill any processes that are running on port 8000
kill {pid}

# Build the Dockerfile
docker build -f Dockerfile . -t sentiment_analysis_app

# Run Docker image
docker run -p 8000:8000 sentiment_analysis_app

# Example CURL commands to call the API
curl -H "Content-Type: application/json" -X POST http://localhost:8000/sentiment_analysis -d '{"text": "Who is the best brother?"}'
curl -H "Content-Type: application/json" -X POST http://localhost:8000/sentiment_analysis -d '{"text": "Who is the worst brother?"}' 
curl -H "Content-Type: application/json" -X POST http://localhost:8000/sentiment_analysis -d '{"text": "Who is the okayest sister?"}'

# Download ngrok, add the API key, and serve the localhost
ngrok http 8000
https://cf57-208-117-121-157.ngrok-free.app

# Example ngrok CURL command
curl -H "Content-Type: application/json" -X POST https://cf57-208-117-121-157.ngrok-free.app/sentiment_analysis -d '{"text": "Who is the best brother?"}'
