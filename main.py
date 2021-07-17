from fastapi import FastAPI
app = FastAPI()

@app.post("/book")
def create_book():
    return {"key": "value"}
