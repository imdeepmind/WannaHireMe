from django.urls import path

from .views import (
    CreateOrListState,
    RetrieveOrEditOrDeleteState,
    CreateOrListCountry,
    RetrieveOrEditOrDeleteCountry,
    RetrieveOrEditOrDeleteSkill,
    CreateOrListSkill,
    CreateOrListLinkType,
    RetrieveOrEditOrDeleteLinkType,
)

urlpatterns = [
    # Skills
    path("skill", CreateOrListSkill.as_view(), name="Create or List Skills"),
    path("skill/<int:pk>", RetrieveOrEditOrDeleteSkill.as_view(), name="Retrieve or Edit or Delete Skill"),
    # Link Types
    path("link-type", CreateOrListLinkType.as_view(), name="Create or List Link Types"),
    path("link-type/<int:pk>", RetrieveOrEditOrDeleteLinkType.as_view(), name="Retrieve or Edit or Delete Link Type"),
    # Country
    path("country", CreateOrListCountry.as_view(), name="Create or List Countries"),
    path("country/<int:pk>", RetrieveOrEditOrDeleteCountry.as_view(), name="Retrieve or Edit or Delete Country"),
    # State
    path("state", CreateOrListState.as_view(), name="Create or List States"),
    path("state/<int:pk>", RetrieveOrEditOrDeleteState.as_view(), name="Retrieve or Edit or Delete State"),
]
