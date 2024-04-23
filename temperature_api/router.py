from fastapi import APIRouter

router = APIRouter()


@router.get("/temperature/")
def read_temperature():
    return {"message": "Hello World temperature"}
