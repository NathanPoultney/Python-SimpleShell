# Python SimpleShell

A lightweight, customisable command-line interface built with Python.

## Features

- Custom prompt showing username, hostname, and current directory
- Built-in commands (`cd`, `help`, `exit`)
- System command execution
- Cross-platform compatibility
- Error handling for common issues

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/NathanPoultney/simpleshell.git
   cd simpleshell
   ```

2. No additional dependencies required - uses Python standard library only.

## Usage

### Linux/MacOS
```bash
# Make the script executable
chmod +x simple_shell.py

# Run the shell
./simple_shell.py
```

### Windows
Simply double-click the `run_shell.bat` file or run it from the command prompt:
```
run_shell.bat
```

## Examples

### Basic Navigation
```
user@localhost:/home/user$ cd /tmp
user@localhost:/tmp$ cd ..
user@localhost:/$ cd
user@localhost:/home/user$
```

### Running System Commands

#### Linux/MacOS
```
user@localhost:/home/user$ ls -la
total 20
drwxr-xr-x 3 user user 4096 May 16 12:34 .
drwxr-xr-x 5 root root 4096 May 16 12:00 ..
-rw-r--r-- 1 user user  220 May 16 12:00 .bash_logout
-rw-r--r-- 1 user user 3771 May 16 12:00 .bashrc
-rw-r--r-- 1 user user  807 May 16 12:00 .profile
```

#### Windows
```
user@localhost:C:\Users\user$ dir
 Volume in drive C has no label.
 Volume Serial Number is 1234-5678

 Directory of C:\Users\user

05/16/2025  12:34 PM    <DIR>          .
05/16/2025  12:00 PM    <DIR>          ..
05/16/2025  12:00 PM             1,543 example.txt
05/16/2025  12:15 PM    <DIR>          Documents
               1 File(s)          1,543 bytes
               3 Dir(s)  256,123,456 bytes free

user@localhost:C:\Users\user$ echo Hello from SimpleShell
Hello from SimpleShell

user@localhost:C:\Users\user$ ipconfig
Windows IP Configuration

Ethernet adapter Ethernet:
   Connection-specific DNS Suffix  . : example.com
   IPv4 Address. . . . . . . . . . . : 192.168.1.100
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
```

### Built-in Help
```
user@localhost:/home/user$ help
Available commands:
  cd: Change the current working directory
  exit: Exit the shell
  help: Show available commands
  Any other input will be executed as a system command
```

## Windows Command Examples

For Windows users, here are additional commands you can try:

```
# List directory contents
dir

# Echo text to console
echo Hello from SimpleShell

# View system information
systeminfo

# Display network configuration
ipconfig

# List running processes
tasklist
```

## Extending the Shell

You can easily add custom commands by extending the `commands` dictionary in the `SimpleShell` class:

```python
def __init__(self):
    self.running = True
    self.commands = {
        'cd': self.change_directory,
        'exit': self.exit_shell,
        'help': self.show_help,
        'mycommand': self.my_custom_function
    }

def my_custom_function(self, args):
    """Description of my custom command"""
    # Your implementation here
    print("Custom command executed with args:", args)
```

## License

MIT License - Feel free to modify and distribute as needed.

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.