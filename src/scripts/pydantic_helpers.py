from types import UnionType
from typing import get_origin, get_args, cast

from pydantic import BaseModel as BaseModelV2
from pydantic.fields import FieldInfo
from pydantic.v1 import BaseModel as BaseModelV1
from pydantic.v1.fields import ModelField
from pydantic.v1.utils import lenient_issubclass


def get_fields_from_model(model_cls: type[BaseModelV1] | type[BaseModelV2]) -> dict[str, ModelField] | dict[str, FieldInfo]:
    if issubclass(model_cls, BaseModelV1):
        return model_cls.__fields__
    elif issubclass(model_cls, BaseModelV2):
        return model_cls.model_fields


def extract_examples_from_field_info(info: ModelField | FieldInfo) -> list[object] | None:
    if isinstance(info, ModelField):
        return info.field_info.extra.get('examples')
    elif isinstance(info, FieldInfo):
        return info.examples


def extract_model_from_field_info(info: ModelField | FieldInfo) -> type[BaseModelV1 | BaseModelV2 | UnionType]:
    if isinstance(info, ModelField):
        return info.type_
    elif isinstance(info, FieldInfo):

        def _extract_model_from_type(_typ: type|None) -> type[BaseModelV2 | UnionType] | None:
            origin = get_origin(_typ)
            if origin is list:
                arg = get_args(_typ)[0]
                if get_origin(arg) is UnionType or lenient_issubclass(arg, BaseModelV2):
                    return cast(type[BaseModelV2 | UnionType], arg)
            else:
                if get_origin(_typ) is UnionType or lenient_issubclass(_typ, BaseModelV2):
                    return cast(type[BaseModelV2 | UnionType], _typ)

        _typ = info.annotation

        model = None
        if get_origin(_typ) is UnionType:
            for arg in get_args(_typ):
                model = _extract_model_from_type(arg)
                if model is not None:
                    break
        else:
            model = _extract_model_from_type(_typ)

        if model is not None:
            return model
        else:
            raise ValueError(f"Could not extract model from type {_typ}")


def field_is_list(info: ModelField | FieldInfo) -> bool:
    if isinstance(info, ModelField):
        return get_origin(info.outer_type_) is list
    elif isinstance(info, FieldInfo):
        if get_origin(info.annotation) is UnionType:
            for arg in get_args(info.annotation):
                if get_origin(arg) is list:
                    return True
            return False
        else:
            return get_origin(info.annotation) is list
