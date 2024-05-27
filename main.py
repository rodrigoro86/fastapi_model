from fastapi import FastAPI, Request
from src.api.router import api_router
import sqlmodel


app = FastAPI(title='API QuantunApp')

app.include_router(api_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0", 
        port=8000
    )