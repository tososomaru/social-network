from fastapi import APIRouter
from .auth import router as auth_router
from .posts import router as users_router
from .base import router as base_router


router = APIRouter()
router.include_router(base_router)
router.include_router(auth_router)

router.include_router(users_router)

