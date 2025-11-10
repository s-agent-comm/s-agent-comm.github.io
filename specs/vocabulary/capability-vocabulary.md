# Capability Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/capability`

Defines the structure and properties for describing an AI Agent's functional competences and operational capacities.

## Classes

### `Capability`

**IRI:** `https://ns.slashlife.ai/agent/capability#Capability`


    A functional competence of an Agent. Describes an operation, method,
    or action family that can be executed under explicit identity and context.
    

### `CapabilityClass`

**IRI:** `https://ns.slashlife.ai/agent/capability#CapabilityClass`


    Categorizes capability types, useful for policy, delegation, or competency grouping.
    

### `CapabilityConstraint`

**IRI:** `https://ns.slashlife.ai/agent/capability#CapabilityConstraint`


    Restrictions on the use of a capability, including safety,
    context limitations, or policy-bound execution gates.
    

### `CapabilityProvenance`

**IRI:** `https://ns.slashlife.ai/agent/capability#CapabilityProvenance`

Captures origin, version, or derivation lineage of a capability.

### `CompositeCapability`

**IRI:** `https://ns.slashlife.ai/agent/capability#CompositeCapability`


    Aggregates multiple capabilities into a higher-level operational construct.
    Used for modeling workflows, multi-step tasks, or protocol sequences.
    

### `ExecutionPattern`

**IRI:** `https://ns.slashlife.ai/agent/capability#ExecutionPattern`


    Formal structure describing expected execution behavior,
    including determinism, interaction, or dependency modes.
    

### `InputSchema`

**IRI:** `https://ns.slashlife.ai/agent/capability#InputSchema`

Defines required input structure for capability invocation.

### `OutputSchema`

**IRI:** `https://ns.slashlife.ai/agent/capability#OutputSchema`

Defines generated output structure for capability execution.

### `PrimitiveCapability`

**IRI:** `https://ns.slashlife.ai/agent/capability#PrimitiveCapability`

Indivisible functional element representing a minimal semantic operation.

## Properties

### `dependsOnCapability`

**IRI:** `https://ns.slashlife.ai/agent/capability#dependsOnCapability`

**Domain:** `https://ns.slashlife.ai/agent/capability#Capability`

**Range:** `https://ns.slashlife.ai/agent/capability#Capability`

Declares capability-level dependencies within an agent or delegation scope.

### `includes`

**IRI:** `https://ns.slashlife.ai/agent/capability#includes`

**Domain:** `https://ns.slashlife.ai/agent/capability#CompositeCapability`

**Range:** `https://ns.slashlife.ai/agent/capability#Capability`

Capability elements that form part of a composite capability.

### `allowedContext`

**IRI:** `https://ns.slashlife.ai/agent/capability#allowedContext`

**Domain:** `https://ns.slashlife.ai/agent/capability#CapabilityConstraint`

**Range:** `http://www.w3.org/2001/XMLSchema#string`

Context(s) in which capability execution is permitted.

