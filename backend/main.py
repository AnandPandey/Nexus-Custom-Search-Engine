from fastapi import FastAPI

app = FastAPI(
    title="Nexus Search Engine",
    description="A custom search engine built from scratch",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Nexus Search Engine"
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "Nexus API"
    }