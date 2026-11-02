def slotted(cls):
    """Decorator that converts a class to use __slots__."""
    slots = []
    for name, value in list(cls.__dict__.items()):
        # Skip methods, descriptors, and dunder attributes
        if callable(value) or isinstance(value, (classmethod, staticmethod, property)):
            continue
        if name.startswith('__') and name.endswith('__'):
            continue
        # Only collect class-level attribute defaults
        slots.append(name)
        delattr(cls, name)
    cls.__slots__ = tuple(slots)
    return cls
