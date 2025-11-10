# Agent Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/agent`

Defines the structure and properties of an AI Agent, including its identity, purpose, capabilities, and operational aspects.

## Classes

### `CapabilityBundle`

**IRI:** `https://ns.slashlife.ai/agent/agent#CapabilityBundle`

Declared capabilities and skills for an Agent.

### `OperationalProfile`

**IRI:** `https://ns.slashlife.ai/agent/agent#OperationalProfile`

Triggers, input schema, and output schema of an Agent.

### `PurposeRole`

**IRI:** `https://ns.slashlife.ai/agent/agent#PurposeRole`

Declares the operational purpose and ownership of the Agent.

### `SystemIntegration`

**IRI:** `https://ns.slashlife.ai/agent/agent#SystemIntegration`

Dependency and interface declarations for OS-level agent execution.

## Properties

### `has profile`

**IRI:** `https://ns.slashlife.ai/agent/agent#hasProfile`

**Domain:** `https://ns.slashlife.ai/agent/core#Agent`

**Range:** `https://ns.slashlife.ai/agent/agent-profile#AgentProfile`

Links an Agent to its pragmatic / behavioral profile.

