import uvicorn

from src.config.config_db import IP_HOST, PORT_HOST


if __name__ == "__main__":
    uvicorn.run(
        "src.api:app",
        host=IP_HOST,
        port=PORT_HOST,
        reload=True
    )