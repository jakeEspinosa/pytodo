import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true")

def version(version=False):
    if version:
        print("0.0.1")
