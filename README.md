# kiwidb

`kiwidb` is a small, in-memory key-value database written in pure Python. It started as a way to experiment with in-memory key-value storage, inspired by the guide from [Building a Simple Redis Server with Python](https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/). It is designed for learning and experimentation.

## Some feature highlights

- Supports basic key-value operations (e.g., `SET`, `GET`, `DEL`).
- In-memory storage for fast access.

## Getting Started

### Installation

Clone the repository:

```bash
git clone https://github.com/ernestofgonzalez/kiwidb.git
cd kiwidb
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