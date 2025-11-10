# Identity Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/identity`

Defines concepts related to the identity of AI Agents, including DIDs and key management.

## Classes

### `AgentIdentity`

**IRI:** `https://ns.slashlife.ai/agent/identity#AgentIdentity`

Represents the verifiable identity of an AI Agent.

### `DecentralizedIdentifier`

**IRI:** `https://ns.slashlife.ai/agent/identity#DecentralizedIdentifier`

A Decentralized Identifier (DID) associated with an Agent.

### `KeyManagementSystem`

**IRI:** `https://ns.slashlife.ai/agent/identity#KeyManagementSystem`

A system responsible for managing cryptographic keys for an Agent.

## Properties

### `hasDID`

**IRI:** `https://ns.slashlife.ai/agent/identity#hasDID`

**Domain:** `https://ns.slashlife.ai/agent/identity#AgentIdentity`

**Range:** `https://ns.slashlife.ai/agent/identity#DecentralizedIdentifier`

Links an AgentIdentity to its Decentralized Identifier.

### `managedByKMS`

**IRI:** `https://ns.slashlife.ai/agent/identity#managedByKMS`

**Domain:** `https://ns.slashlife.ai/agent/identity#AgentIdentity`

**Range:** `https://ns.slashlife.ai/agent/identity#KeyManagementSystem`

Indicates the Key Management System responsible for an Agent's keys.

### `did`

**IRI:** `https://ns.slashlife.ai/agent/identity#did`

**Domain:** `https://ns.slashlife.ai/agent/identity#AgentIdentity`

**Range:** `http://www.w3.org/2001/XMLSchema#string`

The string value of the Decentralized Identifier.

### `kmsEndpoint`

**IRI:** `https://ns.slashlife.ai/agent/identity#kmsEndpoint`

**Domain:** `https://ns.slashlife.ai/agent/identity#KeyManagementSystem`

**Range:** `http://www.w3.org/2001/XMLSchema#anyURI`

The endpoint URI for the Key Management System.

