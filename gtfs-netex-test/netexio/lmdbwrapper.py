import lmdb
import threading
import pickle

class LMDBDatabase:
    def __init__(self, path, initial_size=256 * 1024 * 1024, growth_size=None, max_size=16 * 1024 ** 3):
        self.path = path
        self.initial_size = initial_size
        self.growth_size = growth_size if growth_size else initial_size  # Linear growth
        self.max_size = max_size
        self.lock = threading.Lock()

        self.env = lmdb.open(
            path,
            max_dbs=10,
            map_size=initial_size,
            writemap=True,
            metasync=False,
            sync=False
        )

    def _resize_env(self, min_increase=0):
        """Ensures LMDB grows by at least growth_size or min_increase."""
        with self.lock:
            current_size = self.env.info()["map_size"]
            increase = max(self.growth_size, int(min_increase))  # Ensure enough space
            new_size = min(current_size + increase, self.max_size)
            if new_size > current_size:
                print(f"Resizing LMDB from {current_size} to {new_size} bytes")
                self.env.set_mapsize(new_size)
            else:
                raise RuntimeError("LMDB reached max map size, cannot grow further.")

    def batched_write(self, db_name, items, batch_size=10_000):
        """Batched writes with dynamic resizing."""
        db = self.env.open_db(db_name)

        batch = []
        total_size = 0

        for key, value in items:
            key_p = pickle.dumps(key)
            value_p = pickle.dumps(value)
            batch.append((key_p, value_p))
            total_size += len(key_p) + len(value_p)

            if len(batch) >= batch_size or total_size >= self.growth_size:
                self._write_batch(db, batch, total_size)
                batch.clear()
                total_size = 0

        if batch:
            self._write_batch(db, batch, total_size)

    def _write_batch(self, db, batch, total_size):
        """Writes a batch and retries if LMDB runs out of space."""
        while True:
            try:
                with self.env.begin(write=True) as txn:
                    for key, value in batch:
                        txn.put(key, value, db=db)
                break  # Success, exit loop
            except lmdb.MapFullError:
                print("LMDB full, resizing...")
                self._resize_env(total_size * 1.1)  # Ensure enough space for this batch

    def close(self):
        self.env.close()

if __name__ == '__main__':
    lmdb_db = LMDBDatabase("/tmp/test.lmdb", initial_size=1000 * 1024)
    items = [(i, [b'a' * 3072]) for i in range(0, 1024)]

    lmdb_db.batched_write(db_name=b"test", items=items, batch_size=10000)
    lmdb_db.close()