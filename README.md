PyShell - Modular UNIX-like Shell in Python
Overview
PyShell is a simple UNIX-like command-line shell implemented entirely in Python using the standard library. The shell supports common directory, file, and utility commands and follows a modular architecture where each command is implemented as a separate Python module.

The project demonstrates:

Dynamic module importing
Command-line parsing
File and directory operations
Modular software design
Exception handling
Python standard library usage
Project Structure
PyShellProject/
│
├── pyshell.py
├── hello.txt
│
└── commands/
    ├── __init__.py
    ├── ls.py
    ├── mkdir.py
    ├── pwd.py
    ├── rmdir.py
    ├── cd.py
    ├── cat.py
    ├── cp.py
    ├── rm.py
    ├── mv.py
    ├── grep.py
    ├── head.py
    ├── tail.py
    ├── sizeof.py
    ├── search.py
    ├── date.py
    ├── whoami.py
    ├── hostname.py
    ├── timeit.py
    └── exit.py
Features
Directory Commands
Command	Description
ls	List files and directories
mkdir	Create a directory
pwd	Print current working directory
cd	Change directory
rmdir	Remove an empty directory
File Commands
Command	Description
cat	Display file contents
cp	Copy files
rm	Remove files or directories
mv	Move or rename files
grep	Search text in files
head	Display first N lines
tail	Display last N lines
sizeof	Display file size in bytes
search	Search for files recursively
Miscellaneous Commands
Command	Description
date	Display current date and time
whoami	Display current user
hostname	Display system hostname
timeit	Measure command execution time
exit	Exit the shell
Architecture
The shell uses dynamic importing to load commands at runtime.

When a user enters a command:

PyShell> ls
The shell dynamically imports:

commands.ls
and executes:

run(args)
Every command module contains a run() function.

Example:

def run(args):
    print("Command executed")
This makes the shell scalable and easy to extend.

To add a new command:

Create a new Python file in the commands folder.
Implement a run() function.
Execute the command directly from PyShell.
No changes are required in the main shell program.

Running the Project
Navigate to the project directory:

cd PyShellProject
Run:

python pyshell.py
Usage Examples
List Files
PyShell> ls
hello.txt commands pyshell.py
Create Directory
PyShell> mkdir demo
Change Directory
PyShell> cd demo
Print Working Directory
PyShell> pwd
Copy File
PyShell> cp hello.txt copy.txt
Search Text
PyShell> grep -n Hello hello.txt
Search File
PyShell> search --in=. --file=hello.txt
Measure Execution Time
PyShell> timeit cp hello.txt temp.txt
Technologies Used
Python 3
importlib
os
shutil
datetime
socket
getpass
time
Learning Outcomes
This project helped in understanding:

Modular programming
Dynamic imports using importlib
File handling in Python
Directory management
Exception handling
Command parsing
Recursive file searching
Software scalability and maintainability


Author


Anuj Kumar Yadav
