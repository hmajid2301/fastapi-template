from fastapi import Request


async def catch_exceptions_middleware(request: Request, call_next):
    return await call_next(request)
