from fastapi import FastAPI

app = FastAPI()
def fname():
    pass
def qwe():
    pass
@app.get("/")
async def root():
    return {"message": "Hello World"}

