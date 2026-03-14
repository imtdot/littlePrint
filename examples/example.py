#!/usr/bin/env python3
"""
littlePrint Examples
"""

from littlePrint import pr, py, pv, info, success, warning, error, debug

def main():
    """Showcase littlePrint features"""
    
    print("=" * 50)
    print("littlePrint Examples")
    print("=" * 50)
    
    # Basic printing
    pr("Basic printing example")
    pr("Multiple", "arguments", "here", sep=" | ")
    
    # Python info
    py()
    print()
    
    # Get version
    version = pv()
    pr(f"Python version: {version}", color="cyan")
    print()
    
    # Colorful printing
    pr("Red warning", color="red", bold=True)
    pr("Green success", color="green")
    pr("Blue info", color="blue")
    pr("Yellow caution", color="yellow")
    print()
    
    # Convenience functions
    info("This is an informational message")
    success("Operation completed successfully!")
    warning("This is a warning message")
    error("An error occurred!")
    debug("Debug information with timestamp")
    print()
    
    # With timestamp
    pr("Processing started...", timestamp=True, color="magenta")
    
    # Show all Python info
    py(show_all=True)

if __name__ == "__main__":
    main()
