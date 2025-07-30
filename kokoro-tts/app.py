from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/speak")
async def speak(request: Request):
    data = await request.json()
    text = data.get("text", "Hello world")
    return {"message": f"Synthesized voice for: {text}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
