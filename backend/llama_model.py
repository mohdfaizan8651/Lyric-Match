from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq  
import random 
from dotenv import load_dotenv
import os

load_dotenv()

songs = [
    ("Bohemian Rhapsody", "Queen"),
    ("Shape of You", "Ed Sheeran"),
    ("Blinding Lights", "The Weeknd"),
    ("Rolling in the Deep", "Adele"),
    ("Someone Like You", "Adele"),
    ("Smells Like Teen Spirit", "Nirvana"),
    ("Lose Yourself", "Eminem"),
    ("Billie Jean", "Michael Jackson"),
    ("Hello", "Adele"),
    ("Uptown Funk", "Mark Ronson ft. Bruno Mars"),
    ("Thinking Out Loud", "Ed Sheeran"),
    ("Shallow", "Lady Gaga & Bradley Cooper"),
    ("Take Me to Church", "Hozier"),
    ("Yesterday", "The Beatles"),
    ("Can't Stop the Feeling!", "Justin Timberlake"),
    ("Radioactive", "Imagine Dragons"),
    ("Let Her Go", "Passenger"),
    ("Stay With Me", "Sam Smith"),
    ("Perfect", "Ed Sheeran"),
    ("Hallelujah", "Leonard Cohen")
]

chat=None

def initialize():
    global chat
    # groq_api_key = os.getenv("GROQ_API_KEY")
    groq_api_key ="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"

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is missing from environment variables.")
    
    chat = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama-3.3-70b-Versatile")
    print("Chat model initialized successfully!")


initialize()

def get_lyrics():
    """Generates lyrics using the initialized Groq model."""
    if chat is None:
        return {"error": "Model is still initializing, please wait."}

    system_template = "You are a lyric generation AI designed to create short, recognizable lyric snippets based on a given song title and artist. Your goal is to generate a 2-4 line excerpt that captures the essence of the song while avoiding explicit mention of the song title. Ensure the lyrics are evocative, engaging, and resemble the original style of the song. Do not reveal the song title in your response."
    
    human = "Generate a 2-4 line lyric snippet for the song {title} more related to the title by {singer}"
    
    prompt = ChatPromptTemplate.from_messages([("human", human)])
    response = prompt | chat
    title_sin = random.choice(songs)
    title = title_sin[0]
    singer = title_sin[1]

    output = response.invoke({"title": title, "singer": singer})
    result = {
        "output":output.content,
        "title":title
    }

    return result
