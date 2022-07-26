"""
A script that finds the number of tags present from the entire JSON file.

Written just as a test script to see if the JSON file is working.
"""
import argparse
import json
from random import randint

parser = argparse.ArgumentParser(description="Parses any tags from the generated JSON") 
parser.add_argument("-t", "--tag", type=str, metavar="<string>", help="Find a specific tags")

args = parser.parse_args()

with open("paco-fa-database.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    tags = []
        
    for i in data["database"]:
        for j in i["tags"]:
            tags.append(j)
          
    total_count = len(tags)
      
    if args.tag:
        results = tags.count(args.tag)
        
        if results == 0:
            print(f"No results found for tag '{args.tag}'")
        else:
            print(f"'{args.tag}' returned {results} hits ({results/total_count*100:.5f}% of {total_count})")
    else:
        random_tag = tags[randint(1, total_count)]
        results = tags.count(random_tag)
        print(f"'{random_tag}' returned {results} hits ({results / total_count * 100:.5f}% of {total_count})")
