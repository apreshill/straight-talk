#!/usr/bin/env python3
"""
Package a skill directory into a distributable .skill file.

Usage:
    python scripts/package_skill.py <path/to/skill-folder> [output-directory]

The script validates the skill structure and creates a .skill file (zip archive).
"""

import sys
import os
import zipfile
import yaml
from pathlib import Path


def validate_skill(skill_path):
    """Validate skill structure and return errors."""
    errors = []
    skill_path = Path(skill_path)
    
    # Check if directory exists
    if not skill_path.exists():
        errors.append(f"Skill directory does not exist: {skill_path}")
        return errors
    
    if not skill_path.is_dir():
        errors.append(f"Path is not a directory: {skill_path}")
        return errors
    
    # Check for SKILL.md
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing required file: SKILL.md")
        return errors
    
    # Parse and validate SKILL.md
    try:
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for YAML frontmatter
        if not content.startswith('---\n'):
            errors.append("SKILL.md must start with YAML frontmatter (---)")
            return errors
        
        # Extract frontmatter
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            errors.append("SKILL.md frontmatter not properly closed with ---")
            return errors
        
        frontmatter = parts[1]
        body = parts[2]
        
        # Parse YAML
        try:
            metadata = yaml.safe_load(frontmatter)
        except yaml.YAMLError as e:
            errors.append(f"Invalid YAML frontmatter: {e}")
            return errors
        
        # Check required fields
        if not metadata:
            errors.append("YAML frontmatter is empty")
            return errors
        
        if 'name' not in metadata:
            errors.append("Missing required field in frontmatter: name")
        elif not metadata['name']:
            errors.append("Field 'name' cannot be empty")
        
        if 'description' not in metadata:
            errors.append("Missing required field in frontmatter: description")
        elif not metadata['description']:
            errors.append("Field 'description' cannot be empty")
        elif len(metadata['description']) < 50:
            errors.append(f"Description is too short ({len(metadata['description'])} chars). Should be at least 50 characters and include when to use the skill.")
        
        # Check for extra fields
        allowed_fields = {'name', 'description', 'license'}
        extra_fields = set(metadata.keys()) - allowed_fields
        if extra_fields:
            errors.append(f"Unexpected fields in frontmatter: {', '.join(extra_fields)}")
        
        # Check body exists
        if not body.strip():
            errors.append("SKILL.md body is empty")
        
        # Check skill name matches directory name
        if metadata.get('name') and metadata['name'] != skill_path.name:
            errors.append(f"Skill name '{metadata['name']}' does not match directory name '{skill_path.name}'")
        
    except Exception as e:
        errors.append(f"Error reading SKILL.md: {e}")
    
    return errors


def package_skill(skill_path, output_dir=None):
    """Package the skill into a .skill file."""
    skill_path = Path(skill_path).resolve()
    skill_name = skill_path.name
    
    # Determine output directory
    if output_dir:
        output_path = Path(output_dir).resolve()
    else:
        output_path = skill_path.parent
    
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create .skill file (zip archive)
    skill_file = output_path / f"{skill_name}.skill"
    
    print(f"Packaging skill: {skill_name}")
    print(f"Output: {skill_file}")
    
    with zipfile.ZipFile(skill_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through skill directory
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                file_path = Path(root) / file
                # Calculate archive name (relative to skill directory)
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)
                print(f"  Added: {arcname}")
    
    print(f"\n✓ Successfully packaged: {skill_file}")
    return skill_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/package_skill.py <path/to/skill-folder> [output-directory]")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    print("Validating skill...")
    errors = validate_skill(skill_path)
    
    if errors:
        print("\n❌ Validation failed:\n")
        for error in errors:
            print(f"  • {error}")
        print("\nFix these errors and try again.")
        sys.exit(1)
    
    print("✓ Validation passed\n")
    
    # Package the skill
    package_skill(skill_path, output_dir)


if __name__ == "__main__":
    main()

