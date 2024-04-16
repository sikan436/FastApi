from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. database import engine,get_db
from .. import models,schemas,oauth2
from .. import utils
from sqlalchemy.orm import Session
from typing import Optional,List

# from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
# from .. database import engine,get_db
# from sqlalchemy.orm import Session
# from .. import models,schemas,utils  

router=APIRouter(
    tags=["Authentication"])

@router.post("/login",response_model=schemas.Token)

def login(user_credentials: OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db) ):
    user=db.query(models.User).filter(models.User.email_id==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentail")
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentail")
    
    token=oauth2.create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "sample_token"}

    # usr=db.query(models.User).filter(models.User.email_id==userauth.email_id).first()
    # print (usr)
# "    if not usr:
#         raise HTTPException(status.HTTP_404_NOT_FOUND,detail="invalid userid or password")
    
#     #if not utils.verify(models.User.password,userauth.password):
#     if not utils.verify(userauth.password,usr.password):
#         raise HTTPException(status.HTTP_404_NOT_FOUND,detail="invalid userid or password")"
        
    
    
    
