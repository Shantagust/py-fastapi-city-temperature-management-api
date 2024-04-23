from fastapi import APIRouter

router = APIRouter()


@router.get("/cities/")
def index():
    return {"message": "Hello World"}
