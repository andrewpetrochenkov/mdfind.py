#!/usr/bin/env python
import mdfind

query = 'kMDItemContentType==public.mp3'
count = mdfind.count(query=query)
print(count)
