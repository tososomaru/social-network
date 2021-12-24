from fastapi import APIRouter
from .users import router as users_router
from .base import router as base_router


router = APIRouter()
router.include_router(base_router)

router_v1 = APIRouter(prefix='/v1')
router_v1.include_router(users_router)


router.include_router(router_v1)

