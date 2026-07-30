# AttrDict

[![PyPI](https://img.shields.io/pypi/v/attrDict)](https://pypi.org/project/attrDict/)
[![Python](https://img.shields.io/pypi/pyversions/attrDict)](https://pypi.org/project/attrDict/)
[![License](https://img.shields.io/pypi/l/attrDict)](LICENSE)

A lightweight dictionary with attribute-style access.

## Introduction

AttrDict is a lightweight subclass of Python's built-in dict that provides attribute-style access while preserving standard dictionary behavior.

## Features

- Attribute access (`obj.name`)
- Standard dictionary behavior
- Automatic conversion of nested mappings
- Recursive conversion in lists, tuples, sets, and frozensets
- No dependencies
- Lightweight

## Why AttrDict?

- Keeps full `dict` compatibility.
- Supports both attribute and item access.
- Automatically converts nested mappings.
- Uses no external dependencies.

## Requirements

- Python 3.8+

## Installation

```bash
pip install attrDict
```

## Quick Start

```python
from attrDict import AttrDict

data = AttrDict({
    "name": "Alice",
    "age": 20,
    "address": {
        "city": "London"
    }
})

print(data.name)
print(data.address.city)

data.country = "UK"
print(data["country"])
```

## Examples

```python
user = AttrDict(name="Alice", age=20)

print(user.name)
```

## Name Conflicts

Attribute access follows normal Python attribute lookup.  
If a key has the same name as an existing attribute or method,
attribute access refers to the attribute or method.  
Use item access (`[]`) to access conflicting keys.  

```python
data = AttrDict({
    "items": 123
})

print(data.items())      # dict.items method
print(data["items"])     # 123
```

## API

### Constructor

```python
AttrDict(*args, **kwargs)
```
Creates an AttrDict from the given mapping or keyword arguments.

### Behavior

- `obj.key` → equivalent to `obj["key"]`
- `obj.key = value` → equivalent to `obj["key"] = value`
- `del obj.key` → equivalent to `del obj["key"]`
- Nested mappings are automatically converted to AttrDict.

## License

This project is licensed under the [MIT License.](LICENSE)

Copyright (c) 2026 Hoàng Long