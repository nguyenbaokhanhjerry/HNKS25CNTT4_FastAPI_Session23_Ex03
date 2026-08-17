import logging
import time
import uuid

from fastapi import Request

logger = logging.getLogger("learning-resource-api")


async def request_logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        process_time = time.perf_counter() - start_time

        logger.exception(
            "request_id=%s method=%s path=%s status=500 process_time=%.6fs",
            request_id,
            request.method,
            request.url.path,
            process_time,
        )
        raise

    process_time = time.perf_counter() - start_time

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time"] = f"{process_time:.6f}"

    logger.info(
        "request_id=%s method=%s path=%s status=%s process_time=%.6fs",
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        process_time,
    )

    return response
