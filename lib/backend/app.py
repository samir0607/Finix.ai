from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from chatbot import chatbot

app = FastAPI()

class Message(BaseModel):
  message: str

@app.post("/")
async def send_message(message: Message):
	response_text = chatbot(message.message)
	return {"response": response_text}

if __name__ == "__main__":
	uvicorn.run(app, host='192.168.1.1', port=8000)
