# Agent Profile Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/agent-profile`

Defines the pragmatic and behavioral parameters of an autonomous AI Agent, including personality, language, and tone models.

## Classes

### `Agent Profile`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#AgentProfile`


    Defines the pragmatic and behavioral parameters of an autonomous Agent.

    While operational semantics (identity, capability, delegation, ledger)
    describe what an Agent *can* do, the AgentProfile describes *how* it behaves:
    linguistic preferences, tone patterns, and personality-like behavioral biases.

    This layer influences task decomposition, intent interpretation,
    and multi-agent coordination stability. It is not executable semantics,
    but a stable behavioral descriptor.
    

### `Language Preference`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#LanguagePreference`


    Linguistic parameters suchs as preferred language, register, clarity constraints,
    or structural tendencies affecting expression and parsing.
    

### `Personality`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#Personality`


    A stable behavioral schema shaping decision preference, risk style,
    response architecture, and interaction patterns.
    

### `Tone Model`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#ToneModel`


    Pragmatic modulation model guiding emotional stance, pacing, softness/firmness,
    or collaborative rhythm.
    

## Properties

### `has personality profile`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#hasPersonality`

**Domain:** `https://ns.slashlife.ai/agent/agent-profile#AgentProfile`

**Range:** `https://ns.slashlife.ai/agent/agent-profile#Personality`

Describes behavioral bias patterns shaping interaction and task choices.

### `tone model`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#hasToneModel`

**Domain:** `https://ns.slashlife.ai/agent/agent-profile#AgentProfile`

**Range:** `https://ns.slashlife.ai/agent/agent-profile#ToneModel`

Describes pragmatics: cadence, pacing, assertiveness, contextual modulation.

### `language preference`

**IRI:** `https://ns.slashlife.ai/agent/agent-profile#usesLanguage`

**Domain:** `https://ns.slashlife.ai/agent/agent-profile#AgentProfile`

**Range:** `https://ns.slashlife.ai/agent/agent-profile#LanguagePreference`

Defines preferred linguistic expression, grammar formality, and interaction mode.

