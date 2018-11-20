#!/usr/bin/env python
import mdfind

query = 'kMDItemContentType==com.apple.web-internet-location'
matches = mdfind.query(query=query)
print("\n".join(matches))
