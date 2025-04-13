from fastapi import FastAPI
from app.database import engine
from app.models import Base 
from app.routers import health, auth, file_upload, report, config, scheduler, metrics

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(file_upload.router)
app.include_router(report.router)
app.include_router(config.router)
app.include_router(scheduler.router)
app.include_router(metrics.router)
