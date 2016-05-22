# Tuesday - Modules, PIP, IO

## Before lesson materials

Mandatory:

* https://www.youtube.com/watch?v=YV6qm6erphk
* https://www.youtube.com/watch?v=WN4A6iJOUns
* [General introduction to modules][1]
* [General introduction to file handling / IO][2]

## Assignment Review
- `open()` and parameters `r, w, a`
- `close()`
- `write()`
- `read()`, `readline()` and `readlines()`
- `module` and `submodule`
- `import`
- `from`
- `help()`
- OS module
- Requests module

## Tasks
- First of all, you should copy all files to your working directory from
    - `01-io` and
    - `02-pip` folders
- You can see all the tasks there, with a prepared skeleton to work in
- The reason for that is so you can check your work with tests
- There's a `test.py` in every corresponding folder, try and run it
- The only thing matters from here is to get these to pass :)

### I/O

`my_file = open("file_name.txt", "r")`

4 different ways of reading:

`my_file.read()`

`my_file.readline()`

`my_file.readlines()`

```
for line in my_file:
      print(line.rstrip())
```

` >>> help(str.rstrip) `

`split()`

`" ".join()`

`my_list[start:end:step]`

`ord('a')`

`chr(97)`

### Modules

#### CSV built-in module

[CSV - The Python Standard Library Docs][10]

#### Lottery

Print the five most frequent numbers and how many times they have occurred!

### PIP

PIP is a tool for installing packages from the Python Package Index.

`pip3 --version` /// `pip --version`

Install an external package

[PrettyTable][7]
[PrettyTable short tutorial][9]

`pip3 install prettytable` /// `pip install prettytable`

## References

* [The Python Standard Library][3]
* [Python Module Index][4]
* [PyPI - the Python Package Index][5]
* [Find famous Python modules and authors][6]
* [A curated list of awesome Python packages][8]

[1]: http://pymbook.readthedocs.org/en/latest/modules.html
[2]: http://pymbook.readthedocs.org/en/latest/file.html
[3]: https://docs.python.org/3/library/
[4]: https://docs.python.org/3/py-modindex.html
[5]: https://pypi.python.org/pypi
[6]: http://pypi-ranking.info/
[7]: https://pypi.python.org/pypi/PrettyTable
[8]: http://awesome-python.com/
[9]: https://code.google.com/p/prettytable/wiki/Tutorial
[10]: https://docs.python.org/3/library/csv.html
