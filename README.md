[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/mdfind.svg?longCache=True)](https://pypi.org/pypi/mdfind/)
[![](https://img.shields.io/pypi/v/mdfind.svg?maxAge=3600)](https://pypi.org/pypi/mdfind/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mdfind.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mdfind.py/)

#### Install
```bash
$ [sudo] pip install mdfind
```

#### Functions
function|description
-|-
`mdfind.count(query=None, name=None, onlyin=None)`|return search results count
`mdfind.mdfind(args)`|execute mdfind with arguments
`mdfind.name(name, onlyin=None)`|`mdfind -name name` search by name
`mdfind.query(query, onlyin=None)`|search by Spotlight query

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>