import re


def extract_file_name(dirty_file_name):
    return re.search("(_[A-z-]*.{1}[A-z\d]*)", dirty_file_name).group(1)[1:]
