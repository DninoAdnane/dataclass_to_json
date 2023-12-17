from typing import get_type_hints


def dataclass_to_json(pydantic_cls):
    json_structure = {}
    type_hints = get_type_hints(pydantic_cls)

    for field_name, field_type in type_hints.items():
        if hasattr(field_type, "__annotations__"):
            field_structure = dataclass_to_json(field_type)
        elif hasattr(field_type, "__args__") and len(field_type.__args__) > 0:
            inner_type = field_type.__args__[0]
            if hasattr(inner_type, "__annotations__"):
                if "Union" in str(field_type):
                    field_structure = dataclass_to_json(inner_type)
                else:
                    field_structure = [dataclass_to_json(inner_type)]
            else:
                field_structure = str(field_type).replace("typing.", "")
                if not field_structure.startswith("Literal"):
                    field_structure = (
                        str(inner_type)
                        .replace("<class '", "")
                        .replace("'>", "")
                        if "class" in str(inner_type)
                        else "str"
                    )
        else:
            field_structure = (
                str(field_type).replace("<class '", "").replace("'>", "")
                if "class" in str(field_type)
                else "str"
            )

        json_structure[field_name] = field_structure

    return json_structure
