#!/usr/bin/env python3


from pathlib import Path
import shutil
from string import Template


CURRENT_PATH = Path.cwd()

INPUT_PATH = CURRENT_PATH / "input"

OUTPUT_PATH = CURRENT_PATH / "output"
IMG_PATH = OUTPUT_PATH / "img"

TEMPLATE_PATH = CURRENT_PATH / "templates"
TEMPLATE_INDEX_PATH = TEMPLATE_PATH / "index.html"
OUTPUT_INDEX_PATH = OUTPUT_PATH / "index.html"
TEMPLATE_ROW_PATH = TEMPLATE_PATH / "row.html"

ASSETS_PATH = CURRENT_PATH / "assets"
OUTPUT_ASSETS_PATH = OUTPUT_PATH / "assets"


# clean output dir
shutil.rmtree(OUTPUT_PATH, ignore_errors=True)
OUTPUT_PATH.mkdir()

# copy mages and assets
shutil.copytree(INPUT_PATH, IMG_PATH)
shutil.copytree(ASSETS_PATH, OUTPUT_ASSETS_PATH)

# collect image paths, assuming all non-hidden files
path = Path(INPUT_PATH).glob("**/[!.]*")
images = sorted([element for element in path if element.is_file()])


# generate table, populate and write index page
with open(TEMPLATE_ROW_PATH) as row_file:
    # generate table HTML
    row_template = Template(row_file.read())
    rows = [
        row_template.substitute(image_name=image.name, image_stem=image.stem)
        for image in images
    ]
    table = "".join(rows)

    # generate index page
    with open(TEMPLATE_INDEX_PATH) as index_file:
        template = Template(index_file.read())
        contents = template.substitute(table_body=table)

        # save output/index.html
        with open(OUTPUT_INDEX_PATH, "w") as index_file:
            index_file.write(contents)
