from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from . import models
# from .database import engine
from .routers import user, post, auth, vote

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
# origins = ["https://www.google.com/"]
# Here we can set which domain are allowed to send request to our API server.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}

# my_posts = [{"title": "Title 1", "content": "Content of 1", "id": 1},
#             {"title": "Title 2", "content": "Content of 2", "id": 2}]

# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post
