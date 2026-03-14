#!/usr/bin/env python3
"""
littlePrint Command Line Interface
"""

import sys
import argparse
from .core import pr, py, pv, info, success, warning, error

def main():
    """Command line entry point"""
    parser = argparse.ArgumentParser(
        description='littlePrint - A tiny print utility for Python',
        epilog='Examples:\n'
               '  python -m littlePrint "Hello World"\n'
               '  python -m littlePrint py\n'
               '  python -m littlePrint info "Processing data"\n'
               '  lprint "Hello from command line"',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # print command
    print_parser = subparsers.add_parser('print', help='Print text (alias: pr)')
    print_parser.add_argument('text', nargs='+', help='Text to print')
    print_parser.add_argument('--color', help='Text color')
    print_parser.add_argument('--bold', action='store_true', help='Bold text')
    print_parser.add_argument('--timestamp', action='store_true', help='Add timestamp')
    
    # pr command (alias for print)
    pr_parser = subparsers.add_parser('pr', help='Print text (shortcut)')
    pr_parser.add_argument('text', nargs='+', help='Text to print')
    pr_parser.add_argument('--color', help='Text color')
    pr_parser.add_argument('--bold', action='store_true', help='Bold text')
    
    # py command
    py_parser = subparsers.add_parser('py', help='Show Python info')
    py_parser.add_argument('-a', '--all', action='store_true', 
                          help='Show all details')
    py_parser.add_argument('-s', '--simple', action='store_true',
                          help='Show only version number')
    
    # pv command
    pv_parser = subparsers.add_parser('pv', help='Show Python version only')
    
    # Special commands
    for cmd_name, cmd_func in [('info', info), ('success', success), 
                               ('warning', warning), ('error', error)]:
        cmd_parser = subparsers.add_parser(cmd_name, 
                                         help=f'Print {cmd_name} message')
        cmd_parser.add_argument('message', help='Message text')
    
    # If no arguments, print help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    # Handle commands
    if args.command in ['print', 'pr']:
        pr(*args.text, color=args.color, bold=args.bold, 
           timestamp=getattr(args, 'timestamp', False))
    
    elif args.command == 'py':
        py(show_all=args.all, simple=args.simple)
    
    elif args.command == 'pv':
        print(pv())
    
    elif args.command == 'info':
        info(args.message)
    
    elif args.command == 'success':
        success(args.message)
    
    elif args.command == 'warning':
        warning(args.message)
    
    elif args.command == 'error':
        error(args.message)

if __name__ == '__main__':
    main()
