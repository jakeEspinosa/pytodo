from cli import parser, get_version

args = parser.parse_args()

def main():
    print(get_version(args.version))

if __name__ == "__main__":
    main()
