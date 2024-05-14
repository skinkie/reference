import sqlite3

from anyintodbnew import  get_interesting_classes, setup_database, open_netex_file, insert_database

DATABASE_FILE = "/home/netex/swiss.sqlite"
SWISS_ZIP_FILE = "/home/skinkie/Downloads/prod_netex_tt_1.10_che_ski_2024_oev-schweiz__1_1_202404140804.zip"
CLEAN_DATABASE = True

with sqlite3.connect(DATABASE_FILE) as con:
    classes = get_interesting_classes()

    if CLEAN_DATABASE:
        setup_database(con, classes, CLEAN_DATABASE)

        for file in open_netex_file(SWISS_ZIP_FILE):
            insert_database(con, classes, file)
