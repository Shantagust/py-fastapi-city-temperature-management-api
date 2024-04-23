from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from city_api import crud, schemas
from dependencies import get_db

router = APIRouter()


@router.get("/cities/", response_model=list[schemas.CityBase])
async def read_all_cities(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_cities(db=db)


@router.post("/cities/", response_model=schemas.CityIn)
async def add_city(
        city: schemas.CityIn,
        db: AsyncSession = Depends(get_db)
):
    return await crud.create_city(db=db, city=city)


@router.get("/cities/{city_id}")
async def read_city(city_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_city_by_id(db=db, city_id=city_id)


@router.delete("/cities/{city_id}")
async def delete_city(city_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.delete_city_by_id(db=db, city_id=city_id)
