from fastapi import FastAPI

app = FastAPI(title="AWS CI/CD Demo")


@app.get("/")
def home():
    return {"message": "Hello from FastAPI CI/CD!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
