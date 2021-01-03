import argparse
from PIL import Image
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument('dir', type=str, help="The directory where the webp files reside")

args = parser.parse_args()
webp_dir = args.dir

if not os.path.isdir(webp_dir):
    print(f"ERROR: directory {webp_dir} does not exist")
    sys.exit(1)

for f_path in os.listdir(webp_dir):
    if f_path.endswith(".webp"):
        f_name, _ = f_path.rsplit(".", maxsplit=1)
        out_f_path = os.path.join(webp_dir, f_name + ".jpg")
        in_f_path = os.path.join(webp_dir, f_path)
        try:
            with Image.open(in_f_path) as im:
                im.convert("RGB")
                im.save(out_f_path, 'jpeg')
        except Exception as e:
            print(f"ERROR: can't convert file {in_f_path}")
            print(e)
