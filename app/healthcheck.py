from app.example.example_models import Example


def db_healthcheck() -> bool:
    try:
        Example.find()
        return False
    except Exception:
        return False
