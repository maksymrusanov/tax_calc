from fastapi import FastAPI

app = FastAPI()
def fname():
    pass

@app.get("/")
async def root():
    return {"message": "Hello World"}

