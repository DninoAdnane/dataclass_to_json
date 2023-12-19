# Dataclass_to_json
**Dataclass_to_json** is a lightweight and simple library for Converting a dataclass structure to a JSON object. The dataclass_to_json library allows you to retrieve a JSON object representing the class *attributes* and their *types*. 

## Installing Dataclass_to_json
dataclass_to_json in available on PyPI:
```bash
python -m pip install dataclass_to_json
```
Dataclass_to_json officially supports Python 3.7+.

## Usage
```python
from dataclass_to_json import dataclass_to_json
from typing import List
import json

class Employee:
    name: str
    age: int
    salary: float
    remarks: List[str]

class Entreprise:
    name: str
    address: str
    employees: List[Employee]


json_structure = dataclass_to_json(Entreprise)

print(json.dumps(json_structure, indent= 2))
```

### The output:
```json
{
  "name": "str",
  "address": "str",
  "employees": [
    {
      "name": "str",
      "age": "int",
      "salary": "float",
      "remarks": [
        "str"
      ]
    }
  ]
}
```

