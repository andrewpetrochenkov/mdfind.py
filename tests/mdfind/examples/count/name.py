#!/usr/bin/env python
import mdfind
import tests_os.mac

name="Downloads"
count = mdfind.count(name=name)
print(count)
