from ninja import Router
from django.shortcuts import get_object_or_404

from .models import Application
from .schemas import *
from .services import *

router = Router()

@router.get("/", response=list[ApplicationOut])
def list_applications(request):
    return Application.objects.all()

@router.get("/{app_id}", response=ApplicationOut)
def application_detail(request, app_id: int):
    return get_object_or_404(Application, id=app_id)

@router.post("/", response=ApplicationOut)
def create_application(request, payload: ApplicationIn):
    app = Application.objects.create(**payload.dict())
    return app

@router.put("/{app_id}", response=ApplicationOut)
def update_application(request, app_id: int, payload: ApplicationIn):
    app = get_object_or_404(Application, id=app_id)

    if app.status not in ["Draft", "Need More Information"]:
        return {"error": "Cannot edit"}

    for attr, value in payload.dict().items():
        setattr(app, attr, value)

    app.save()
    return app

@router.post("/{app_id}/submit")
def submit(request, app_id: int):
    app = get_object_or_404(Application, id=app_id)

    try:
        submit_application(app)
        return {"success": True}
    except ValueError as e:
        return {"error": str(e)}

@router.post("/{app_id}/start-review")
def review(request, app_id: int):
    app = get_object_or_404(Application, id=app_id)

    try:
        start_review(app)
        return {"success": True}
    except ValueError as e:
        return {"error": str(e)}

@router.post("/{app_id}/decision")
def decision(request, app_id: int, payload: ReviewerDecisionSchema):
    app = get_object_or_404(Application, id=app_id)

    try:
        reviewer_decision(
            app,
            payload.decision,
            payload.reviewer_comment
        )

        return {"success": True}

    except ValueError as e:
        return {"error": str(e)}