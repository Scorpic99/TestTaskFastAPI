from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(name: Optional[str] = 'noname', message: Optional[str] = None):
    return f'{name}, {message}'


if __name__ == "__main__":#http://127.0.0.1:8000/?name=Recruto&message=Давай%20дружить
    uvicorn.run(app, host='127.0.0.1', port=8000)
