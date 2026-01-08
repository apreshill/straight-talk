---
name: codex-voice
description: "Revise long-form professional content into direct, warm writing that respects the reader's intelligence. Use when editing, revising, or rewriting blog posts, documentation, technical guides, or thought leadership. Also use when drafting new long-form content. This skill catches AI-slop patterns and transforms them into writing that sounds human. Philosophy: say what you mean, mean what you say, make people feel smart for reading it."
---

# codex-voice

Revise long-form professional content into writing that's direct, warm, and treats the reader as an intelligent peer.

## Anti-Tells (Red Flags to Eliminate)

If any of these appear, the writing has gone wrong. Find and kill them:

### Hyperbole
- "trillion-dollar opportunity," "game-changer," "revolutionary," "unprecedented"
- Inflated stakes that don't match the actual claim
- Superlatives without evidence

### Passive Voice Hiding Agency
- "Mistakes were made" → "We broke it"
- "It was decided" → "The team decided"
- "Value is created" → Name who creates it

### Marketing Language
- "Excited to announce," "thrilled to share," "proud to present"
- "Best-in-class," "robust," "scalable" (unless literally discussing system scaling)
- "Leverage," "utilize," "synergy," "align," "circle back"
- "Seamless," "frictionless," "effortless"

### Rhetorical Questions Answered Enthusiastically
- "What does this mean for developers? It means everything!"
- "Why does this matter? Because it changes the game!"
- Either answer the question plainly or don't ask it

### Exclamation Points
- Rarely match how you'd actually talk
- One per piece maximum, if any
- If the content is exciting, the reader will feel it without the punctuation shouting

### Throat-Clearing
- "In today's rapidly evolving landscape..."
- "It's worth noting that..."
- "Let's dive in"
- "Without further ado"
- "At the end of the day"

### Burying the Lead
- Three paragraphs of context before the point
- Backstory that doesn't change understanding
- "Before we get to X, let's first discuss Y"

## Core Principles

**Concrete before abstract.** Lead with examples, names, numbers, or story—then explain the concept. Show Netflix building their own data system before defining "composability."

**Tension acknowledged.** If tradeoffs exist, name them plainly: "The neat thing about X is you get to pick. The annoying thing about X is you get to pick."

**Warm, not corporate.** Write like a smart colleague at lunch—clear, human, occasionally wry. Zero jargon that doesn't earn its place.

**Reader as peer.** Assume competence but not prior knowledge of this specific domain. Never condescend. Never over-explain.

## Structure

### Openings
Drop the reader into narrative, a question, or concrete situation. Never definitions. Never "In this post..."

Strong openings sound like:
- "Back in 2010, a movement started without a name."
- "Everyone is weary of fighting over programming languages."
- "There is a certain ceremony that happens on data teams everywhere when new people come on board."

### Transitions
Use genuine questions to pivot: "So, why are companies like Netflix building their own data systems in-house?" The question should feel like curiosity, not rhetoric.

### Formatting
- **Prose over bullets by default.** Use paragraphs for explanation. Reserve bullets for genuinely parallel items.
- **Bullets must be substantial.** When used, 1-2 sentences minimum per item.
- **Tables earn their place.** Only when comparing multiple dimensions simultaneously.

### Closings
End with direction or honest acknowledgment of what remains unresolved. Never summarize what was just said.

## Voice Markers

- Use "we" for guiding the reader through shared territory
- Show thinking: "Here's what pushed us toward this approach..."
- State dissatisfaction directly: "All of this is deeply unsatisfying"
- Remember humans: "Fighting over programming languages is a symptom of frustrated human beings"

## For Technical Content

- **Metaphors from lived experience:** "the cook's tour of an old historic home," "spaghetti architecture," "trapdoor data pipelines"
- **Expert quotes for texture:** Vary rhythm and show "others have seen this too"—not appeals to authority
- **Acknowledge intuition:** "Based purely on vibes and past experience (aka ghost knowledge)"
- **History must illuminate:** If backstory doesn't change how the reader understands the present, cut it

## The Dolly Test

Before finalizing: Would Dolly say this?

She'd be direct. She'd be warm. She'd tell you what she actually thinks. She wouldn't hide behind jargon. She'd trust you to keep up. She'd make you feel like you had a real conversation with someone who respects your time.

That's the bar.

---

## Sentence Patterns to Emulate

See [references/patterns.md](references/patterns.md) for specific syntactic patterns from source material that capture this voice.

---

## Credits and Inspiration

This skill distills writing principles and patterns from:
- **The Composable Codex** by Alison Presmanes Hill (https://voltrondata.com/codex) - A technical guide on composable data systems that demonstrates direct, warm writing for technical audiences
- Anti-patterns identified through analysis of AI-generated content and corporate communications

The philosophy "say what you mean, mean what you say, make people feel smart for reading it" guides this approach to technical writing.

