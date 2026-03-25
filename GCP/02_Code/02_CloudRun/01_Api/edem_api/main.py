from fastapi import FastAPI, APIRouter
from edem_api.routers import router_events

base_path = "/api/v1"
router = APIRouter(prefix=f"{base_path}")

app = FastAPI(
    title="My FastAPI App",
    docs_url=f"{base_path}/docs",
    swagger_ui_parameters={"displayRequestDuration": True},
    version="1.0.0",
)

app.include_router(prefix=router.prefix, router=router_events.router)