from cli import parser, version

args = parser.parse_args()

def main():
    version(args.version)

if __name__ == "__main__":
    main()
