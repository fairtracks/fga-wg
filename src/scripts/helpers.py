import sys
from _frozen_importlib import module_from_spec
from _frozen_importlib_external import spec_from_file_location
from pathlib import Path
from types import ModuleType


def import_from_path(module_name: str, file_path: Path) -> ModuleType:
    spec = spec_from_file_location(module_name, str(file_path))
    assert spec is not None, f"Could not load module {module_name} from {file_path}"
    module = module_from_spec(spec)
    sys.modules[module_name] = module
    loader = spec.loader
    assert loader is not None, f"Loader is None for module {module_name} from {file_path}"
    loader.exec_module(module)
    return module
