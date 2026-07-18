class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = value

    def remove(self, key):
        hashed = self.hash(key)
        bucket = self.collection.get(hashed)
        if bucket and key in bucket:
            del bucket[key]
            if not bucket:
                del self.collection[hashed]

    def lookup(self, key):
        hashed = self.hash(key)
        bucket = self.collection.get(hashed)
        if bucket is None:
            return None
        return bucket.get(key)
