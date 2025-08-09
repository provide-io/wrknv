#!/usr/bin/env python3
"""Fix imports from wrkenv.env and wrkenv.env to wrkenv.env"""
import os
import re

def fix_imports_in_file(filepath):
    """Fix imports in a single file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace wrkenv.env and wrkenv.env with wrkenv.env
    original = content
    content = re.sub(r'wrkenv\.workenv', 'wrkenv.env', content)
    content = re.sub(r'wrkenv\.wrkenv', 'wrkenv.env', content)
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Fixed imports in {filepath}")
        return True
    return False

def main():
    """Fix all Python files."""
    fixed_count = 0
    
    # Fix all Python files
    for root, dirs, files in os.walk('/Users/tim/code/gh/provide-io/wrkenv'):
        # Skip .git directory
        if '.git' in root:
            continue
            
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                if fix_imports_in_file(filepath):
                    fixed_count += 1
    
    print(f"\nFixed {fixed_count} files")

if __name__ == '__main__':
    main()