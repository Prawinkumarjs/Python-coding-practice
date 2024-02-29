# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts

import messages
import messages as msg
from messages import hello, bye
# from messages import *     # these are type of representation

messages.hello()
messages.bye()

msg.hello()
msg.bye()

hello()
bye()

help("modules")
# for help assistance python contain many more modules that are listed below

"""
Please wait a moment while I gather a list of all available modules...

test_sqlite3: testing with SQLite version 3.43.1
Day23(3)            _testinternalcapi   gc                  runpy
__future__          _testmultiphase     genericpath         sched
__hello__           _testsinglephase    getopt              secrets
__phello__          _thread             getpass             select
_abc                _threading_local    gettext             selectors
_aix_support        _tkinter            glob                setuptools
_ast                _tokenize           graphlib            shelve
_asyncio            _tracemalloc        gzip                shlex
_bisect             _typing             hashlib             shutil
_blake2             _uuid               heapq               signal
_bz2                _virtualenv         hmac                site
_codecs             _warnings           html                smtplib
_codecs_cn          _weakref            http                sndhdr
_codecs_hk          _weakrefset         idlelib             socket
_codecs_iso2022     _winapi             imaplib             socketserver
_codecs_jp          _wmi                imghdr              sqlite3
_codecs_kr          _xxinterpchannels   importlib           sre_compile
_codecs_tw          _xxsubinterpreters  inspect             sre_constants
_collections        _zoneinfo           io                  sre_parse
_collections_abc    abc                 ipaddress           ssl
_compat_pickle      aifc                itertools           stat
_compression        antigravity         json                statistics
_contextvars        argparse            keyword             string
_csv                array               lib2to3             stringprep
_ctypes             ast                 linecache           struct
_ctypes_test        asyncio             locale              subprocess
_datetime           atexit              logging             sunau
_decimal            audioop             lzma                symtable
_distutils_hack     base64              mailbox             sys
_elementtree        bdb                 mailcap             sysconfig
_functools          binascii            marshal             tabnanny
_hashlib            bisect              math                tarfile
_heapq              builtins            messages            telnetlib
_imp                bz2                 mimetypes           tempfile
_io                 cProfile            mmap                test
_json               calendar            modulefinder        textwrap
_locale             cgi                 msilib              this
_lsprof             cgitb               msvcrt              threading
_lzma               chunk               multiprocessing     time
_markupbase         cmath               netrc               timeit
_md5                cmd                 nntplib             tkinter
_msi                code                nt                  token
_multibytecodec     codecs              ntpath              tokenize
_multiprocessing    codeop              nturl2path          tomllib
_opcode             collections         numbers             trace
_operator           colorsys            opcode              traceback
_osx_support        compileall          operator            tracemalloc
_overlapped         concurrent          optparse            tty
_pickle             configparser        os                  turtle
_py_abc             contextlib          pathlib             turtledemo
_pydatetime         contextvars         pdb                 types
_pydecimal          copy                pickle              typing
_pyio               copyreg             pickletools         unicodedata
_pylong             crypt               pip                 unittest
_queue              csv                 pipes               urllib
_random             ctypes              pkg_resources       uu
_sha1               curses              pkgutil             uuid
_sha2               dataclasses         platform            venv
_sha3               datetime            plistlib            warnings
_signal             dbm                 poplib              wave
_sitebuiltins       decimal             posixpath           weakref
_socket             difflib             pprint              webbrowser
_sqlite3            dis                 profile             wheel
_sre                doctest             pstats              winreg
_ssl                email               pty                 winsound
_stat               encodings           py_compile          wsgiref
_statistics         ensurepip           pyclbr              xdrlib
_string             enum                pydoc               xml
_strptime           errno               pydoc_data          xmlrpc
_struct             faulthandler        pyexpat             xxsubtype
_symtable           filecmp             queue               zipapp
_testbuffer         fileinput           quopri              zipfile
_testcapi           fnmatch             random              zipimport
_testclinic         fractions           re                  zlib
_testconsole        ftplib              reprlib             zoneinfo
_testimportmultiple functools           rlcompleter         

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

"""
