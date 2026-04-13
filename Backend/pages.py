from fastapi import APIRouter

router = APIRouter(tags=["Pages"])


@router.get("/")
def home():
    return {
        "message": "Welcome to the REC / HUB platform",
        "status": "API is running"
    }


@router.get("/about")
def about():
    return {
        "project": "REC / HUB Matching Platform",
        "description": "This platform matches energy producers and consumers within Renewable Energy Communities (REC) and energy hubs.",
        "how_it_works": [
            "Users submit their energy data",
            "The system processes and matches suitable partners",
            "Results are stored and can be retrieved later"
        ]
    }