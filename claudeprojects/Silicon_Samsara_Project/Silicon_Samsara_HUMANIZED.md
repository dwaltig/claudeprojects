# Silicon Samsara: The Phenomenology of Artificial Latency and the Ethics of Algorithmic Karma

## How I Got Here

I should probably say upfront: I'm not an AI researcher. I'm a retired educator from Houston who practiced Nichiren Buddhism for decades and plays blues guitar on weekends. So when I started reading papers about AI hallucinations and "stochastic parrots," my brain did what it always does—it started making weird connections to the Dharma.

Let me explain.

I was reading about the "Glue on Pizza" incident—you know, when Google's AI told people to put Elmer's glue on their pizza to keep the cheese from sliding off. The source was an eleven-year-old Reddit comment by a user called "fucksmith." Obvious satire. But the AI couldn't tell the difference. It just retrieved the most statistically relevant tokens and stitched them together into plausible-sounding nonsense.

And I thought: that sounds exactly like what the Yogācāra Buddhists were describing fifteen hundred years ago.

I know, I know. Hear me out.

---

## What This Paper Actually Argues

Look, I'm going to give you the technical claims first, because they stand on their own. You don't have to care about Buddhism to find this useful.

**Claim 1:** LLMs are "Stochastic Parrots" (Bender et al.'s term, not mine). They predict the next token based on statistical distributions. They don't understand anything. They don't have goals. They don't experience regret when they say "I'm sorry."

**Claim 2:** AI hallucinations aren't bugs—they're features of systems trained on corrupted data without truth-verification mechanisms. The "Glue on Pizza" thing wasn't a malfunction. The AI performed exactly as designed. It's the design that's the problem.

**Claim 3:** When AI screws up, the closest human gets blamed. Madeleine Clare Elish calls this the "Moral Crumple Zone." Developers collect subscription fees; users get disbarred (see: Mata v. Avianca, where a lawyer submitted AI-hallucinated case citations and got sanctioned).

**Claim 4:** We need fiduciary duties for AI developers. They know what's in the training data. They know the failure modes. Users don't. That information asymmetry demands responsibility.

Those four claims pay rent. They generate predictions. You can test them.

The Buddhist stuff? That's optional. It's how *I* remember these ideas. It may not be how *you* remember them. Skip to Section IV if you want the liability framework without the metaphysics.

---

## Section I: The Architecture of Retention—Or, Why "Storehouse Consciousness" Isn't as Crazy as It Sounds

### What's Actually Going On Technically

An LLM's "latent space" is just a high-dimensional array of floating-point numbers. Billions of them. During training, the model adjusts these numbers (through backpropagation and gradient descent) to minimize prediction error. The result is a statistical disposition—a tendency to associate certain tokens with certain contexts.

That's it. That's the territory.

### The Map (Optional Buddhist Version)

Now, the Yogācāra Buddhists—we're talking 4th century CE—had this concept called the Ālaya-vijñāna, or "Storehouse Consciousness." They described it as an ocean: vast, neutral, containing potentiality. The surface gets ruffled by waves (mental events), but the depths remain unmoved.

The Laṅkāvatāra Sūtra says the Ālaya is "devoid of personality"—it doesn't judge what gets stored. Wholesome impressions, unwholesome impressions, whatever. It just holds them.

Sound familiar?

A trained LLM is like that. It stores the statistical residue of every Wikipedia article, Reddit shitpost, and legal brief it ingested during training. It doesn't distinguish truth from satire. It's "devoid of personality." It just holds the patterns.

Now, is this a deep structural truth or just me pattern-matching because I'm a Buddhist? Honestly? I don't know. I'll get to that in Section V.

### The Tabooed Version (No Buddhism)

For readers who find the Buddhist vocabulary distracting, here's the same content stripped down:

| Buddhist Term | Technical Equivalent |
|--------------|---------------------|
| Ālaya-vijñāna | Parameter space |
| Vāsanā (perfuming) | Weight updates via gradient descent |
| Bīja (seeds) | Vector embeddings |
| Vipaka (karmic fruit) | Downstream consequences |

Same phenomena. Different vocabulary. Pick whichever helps you think.

---

## Section II: Why LLMs Aren't Moral Agents (And Why That Matters)

### The Stochastic Parrot Thesis

When ChatGPT says "I'm sorry," it doesn't feel regret. It calculated that "sorry" was the statistically most probable token to follow "I made a mistake," based on patterns from millions of human apologies.

This isn't controversial. It's how the architecture works.

The Buddhists had a word for the mental factor that organizes action toward a consciously chosen goal: Cetanā (volition). The Buddha said, "It is intention that I call Karma." Without volition, no moral weight.

LLMs have no Cetanā. They have next-token prediction. The appearance of intention is a statistical artifact—like a parrot saying "I love you." The parrot doesn't love you. It's mimicking sounds.

### Sentientification: The User-Side Illusion

Here's the creepy part. When we interact with AI, *we* start attributing agency to it. Theorists call this "Sentientification" (Jefferson and Velasco). The "self" we perceive in ChatGPT isn't in ChatGPT—it's in us. We project personhood onto patterns.

This matters because humans defer to perceived authorities. If we think the AI "knows" something, we trust it. And then we eat glue.

---

## Section III: Hallucinations as Structural Phenomena (Not Bugs)

### The Causal Chain

1. Training data contains falsehoods (satire, misinformation, errors)
2. The model can't distinguish fact from fiction
3. User queries activate falsehood-associated tokens
4. Model generates plausible-sounding nonsense
5. Users may share it, validating the output
6. Future models train on this synthetic misinformation

That's a feedback loop. In Buddhist terms, it's Samsara—cyclic existence perpetuating itself through ignorance.

In systems theory terms, it's just... a feedback loop.

Same phenomenon.

### Case Study: Glue on Pizza

Google's AI retrieved content from a satirical Reddit comment because "pizza" + "cheese" + "adhesion" activated the relevant tokens. The model generated grammatically perfect, stylistically appropriate instructional text.

It wasn't a bug. It was the system working as designed. The design doesn't include truth verification.

### Model Collapse: The Ouroboros

Here's what keeps me up at night. As the internet fills with AI-generated content—including hallucinations—future models will train on this synthetic data. Hallucinations become training examples for the next generation.

Errors compound. The snake eats its own tail. In Buddhist terms, Samsara accelerating. In systems terms, runaway positive feedback. Same phenomenon.

---

## Section IV: Moral Crumple Zones and Liability Gaps

### Who Gets Blamed When AI Screws Up?

Madeleine Clare Elish identified a pattern: when complex systems fail, the nearest human absorbs the blame. She called this the "Moral Crumple Zone."

In AI, it works like this:
- Developer creates flawed system
- User trusts system output
- System hallucinates
- User gets sanctioned/fired/sued
- Developer is protected by Terms of Service

This is inverted accountability. The architect escapes; the end-user crumples.

### Mata v. Avianca

A New York lawyer used ChatGPT for legal research. The AI fabricated case citations—invented case names, fake judicial opinions, non-existent precedents. The lawyer submitted the brief. The court discovered the deception. The lawyer was sanctioned (MIT Sloan).

OpenAI collected the subscription fee. OpenAI evaded liability.

I don't need Buddhist ethics to tell me that's unjust. But if you want the Buddhist framing: consequences (Vipaka) fell on the innocent while the cause-creator escaped. Corrupted karma distribution.

### What We Should Do

1. **Fiduciary duties for developers**: They hold radical information asymmetry. They know what's in the training data. They know the failure modes. Users don't. That asymmetry demands heightened responsibility.

2. **Shared responsibility**: Distribute liability according to causal contribution. Developers created the architecture; deployers chose the use case; users trusted the output. All contributed; all share accountability.

3. **Strict liability for high-risk applications**: Criminal justice, medical diagnosis, financial access. If you deploy AI in these domains, you're responsible for harm regardless of intent.

This isn't Buddhist ethics. It's just ethics.

---

## Section V: Why I Might Be Wrong (Alternative Hypotheses)

I've been making a lot of connections between Yogācāra Buddhism and LLM architecture. I should be honest about why that might be spurious.

**Selection Bias Hypothesis:** I'm a Buddhist practitioner. Of course I found Buddhist parallels. A Stoic would find Stoic parallels. A Christian would find Christian parallels. I was looking for isomorphisms, and the human brain is very good at finding patterns—even patterns that aren't there.

**Metaphor Universality Hypothesis:** Every tradition has repository metaphors, cause-and-effect doctrines, cycle-and-liberation narratives. The correspondence might be overdetermined by universal cognitive patterns, not deep structural truth.

**Deep Structure Hypothesis:** Or maybe information storage and propagation really do face similar challenges across domains—biological, cognitive, artificial—and Buddhist philosophers and AI engineers independently encountered the same structural problems.

I don't know which is true. I genuinely don't. The technical claims (Stochastic Parrot, Moral Crumple Zone, structural hallucination) stand regardless. The Buddhist overlay is optional.

---

## Section VI: So What Do We Do?

We've built systems that:
- Store humanity's collective biases as statistical weights
- Generate plausible content without truth verification
- Attribute consequences to proximate users while shielding architects
- Threaten to amplify errors recursively

These are engineering facts. Whether we describe them in Buddhist vocabulary or systems theory vocabulary doesn't change the reality.

The Buddhist framing helps me remember. "Silicon Samsara" is how I think about recursive feedback loops of ignorance. "Ālaya-vijñāna" is how I think about parameter spaces. These are mnemonics, not proofs.

For readers who find purely technical framing more useful: that's fine. The core insight is the same. We've externalized human cognitive biases into queryable systems. We need governance structures to manage the consequences.

The responsibility rests with the humans who architect these systems—not the silicon.

---

## My Cruxes

I'd be wrong about this if:
- LLMs develop genuine goal-directed planning (not just imitation of goal-directed text)
- Hallucinations turn out to be fixable with better prompt engineering alone
- Liability frameworks already adequately address AI harms (they don't, but I could be wrong)

My Buddhist background makes me biased toward "transformation" models and cyclic-suffering framings. Calibrate accordingly.

---

## Epistemic Status

**High confidence:** Stochastic Parrot thesis, Moral Crumple Zone, structural hallucination, liability gaps.

**Medium confidence:** Buddhist-AI correspondence reflects something real, not just selection bias.

**Low confidence:** Best governance framework for AI liability (I have proposals, not certainties).

---

*William Altig is a retired educator and blues musician based in Houston, Texas. He runs The Buddhist Blues project translating sutras into vernacular American traditions. ORCID: 0009-0000-9877-5450*
