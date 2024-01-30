# BasicCache

This repository contains the code for a basic caching system implemented in Python. The `BasicCache` class is a subclass of the `BaseCaching` class, which provides a basic caching interface.

## Installation

To install the `BasicCache` class, simply clone this repository and add the `basic_cache` directory to your Python path.

## Usage

To use the `BasicCache` class, simply create an instance of the class and call the `put()` and `get()` methods to add and retrieve items from the cache.

The following code snippet shows how to use the `BasicCache` class:

```python
from basic_cache import BasicCache

# Create an instance of the BasicCache class
cache = BasicCache()

# Add an item to the cache
cache.put("key1", "value1")

# Retrieve an item from the cache
value = cache.get("key1")

# Print the retrieved value
print(value)
```

## Implementation Details

The `BasicCache` class is a simple implementation of a caching system that uses a dictionary to store items. The `put()` method adds an item to the dictionary, and the `get()` method retrieves an item from the dictionary.

If the `key` argument is `None`, the `put()` and `get()` methods do nothing. This is because `None` is not a valid key for a dictionary.

The `BasicCache` class also inherits the `max_items` attribute from the `BaseCaching` class. This attribute specifies the maximum number of items that can be stored in the cache. If the cache is full, the oldest item is removed from the cache before a new item is added.

## Conclusion

The `BasicCache` class is a simple but effective caching system that can be used to improve the performance of your applications. The class is easy to use and can be easily integrated into your existing code.
