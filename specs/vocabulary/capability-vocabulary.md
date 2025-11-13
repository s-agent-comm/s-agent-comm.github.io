# Capability Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/capability`
**Prefix:** `cap`

Defines the structure and properties for describing an AI Agent's functional competences and operational capacities, distinguishing between high-level semantic Capabilities and atomic, executable Skills.

## Classes

### `Capability`

**IRI:** `https://ns.slashlife.ai/agent/capability#Capability`
**Subclass Of:** `https://ns.slashlife.ai/agent/core#Capability`

A high-level, declarative, and semantically rich description of an Agent's functional competence or operational capacity. Capabilities are designed for semantic matching and high-level planning by LLMs.

### `Skill`

**IRI:** `https://ns.slashlife.ai/agent/capability#Skill`

An atomic, machine-executable function or API call that an Agent can perform. Skills are the concrete, auditable units of execution.

### `Parameter`

**IRI:** `https://ns.slashlife.ai/agent/capability#Parameter`

Defines a single input or output parameter for a `cap:Skill`, including its name, data type, and description.

## Properties

### `capabilityExpression`

**IRI:** `https://ns.slashlife.ai/agent/capability#capabilityExpression`
**Domain:** `https://ns.slashlife.ai/agent/capability#Capability`
**Range:** `http://www.w3.org/2001/XMLSchema#string`

A natural language description of the capability, suitable for vector embedding and fuzzy matching by LLMs.

### `hasSkill`

**IRI:** `https://ns.slashlife.ai/agent/capability#hasSkill`
**Domain:** `https://ns.slashlife.ai/agent/capability#Capability`
**Range:** `https://ns.slashlife.ai/agent/capability#Skill`

Links a high-level `cap:Capability` to one or more atomic `cap:Skill`s that implement it.

### `function`

**IRI:** `https://ns.slashlife.ai/agent/capability#function`
**Domain:** `https://ns.slashlife.ai/agent/capability#Skill`
**Range:** `http://www.w3.org/2001/XMLSchema#string`

The name of the executable function or API endpoint that this skill invokes.

### `hasParameter`

**IRI:** `https://ns.slashlife.ai/agent/capability#hasParameter`
**Domain:** `https://ns.slashlife.ai/agent/capability#Skill`
**Range:** `https://ns.slashlife.ai/agent/capability#Parameter`

Links a `cap:Skill` to its input or output parameters.

### `name`

**IRI:** `https://ns.slashlife.ai/agent/capability#name`
**Domain:** `https://ns.slashlife.ai/agent/capability#Parameter`
**Range:** `http://www.w3.org/2001/XMLSchema#string`

The name of the parameter.

### `datatype`

**IRI:** `https://ns.slashlife.ai/agent/capability#datatype`
**Domain:** `https://ns.slashlife.ai/agent/capability#Parameter`
**Range:** `http://www.w3.org/2001/XMLSchema#string`

The expected data type of the parameter (e.g., `xsd:string`, `xsd:integer`, `application/json`).

### `description`

**IRI:** `https://ns.slashlife.ai/agent/capability#description`
**Domain:** `https://ns.slashlife.ai/agent/capability#Parameter`
**Range:** `http://www.w3.org/2001/XMLSchema#string`

A human-readable description of the parameter's purpose.

### `required`

**IRI:** `https://ns.slashlife.ai/agent/capability#required`
**Domain:** `https://ns.slashlife.ai/agent/capability#Parameter`
**Range:** `http://www.w3.org/2001/XMLSchema#boolean`

Indicates whether the parameter is mandatory for the skill's execution.