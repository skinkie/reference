from collections import OrderedDict

class ActiveLRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = OrderedDict()
        self.current_access = set()

    def get(self, key, load_func):
        """Retrieve item from cache or load it using load_func."""
        if key in self.cache:
            self.current_access.add(key)
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]

        # TODO
        # value = load_func(key)
        # self._add(key, value)
        # return value

    def add(self, key, value):
        self._add(key, value)

    def _add(self, key, value):
        if len(self.cache) >= self.max_size:
            self._evict()
        self.cache[key] = value
        self.current_access.add(key)

    def _evict(self):
        """Evicts least recently used items that were not accessed in the last cycle."""
        to_remove = [k for k in self.cache.keys() if k not in self.current_access]
        for k in to_remove:
            del self.cache[k]
        while len(self.cache) >= self.max_size:  # In case everything was accessed, evict normally
            self.cache.popitem(last=False)

    def new_cycle(self):
        """Call this at the start of a new access cycle."""
        self.current_access.clear()