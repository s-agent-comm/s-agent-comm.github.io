# Delegation Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/delegation`

Defines the structured transfer of authority between AI Agents, including scope, actors, and constraints.

## Classes

### `Delegation`

**IRI:** `https://ns.slashlife.ai/agent/delegation#Delegation`


    Represents a structured transfer of authority, allowing one Agent to act 
    under a bounded, semantically defined scope on behalf of another Agent.
    

### `DelegationChain`

**IRI:** `https://ns.slashlife.ai/agent/delegation#DelegationChain`


    A sequence of Delegation instances forming a multi-level authority graph.
    Useful for modeling nested or transitive delegation across agents.
    

### `DelegationScope`

**IRI:** `https://ns.slashlife.ai/agent/delegation#DelegationScope`


    Defines the semantic boundaries of delegated authority, including 
    capability constraints, intent framing, and operational limits.
    

### `ExecutionConstraint`

**IRI:** `https://ns.slashlife.ai/agent/delegation#ExecutionConstraint`

Operational or environmental constraints limiting the delegate's permissible actions.

## Properties

### `accountableFor`

**IRI:** `https://ns.slashlife.ai/agent/delegation#accountableFor`

**Domain:** `https://ns.slashlife.ai/agent/delegation#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#Action`

Connects a Delegation to the Actions executed under that delegated authority.

### `allowedCapability`

**IRI:** `https://ns.slashlife.ai/agent/delegation#allowedCapability`

**Domain:** `https://ns.slashlife.ai/agent/delegation#DelegationScope`

**Range:** `https://ns.slashlife.ai/agent/capability#Capability`

Capabilities the delegated Agent is authorized to perform.

### `delegatedBy`

**IRI:** `https://ns.slashlife.ai/agent/delegation#delegatedBy`

**Domain:** `https://ns.slashlife.ai/agent/delegation#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#Agent`

Agent granting the authority.

### `delegatesTo`

**IRI:** `https://ns.slashlife.ai/agent/delegation#delegatesTo`

**Domain:** `https://ns.slashlife.ai/agent/delegation#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#Agent`

Agent receiving delegated authority.

### `intentConstraint`

**IRI:** `https://ns.slashlife.ai/agent/delegation#intentConstraint`

**Domain:** `https://ns.slashlife.ai/agent/delegation#DelegationScope`

**Range:** `https://ns.slashlife.ai/agent/core#Intent`

Specifies the intent boundary under which the delegate may operate.

### `recordedIn`

**IRI:** `https://ns.slashlife.ai/agent/delegation#recordedIn`

**Domain:** `https://ns.slashlife.ai/agent/delegation#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#TraceEvent`

Records delegation-related events within the semantic accountability chain.

