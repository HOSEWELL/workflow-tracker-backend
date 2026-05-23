from ninja import NinjaAPI
from applications.api import router as app_router

api = NinjaAPI(
    title="Workflow Tracker API",
    version="1.0.0",
    description="Workflow Tracker Backend APIs"
)

api.add_router("/applications/", app_router)