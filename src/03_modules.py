"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
# print(dir(sys))
# output: ['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_git', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions']

# Print out the OS platform you're using:
# YOUR CODE HERE
# print(sys.platform)
# output: darwin

# Print out the version of Python you're using:
# YOUR CODE HERE
# print(sys.version)
# output: 2.7.16 (default, Jul  5 2020, 02:24:03) [GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.21) (-macos10.15-objc-

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# print(dir(os))
# Print the current process ID
# YOUR CODE HERE
# print(os.getpid())

# output: 28638

# Print the current working directory (cwd):
# YOUR CODE HERE
# print(os.getcwd())
# output: /Users/chaycesolchaga/Desktop/Lambda/CS/python-basics/Intro-Python-I

# Print out your machine's login name
# YOUR CODE HERE

# print(os.uname())
# output: ('Darwin', 'Chayces-Air.lan1', '19.6.0', 'Darwin Kernel Version 19.6.0: Sun Jul  5 00:43:10 PDT 2020; root:xnu-6153.141.1~9/RELEASE_X86_64', 'x86_64')