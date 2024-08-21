from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.database import engine, Base
from app.routers import data_router, user_router
from app.models import user_models, data_models

app = FastAPI(
    title="Data Management Platform (DMP) API",
    description="This API allows you to collect, organize, and activate data for advertising campaigns.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "url": "http://yourwebsite.com",
        "email": "your.email@domain.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the routers
app.include_router(data_router.router)
app.include_router(user_router.router)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
