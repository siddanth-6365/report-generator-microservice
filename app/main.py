from fastapi import FastAPI
from app.routers import health, auth, file_upload, report, config, scheduler, metrics 
import app.logging_config
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(file_upload.router)
app.include_router(report.router)
app.include_router(config.router)
app.include_router(scheduler.router)
app.include_router(metrics.router)
