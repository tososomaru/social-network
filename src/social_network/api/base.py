from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get('/')
def redirect_docs():
    return RedirectResponse('/docs')
