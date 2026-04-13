import json
import sys
from os.path import abspath
from pathlib import Path
from types import ModuleType, UnionType
from typing import get_args, get_origin

from pydantic.v1.fields import ModelField
from pydantic.fields import FieldInfo
from pydantic.v1 import BaseModel as BaseModelV1
from pydantic import BaseModel as BaseModelV2


from .pydantic_helpers import get_fields_from_model, extract_examples_from_field_info, \
    extract_model_from_field_info, field_is_list
from .helpers import import_from_path

TOP_LEVEL = 'TopLevel'

_project_root = Path(abspath(__file__ + '/../../../'))
schema_v1 = import_from_path('pydantic_v1_model', _project_root / 'generated' / 'pydantic_v1_model.py')
schema_v2 = import_from_path('pydantic_v2_model', _project_root / 'generated' / 'pydantic_v2_model.py')


def _get_reordered_top_level_fields(schema: ModuleType) -> dict[str, ModelField | FieldInfo]:
    top_level_fields = get_fields_from_model(schema.TopLevel).copy()
    ordered_fields = {'document': top_level_fields.pop('document')}
    ordered_fields.update(top_level_fields)
    return ordered_fields


def _extract_model_example(model_cls: type[BaseModelV1 | BaseModelV2]) -> dict[str, object]:
    model_example: dict[str, object] = {}
    model_cls
    for field, info in get_fields_from_model(model_cls).items():
        examples = extract_examples_from_field_info(info)
        if examples:
            model_example[field] = examples[0]
    return model_example


def _generate_top_level_example(schema: ModuleType) -> dict[str, object]:
    top_level_example = {}

    top_level_fields = _get_reordered_top_level_fields(schema)

    for field_name, info in top_level_fields.items():
        model = extract_model_from_field_info(info)

        if get_origin(model) is UnionType and schema.File in get_args(model):
            model = schema.GenomicAnnotationFile

        model_example = _extract_model_example(model)
        top_level_example[field_name] = [model_example] if field_is_list(info) else model_example

    return top_level_example

def _generate_example_for_model(model_name: str, schema: ModuleType) -> dict[str, object]:
    model_cls = getattr(schema, model_name)
    return _extract_model_example(model_cls)


def generate_examples(schema: ModuleType, model_names: list[str]) -> dict[str, dict[str, object]]:
    examples = {}

    for model_name in model_names:
        if model_name == TOP_LEVEL:
            model_example = _generate_top_level_example(schema)
        else:
            model_example = _generate_example_for_model(model_name, schema)
        examples[model_name] = model_example

    return examples


def write_example_json_files(examples: dict[str, dict[str, object]]):
    examples_dir = _project_root / 'generated' / 'examples'
    examples_dir.mkdir(parents=True, exist_ok=True)

    for field_name, example in examples.items():
        example_path = examples_dir / f'{field_name}.json'
        with open(example_path, 'w') as f:
            f.write(json.dumps(example, indent=2))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_examples.py <model1> <model2> ...")
        sys.exit(1)

    model_names = sys.argv[1:]

    examples_v1 = generate_examples(schema_v1, model_names)
    examples_v2 = generate_examples(schema_v2, model_names)

    assert examples_v1 == examples_v2, "Examples generated from pydantic v1 and v2 models do not match"

    write_example_json_files(examples_v1)