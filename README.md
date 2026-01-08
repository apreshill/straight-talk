# straight-talk

A Claude skill for revising long-form professional content into direct, warm writing that respects the reader's intelligence.

## What This Skill Does

Transforms AI-slop and corporate speak into writing that sounds human—specifically, writing in Alison's voice. Inspired by Dolly Parton: say what you mean, mean what you say, make people feel smart for reading it.

Use this skill when:
- Editing or revising blog posts, documentation, technical guides, or thought leadership
- Drafting new long-form content
- Catching and eliminating AI writing patterns

## Skills in This Repo

### codex-voice
Writing style skill for long-form technical and professional content. Based on The Composable Codex writing style—direct, warm writing that respects the reader's intelligence.

**Location:** `codex-voice/`  
**Packaged file:** `codex-voice.skill`

### brand-voice
Brand and corporate communications skill. Clear, respectful, considered writing for marketing copy, product descriptions, and customer-facing content. Inspired by Aesop's philosophy.

**Location:** `brand-voice/`  
**Packaged file:** `brand-voice.skill`

## Using the Skills

To use a skill with Claude:
1. Download the `.skill` file
2. Import it into your Claude workspace
3. The skill will automatically trigger when you're working on relevant content

## Development

### Creating New Skills

Initialize a new skill:

```bash
python scripts/init_skill.py <skill-name> --path .
```

### Packaging Skills

Package a skill for distribution:

```bash
python scripts/package_skill.py <skill-folder-name>
```

The script validates the skill structure and creates a `.skill` file (zip archive).

### Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter with name and description
│   └── Markdown instructions
└── references/ (optional)
    └── Additional documentation loaded as needed
```

## Repository Structure

```
straight-talk/
├── scripts/                    # Utility scripts
│   ├── init_skill.py          # Initialize new skill
│   └── package_skill.py       # Package skill for distribution
├── codex-voice/               # Composable Codex writing style
│   ├── SKILL.md              # Main skill file
│   └── references/
│       └── patterns.md       # Sentence patterns to emulate
├── brand-voice/               # Brand voice writing skill
│   ├── SKILL.md              # Main skill file
│   └── references/
│       └── word-lists.md     # Vocabulary guidance
├── codex-voice.skill         # Packaged skill files
└── brand-voice.skill
```
