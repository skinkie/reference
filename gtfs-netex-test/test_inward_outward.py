from cloudpickle import cloudpickle

from netex import ServiceJourney, ServiceJourneyPattern, StopPlace, Quay
from netexio.database import Database
from netexio.dbaccess import load_embedded_transparent_generator, load_referencing, load_referencing_inwards, \
    fetch_references_classes_generator
from refs import getRef
from netexio.pickleserializer import MyPickleSerializer
from tmp.netex.models import QuaysRelStructure

import time

def show(db_write, db_handle, id, version, clazz):
    prefix = db_write.serializer.encode_key(id, version, clazz, include_clazz=True)
    print(prefix)
    with db_write.env.begin(db=db_handle, buffers=True, write=False) as txn:
        cursor = txn.cursor()
        if cursor.set_range(prefix):  # Position cursor at the first key >= prefix
            for key, value in cursor:
                if not bytes(key).startswith(prefix):
                    break  # Stop when keys no longer match the prefix
                _tmp = cloudpickle.loads(value)
                print(id, clazz, prefix, _tmp)

with Database("/tmp/test.lmdb", MyPickleSerializer(compression=True), readonly=False) as db_write:
    # db_write.drop([ServiceJourney, ServiceJourneyPattern, StopPlace], embedding=True)

    sjp = ServiceJourneyPattern(id="sjp-test", version="sjp")
    sj1 = ServiceJourney(id="sj1-test", version="sj", journey_pattern_ref=getRef(sjp))
    sj2 = ServiceJourney(id="sj2-test", version="sj", journey_pattern_ref=getRef(sjp))

    quay1 = Quay(id="quay1-test", version="embedding-test")
    quay2 = Quay(id="quay2-test", version="embedding-test")

    sp1 = StopPlace(id="sp1-test", version="sp1-version", quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[quay1, quay2]))
    sp2 = StopPlace(id="sp2-test", version="sp2-version", quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[getRef(quay1), getRef(quay2)]))

    db_write.insert_one_object(sjp)
    db_write.insert_one_object(sj1)
    db_write.insert_one_object(sj2)
    db_write.insert_one_object(sp1)
    db_write.insert_one_object(sp2)

    db_write.block_until_done()

    with db_write.env.begin(db=db_write.db_embedding, write=False) as src1_txn:
        cursor = src1_txn.cursor()
        print("embedding empty?", not cursor.first())

    with db_write.env.begin(db=db_write.db_embedding_inverse, write=False) as src1_txn:
        cursor = src1_txn.cursor()
        print("embedding inverse empty?", not cursor.first())

    with db_write.env.begin(db=db_write.db_referencing, write=False) as src1_txn:
        cursor = src1_txn.cursor()
        print("referencing empty?", not cursor.first())

    with db_write.env.begin(db=db_write.db_referencing_inwards, write=False) as src1_txn:
        cursor = src1_txn.cursor()
        print("referencing inwards empty?", not cursor.first())

    with db_write.env.begin() as txn:
        with txn.cursor(db=db_write.env.open_db(None)) as cursor:
            print("Named Databases:", [key.decode() for key, _ in cursor])

    with db_write.env.begin(db=db_write.open_db(ServiceJourney), write=True) as src1_txn:
        cursor = src1_txn.cursor()
        print("service journey inwards empty?", not cursor.first())


    """
    print("embedding")
    show(db_write, db_write.db_embedding, sp1.id, None, sp1.__class__)
    show(db_write, db_write.db_embedding, sp2.id, None, sp2.__class__)

    print("embedding_inverse")
    show(db_write, db_write.db_embedding_inverse, quay1.id, None, quay1.__class__)
    show(db_write, db_write.db_embedding_inverse, quay2.id, None, quay2.__class__)
    """
    """

    print("referencing")
    show(db_write, db_write.db_referencing, sp1.id, None, sp1.__class__)
    show(db_write, db_write.db_referencing, sp2.id, None, sp2.__class__)
    show(db_write, db_write.db_referencing, sjp.id, None, sjp.__class__)

    print("referencing_inwards")
    show(db_write, db_write.db_referencing_inwards, quay1.id, None, quay1.__class__)
    show(db_write, db_write.db_referencing_inwards, quay2.id, None, quay2.__class__)
    show(db_write, db_write.db_referencing_inwards, sjp.id, None, sjp.__class__)

    # print(list(load_embedded_transparent_generator(db_write, quay1.__class__, filter=quay1.id)))
    # print(list(load_referencing(db_write, sp2.__class__, sp2.id)))
    # print(list(load_referencing_inwards(db_write, sjp.__class__, sjp.id)))

    with db_write.env.begin(db=db_write.db_referencing_inwards, buffers=True, write=False) as src1_txn:
        cursor = src1_txn.cursor()
        print("Database is empty?", not cursor.first())
        for _key, value in cursor:
            print('hello', cloudpickle.loads(value))

    """
    print(list(fetch_references_classes_generator(db_write, [ServiceJourney])))
