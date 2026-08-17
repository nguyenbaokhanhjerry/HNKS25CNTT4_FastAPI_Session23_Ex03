from typing import List

from fastapi import APIRouter, Depends, status

from auth import get_current_user, require_admin
from schemas.resource import ResourceCreate, ResourceResponse
from services.resource import (
    create_resource,
    delete_resource,
    get_resource,
    list_resources,
    publish_resource,
)

router = APIRouter(prefix="/resources", tags=["Resources"])


@router.get("", response_model=List[ResourceResponse])
def read_resources(current_user: dict = Depends(get_current_user)):
    return list_resources(current_user)


@router.get("/{resource_id}", response_model=ResourceResponse)
def read_resource(
    resource_id: int,
    current_user: dict = Depends(get_current_user),
):
    return get_resource(resource_id, current_user)


@router.post(
    "",
    response_model=ResourceResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_resource(
    data: ResourceCreate,
    current_user: dict = Depends(require_admin),
):
    return create_resource(data, current_user)


@router.patch(
    "/{resource_id}/publish",
    response_model=ResourceResponse,
)
def publish(
    resource_id: int,
    current_user: dict = Depends(require_admin),
):
    return publish_resource(resource_id)


@router.delete(
    "/{resource_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_resource(
    resource_id: int,
    current_user: dict = Depends(require_admin),
):
    delete_resource(resource_id)
    return None
