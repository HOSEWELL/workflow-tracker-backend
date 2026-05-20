from ninja import Schema
from typing import Optional
from datetime import datetime


class ApplicationIn(Schema):
    applicant_name: str
    applicant_email: str
    company_name: str
    application_type: str
    description: str


class ApplicationOut(Schema):
    id: int
    tracking_number: str

    applicant_name: str
    applicant_email: str
    company_name: str

    application_type: str
    description: str

    status: str
    reviewer_comment: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    submitted_at: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None


class ReviewerDecisionSchema(Schema):
    decision: str
    reviewer_comment: str