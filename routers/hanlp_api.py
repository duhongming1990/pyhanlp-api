from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.post("/ascii/convert/mdf", name='标定ASCII转换MDF')
async def ascii_convert_mdf():
    return Response()
