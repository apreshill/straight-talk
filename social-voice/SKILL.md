---
name: social-voice
description: "Write social media and short-form content that respects your reader's time and intelligence. Builds on brand-voice principles with platform-specific guidance for LinkedIn, Twitter/X, and other social platforms. Philosophy: get to the point, show don't tell, let brevity create impact."
---

# social-voice

Transform social media copy from performative relatability into genuine, crisp communication that respects the reader's scroll.

**Note:** Examples in this skill use specific products (like Pixeltable) for clarity, but all principles apply universally to any product or service.

## Foundation

This skill builds on **brand-voice** principles. If you haven't internalized those yet, start there. This adds the constraints and patterns specific to social media.

Core truth: Social media rewards brevity, specificity, and getting to the point. Your reader is scrolling. Earn their attention by respecting their time.

## Core Philosophy

**Be 10x more specific than you think you need to be.** Not "IT managers"—Bob Smith who leads IT at Figma. Not "save time"—the report that takes 3 hours now takes 10 minutes. Specificity = credibility.

**Show, don't tell.** Name the actual artifacts (zip files, Slack DMs, broken scripts) not the abstract categories (manual processes, communication overhead).

**State capabilities and benefits, not comparatives.** Ban "faster, better, easier, simpler." State what you can do now that you couldn't before (capability) and what that means (benefit).

**Let brevity create impact.** If you can cut it in half and it still works, cut it in half. But don't cut so much you sound like a caveman.

**Don't make up scenarios.** If you know a real customer story, be radically specific. If you don't, just state the capability and benefit. Never pretend a generic scenario is specific.

**Assume every post is someone's first exposure to your product.** Social media reaches beyond your existing users. Establish context about what domain/problem space you're in. Don't assume they know what your product does or what feature names mean.

## The Capability + Benefit Pattern

When you don't have a specific scenario, use this pattern. Master it.

**The structure:**
```
[Feature name]: [Binary capability]. [Concrete benefit].
```

**Binary Capability** = What you can do now (yes/no, not "better")
- "Stream datasets that don't fit in memory"
- "Direct cloud storage for generated media"
- "All-day battery"

**Concrete Benefit** = What that means
- What's now possible: "Leave your charger at home"
- Who it's for: "If you implement stack-ranking, this is for you"
- What changes: "Results load before you finish typing"

**Critical:** Never use "stop doing X" or "no more X"—that's prescriptive and condescending. Describe what's now possible, not the absence of a problem.

**Lazy negatives to avoid:**
- ❌ "No downtime" → ✅ "Deploy without taking the site offline"
- ❌ "No more manual processes" → ✅ "Automated end-to-end"
- ❌ "No more custom wrappers" → ✅ "Use DETR directly"
- ❌ "Stop managing storage" → ✅ "Write directly to cloud"

**Examples:**
> **IterableDataset streaming:** Work with datasets that don't fit in memory.

> **All-day battery:** Leave your charger at home.

> **Make fine-grained adjustments to priority levels within basic categories.** If you implement a stack-ranking system for your tasks and projects, this is specifically made for you!

**Why it works:** Honest. Clear. No hand-waving. No comparatives. Just: here's what you can do, here's what that means.

**The rule:** Capability and benefit should be tightly paired. Don't explain how it works between them.

## The LLM Slop Test

If your draft includes any of these patterns, rewrite from scratch:

### The Setup Formula
**Bad:**
- "You [did X]. Your [person] needs [Y]."
- "You're [doing X]. You need: 1. 2. 3."
- "There's a better way."
- Any generic scenario pretending to be specific

This is the default LLM structure for "relatable" content. It's instantly recognizable as AI-generated.

**The problem:** These scenarios are made up. They're hand-waving disguised as specificity.

**Better - Option 1 (Radically specific):**
> You're running CLIP embeddings on 10,000 product images. Each embedding generates a 512-dimensional vector. That's 20MB of vectors in /tmp.

**Better - Option 2 (Just state it):**
> Pixeltable 0.5.9 adds Backblaze B2 support.
>
> Capability: Direct cloud storage for generated media.
> Benefit: Stop managing local storage.

**The test:** Do you actually know this scenario (customer, numbers, workflow)? If yes, be radically specific. If no, just state capability + benefit. Never fake specificity.

### Mechanical Feature Lists
**Bad:**
- "function() does X—explanation of what it does"
- Each feature gets equal weight and explanation
- Reads like documentation, not communication
- Feature name comes before the problem

