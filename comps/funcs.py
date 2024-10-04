from enums import Cost_Types

def is_responsive(parm) -> bool:
    ret = False
    if parm["responsive"]:
        ret = True
    return ret


def can_off_rail(parm) -> bool:
    ret = False
    if parm:
        ret = True
    return ret


def is_afv(parm: list[str]) -> bool:
    ret = False
    if "AFV" in parm:
        ret = True
    return ret


def not_is_afv(parm: list[str]) -> bool:
    return not is_afv(parm)


def new_speed_table(parm: str) -> bool:
    ret = False
    if parm == "Wind-powered":
        ret = True
    return ret

