import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="store_true")

def get_version(version=False):
    if version:
        return "0.0.1"
