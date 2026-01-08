#!/usr/bin/env python3
"""
Initialize a new skill directory with template structure.

Usage:
    python scripts/init_skill.py <skill-name> --path <output-directory>

Creates a skill directory with:
- SKILL.md with frontmatter template
- Example directories: scripts/, references/, assets/
- Example files in each directory
"""

import sys
import os
from pathlib import Path


SKILL_MD_TEMPLATE = """---
name: {skill_name}
description: TODO - Describe what this skill does and when to use it (be comprehensive - this is the primary trigger mechanism)
---

# {skill_name}

TODO: Write instructions for using this skill.

## Overview

TODO: Brief description of what this skill helps with.

## Usage

TODO: Explain how to use this skill and its resources.

## Resources

- **Scripts**: See `scripts/` for executable code
- **References**: See `references/` for documentation
- **Assets**: See `assets/` for templates and output files
"""

EXAMPLE_SCRIPT = """#!/usr/bin/env python3
\"\"\"
Example script - replace or delete this file.
\"\"\"

def main():
    print("This is an example script")

if __name__ == "__main__":
    main()
"""

EXAMPLE_REFERENCE = """# Example Reference

Replace or delete this file.

This is an example reference file that would contain:
- Documentation
- API specifications
- Database schemas
- Domain knowledge
- Detailed workflow guides

Reference files are loaded into context only when Claude determines they're needed.
"""

EXAMPLE_ASSET_README = """# Assets Directory

This directory contains files used in output (not loaded into context):
- Templates
- Images/icons
- Boilerplate code
- Fonts
- Sample documents

These files get copied or modified in the final output.
"""


def init_skill(skill_name, output_path):
    """Initialize a new skill directory."""
    skill_path = Path(output_path) / skill_name
    
    # Check if directory already exists
    if skill_path.exists():
        print(f"Error: Directory already exists: {skill_path}")
        sys.exit(1)
    
    print(f"Creating skill: {skill_name}")
    print(f"Location: {skill_path}\n")
    
    # Create main directory
    skill_path.mkdir(parents=True)
    print(f"✓ Created {skill_path}")
    
    # Create SKILL.md
    skill_md = skill_path / "SKILL.md"
    with open(skill_md, 'w') as f:
        f.write(SKILL_MD_TEMPLATE.format(skill_name=skill_name))
    print(f"✓ Created {skill_md.name}")
    
    # Create scripts directory with example
    scripts_dir = skill_path / "scripts"
    scripts_dir.mkdir()
    example_script = scripts_dir / "example_script.py"
    with open(example_script, 'w') as f:
        f.write(EXAMPLE_SCRIPT)
    os.chmod(example_script, 0o755)
    print(f"✓ Created {scripts_dir.name}/ with example_script.py")
    
    # Create references directory with example
    references_dir = skill_path / "references"
    references_dir.mkdir()
    example_ref = references_dir / "example_reference.md"
    with open(example_ref, 'w') as f:
        f.write(EXAMPLE_REFERENCE)
    print(f"✓ Created {references_dir.name}/ with example_reference.md")
    
    # Create assets directory with README
    assets_dir = skill_path / "assets"
    assets_dir.mkdir()
    assets_readme = assets_dir / "README.md"
    with open(assets_readme, 'w') as f:
        f.write(EXAMPLE_ASSET_README)
    print(f"✓ Created {assets_dir.name}/ with README.md")
    
    print(f"\n✓ Skill initialized successfully!")
    print(f"\nNext steps:")
    print(f"1. Edit {skill_md.name} - update frontmatter and add instructions")
    print(f"2. Add your scripts, references, and assets")
    print(f"3. Delete example files you don't need")
    print(f"4. Package with: python scripts/package_skill.py {skill_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/init_skill.py <skill-name> --path <output-directory>")
        print("\nExample:")
        print("  python scripts/init_skill.py my-skill --path ./skills")
        sys.exit(1)
    
    skill_name = sys.argv[1]
    
    # Parse --path argument
    output_path = "."
    if "--path" in sys.argv:
        path_index = sys.argv.index("--path")
        if path_index + 1 < len(sys.argv):
            output_path = sys.argv[path_index + 1]
        else:
            print("Error: --path requires a directory argument")
            sys.exit(1)
    
    init_skill(skill_name, output_path)


if __name__ == "__main__":
    main()

