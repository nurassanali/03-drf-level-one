from django.urls import path
from jobs.api.views import (JobOfferListCreateAPIView, JobOfferDetailAPIView)

urlpatterns = [
  path("job_offers/", JobOfferListCreateAPIView.as_view(), name="jobs-list"),
  path("job_offers/<int:pk>/", JobOfferDetailAPIView.as_view(), name="jobs-detail")
]