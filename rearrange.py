#!/usr/bin/env python3

import re

def rearrange_name(name):
    name = name.strip()
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
