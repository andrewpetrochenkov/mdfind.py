#!/usr/bin/env python
import mdfind

name = "Downloads"
matches = mdfind.name(name=name)
print("\n".join(matches))
