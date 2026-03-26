from fastapi import FastAPI

app = FastAPI(title="GitHub DevOps Template API")


def add(a: int, b: int) -> int:
    return a + b


@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI",
        "project": "github-devops-template",
        "status": "ok"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": add(a, b)}
