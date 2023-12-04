import sys

def echo(phrase: str) -> None:
   print(phrase)

def main() -> int:
    """Echo the input arguments to standard output"""
    phrase = "salve"
    echo(phrase)
    return 0

if __name__ == '__main__':
    sys.exit(main())