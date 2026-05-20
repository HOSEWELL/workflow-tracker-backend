from django.utils import timezone

def submit_application(application):
    if application.status not in ["Draft", "Need More Information"]:
        raise ValueError("Application cannot be submitted")

    application.status = "Submitted"
    application.submitted_at = timezone.now()
    application.save()


def start_review(application):
    if application.status != "Submitted":
        raise ValueError("Only submitted applications can be reviewed")

    application.status = "Under Review"
    application.save()


def reviewer_decision(application, decision, comment):
    if application.status != "Under Review":
        raise ValueError("Application is not under review")

    if decision in ["Rejected", "Need More Information"] and not comment:
        raise ValueError("Comment required")

    application.status = decision
    application.reviewer_comment = comment
    application.reviewed_at = timezone.now()

    application.save()