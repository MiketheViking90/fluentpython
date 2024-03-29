from inspect import signature


def clip(text: str, max_len: int =80) -> str:
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
    else:
        space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None: # no spaces were found
        end = len(text)
    return text[:end].rstrip()

print(clip.__defaults__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

sig = signature(clip)
print(str(sig))
print(clip.__annotations__)