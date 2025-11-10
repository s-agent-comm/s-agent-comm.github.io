# Intent Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/intent`

Defines concepts related to the semantic expression of purpose and objectives for AI Agent actions.

## Classes

### `ActionType`

**IRI:** `https://ns.slashlife.ai/agent/intent#ActionType`

Category of an actionable execution unit.

### `Intent`

**IRI:** `https://ns.slashlife.ai/agent/intent#Intent`

A semantic statement expressing what an agent aims to achieve.

### `IntentParameter`

**IRI:** `https://ns.slashlife.ai/agent/intent#IntentParameter`

Typed parameters specifying the scope and execution conditions of an intent.

### `IntentType`

**IRI:** `https://ns.slashlife.ai/agent/intent#IntentType`

Categorizes an intent (e.g., fetch-data, make-decision, generate-artifact).

## Properties

### `authorizedBy`

**IRI:** `https://ns.slashlife.ai/agent/intent#authorizedBy`

**Domain:** `https://ns.slashlife.ai/agent/intent#Intent`

**Range:** `https://ns.slashlife.ai/agent/delegation#Delegation`

Links an intent to the delegation statement that authorizes it.

### `loggedAs`

**IRI:** `https://ns.slashlife.ai/agent/intent#loggedAs`

**Domain:** `https://ns.slashlife.ai/agent/core#Action`

**Range:** `https://ns.slashlife.ai/agent/ledger#RuntimeLedgerRecord`

Links an executed action to its ledger record.

