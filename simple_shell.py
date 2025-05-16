#!/usr/bin/env python3
import os
import subprocess
import shlex
import sys

class SimpleShell:
    def __init__(self):
        self.running = True
        self.commands = {
            'cd': self.change_directory,
            'exit': self.exit_shell,
            'help': self.show_help
        }
    
    def show_prompt(self):
        cwd = os.getcwd()
        username = os.getenv('USER', 'user')
        hostname = os.getenv('HOSTNAME', 'localhost')
        return f"{username}@{hostname}:{cwd} -> "
    
    def change_directory(self, args):
        """Change the current working directory"""
        if not args:
            # Default to home directory if no path provided
            home_dir = os.path.expanduser("~")
            os.chdir(home_dir)
        else:
            try:
                os.chdir(args[0])
            except FileNotFoundError:
                print(f"Directory not found: {args[0]}")
            except PermissionError:
                print(f"Permission denied: {args[0]}")
    
    def exit_shell(self, args):
        """Exit the shell"""
        self.running = False
        return "Goodbye!"
    
    def show_help(self, args):
        """Show available commands"""
        print("Available commands:")
        for cmd, func in self.commands.items():
            print(f"  {cmd}: {func.__doc__}")
        print("  Any other input will be executed as a system command")
    
    def execute_command(self, command_line):
        """Execute the given command"""
        if not command_line.strip():
            # Empty command, just show the prompt again
            return
            
        # Split the command line into command and arguments
        tokens = shlex.split(command_line)
        command = tokens[0]
        args = tokens[1:] if len(tokens) > 1 else []
        
        # Check if it's a built-in command
        if command in self.commands:
            return self.commands[command](args)
        
        # Otherwise, execute as a system command
        try:
            # Use shell=True on Windows for built-in commands like 'dir'
            if os.name == 'nt':
                process = subprocess.run(command_line, shell=True)
            else:
                process = subprocess.run(tokens, capture_output=False)
                
            if process.returncode != 0:
                print(f"Command exited with status {process.returncode}")
        except FileNotFoundError:
            print(f"Command not found: {command}")
        except PermissionError:
            print(f"Permission denied: {command}")
        except Exception as e:
            print(f"Error executing command: {e}")
    
    def run(self):
        """Main shell loop"""
        print("Simple Python Shell. Type 'help' for available commands.")
        
        while self.running:
            try:
                command = input(self.show_prompt())
                self.execute_command(command)
            except KeyboardInterrupt:
                print("\nUse 'exit' to exit the shell")
            except EOFError:
                self.running = False
                print("\nGoodbye!")

if __name__ == "__main__":
    shell = SimpleShell()
    shell.run()