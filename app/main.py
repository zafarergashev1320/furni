import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from starlette.responses import HTMLResponse

from app.bot import bot, CHAT_ID

app = FastAPI()

# Templates va static papkalarni ulash
templates = Jinja2Templates(directory="app/templates")
UPLOAD_DIRECTION = "app/static/media"
os.makedirs(UPLOAD_DIRECTION, exist_ok=True)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# ---------- Pydantic model ----------
class Message(BaseModel):
    fname: str
    lname: str
    email: str
    message: str


# ---------- HTML ROUTERLAR ----------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/{page_name}", response_class=HTMLResponse)
async def pages(request: Request, page_name: str):
    # Masalan contact.html, about.html, shop.html
    return templates.TemplateResponse(page_name, {"request": request})


# ---------- Telegramga yuborish ----------
@app.post("/send_message")
async def send_message(data: Message):
    text = f"""
🔔 Yangi xabar!

👤 {data.fname} {data.lname}
📧 {data.email}

💬 {data.message}
"""
    await bot.send_message(CHAT_ID, text)
    return {"status": "ok"}
