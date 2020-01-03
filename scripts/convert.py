#!/usr/bin/env python3
#
# QUALINET DB Conversion Script.
#
# Author: Werner Robitza
#
# Requirements:
# * Python 3.7
# * pip3 install stringcase pandas tqdm
#
# Under macOS you need:
#
#    export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
#
# License: MIT


import pandas as pd
import os
import argparse
import stringcase
import yaml
import sys
import math
import re
from tqdm import tqdm
import urllib.request
import multiprocessing

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def url_is_deprecated(url):
    tqdm.write(f"Testing URL {url}")
    try:
        response = urllib.request.urlopen(url).getcode()
        return response not in [200, 301, 302]
    except Exception as e:
        print(f"Error fetching {url}")
        return True


def create_post(args):
    data, filename = args
    # print(data)
    data = data.fillna("")

    try:
        email = re.findall(r'[\w\.-]+@[\w\.-]+', data.Contacts)[0]
    except Exception as e:
        email = ""
        pass

    references = {}
    if len(data.References):
        for ref in data.References.strip().replace("\n\n", "\n").split("\n"):
            ref_key, ref_text = ref.split(" ", 1)
            ref_key = ref_key.replace("[", "").replace("]", "")
            ref_text = ref_text.replace("\n", " ")
            references[ref_key] = ref_text

    tags = []
    type_str = data.Type.replace("Audio+Video", "Audiovisual")
    type_str = type_str.replace("+", ",")
    type_str = type_str.replace("Images", "Image")
    for extra_type in ["HDR", "Point Cloud", "3D"]:
        if extra_type in type_str:
            tags.append(extra_type)
            type_str = type_str.replace(extra_type, "")
    tags.extend([s.strip() for s in type_str.split(",")])
    tags = [t.lower() for t in tags]
    # if len(data.Other):
    #     tags.append(data.Other)

    categories = []
    for category_name in "audio", "video", "image", "audiovisual":
        if category_name in tags:
            categories.append(category_name)

    access = data["Access (visible only to Qualinet partner or to all users if PUBLICLY AVAILABLE)"].replace("\n", " ").strip()

    total = int(data.Total) if data.Total != "" else None
    src = int(data.SRC) if data.SRC != "" else None
    hrc = int(data.HRC) if data.HRC != "" else None
    ratings = int(data.Ratings) if data.Ratings != "" else None

    if data.Link != "" and not data.Link.startswith("ftp"):
        deprecated = url_is_deprecated(data.Link)
    else:
        deprecated = False

    yaml_data = {
        "title": data.Database,
        "database": data.Database,
        "categories": categories,
        "author": data.Institution,
        "partner": data["Qualinet Partner"] == "YES",
        "external_link": data.Link,
        "deprecated": deprecated,
        "access": access,
        "publicly_available": data["Publicly available"] == "YES",
        "citation": data.Citation.replace("\n", " "),
        "license": data.Copyright.replace("\n", " "),
        "contact_name": data.Contacts.replace("\n", " "),
        # "contact_email": email,
        "contact_email": None,
        "tags": tags,
        "other": data.Other,
        "subjective_scores": data.MOS == "YES",
        "total": total,
        "src": src,
        "hrc": hrc,
        "ratings": ratings,
        "resolution": data.Resolution,
        "method": data.Method,
    }

    if references:
        yaml_data["references"] = references

    # remove all empty keys
    yaml_data = {k: v for k, v in yaml_data.items() if v not in [None, ""]}

    # do add empty excerpt
    yaml_data["excerpt"] = ""

    # print(yaml.dump(yaml_data))
    body = data.Description

    with open(filename, "w") as out_f:
        out_f.write("---\n")
        out_f.write(yaml.dump(yaml_data))
        out_f.write("---\n\n")
        out_f.write(body)


def create_posts(input_file, output_path, specific_index=None, parallel=False):
    df = pd.read_excel(input_file)
    print(f"Got {df.shape[0]} rows")

    args = []

    for index, row in df.iterrows():
        if specific_index and (index + 1) != int(specific_index):
            print(f"skipping index {index}")
            continue

        # print(f"Extracting row {index + 1}")
        filename = "-".join([
            "2020-01-01",
            re.sub(r"\W+", "", stringcase.snakecase(row.Database.lower().replace("  ", " ")))
        ]) + ".md"
        output_file_path = os.path.join(output_path, filename)
        args.append((row, output_file_path))

    if parallel:
        pool = multiprocessing.Pool(multiprocessing.cpu_count())
        results = list(tqdm(pool.imap(create_post, args), total=len(args)))
    else:
        for arg in tqdm(args):
            create_post(arg)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    parser.add_argument(
        "-o", "--output", help="output path", default=os.path.join(ROOT_PATH, "_posts")
    )
    parser.add_argument(
        "-i", "--index", help="only convert specific index"
    )
    parser.add_argument(
        "-p", "--parallel", help="parallel processing", action="store_true"
    )
    args = parser.parse_args()

    create_posts(args.input, args.output, args.index, args.parallel)


if __name__ == "__main__":
    main()