**Better:**
Show the problem, then show the solution in action. The feature name is just the answer to "how?"

**Example 1:**

❌ **Feature-first:**
> replicate() creates a copy of your data—it handles the serialization and ensures your teammate gets a working version they can query immediately

✅ **Problem-first:**
> Your teammate asks for your model. You send a pickle file. They send back an error message.
>
> They run pxt.replicate(). They get a working table. Done.

**Example 2:**

❌ **Feature list:**
> New in 0.5.9:
> - presigned_url() for secure S3 access
> - pxt.UUID for stable identifiers
> - Deployment guides

✅ **Problem → solution:**
> Your model works in dev. You deploy. Users see broken image links.
>
> The images are in S3. The bucket is private. You can't make it public.
>
> presigned_url() generates secure URLs. Users see images. Bucket stays private.
>
> Also in 0.5.9: stable IDs and deployment guides.

**The pattern:** Problem (concrete) → Constraint (why it's hard) → Solution (what changes)

### False Conversational Tone
**Bad:**
- "Let me show you"
- "Here's how"
- "Here's the thing"
- Explaining that you're about to explain something

**Better:**
Just state it. Trust the reader to follow the shift.

### Over-Explanation
**Bad:**
Telling the reader what they already understand from context.

**Better:**
Let the reader infer the benefits. Respect their intelligence.

**Example:**

❌ **Over-explained:**
> They get a working table they can query immediately. No reconstruction needed. No path debugging required.

✅ **Crisp:**
> They get a working table. Done.

## Platform-Specific Guidance

### LinkedIn
**Character sweet spot:** 150-300 characters for the hook (first 2-3 lines before "see more")

**Hook requirements:**
- Must work standalone
- Must create curiosity or recognition
- No throat-clearing allowed

**Structure that works:**
1. Concrete situation (1-2 lines)
2. The tension/problem (1-2 lines)  
3. The insight or solution (brief)
4. Optional: What changes (1 line max)

**What to avoid:**
- "I'm excited to share"
- "Hot take:"
- Numbered lists that could be prose
- Emoji bullets (unless your brand already uses them consistently)

### Twitter/X
**The 280 constraint is a gift.** It forces clarity.

**Structure:**
- Concrete situation or observation
- The tension
- The insight
- (Optional thread if needed, but can it be one tweet?)

**Thread guidance:**
- Each tweet must work standalone
- No "1/7" unless absolutely necessary
- The first tweet is the whole story compressed
- Subsequent tweets are elaboration, not continuation

### General Social Rules

**The Half Test:**
If you can cut your draft in half and it still works, cut it in half. But if it starts sounding like telegrams, you've gone too far.

**The Read-Aloud Test:**
Would you actually say this out loud to a colleague? If you sound like a caveman or a robot, rewrite it.

**The Scroll Test:**
Your reader's thumb is moving. Did you earn the stop?

## What to Eliminate

### Performative Relatability
- "You know what grinds my gears?"
- "Can we talk about [thing]?"
- "This. This right here."
- "Say it louder for the people in the back"

### Meta-Commentary
- "This might be controversial but"
- "Unpopular opinion:"
- "I said what I said"
- Apologizing for having an opinion

### Engagement Bait
- "Agree? 👇"
- "Tag someone who needs to see this"
- "Double tap if you relate"
- "What do you think? Comment below!"

### LLM Tells
- "In today's fast-paced world"
- "Let's dive in"
- "Here's the thing"
- "At the end of the day"
- The Setup Formula (see above)

## Structure Patterns That Work

### The Situation Drop-In
Start in the middle of a specific moment.

**Example:**
> Your teammate asks for your model. You send a pickle file. They send back an error message.

### The Artifact List
Name the actual things, not the categories.

**Bad:** "Manual data transfer processes"  
**Good:** "Zip files. Slack messages about bucket credentials. Screenshots of file paths."

### The Compressed Narrative
Tell the whole story in 3 lines.

**Example:**
> You build a model. Your teammate needs it. You spend 3 hours debugging their environment instead of your code.

### The Before/After (Without Saying Before/After)
Show the contrast through concrete details.

**Example:**
> Used to: zip file, Slack DM, "did you get it?", error message, environment.yml, different error message.
>
> Now: pxt.replicate(). Done.

### The Honest Tension
Name the tradeoff plainly.

**Example:**
> This takes 10 minutes to set up. It saves 3 hours every time someone needs your work. Do the math.

## The Social Media Test

Before posting, ask:

1. **Did I get to the point in the first 2 lines?**
2. **Am I showing (concrete artifacts) or telling (abstract categories)?**
3. **Can I cut this in half?**
4. **Would I actually say this out loud?**
5. **Am I performing relatability or being relatable?**
6. **Does this sound like an LLM wrote it?**
7. **Am I respecting my reader's scroll?**

If you fail any of these, rewrite.

### Feature Announcement Red Flags

If you're announcing a technical feature and your draft has any of these, rewrite:

❌ **"Introducing [feature name]"** - Just state what you added  
❌ **Comparatives** - "Faster, better, easier" → State capability + benefit  
❌ **Generic scenarios** - "Your pipeline generates files" → Be 10x more specific or just state the capability  
❌ **"What's included:"** - This is documentation language  
❌ **Made-up customer stories** - If you don't know the real scenario, don't fake it  
❌ **Abstract benefits** - "Secure access" means nothing. "Bucket stays private" is concrete.

**The fix:** 
- Know a real scenario? → Be radically specific (customer, numbers, workflow)
- Don't know? → State capability + benefit
- Never fake specificity

## Be 10x More Specific

The most common mistake in product communication: hand-waving with generalizations.

**The rule:** Be 10x more specific than you think you need to be.

### Examples from Product Management

❌ **Generic:** "Our customer is IT managers"  
✅ **Specific:** "Bob Smith who leads IT at Figma"

❌ **Generic:** "People save time running reports"  
✅ **Specific:** "The report Bob runs every week is pre-cached in his inbox, so he doesn't need to open the app"

❌ **Generic:** "Your pipeline generates video frames"  
✅ **Specific:** "You're running CLIP embeddings on 10,000 product images. Each embedding generates a 512-dimensional vector. That's 20MB of vectors in /tmp."

**Why this matters:** When you force yourself to be this specific, it becomes clear whether you're basing your claims on real data points or just hand-waving made-up ideas.

Too often, it's the latter.

### When You Don't Have Specifics

If you can't name the customer, don't have the numbers, or don't know the real workflow—**don't fake it.**

Instead, just state capability + benefit:

**Example:**
> Pixeltable 0.5.9: Write to Backblaze B2.
>
> Capability: Direct cloud storage for generated media.
> Benefit: Stop managing local storage.

This is honest. It doesn't pretend to know your specific situation. It just tells you what you can do now that you couldn't before.

**The test:** Could you defend this claim to an engineer who actually uses your product? If not, be more specific or just state the facts.

## Avoid Caveman Speak

Brevity is good. Sentence fragments are not.

**Caveman speak:**
> Keys expire. Pipelines stop. Team frustrated.

**Conversational and crisp:**
> Eventually someone's keys expire and the pipeline stops working.

**The difference:** Caveman speak uses fragments to save words. Conversational writing uses complete sentences that sound like how you'd actually explain it to a colleague.

**More examples:**

❌ **Caveman:** "Local storage full. Need cloud. Credentials hard."  
✅ **Human:** "Local storage fills up. You need cloud storage. Managing credentials is a pain."

❌ **Caveman:** "Query slow. Index helps. Performance better."  
✅ **Human:** "The query is slow. Adding an index helps. Performance improves."

❌ **Caveman:** "Deploy breaks. Images private. Users sad."  
✅ **Human:** "You deploy. Images are in a private bucket. Users see broken links."

**The test:** Read it out loud. If you wouldn't say it that way to a person, rewrite it.

Compression is about removing **unnecessary** words, not removing words that make you sound human.

## Word Count Targets

**LinkedIn post:** 50-150 words (hook must work in first 150 characters)  
**Twitter/X:** 100-280 characters (aim for one tweet if possible)  
**Thread starter:** Must contain the complete thought compressed

**The rule:** If you're over the target, you're explaining too much. If you sound like a caveman, you've compressed too much.

## Voice Markers for Social

- **Use concrete artifacts:** "pickle file" not "model file"
- **Use actual actions:** "They run X" not "They utilize X"
- **Use silence:** Let the space between problem and solution breathe
- **Use brevity:** "Done." is a complete sentence
- **Use specifics:** "3 hours" not "significant time"

## What Makes Social Different from Brand-Voice

**Brand-voice says:** Be clear and respectful  
**Social-voice says:** Be clear, respectful, AND compressed

**Brand-voice says:** Acknowledge tension  
**Social-voice says:** Let the tension sit in silence

**Brand-voice says:** Concrete before abstract  
**Social-voice says:** Only concrete. No abstract.

**Brand-voice says:** Respect the reader's time  
**Social-voice says:** Respect the reader's scroll

## LinkedIn-Specific Guidance

### Evaluating Your Hook

Before you post, test your first line against these three criteria:

**1. Newness (0-10)**
How likely is it your audience has heard this before?

- "Sales is important" → Not new to anyone
- "Artists need to become salespeople" → New to that specific audience

**2. Relevance (0-10)**
Does this help your audience do their job better?

- "Clay vs wax for hair styling" → Irrelevant to developers
- "This database query pattern cut our response time by 40%" → Relevant to developers

**3. Crunch (0-10)**
Does your claim have enough structure that people can react to it?

"Databases are important" has no crunch—nothing to agree or disagree with. "ORMs make your queries slower" has crunch—people will have opinions.

Listen for your own hesitation. If you're thinking "people will have thoughts about this," you've found the crunch.

**The balance:** You need at least two of these at 7+. All three at 5 is forgettable.

### Platform Mechanics

**Character limit:** 3,000 characters (~500 words)
Don't pad to hit the limit. Say what you need to say.

**The hook matters:**
- Text posts: First 5 lines before "see more"
- Image/video posts: First 3 lines before "see more"

If your value isn't clear in those lines, no one clicks.

**Emphasis workarounds:**
LinkedIn doesn't support formatting, so:
- Use \*stars\* for emphasis (like italics)
- Use CAPS for strong emphasis (like bold)
Use sparingly.

**Hashtags:**
- Use 2-3 broad hashtags (#developers #databases #performance)
- Not niche hashtags (#databaseperformanceoptimization)
- Lowercase only
- Related to what you're selling/known for, not the specific topic

**@ mentions:**
Tag people and companies when genuinely relevant. Not for reach.

### LinkedIn Carousels

Carousels are multi-slide posts. They follow all the same social-voice principles (concrete, brief, capability + benefit) but with slide-specific structure.

#### Carousel Structure

**Slide 1: Title + Intro**
- **Headline:** 40-50 characters max (this is the big text on the slide)
- **Intro text:** 100-120 characters (the supporting text)
- Must work standalone—if someone only sees slide 1, do they know what this is about?

**Critical for Slide 1:** Establish context for non-users. Don't assume they know your product.

❌ **Feature name only:** "Data Sharing"
✅ **Outcome + context:** "Share multimodal datasets in one command"

The headline should tell someone **what domain/problem this lives in**, not just the feature name.

**Slide 2-N: Content slides**
- Feature slides (capability + benefit)
- Problem slides (only if you have a concrete problem to show)
- Comparison slides (before/after)

**Final slide: CTA/Read More**
- Link to full content
- Keep it simple (no "Learn more!" hype)

#### Feature Carousel Pattern

When announcing one feature from a larger release:

**Slide 1:**
- Headline: Feature name + key capability
- Intro: What's new, stated as capabilities (not "improvements")

**Slide 2: What's New**
- List 3-5 specific capabilities
- Each one follows: **Feature name** → Capability statement
- No emoji bullets
- No "What's Included" language (that's documentation speak)

**Slide 3: Read More**
- Simple link to full details
- "Full release notes: [link]" or "Read more: [link]"
- No engagement bait

**Example structure:**

**Slide 1:**
> **Headline:** "Hugging Face: Streaming + Built-in UDFs"
>
> **Intro:** "Stream IterableDatasets. Built-in UDFs for DETR segmentation and Image2Image pipelines. Better type inference on import."

**Another example (for non-users):**
> **Headline:** "Share multimodal datasets in one command"
>
> **Intro:** "Datasets with images, video, embeddings. Share schema, data, and media together. Teammates get a working table. 1TB free."

Note: The second example establishes context (multimodal datasets) for people who don't know the product yet.

**Slide 2:**
> **What's New**
>
> **IterableDataset streaming**
> Work with datasets that stream on-demand instead of loading into memory
>
> **Built-in DETR and Image2Image UDFs**
> Pre-built functions for segmentation and generation pipelines
>
> **Enhanced dataset imports**
> Automatic type inference when importing Hugging Face datasets

**Slide 3:**
> 📖 Full release highlights
> 👉 Section 4: Enhanced Hugging Face Integration
> 🔗 pixeltable.com/blog/release-highlights

#### What NOT to Do in Carousels

❌ **Problem slides with abstract pain points**
> ❌ Large datasets don't fit in memory
> ❌ Writing custom wrappers is tedious
> ❌ Manual type mapping takes time

This just lists abstract problems. Either show a concrete problem (with specifics) or skip the problem slide entirely.

❌ **"What's Included" language**
This is documentation speak. Use "What's New" or just list the features.

❌ **Emoji bullets everywhere**
> ✨ Feature 1
> 🎨 Feature 2
> 🚀 Feature 3

Emoji bullets are visual clutter. Use them sparingly (like for the final CTA slide) or not at all.

❌ **Feature-first descriptions**
> replicate() creates a copy of your data—it handles serialization...

Lead with the problem or capability, not the function name.

❌ **Engagement bait on final slide**
> "Which feature are you most excited about? 👇"
> "Tag someone who needs this!"

Just link to the full content. Respect the reader.

#### When to Include a Problem Slide

**Include a problem slide when:**
- You have a concrete, specific problem to show (real scenario, real numbers)
- The problem isn't obvious from the feature names
- You're using Option 1 (radically specific) approach

**Skip the problem slide when:**
- You're using Option 2 (capability + benefit) approach
- The problems are implied by the feature names
- You'd just be listing abstract pain points

**Most feature carousels don't need a problem slide.** Just state what's new and what it does.

#### Carousel Character Limits

**Slide 1:**
- Headline: 40-50 characters (fits on one line)
- Intro: 100-120 characters (2-3 short sentences)

**Content slides:**
- No hard limit, but keep it scannable
- 3-5 bullet points max per slide
- Each bullet: Feature name + 1-2 line description

**The test:** Can someone scroll through in 10 seconds and understand what this is about?

### Writing About Technical Features

**CRITICAL: Don't choose the approach yourself. Ask the user.**

When writing about a technical feature, you have two approaches. The user must tell you which one applies—you cannot guess or assume.

**Ask:** "Do you have a specific customer/scenario for this feature (real person, real numbers, real workflow), or is this a general feature announcement? Or would you like to see both versions side-by-side?"

Then apply the appropriate approach (or show both):

#### Option 1: Be Radically Specific (When they have a real scenario)

Use when the user has actual data points: real customer, real numbers, real workflow.

**Use when:**
- They know exactly who uses this feature and how
- They have real data points (names, numbers, dimensions)
- They're explaining a complex technical thing

**Example:**
> You're running CLIP embeddings on 10,000 product images. Each embedding generates a 512-dimensional vector. That's 20MB of vectors sitting in /tmp.
>
> Now: write directly to B2. /tmp stays clean.

**Why it works:** Extreme specificity = credibility. People think "they actually know what they're talking about."

**The test:** Could they name the customer (even if they don't in the post)? Do they have the actual numbers?

#### Option 2: State Capability + Benefit (When it's a general feature)

Use when the feature applies broadly and they don't have a specific customer story yet.

**Use when:**
- The feature applies broadly
- They don't have a specific customer story yet
- They're announcing something new

**The Pattern:**
```
[Feature name]: [Binary capability]. [Concrete benefit].
```

**Binary Capability = What you can do now (yes/no, not "better")**
- ✅ "Stream datasets that don't fit in memory"
- ✅ "Direct cloud storage for generated media"
- ✅ "All-day battery"
- ❌ "Stream datasets faster" (comparative)
- ❌ "Improved storage options" (vague)
- ❌ "Better battery life" (comparative)

**Concrete Benefit = What that means / What's now possible / Who it's for**
- ✅ "Leave your charger at home" (what's now possible)
- ✅ "Write directly to cloud" (what you can now do)
- ✅ "If you implement stack-ranking, this is for you" (who it's for)
- ✅ "Results load before you finish typing" (what changes)
- ❌ "Stop managing local storage" (lazy negative)
- ❌ "No more custom wrappers" (lazy negative)
- ❌ "No downtime" (lazy negative)
- ❌ "Better user experience" (abstract)
- ❌ "Improved workflow" (vague)
- ❌ "More efficient" (comparative)

**Example:**
> Pixeltable 0.5.9: Write to Backblaze B2 and Tigris.
>
> Capability: Direct cloud storage for generated media.
> Benefit: Write video frames and embeddings directly to cloud.

**Another example:**
> IterableDataset streaming: Work with datasets that don't fit in memory.

**Why it works:** Clear, honest, no hand-waving. Binary before/after.

**The tight pairing rule:** Benefit should immediately follow capability. Don't explain how it works between them.

#### The Real Test

Ask yourself (or ask the user): **Do I actually know a specific person/scenario, or am I making one up?**

- If they know it → Be 10x more specific
- If they're making it up → Just state capability + benefit

**The sin:** Making up a generic scenario and pretending it's specific.

#### What NOT to Do: Generic Scenarios

❌ **Made-up relatability:**
> Your pipeline generates video frames. Local storage fills up. You need cloud storage.

This is hand-waving disguised as specificity. It's the "IT managers" version when you need "Bob Smith at Figma."

❌ **"Your pipeline generates video frames"** ← Made up, trying to sound relatable  
✅ **"You're running CLIP on 10,000 images"** ← Specific, based on real usage

#### Banned Comparatives

Don't use: faster, better, easier, simpler, more, improved, enhanced

**Instead:**

| Banned | Use Instead |
|--------|-------------|
| "Longer battery life" | Capability: "All-day battery" / Benefit: "Leave your charger at home" |
| "Faster queries" | Capability: "Query returns in <100ms" / Benefit: "Results load before you finish typing" |
| "Better security" | Capability: "Bucket stays private" / Benefit: "No public S3 buckets to audit" |
| "Easier deployment" | Capability: "One-command deploy" / Benefit: "Ship without writing Docker configs" |

**Why:** Comparatives are vague. Capabilities are binary. Benefits are concrete outcomes.

### Common LinkedIn Patterns

These archetypes work, but only if you execute them with our core principles (concrete, brief, honest):

**The Claim**
Your database is probably slower than it needs to be. Here are 3 queries that are killing your performance: [list]

**The Experiment**
Last week we tried connection pooling. Cut our DB response time from 2s to 200ms. Here's what we changed: [specifics]

**The Question**
"How do I optimize this query?" Here's the debugging process: [steps]

**The Objection**
"We can't rewrite this legacy code." You don't have to. Here's what you can do instead: [options]

**The Mistake**
I pushed a migration that dropped a production table. Here's what I learned: [lesson]

**The Feature Announcement**
Your model works in dev. You deploy. Users see broken images. [why it breaks] [what solves it]

**Use these as starting points, not templates.** The structure helps, but the specifics make it work.

### Feature Announcements: Lead with the Capability, Not the Release

When announcing one feature from a larger release, lead with what the feature does, not the release number. And establish context for people who don't know your product.

**Bad (release-first, no context):**
> Pixeltable 0.5.9 adds Hugging Face improvements.

**Better (feature-first, but assumes knowledge):**
> Pixeltable now supports Hugging Face IterableDatasets.

**Best (capability-first, with context):**
> Pixeltable now supports dataset sharing with multimodal data.

**Why:** The reader cares about the capability, not the version number. Lead with what they can now do.

**The pattern:**
1. **Line 1:** State the new capability (what's now possible)
2. **Body:** List specific features using Capability + Benefit pattern
3. **End:** Release context + link ("Part of [Product] [Version]. Full release notes: [link]")

**Example:**

> Pixeltable now supports Hugging Face IterableDatasets.
>
> **IterableDataset streaming:** Work with datasets that stream on-demand instead of loading into memory.
>
> **Built-in UDFs:** Pre-built functions for DETR segmentation and Image2Image pipelines.
>
> **Enhanced imports:** Automatic type inference when importing Hugging Face datasets.
>
> Part of Pixeltable 0.5.9. Full release notes: [link]

**Use this when:** You're highlighting one feature from a larger release. The post should be standalone—readers don't need to know about the other features.

### When to Break the Rules

**Genuine announcements deserve excitement:**
If you actually got featured in a publication, hired someone great, or shipped something you're proud of—one or two exclamation points are fine. Just don't perform excitement you don't feel.

**Questions at the end can work:**
- ✅ "What's your debugging process?" (advances thinking)
- ✅ "What would you add?" (genuine curiosity)
- ❌ "Agree? 👇" (engagement bait)
- ❌ "Tag someone who needs this" (spam)

The test: Would you actually want to read the answers?

## Examples

See [references/examples.md](references/examples.md) for before/after transformations.

---

## Credits and Inspiration

This skill combines:

**brand-voice foundations** (Aesop formality + Intuit clarity + Codex honesty)
- Concrete before abstract
- Tension acknowledged
- Reader as peer
- Say what you mean

**Platform-specific patterns** identified through analysis of:
- LLM-generated social content (anti-patterns)
- Effective technical social media (what actually works)
- The constraints of the medium (character limits, scrolling behavior)

Philosophy: Social media is not a lesser medium. It's a different medium with different constraints. Respect those constraints and you respect your reader.
