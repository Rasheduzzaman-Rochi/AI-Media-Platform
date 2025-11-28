from fastapi import APIRouter

router = APIRouter()

@router.get("/feature-1")
async def feature_one_test():
    return {"message": "Feature 1 is connected!"}