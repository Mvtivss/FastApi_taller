import fastapi as FastAPI
from routes import router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

origins = ["*"]

app = FastAPI.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")

def read_root():
    return {"Mi primera Api de cero ;)"}

app.include_router(router)