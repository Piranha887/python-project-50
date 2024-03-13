import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    return parser.parse_args()


def main():
    args = parse_args()
    # TODO: Add your logic here


if __name__ == '__main__':
    main()
