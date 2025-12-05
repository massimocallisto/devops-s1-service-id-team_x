from fastapi import FastAPI
import random


from status_report import get_status

app = FastAPI()

import json



@app.get("/status")
async def fetch_status():
    return get_status()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)