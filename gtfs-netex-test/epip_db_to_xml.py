from netex import PublicationDelivery
from netexio.database import Database
from netexio.xml import export_publication_delivery_xml
import traceback

from aux_logging import *
from transformers.epip import export_epip_network_offer

def main(database_original: str, database_target: str, output_filename: str):
    # TODO: EPIP refactor to a single db_target
    with Database(database_original) as db_orig:
        with Database(database_target) as db_target:
            publication_delivery: PublicationDelivery = export_epip_network_offer(db_orig, db_target)
            export_publication_delivery_xml(publication_delivery, output_filename)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Export a prepared EPIP import into DuckDB')
    argument_parser.add_argument('original', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('target', type=str, help='The transformed DuckDB NeTEx database')
    argument_parser.add_argument('output', type=str, help='The NeTEx output filename, for example: netex.xml.gz')
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')

    args = argument_parser.parse_args()
    mylogger = prepare_logger(logging.INFO, args.log_file)

    try:
        main(args.original, args.target, args.output)
    except Exception as e:
        log_all(logging.ERROR, f'{e}', traceback.format_exc())
        raise e

