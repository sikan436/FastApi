from fastapi import FastAPI
from app import models
from app.database import engine
from .routers import post,user,auth ,vote
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)
app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def root():   
    return {"message": "hello world dy "}

files=[post,user,auth,vote]
for file in files:
    app.include_router(file.router)

app.include_router(auth.router)
    


# my_posts=[{"title":"title post 1","content":"content post 1","id":1},
#           {"title": "fav food","content":"halru fkfn ldh fh","id":2}
# ]

# def find_post(id):
#     for post in my_posts:
#         print ("inside find post")
#         if post["id"]== id:
#             return post    

# def find_post_index(id):
#     for i,post in  enumerate(my_posts):
#         if post["id"]==id:
#             return i
              
