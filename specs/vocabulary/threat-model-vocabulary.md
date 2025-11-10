# Minimal Agent Semantic Communication Ontology Vocabulary

**Namespace:** `https://slashlife.ai/ontology/agent-semantic-communication#`

Ontology for minimal semantic interoperability and threat modeling among AI Agents.

## Classes

### `Agent`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

An autonomous computational entity capable of semantic communication.

### `Capability`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#Capability`

A functional ability that an Agent claims or possesses.

### `Delegation`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#Delegation`

An assignment of authority or responsibility between Agents.

### `Intent`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#Intent`

A purpose or goal communicated by an Agent.

### `Task`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

A well-defined action unit exchanged between Agents.

### `TaskDependency`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#TaskDependency`

Dependency relation in a task graph.

### `TaskNode`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#TaskNode`

Node in a task dependency graph.

## Properties

### `IntentAlignsWithTask`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#IntentAlignsWithTask`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Intent`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

Links expressed Intent to the Task it authorizes or motivates.

### `delegatedFrom`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#delegatedFrom`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Delegation`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

Specifies the Agent delegating a task or authority.

### `delegatedTo`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#delegatedTo`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Delegation`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

Specifies the Agent to whom a task or authority is delegated.

### `delegatesTask`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#delegatesTask`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

An Agent delegates a specific Task to another Agent.

### `expressesIntent`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#expressesIntent`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Intent`

An Agent expresses a certain Intent.

### `hasCapability`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#hasCapability`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Capability`

Declares that an Agent possesses a specific Capability.

### `hasDependency`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#hasDependency`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#TaskNode`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#TaskNode`

Represents a dependency between task nodes.

### `hasSubtask`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#hasSubtask`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

Represents hierarchical task decomposition.

### `performsTask`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#performsTask`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Agent`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

An Agent performs a given Task.

### `requiresCapability`

**IRI:** `https://slashlife.ai/ontology/agent-semantic-communication#requiresCapability`

**Domain:** `https://slashlife.ai/ontology/agent-semantic-communication#Task`

**Range:** `https://slashlife.ai/ontology/agent-semantic-communication#Capability`

Declares that a Task requires a specific Capability.

