class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    import re\n    if not re.fullmatch(r"[a-z][a-z0-9-]{2,20}", str(body.get("name") or "")): failed.append("bad_name")\n    if body.get("region") not in {"us-central1", "europe-west1"}: failed.append("bad_region")
    return {"passed": not failed, "failed": failed, "applied": False}
