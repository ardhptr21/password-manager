import os


def delete_file(file):
    if os.path.exists(file) and os.path.isfile(file):
        os.remove(file)
