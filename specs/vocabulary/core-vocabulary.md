# Core Agent Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/core`

The foundational ontology for AI Agent semantics, defining core concepts for communication, delegation, and execution.

## Classes

### `Action`

**IRI:** `https://ns.slashlife.ai/agent/core#Action`

A concrete execution event initiated by an Agent, producing observable or verifiable consequences.

### `Agent`

**IRI:** `https://ns.slashlife.ai/agent/core#Agent`

An autonomous actor capable of perceiving, interpreting, or executing actions within a delegated semantic environment.

### `AgentEntity`

**IRI:** `https://ns.slashlife.ai/agent/core#AgentEntity`

A general semantic entity participating in agent communication, delegation, or execution.

### `Artifact`

**IRI:** `https://ns.slashlife.ai/agent/core#Artifact`

A produced output or result generated through agent execution.

### `Capability`

**IRI:** `https://ns.slashlife.ai/agent/core#Capability`

A describable functional competence or operational capacity of an Agent.

### `Delegation`

**IRI:** `https://ns.slashlife.ai/agent/core#Delegation`

A structured semantic relation where one Agent authorizes another to act within a defined scope.

### `ExecutionContext`

**IRI:** `https://ns.slashlife.ai/agent/core#ExecutionContext`

A contextual frame describing conditions, trust anchors, or constraints associated with an Agent action.

### `Intent`

**IRI:** `https://ns.slashlife.ai/agent/core#Intent`

A semantic expression of purpose, objective, or expected action outcome.

### `Task`

**IRI:** `https://ns.slashlife.ai/agent/core#Task`

A well-defined action unit exchanged between Agents.

### `TaskDependency`

**IRI:** `https://ns.slashlife.ai/agent/core#TaskDependency`

Dependency relation in a task graph.

### `TaskNode`

**IRI:** `https://ns.slashlife.ai/agent/core#TaskNode`

Node in a task dependency graph.

### `TraceEvent`

**IRI:** `https://ns.slashlife.ai/agent/core#TraceEvent`

A verifiable record linking an Agent, an Action, and contextual constraints.

## Properties

### `contextOf`

**IRI:** `https://ns.slashlife.ai/agent/core#contextOf`

**Domain:** `https://ns.slashlife.ai/agent/core#ExecutionContext`

**Range:** `https://ns.slashlife.ai/agent/core#Action`

Indicates that an ExecutionContext applies to a specific Action.

### `delegatedBy`

**IRI:** `https://ns.slashlife.ai/agent/core#delegatedBy`

**Domain:** `https://ns.slashlife.ai/agent/core#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#Agent`

Indicates the Agent granting delegated authority.

### `delegatesTo`

**IRI:** `https://ns.slashlife.ai/agent/core#delegatesTo`

**Domain:** `https://ns.slashlife.ai/agent/core#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#Agent`

Indicates the Agent receiving delegated authority.

### `delegationScope`

**IRI:** `https://ns.slashlife.ai/agent/core#delegationScope`

**Domain:** `https://ns.slashlife.ai/agent/core#Delegation`

**Range:** `https://ns.slashlife.ai/agent/core#Capability`

Specifies the scope of allowed capabilities within a Delegation relation.

### `executesAction`

**IRI:** `https://ns.slashlife.ai/agent/core#executesAction`

**Domain:** `https://ns.slashlife.ai/agent/core#Agent`

**Range:** `https://ns.slashlife.ai/agent/core#Action`

Associates an Agent with an Action it performs.

### `hasCapability`

**IRI:** `https://ns.slashlife.ai/agent/core#hasCapability`

**Domain:** `https://ns.slashlife.ai/agent/core#Agent`

**Range:** `https://ns.slashlife.ai/agent/core#Capability`

Associates an Agent with a Capability it is able to perform.

### `hasDependency`

**IRI:** `https://ns.slashlife.ai/agent/core#hasDependency`

**Domain:** `https://ns.slashlife.ai/agent/core#TaskNode`

**Range:** `https://ns.slashlife.ai/agent/core#TaskNode`

Represents a dependency between task nodes.

### `hasIntent`

**IRI:** `https://ns.slashlife.ai/agent/core#hasIntent`

**Domain:** `https://ns.slashlife.ai/agent/core#Agent`

**Range:** `https://ns.slashlife.ai/agent/core#Intent`

Associates an Agent with its intended objective or semantic purpose.

### `hasSubtask`

**IRI:** `https://ns.slashlife.ai/agent/core#hasSubtask`

**Domain:** `https://ns.slashlife.ai/agent/core#Task`

**Range:** `https://ns.slashlife.ai/agent/core#Task`

Represents hierarchical task decomposition.

### `performsTask`

**IRI:** `https://ns.slashlife.ai/agent/core#performsTask`

**Domain:** `https://ns.slashlife.ai/agent/core#Agent`

**Range:** `https://ns.slashlife.ai/agent/core#Task`

An Agent performs a given Task.

### `producesArtifact`

**IRI:** `https://ns.slashlife.ai/agent/core#producesArtifact`

**Domain:** `https://ns.slashlife.ai/agent/core#Action`

**Range:** `https://ns.slashlife.ai/agent/core#Artifact`

Specifies the Artifact produced by an Action.

### `recordedIn`

**IRI:** `https://ns.slashlife.ai/agent/core#recordedIn`

**Domain:** `https://ns.slashlife.ai/agent/core#Action`

**Range:** `https://ns.slashlife.ai/agent/core#TraceEvent`

Links an Action to its verifiable trace record.

### `requiresCapability`

**IRI:** `https://ns.slashlife.ai/agent/core#requiresCapability`

**Domain:** `https://ns.slashlife.ai/agent/core#Task`

**Range:** `https://ns.slashlife.ai/agent/core#Capability`

Declares that a Task requires a specific Capability.

### `description`

**IRI:** `https://ns.slashlife.ai/agent/core#description`

**Domain:** `https://ns.slashlife.ai/agent/core#Artifact`

**Range:** `http://www.w3.org/2001/XMLSchema#string`

A human-readable description of an Artifact.

### `timestamp`

**IRI:** `https://ns.slashlife.ai/agent/core#timestamp`

**Domain:** `https://ns.slashlife.ai/agent/core#TraceEvent`

**Range:** `http://www.w3.org/2001/XMLSchema#dateTime`

Timestamp corresponding to the trace event.

