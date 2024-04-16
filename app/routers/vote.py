from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. database import engine,get_db
from .. import models,schemas,oauth2
from .. import utils
from sqlalchemy.orm import Session
from typing import Optional,List
from app import schemas,database,models,oauth2

router=APIRouter(tags=["Vote"],prefix="/vote")

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote,db:Session=Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    print("########")
    print("post" ,post)
    print("#######")


    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {vote.post_id} not found")
 
    check_vote=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
    found_vote=check_vote.first()
    print (f"models.Vote.post_id {models.Vote.post_id}")
    if  vote.dir==1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"user {current_user.id} already voted on {vote.post_id}")
        else:
            result=models.Vote(post_id=vote.post_id,user_id=current_user.id)
            db.add(result)
            db.commit()
            db.refresh(result)
            return {"message":"voted successfully"}
    else:
        if found_vote:
            check_vote.delete(synchronize_session=False)
            db.commit()
            return {"message":"vote deleted "}
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"user {current_user.id} has not voted yet")


    


            
        
        
