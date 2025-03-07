import pickle
import sys

import lmdb
import cloudpickle

from netex import StopPlace
from netexio.database import Database
from netexio.dbaccess import load_local
from netexio.pickleserializer import MyPickleSerializer
from tmp.netex.models import PassengerStopAssignment

with Database(sys.argv[1], serializer=MyPickleSerializer(compression=True), readonly=True) as db_read:
    """for x in load_local(db_read, PassengerStopAssignment):
        if isinstance(x, StopPlace):
            print("ja")

        # cursor = txn.cursor()
        # for key, _ in cursor:
        #    print(key)
    """

    """
    with db_read.env.begin() as txn:
        cursor = txn.cursor()
        for key, _ in cursor:
            print(key)
            db_read.env.open_db(key, create=False)
    
    """
    print("embedding")
    with db_read.env.begin(db=db_read.db_embedding, write=False) as txn:
        cursor = txn.cursor()
        i = 0
        for _key, value in cursor:
            _tmp = cloudpickle.loads(value)
            # parent_clazz, parent_id, parent_version, embedding_path = _tmp
            print(_tmp)

    print("embedding_inverse")
    with db_read.env.begin(db=db_read.db_embedding_inverse, write=False) as txn:
        cursor = txn.cursor()
        i = 0
        for _key, value in cursor:
            _tmp = cloudpickle.loads(value)
            # embedding_clazz, embedding_id, embedding_version, embedding_path = _tmp
            print(_tmp)


    """
    # db_read.env.open_db(b'_embedding', create=False)

    print("test embedding")
    db_src = db_read.db_embedding
    if db_src:
        with db_read.env.begin(write=False, db=db_src) as txn_ro:
            cursor = txn_ro.cursor()
            for db_key, db_value in cursor:
                # print(pickle.loads(db_key))
                print(cloudpickle.loads(db_value))

    print("test referencing")
    try:
        db_src = db_read.db_referencing
        if db_src:
            with db_read.env.begin(write=False, db=db_src) as txn_ro:
                cursor = txn_ro.cursor()
                for db_key, db_value in cursor:
                    # print(pickle.loads(db_key))
                    print(cloudpickle.loads(db_value))
    except lmdb.Error:
        pass
    """