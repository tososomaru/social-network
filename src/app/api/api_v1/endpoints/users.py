from fastapi import Depends, APIRouter

from src.app.schemas.user import UserDB
from src.app.services.users import fastapi_users, jwt_authentication, current_active_user

router = APIRouter()

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)

router.include_router(
    fastapi_users.get_register_router(), prefix="/auth", tags=["auth"]
)

router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(fastapi_users.get_users_router(), prefix="/users", tags=["users"])


@router.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
