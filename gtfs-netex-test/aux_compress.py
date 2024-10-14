import gzip
import os


def compress_file(input_file, cleanup=False):
    if not input_file.lower().endswith('.xml'):
        raise ValueError('Input file must have an XML extension')

    output_file = input_file + '.gz'

    with open(input_file, 'rb') as file_in:
        with gzip.open(output_file, 'wb') as file_out:
            file_out.writelines(file_in)

    if cleanup:
        os.remove(input_file)

    return output_file

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Compresses a NeTEx file')
    parser.add_argument('file', type=str, help='file name')
    parser.add_argument('--cleanup', type=bool, default=False, help='If set, then the original file is removed.')

    args = parser.parse_args()

    compress_file(args.file, cleanup=args.cleanup)