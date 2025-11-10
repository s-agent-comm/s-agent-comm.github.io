# Security Binding Ontology Vocabulary

**Namespace:** `https://ns.slashlife.ai/agent/security-binding`

Defines concepts for security binding, trust chains, and threat mitigation in AI Agent systems.

## Classes

### `AccessControlRule`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#AccessControlRule`

A rule that specifies permissions for an agent or role to perform an action on a resource.

### `DataHandlingPolicy`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#DataHandlingPolicy`

A policy governing the processing, storage, and transmission of data.

### `HardwareRootOfTrust`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#HardwareRootOfTrust`

TEE / TPM / Secure Element providing attested identity and execution guarantees.

### `KeyMaterial`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#KeyMaterial`

A cryptographic key associated with an agent identity.

### `KeyType`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#KeyType`

Specifies the cryptographic algorithm or format (Ed25519, RSA, secp256k1).

### `SecurityBinding`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#SecurityBinding`

Represents the chain binding DID → Key Material → Hardware → Ledger verification.

### `TrustAnchor`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#TrustAnchor`

A root-level verifier or certificate authority validating hardware attestation.

## Properties

### `IntentAlignsWithTask`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#IntentAlignsWithTask`

**Domain:** `https://ns.slashlife.ai/agent/core#Intent`

**Range:** `https://ns.slashlife.ai/agent/core#Task`

Links expressed Intent to the Task it authorizes or motivates.

### `signsRecord`

**IRI:** `https://ns.slashlife.ai/agent/security-binding#signsRecord`

**Domain:** `https://ns.slashlife.ai/agent/security-binding#KeyMaterial`

**Range:** `https://ns.slashlife.ai/agent/ledger#LedgerRecord`

Indicates ledger entries signed using this key material.

