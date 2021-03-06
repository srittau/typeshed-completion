# Legend

Package names in *italics* are not documented in the
[Python 3.8 Library Reference](https://docs.python.org/3.8/library/index.html).

| Completion   | Description |
| ------------ | ----------- |
| *unchecked*  | stub file exists, but has not been checked, yet |
| missing      | stub file needs to be written |
| incomplete   | stub file exists, but some members are missing or have incomplete annotations |
| **3.8**      | stub file exists, has all documented members and complete annotations for the given Python version |

# Completion

| Package                    | Completion    | Notes |
| -------------------------- | ------------- | ----- |
| \_\_future\_\_             | **3.8**       |
| *_ast*                     | incomplete    | missing `excepthandler` and `Constant` |
| *_bisect*                  | *unchecked*   |
| *_codecs*                  | *unchecked*   |
| *_compression*             | incomplete    | missing annotations |
| *_csv*                     | *unchecked*   |
| *_curses*                  | *unchecked*   |
| _dummy_thread              | *unchecked*   |
| *_heapq*                   | *unchecked*   |
| *_imp*                     | *unchecked*   |
| *_importlib_modulespec*    | *unchecked*   |
| *_json*                    | incomplete    | missing annotations |
| *_markupbase*              | *unchecked*   |
| *_msi*                     | **3.8**       |
| *_operator*                | *unchecked*   |
| *_posixsubprocess*         | *unchecked*   |
| *_random*                  | *unchecked*   |
| *_stat*                    | *unchecked*   |
| *_subprocess*              | incomplete    | missing annotations |
| \_thread                   | **3.8**       |
| *_threading_local*         | *unchecked*   |
| *_tracemalloc*             | incomplete    | missing annotations |
| *_warnings*                | *unchecked*   |
| *_weakref*                 | *unchecked*   |
| *_weakrefset*              | *unchecked*   |
| *_winapi*                  | incomplete    | missing annotations |
| abc                        | *unchecked*   |
| aifc                       | missing       |
| *antigravity*              | missing       |
| argparse                   | *unchecked*   |
| array                      | *unchecked*   |
| atexit                     | missing       |
| ast                        | incomplete    | see `_ast` |
| asynchat                   | *unchecked*   |
| asyncio                    | *unchecked*   |
| asyncore                   | *unchecked*   |
| atexit                     | *unchecked*   |
| audioop                    | missing       |
| base64                     | *unchecked*   |
| bdb                        | missing       |
| binascii                   | *unchecked*   |
| binhex                     | *unchecked*   |
| bisect                     | *unchecked*   |
| builtins                   | incomplete    | missing annotations |
| bz2                        | *unchecked*   |
| cProfile                   | *unchecked*   |
| calendar                   | *unchecked*   |
| cgi                        | *unchecked*   |
| cgitb                      | missing       |
| chunk                      | *unchecked*   |
| cmath                      | *unchecked*   |
| cmd                        | *unchecked*   |
| code                       | *unchecked*   |
| codecs                     | *unchecked*   |
| codeop                     | *unchecked*   |
| collections                | *unchecked*   |
| collections.abc            | *unchecked*   |
| colorsys                   | *unchecked*   |
| compileall                 | *unchecked*   |
| concurrent                 | *unchecked*   |
| concurrent.futures         | *unchecked*   |
| configparser               | *unchecked*   |
| contextlib                 | *unchecked*   |
| contextvars                | *unchecked*   |
| copy                       | *unchecked*   |
| copyreg                    | missing       |
| crypt                      | *unchecked*   |
| csv                        | *unchecked*   |
| ctypes                     | *unchecked*   |
| curses                     | *unchecked*   |
| curses.ascii               | missing       |
| curses.panel               | missing       |
| curses.textpad             | missing       |
| dataclasses                | incomplete    | missing annotations |
| datetime                   | *unchecked*   |
| dbm                        | missing       |
| decimal                    | incomplete    | missing annotations |
| difflib                    | *unchecked*   |
| dis                        | *unchecked*   |
| distutils                  | *unchecked*   |
| doctest                    | *unchecked*   |
| dummy_threading            | missing       |
| email                      | *unchecked*   |
| *encodings*                | *unchecked*   |
| ensurepip                  | **3.8**       |
| enum                       | *unchecked*   |
| errno                      | *unchecked*   |
| faulthandler               | **3.8**       |
| fcntl                      | *unchecked*   |
| filecmp                    | *unchecked*   |
| fileinput                  | *unchecked*   |
| fnmatch                    | *unchecked*   |
| fpectl                     | missing       |
| formatter                  | incomplete    | missing annotations |
| fractions                  | incomplete    | missing annotations |
| ftplib                     | *unchecked*   |
| functools                  | *unchecked*   |
| gc                         | *unchecked*   |
| *genericpath*              | **3.8**       |
| getopt                     | *unchecked*   |
| getpass                    | *unchecked*   |
| gettext                    | incomplete    | missing annotations |
| glob                       | *unchecked*   |
| grp                        | *unchecked*   |
| gzip                       | incomplete    | missing annotations |
| hashlib                    | *unchecked*   |
| heapq                      | *unchecked*   |
| hmac                       | *unchecked*   |
| html                       | *unchecked*   |
| html.entities              | *unchecked*   |
| html.parser                | *unchecked*   |
| http                       | incomplete    | missing annotations |
| http.client                | *unchecked*   |
| http.cookiejar             | *unchecked*   |
| http.cookies               | *unchecked*   |
| http.server                | *unchecked*   |
| *idlelib*                  | missing       |
| imaplib                    | *unchecked*   |
| imaplib                    | missing       |
| imghdr                     | **3.8**       |
| imp                        | *unchecked*   |
| importlib                  | *unchecked*   |
| inspect                    | *unchecked*   |
| io                         | *unchecked*   |
| ipaddress                  | *unchecked*   |
| itertools                  | *unchecked*   |
| json                       | *unchecked*   |
| keyword                    | *unchecked*   |
| lib2to3                    | incomplete    | missing several modules |
| linecache                  | *unchecked*   |
| locale                     | *unchecked*   |
| logging                    | *unchecked*   |
| logging.config             | *unchecked*   |
| logging.handlers           | *unchecked*   |
| lzma                       | *unchecked*   |
| macpath                    | incomplete    | missing annotations |
| mailbox                    | missing       |
| mailcap                    | missing       |
| marshal                    | *unchecked*   |
| math                       | *unchecked*   |
| mimetypes                  | *unchecked*   |
| mmap                       | *unchecked*   |
| modulefinder               | missing       |
| msilib                     | **3.8**       |
| msvcrt                     | **3.8**       |
| multiprocessing            | *unchecked*   |
| multiprocessing.shared\_memory | **3.8**      | |
| netrc                      | *unchecked*   |
| nis                        | *unchecked*   |
| nntplib                    | *unchecked*   |
| ntpath                     | incomplete    | missing annotations |
| *nturl2path*               | *unchecked*   |
| numbers                    | incomplete    | missing annotations |
| *opcode*                   | *unchecked*   |
| operator                   | *unchecked*   |
| optparse                   | incomplete    | missing annotations |
| os                         | *unchecked*   |
| os.path                    | *unchecked*   |
| ossaudiodev                | missing       |
| parser                     | missing       |
| pathlib                    | *unchecked*   |
| pdb                        | *unchecked*   |
| pickle                     | *unchecked*   |
| pickletools                | *unchecked*   |
| pipes                      | *unchecked*   |
| pkgutil                    | **3.8**       |
| platform                   | *unchecked*   |
| plistlib                   | *unchecked*   |
| poplib                     | *unchecked*   |
| posix                      | *unchecked*   |
| posixpath                  | incomplete    | missing annotations |
| pprint                     | *unchecked*   |
| profile                    | *unchecked*   |
| pstats                     | *unchecked*   |
| pty                        | *unchecked*   |
| pwd                        | *unchecked*   |
| py_compile                 | *unchecked*   |
| pyclbr                     | *unchecked*   |
| pydoc                      | missing       |
| *pydoc_data*               | missing       |
| *pyexpat*                  | **3.8**       | identical to xml.parsers.expat |
| queue                      | *unchecked*   |
| quopri                     | *unchecked*   |
| random                     | *unchecked*   |
| re                         | incomplete    | missing annotations |
| readline                   | *unchecked*   |
| reprlib                    | *unchecked*   |
| resource                   | *unchecked*   |
| rlcompleter                | *unchecked*   |
| runpy                      | incomplete    | missing annotations |
| sched                      | *unchecked*   |
| secrets                    | *unchecked*   |
| select                     | *unchecked*   |
| selectors                  | *unchecked*   |
| shelve                     | *unchecked*   |
| shlex                      | incomplete    | missing annotations |
| shutil                     | **3.8**       |
| signal                     | incomplete    | missing annotations |
| site                       | *unchecked*   |
| smtpd                      | *unchecked*   |
| smtplib                    | **3.8**       | |
| sndhdr                     | *unchecked*   |
| socket                     | incomplete    | missing annotations |
| socketserver               | *unchecked*   |
| spwd                       | *unchecked*   |
| sqlite3                    | *unchecked*   |
| *sre_compile*              | *unchecked*   |
| *sre_constants*            | incomplete    | missing annotations |
| *sre_parse*                | *unchecked*   |
| ssl                        | *unchecked*   |
| stat                       | incomplete    | missing annotations |
| statistics                 | *unchecked*   |
| string                     | *unchecked*   |
| stringprep                 | *unchecked*   |
| struct                     | *unchecked*   |
| subprocess                 | incomplete    | missing annotations |
| sunau                      | *unchecked*   |
| symbol                     | *unchecked*   |
| symtable                   | *unchecked*   |
| sys                        | *unchecked*   |
| sysconfig                  | *unchecked*   |
| syslog                     | *unchecked*   |
| tabnanny                   | *unchecked*   |
| tarfile                    | *unchecked*   |
| telnetlib                  | *unchecked*   |
| tempfile                   | *unchecked*   |
| termios                    | *unchecked*   |
| test                       | missing       |
| test.support               | missing       |
| textwrap                   | *unchecked*   |
| *this*                     | missing       |
| threading                  | *unchecked*   |
| time                       | *unchecked*   |
| timeit                     | *unchecked*   |
| tkinter                    | incomplete    | missing annotations |
| tkinter.scrolledtext       | missing       |
| tkinter.tix                | missing       |
| tkinter.ttk                | incomplete    | missing annotations |
| token                      | *unchecked*   |
| tokenize                   | *unchecked*   |
| trace                      | *unchecked*   |
| traceback                  | *unchecked*   |
| tracemalloc                | *unchecked*   |
| tty                        | *unchecked*   |
| turtle                     | missing       |
| types                      | *unchecked*   |
| typing                     | incomplete    | missing annotations |
| unicodedata                | *unchecked*   |
| unittest                   | *unchecked*   |
| unittest.mock              | *unchecked*   |
| urllib                     | *unchecked*   |
| urllib.error               | incomplete.   | missing annotations |
| urllib.parse               | incomplete    | missing annotations |
| urllib.request             | incomplete    | missing annotations |
| urllib.response            | *unchecked*   |
| urllib.robotparser         | *unchecked*   |
| uu                         | *unchecked*   |
| uuid                       | *unchecked*   |
| venv                       | missing       |
| warnings                   | *unchecked*   |
| wave                       | *unchecked*   |
| weakref                    | *unchecked*   |
| webbrowser                 | *unchecked*   |
| winreg                     | missing       |
| winsound                   | missing       |
| wsgiref                    | *unchecked*   |
| xdrlib                     | *unchecked*   |
| xml                        | **3.8**       | empty |
| xml.etree.ElementTree      | *unchecked*   |
| xml.dom                    | **3.8**       |
| xml.dom.minidom            | incomplete    | marked incomplete |
| xml.dom.pulldom            | incomplete    | marked incomplete |
| xml.parsers.expat          | **3.8**       |
| xml.sax                    | incomplete    | missing annotations |
| xml.sax.handler            | incomplete    | missing annotations |
| xml.sax.saxutils           | incomplete    | missing annotations |
| xml.sax.xmlreader          | incomplete    | missing annotations |
| xmlrpc                     | missing       |
| xmlrpc.client              | missing       |
| xmlrpc.server              | missing       |
| zipapp                     | *unchecked*   |
| zipfile                    | incomplete    | missing at least `ZipExtFile` |
| zipimport                  | *unchecked*   |
| zlib                       | *unchecked*   |
