#!/usr/bin/env python3
"""
littlePrint Core Module
"""

import sys
import platform
import datetime
from typing import Any, Optional

# ANSI color codes for colorful output
COLORS = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bright_black': '\033[90m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
    'bright_magenta': '\033[95m',
    'bright_cyan': '\033[96m',
    'bright_white': '\033[97m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italic': '\033[3m',
    'underline': '\033[4m',
}

def pr(*args: Any, 
       sep: str = ' ', 
       end: str = '\n', 
       file=None, 
       flush: bool = False,
       color: Optional[str] = None,
       bold: bool = False,
       timestamp: bool = False) -> None:
    """
    Print with style - A better print function
    
    Args:
        *args: Values to print
        sep: Separator between values
        end: End of line character
        file: File to write to (default: sys.stdout)
        flush: Whether to flush the stream
        color: Text color (see COLORS dictionary)
        bold: Whether to make text bold
        timestamp: Add timestamp prefix
    
    Examples:
        >>> pr("Hello World!")
        Hello World!
        
        >>> pr("Error!", color="red", bold=True)
        Error! (in red bold)
        
        >>> pr("Processing...", timestamp=True)
        [14:30:25] Processing...
    """
    if file is None:
        file = sys.stdout
    
    # Prepare output string
    output = sep.join(str(arg) for arg in args)
    
    # Add timestamp if requested
    if timestamp:
        now = datetime.datetime.now()
        timestamp_str = f"[{now.strftime('%H:%M:%S')}] "
        output = timestamp_str + output
    
    # Apply styling
    if color or bold:
        style = ""
        if bold:
            style += COLORS['bold']
        if color and color in COLORS:
            style += COLORS[color]
        
        output = style + output + COLORS['reset']
    
    # Print
    print(output, sep='', end=end, file=file, flush=flush)


def py(show_all: bool = False, 
       simple: bool = False) -> None:
    """
    Show Python information
    
    Args:
        show_all: Show all detailed information
        simple: Show only version in simple format
    
    Examples:
        >>> py()
        🐍 Python 3.11.0
        
        >>> py(simple=True)
        3.11.0
        
        >>> py(show_all=True)
        ===== Python Details =====
        ...
    """
    version_info = sys.version.split()[0]
    
    if simple:
        print(version_info)
        return
    
    if show_all:
        print("=" * 40)
        print(f"{COLORS['bold']}{COLORS['cyan']}🐍 Python Information{COLORS['reset']}")
        print("=" * 40)
        print(f"{COLORS['bold']}Version:{COLORS['reset']} {version_info}")
        print(f"{COLORS['bold']}Implementation:{COLORS['reset']} {platform.python_implementation()}")
        print(f"{COLORS['bold']}Compiler:{COLORS['reset']} {platform.python_compiler()}")
        print(f"{COLORS['bold']}Build:{COLORS['reset']} {platform.python_build()[0]}")
        print(f"{COLORS['bold']}Executable:{COLORS['reset']} {sys.executable}")
        print(f"{COLORS['bold']}Platform:{COLORS['reset']} {platform.platform()}")
        print(f"{COLORS['bold']}System:{COLORS['reset']} {platform.system()} {platform.release()}")
        print(f"{COLORS['bold']}Architecture:{COLORS['reset']} {platform.architecture()[0]}")
        print(f"{COLORS['bold']}Current Time:{COLORS['reset']} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 40)
    else:
        print(f"{COLORS['green']}🐍 Python {version_info}{COLORS['reset']}")


def pv() -> str:
    """
    Get Python version as string
    
    Returns:
        Python version string
    
    Examples:
        >>> version = pv()
        >>> print(version)
        3.11.0
    """
    return sys.version.split()[0]


def lprint(*args: Any, **kwargs: Any) -> None:
    """
    Alias for pr() - littlePrint's main function
    
    This is the same as pr() but with a different name.
    """
    pr(*args, **kwargs)


def info(message: str) -> None:
    """Print informational message"""
    pr(f"[INFO] {message}", color="cyan")


def success(message: str) -> None:
    """Print success message"""
    pr(f"[✓] {message}", color="green", bold=True)


def warning(message: str) -> None:
    """Print warning message"""
    pr(f"[!] {message}", color="yellow", bold=True)


def error(message: str) -> None:
    """Print error message"""
    pr(f"[✗] {message}", color="red", bold=True)


def debug(message: str) -> None:
    """Print debug message with timestamp"""
    pr(f"[DEBUG] {message}", color="magenta", timestamp=True)
