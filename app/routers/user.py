from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from .. database import engine,get_db
from .. import models,schemas
from .. import utils
from sqlalchemy.orm import Session

# router=APIRouter(prefix="/user",tags=["User"])
router=APIRouter(tags=["User"])
@router.post("/user/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
async def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):
    print("inside create")
    h_pass=utils.hash(user.password)
    user.password=h_pass
    result=models.User(**user.model_dump())
    print(result)
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id: int,db: Session = Depends(get_db)):
    usr=db.query(models.User).filter(models.User.id==id).first()
    if not usr:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    return usr




    

    # cursor.execute("""update posts set title=%s ,content=%s,published=%s where id=%s RETURNING *""",(post.title,post.content,post.published,id))
    # result=cursor.fetchone()
    # conn.commit()
    # if not result:
    #      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} not found")
    # return {"data":result}
