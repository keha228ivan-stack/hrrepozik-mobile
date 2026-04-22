from __future__ import annotations

from copy import deepcopy
from datetime import datetime
from typing import Any, Union, get_args, get_origin
import types

try:
    from pydantic import BaseModel, Field  # type: ignore
except Exception:
    _MISSING = Ellipsis

    def Field(*, default: Any = _MISSING, **_: Any) -> Any:
        return default

    class BaseModel:
        def __init__(self, **data: Any) -> None:
            annotations = getattr(self.__class__, "__annotations__", {})
            for name, hint in annotations.items():
                if name in data:
                    value = data[name]
                elif hasattr(self.__class__, name):
                    default = getattr(self.__class__, name)
                    if default is _MISSING:
                        raise TypeError(f"Missing required field: {name}")
                    value = deepcopy(default)
                else:
                    raise TypeError(f"Missing required field: {name}")
                setattr(self, name, self._coerce_value(hint, value))

        @classmethod
        def model_validate(cls, obj: Any) -> "BaseModel":
            if isinstance(obj, cls):
                return obj
            if not isinstance(obj, dict):
                raise TypeError(f"{cls.__name__}.model_validate expects dict, got {type(obj).__name__}")
            return cls(**obj)

        def model_dump(self, *, mode: str = "python", **_: Any) -> dict[str, Any]:
            result: dict[str, Any] = {}
            annotations = getattr(self.__class__, "__annotations__", {})
            for name in annotations:
                value = getattr(self, name)
                if mode == "json" and isinstance(value, datetime):
                    result[name] = value.isoformat()
                else:
                    result[name] = value
            return result

        @staticmethod
        def _coerce_value(hint: Any, value: Any) -> Any:
            if value is None:
                return None

            origin = get_origin(hint)
            if origin in (types.UnionType, Union):
                args = [arg for arg in get_args(hint) if arg is not type(None)]
                for arg in args:
                    try:
                        return BaseModel._coerce_value(arg, value)
                    except Exception:
                        continue
                return value

            if hint is datetime and isinstance(value, str):
                try:
                    return datetime.fromisoformat(value.replace("Z", "+00:00"))
                except ValueError:
                    return value

            if hint in (int, float, str, bool):
                try:
                    return hint(value)
                except Exception:
                    return value

            return value
