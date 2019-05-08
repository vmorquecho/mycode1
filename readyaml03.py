#!/usr/bin/env python3

import yaml

def main():
    yammyfile = open("~/mycode1/yamlintro/myYAML.yml", "r")

    pyyammy = yaml.load(yammyfile)

    print(pyyammy)

main()

