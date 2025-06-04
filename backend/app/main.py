from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def say_hello():
    return {"msg": "Hello from FastAPI!"}


from app.database import Base, engine
from app.models import user  # make sure this imports your User model

Base.metadata.create_all(bind=engine)