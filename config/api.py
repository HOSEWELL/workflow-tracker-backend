from ninja import NinjaAPI
from applications.api import router as app_router

api = NinjaAPI()

api.add_router("/applications/", app_router)