from netexio.database import Database
from transformers.reversion import reversion_all_objects

with Database("/tmp/authorities-any.duckdb", read_only=False) as db:
    reversion_all_objects(db, "20241114")

with Database("/tmp/authorities.duckdb", read_only=True) as db:
    reversion_all_objects(db, "20241114", True)