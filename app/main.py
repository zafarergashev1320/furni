import os
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import JSON
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from app.bot import setup_webhook, bot
from app.database import db

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
UPLOAD_DIRECTION = "app/static/media"
os.makedirs(UPLOAD_DIRECTION, exist_ok=True)
app.mount("/static", StaticFiles(directory='app/static'), name="static")
# app.include_router(read.router)
# app.include_router(create.router)
# app.include_router(update.router)
# app.include_router(delete.router)



@app.get("/register", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("register.html",
                                      {"request": request})


@app.get("/shop.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("shop.html",
                                      {"request": request})


@app.get("/cart.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("cart.html",
                                      {"request": request})


@app.get("/about.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("about.html",
                                      {"request": request})


@app.get("/services.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("services.html",
                                      {"request": request})


@app.get("/contact.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("contact.html",
                                      {"request": request})



@app.get("/checkout.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("checkout.html",
                                      {"request": request})



@app.get("/thankyou.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("thankyou.html",
                                      {"request": request})





@app.get("/blog.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("blog.html",
                                      {"request": request})


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request})

# aasd









@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    await db.feed_raw_update(bot, data)
    return JSONResponse({"ok": True})


# --- FastAPI ishga tushganda webhookni o‘rnatish ---
@app.on_event("startup")
async def on_startup():
    await setup_webhook()



