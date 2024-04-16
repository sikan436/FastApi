import inspect
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from sqlalchemy import func
from .. database import engine,get_db
from .. import models,schemas,oauth2
from .. import utils
from sqlalchemy.orm import Session
from typing import Optional,List
import _json

router=APIRouter(
    prefix="/posts",tags=["Posts"])
# @router.get("/")
# def posts(db: Session = Depends(get_db),current_user: int= Depends(oauth2.get_current_user),limit :int =10
#           ,skip:int=0,search: Optional[str]=""):
#     # cursor.execute("select * from posts")
#     # posts=cursor.fetchall()
#     #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
#     results=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Post.id,
#     isouter=True).group_by(models.Post.id).all()
    
#     return {"results": results}

#     #return results
  
@router.get("/",response_model=List[schemas.PostOut] )
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
    #     models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id)

    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()

    # posts = db.execute(
    #     'select posts.*, COUNT(votes.post_id) as votes from posts LEFT JOIN votes ON posts.id=votes.post_id  group by posts.id')
    # results = []
    # for post in posts:
    #     results.append(dict(post))
    # print(results)
    # posts = db.query(models.Post).filter(
    #     models.Post.title.contains(search)).limit(limit).offset(skip).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).limit(limit).offset(skip).all()
    # posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts = list ( map (lambda x : x._mapping, posts) )
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    # print (post)
    # cursor.execute("""insert into posts(title,content,published) values(%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    # result=cursor.fetchone()
    # conn.commit()
    print(current_user.id)

    result=models.Post(**post.model_dump(),owner_id=current_user.id)
    
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id: int,response: Response,db: Session = Depends(get_db) ,current_user: int= Depends(oauth2.get_current_user)):
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    #result=db.query(models.Post).filter(models.Post.id==id).first()
    
    print 
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
    return posts
    
    


##this was used with driver only
    # cursor.execute("""select * from posts where id=%s""",[int(id)] )
    # result=cursor.fetchone()
    # if not result:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
    # return {"info": result}
    
    ##below was used earlier when we were storing data in list
    # post=find_post(int(id))

    # return {"post": post }

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def del_post(id: int,db: Session = Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found") 
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"not legal")
    post_query.delete(synchronize_session=False)
    db.commit()   
   
    return Response(status_code=status.HTTP_204_NO_CONTENT)



    # cursor.execute("""delete from posts where id=%s RETURNING *""",[int(id)])
    # result=cursor.fetchone()
    # conn.commit()
    # if not result:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
    # return {f"post with {id} deleted successfully"}  

##below was dependency on list
    # index=find_post_index(int(id))
 
    # my_posts.pop(index)


@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int , updated_post: schemas.PostCreate, db: Session = Depends(get_db),current_user: int= Depends(oauth2.get_current_user) ):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found") 
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"not legal")
    post_query.update(updated_post.model_dump(),synchronize_session=False)
    db.commit()   
    return post
    
