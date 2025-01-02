import os
import shutil

from copystatic import copy_files_recursive
from generate_pages import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
content_from_path = "./content/"
content_to_path = "./public/"
template_path = "template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive(content_from_path, template_path, content_to_path)


main()
