<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mdfind.svg?maxAge=3600)](https://pypi.org/project/mdfind/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mdfind.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mdfind.py/actions)

### Installation
```bash
$ [sudo] pip install mdfind
```

#### Examples
```python
>>> import mdfind
>>> mdfind.name('Group Containers')
['/Users/username/Library/Group Containers']
```

```python
>>> mdfind.query('kMDItemContentType==public.shell-script')
[...]
```

```python
>>> mdfind.count(query='kMDItemContentType==public.mp3')
42
>>> mdfind.count(name='Group Containers')
1
```

```python
>>> mdfind.mdfind(['-count','-onlyin','/usr','kMDItemContentType==public.shell-script'])
42
```

#### Links
+   [File Metadata Query Expression Syntax](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
