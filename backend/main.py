from fastapi import FastAPI, HTTPException
import random
import llama_model
from llama_model  import songs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "FastAPI deployed successfully!"}

@app.get("/")
async  def home():
    return {"list": songs}

@app.get("/lyrics")
async  def get_lyrics():
  
    if llama_model.chat is None:
        raise HTTPException(status_code=503, detail="Model is still initializing, please wait.")
    return llama_model.get_lyrics()

@app.get("/guees_title/")
async def get_title(user_title: str, correct_title: str):
    if user_title == correct_title :
        for i in songs:
            if i[0].lower() == correct_title.lower():
                return {"message": "You guessed the correct song title!"}
    return {"message": "You guessed the wrong song title."}
