# kiwidb

[![PyPI](https://img.shields.io/pypi/v/kiwidb.svg)](https://pypi.org/project/kiwidb/)
[![Python 3.x](https://img.shields.io/pypi/pyversions/kiwidb.svg?logo=python&logoColor=white)](https://pypi.org/project/kiwidb/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ernestofgonzalez/kiwidb/blob/main/LICENSE.md)

`kiwidb` is a small, in-memory key-value database written in pure Python. It started as a way to experiment with in-memory key-value storage, inspired by the guide from [Building a Simple Redis Server with Python](https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/). It is designed for learning and experimentation.

## Some feature highlights

- Supports basic key-value operations (e.g., `SET`, `GET`, `DEL`).
- In-memory storage for fast access.

## Getting Started

### Installation

```bash
pip install kiwidb
```

### Using as a library

Run the `kiwidb` server:

```bash
python kiwidb
```

Interact with the database using a client (to be implemented or use a Python script):

```python
import kiwidb

db = kiwidb.Client()
db.set("key", "value")
print(db.get("key"))  # Outputs: value
db.delete("key")
```