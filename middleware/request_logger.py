from fastapi import Request
from utils.logger import logger
import time
from typing import Callable
from starlette.middleware.base import BaseHTTPMiddleware


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable):
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time
        log_dict = {
            "path": request.url.path,
            "args": request.query_params,
            "method": request.method,
            "process_time": f"{process_time:.2f}s",
            "status_code": response.status_code,
            "client_host": request.client.host if request.client else None,
        }

        logger.info(f"Request processed: {log_dict}")

        return response
