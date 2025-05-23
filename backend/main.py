from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from auth.security import limiter
from event.endpoints import router as event_router
from note.endpoints import router as note_router
from task.endpoints import router as task_router
from auth.endpoints_auth import router as auth_router
from auth.endpoints_user import router as user_router


app = FastAPI(
    title="Articly App"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(note_router, prefix="/note", tags=("Notes",))
app.include_router(task_router, prefix="/task", tags=("Tasks",))
app.include_router(event_router, prefix="/event", tags=("Events",))
app.include_router(auth_router, prefix="/auth", tags=("Auth",))
app.include_router(user_router, prefix="/user", tags=("User",))


app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


