# straight-talk

Claude skills for capturing specific writing voices and styles. These skills are **content-agnostic**—they teach Claude how to write in a particular voice, not what to write about.

## What These Skills Do

These skills distill the voice, style, and structural patterns from exemplary writing to make technically complex or professional content more approachable and human. They capture **how** to write, not **what** to write.

Think of them as voice cloning for writing style: the patterns, rhythms, and techniques that make writing feel direct, warm, honest, and intelligent—without dictating subject matter.

**See it in action:** Check out [test-skill-usage.md](test-skill-usage.md) for before/after examples showing how the skills transform generic writing into clear, human communication.

### How the Skills Build on Each Other

```
codex-voice (foundation)
    ↓
    Adds: narrative intelligence, concrete-before-abstract, 
          tension acknowledged, reader as peer
    ↓
brand-voice (adds formality + clarity)
    ↓
    Adds: Aesop's word discipline, Intuit's conversational clarity,
          professional polish while maintaining warmth
    ↓
social-voice (compresses + adds platform constraints)
    ↓
    Adds: brevity, platform mechanics, crunch framework,
          respect for the scroll
```

Each skill builds on the previous one. Use codex-voice for long-form technical writing, brand-voice for brand communications, and social-voice for social media where every word must earn its place.

## Skills in This Repo

### codex-voice
**Voice & style for long-form technical writing**

Captures the writing patterns from The Composable Codex: how to make technically complex material approachable while respecting the reader's intelligence. This is about sentence structure, opening moves, transition patterns, and voice markers—not about data systems or composability.

Use when writing about any technical topic where you want to:
- Make complexity accessible without dumbing it down
- Write with warmth and personality, not corporate blandness
- Trust your reader to keep up while still being clear

**Location:** `codex-voice/`  
**Packaged file:** `codex-voice.skill`

### brand-voice
**Voice & style for brand and corporate communications**

Combines the best of three worlds: Aesop's respectful formality and word discipline, Intuit's conversational clarity, and The Composable Codex's honest directness. This is about word choice, tone, and philosophy—not about skincare or financial software.

Use when writing any brand or customer-facing content where you want to:
- Sound human, not like a marketing robot
- Be clear and precise without being cold
- Show respect for your reader's time and intelligence
- Be honest about tradeoffs instead of claiming perfection

**Location:** `brand-voice/`  
**Packaged file:** `brand-voice.skill`

### social-voice
**Voice & style for social media and short-form content**

Builds on brand-voice principles with platform-specific guidance for LinkedIn, Twitter/X, and other social platforms. Combines clarity, crispness, and respect for the reader's scroll. Includes extensive anti-patterns for recognizing and eliminating LLM slop.

Use when writing social media content where you want to:
- Get to the point in the first 2 lines
- Show through concrete artifacts, not abstract categories
- Let brevity create impact
- Respect your reader's scroll
- Avoid the telltale patterns of AI-generated social content

**Location:** `social-voice/`  
**Packaged file:** `social-voice.skill`

## Using the Skills

To use a skill with Claude:
1. Download the `.skill` file
2. Import it into your Claude workspace
3. The skill will guide Claude's writing style for your content

**Important:** These skills teach Claude *how* to write (voice, structure, patterns), not *what* to write about. You bring the subject matter and expertise; the skill brings the voice and style.

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
├── codex-voice/               # Long-form technical writing
│   ├── SKILL.md              # Main skill file
│   └── references/
│       └── patterns.md       # Sentence patterns to emulate
├── brand-voice/               # Brand & corporate communications
│   ├── SKILL.md              # Main skill file
│   └── references/
│       └── word-lists.md     # Vocabulary guidance
├── social-voice/              # Social media & short-form
│   ├── SKILL.md              # Main skill file
│   └── references/
│       └── examples.md       # Before/after transformations
├── codex-voice.skill         # Packaged skill files
├── brand-voice.skill
└── social-voice.skill
```
