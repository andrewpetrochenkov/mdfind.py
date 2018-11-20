#!/usr/bin/env python
import mdfind

args = ["-count", "-name", "Downloads"]
out = mdfind.mdfind(args)
print(out)
