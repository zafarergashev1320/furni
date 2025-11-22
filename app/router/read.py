from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from app.model import db, User

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
UPLOAD_DIRECTION = "app/media"


