# API Key Authentication (planned)

This file will contain instructions or implementation notes for adding a simple API key mechanism to protect the /predict endpoint.

Goals:
- Use FastAPI dependency injection
- Accept `X-API-Key` header
- Compare with known key stored in environment variable
