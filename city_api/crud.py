from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from . import models, schemas


async def get_all_cities(db: AsyncSession):
    query = select(models.City)
    cities = await db.execute(query)
    return [city[0] for city in cities.fetchall()]


async def get_city_by_id(db: AsyncSession, city_id: int):
    query = select(models.City).where(models.City.id == city_id)
    result = await db.execute(query)
    city = result.first()
    if city:
        return city[0]
    return {"message": "city with this id not found !"}


async def create_city(db: AsyncSession, city: schemas.CityIn):
    query = insert(models.City).values(city.dict())
    result = await db.execute(query)
    await db.commit()
    resp = {**city.model_dump(), "id": result.lastrowid}
    return resp


async def delete_city_by_id(db: AsyncSession, city_id: int):
    query = select(models.City).where(models.City.id == city_id)
    result = await db.execute(query)
    city = result.scalar()

    if city is not None:
        await db.delete(city)
        await db.commit()
        return {"message": "city deleted"}
    return {"message": "city not found"}
