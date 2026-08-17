from fastapi import HTTPException, status

from models.resource import resources
from schemas.resource import ResourceCreate


def list_resources(current_user: dict) -> list:
    if current_user["role"] == "admin":
        return resources

    return [
        resource
        for resource in resources
        if resource["is_published"]
    ]


def get_resource(resource_id: int, current_user: dict) -> dict:
    resource = next(
        (item for item in resources if item["id"] == resource_id),
        None,
    )

    if resource is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    # Không để User biết resource unpublished có tồn tại.
    if current_user["role"] == "user" and not resource["is_published"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    return resource


def create_resource(data: ResourceCreate, current_user: dict) -> dict:
    new_id = max((item["id"] for item in resources), default=0) + 1

    resource = {
        "id": new_id,
        "title": data.title,
        "description": data.description,
        "url": data.url,
        "is_published": data.is_published,
        "created_by": current_user["username"],
    }

    resources.append(resource)
    return resource


def publish_resource(resource_id: int) -> dict:
    resource = next(
        (item for item in resources if item["id"] == resource_id),
        None,
    )

    if resource is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    resource["is_published"] = True
    return resource


def delete_resource(resource_id: int) -> None:
    resource_index = next(
        (index for index, item in enumerate(resources) if item["id"] == resource_id),
        None,
    )

    if resource_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resource not found",
        )

    resources.pop(resource_index)
