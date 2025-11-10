---
title: Minimal Threat Model for Agent Semantic Communication
shortname: minimal-threat-model
status: ED
group: Agent Semantic Communication Community Group
date: 2025-11-10
editors:
  - name: W3C Agent Semantic Communication Community Group
    url: https://www.w3.org/community/asccg/
    affiliation: W3C Agent Semantic Communication CG
---

<div class="head">
<p><a href="https://www.w3.org/"><img src="https://www.w3.org/Icons/w3c_home" alt="W3C" width="72" height="48"></a></p>
<h1>Minimal Threat Model for Agent Semantic Communication</h1>
<h2 id="w3c-status">W3C Editor's Draft, 10 November 2025</h2>
<dl>
  <dt>This version:</dt>
  <dd><a href="https://github.com/slashlifeai/agent-ontology/specs/minimal-threat-model.md">https://github.com/slashlifeai/agent-ontology/specs/minimal-threat-model.md</a></dd>
  <dt>Latest published version:</dt>
  <dd>Not yet published</dd>
  <dt>Editors:</dt>
  <dd>
    <a href="https://www.w3.org/community/asccg/">W3C Agent Semantic Communication Community Group</a>
  </dd>
</dl>
<p class="copyright"><a href="https://www.w3.org/Consortium/Legal/ipr-notice#Copyright">Copyright</a> © 2025 <a href="https://www.w3.org/"><abbr title="World Wide Web Consortium">W3C</abbr></a><sup>®</sup> (<a href="https://www.csail.mit.edu/"><abbr title="Massachusetts Institute of Technology">MIT</abbr></a>, <a href="https://www.ercim.eu/"><abbr title="European Research Consortium for Informatics and Mathematics">ERCIM</abbr></a>, <a href="https://www.keio.ac.jp/">Keio</a>, <a href="https://ev.buaa.edu.cn/">Beihang</a>). W3C <a href="https://www.w3.org/Consortium/Legal/ipr-notice#Legal_Disclaimer">liability</a>, <a href="https://www.w3.org/Consortium/Legal/ipr-notice#W3C_Trademarks">trademark</a> and <a href="https://www.w3.org/Consortium/Legal/copyright-documents">document use</a> rules apply.</p>
</div>

<hr>

# W3C Agent Semantic Communication CG — Minimal Threat Model v0.2

This model describes the fundamental risks encountered when agents exchange information using semantic structures. It has been enhanced to include mitigation strategies, severity levels, and expanded threat categories. The scope remains focused on **communication behavior**, using an ontology as a semantic reference point for standardization.

---

## 1. Purpose

To provide a minimal yet actionable classification of threats, enabling semantic exchanges between agents to maintain:

-   **Basic Understandability:** Ensuring the meaning of exchanged data is preserved.
-   **Basic Consistency:** Ensuring actions and interpretations do not contradict each other.
-   **Basic Security Boundaries:** Ensuring the scope of authority and capability is respected.

This model can be used to:

-   Inform the design of secure agent communication protocols.
-   Develop a minimal consistency model for semantic dialogue interfaces.
-   Establish a cross-system foundation for interoperable and secure agent behavior.

---

## 2. Core Assumptions

1.  **Identifiable Identity:** Every agent possesses a recognizable identity (e.g., DID, cryptographic key).
2.  **Describable Capabilities:** Every agent has a description of its capabilities.
3.  **Semantic Data Format:** Exchanged data exists in a semantic format (e.g., based on a vocabulary or ontology).
4.  **Cross-Domain Communication:** Communication may occur across different domains, environments, and platforms.

---

## 3. Threat Categories

The following categories represent a "minimally necessary" set of threats. They are implementation-agnostic and apply to all AI agent communication scenarios.

### 3.1. Semantic Misalignment Threats

-   **Description:** Occurs when agents use the same data format but interpret its semantics differently (e.g., same property has different meanings).
-   **Severity:** `Medium`
-   **Impact:** Communication succeeds, but the intent is misplaced, leading to subsequent erroneous behavior.
-   **Ontology Reference Points:** `Class`, `Property`, `Domain`, `Range`, `Axiom`
-   **Mitigation Strategies:**
    -   Use shared, version-controlled ontologies.
    -   Explicitly declare the ontology and its version in communication headers.
    -   Implement ontology mapping services for cross-domain communication.

### 3.2. Intent Ambiguity Threats

-   **Description:** Occurs when an agent's message is syntactically correct, but its purpose is unclear or conflicts with its stated goal.
-   **Severity:** `High`
-   **Impact:** Downstream agents are unable to construct a consistent and safe Task Directed Acyclic Graph (DAG).
-   **Ontology Reference Points:** `Action`, `Goal`, `Intent`, `requiresCapability`
-   **Mitigation Strategies:**
    -   Enforce a formal link between `Intent` and `Task` using properties like `sec:IntentAlignsWithTask`.
    -   Require delegation requests to explicitly reference the `Capability` being invoked.
    -   Use reasoners to validate that an agent's task is a logical consequence of its intent.

### 3.3. Capability Misrepresentation Threats

-   **Description:** Occurs when an agent inaccurately declares its capabilities (e.g., exaggerating or classifying them incorrectly).
-   **Severity:** `High`
-   **Impact:** Other agents may delegate incorrect tasks, leading to mission failure or security breaches.
-   **Ontology Reference Points:** `AgentRole`, `Capability`, `hasPermission`, `disjointWith`
-   **Mitigation Strategies:**
    -   Require capability declarations to be digitally signed and verifiable.
    -   Use `owl:disjointWith` axioms to prevent dangerous combinations of capabilities.
    -   Maintain a verifiable Capability Registry.

### 3.4. Task Graph Divergence Threats

-   **Description:** Occurs when multiple agents generate different DAG structures for the same high-level task.
-   **Severity:** `Medium`
-   **Impact:** Results in task chains that cannot be merged, causing system-level collaboration failures and wasted resources.
-   **Ontology Reference Points:** `Task`, `Subtask`, `Dependency`, `Process`
-   **Mitigation Strategies:**
    -   Standardize task decomposition patterns for common goals.
    -   Use a shared vocabulary for defining task nodes and dependencies.
    -   Implement consensus protocols for collaborative task planning.

### 3.5. Identity & Delegation Threats

-   **Description:** Communication risks related to identity and authorization, such as impersonation or opaque delegation chains.
-   **Severity:** `Critical`
-   **Impact:** Lack of clarity regarding responsibility, authority, and audit points, potentially leading to unauthorized system access.
-   **Ontology Reference Points:** `Agent`, `Identity`, `Delegation`, `Authority`
-   **Mitigation Strategies:**
    -   Mandate the use of DIDs for all agent identification.
    -   Implement verifiable delegation chains (e.g., chained signed assertions).
    -   Set explicit limits on delegation depth and scope.

### 3.6. Resource Exhaustion Threats

-   **Description:** A malicious or poorly designed agent consumes excessive computational resources, storage, or funds, leading to a denial of service.
-   **Severity:** `High`
-   **Impact:** The target agent or system becomes unavailable, and financial loss may occur.
-   **Ontology Reference Points:** `ResourceConstraint`, `RateLimit`, `Budget`
-   **Mitigation Strategies:**
    -   Define and enforce explicit resource constraints in the execution context.
    -   Require tasks to be associated with a budget.
    -   Implement rate limiting on incoming requests.

### 3.7. Confidentiality & Privacy Threats

-   **Description:** An agent leaks sensitive information during communication or execution, either intentionally or unintentionally.
-   **Severity:** `Critical`
-   **Impact:** Violation of data privacy, exposure of trade secrets, or compromise of system credentials.
-   **Ontology Reference Points:** `DataHandlingPolicy`, `AccessControlRule`, `EncryptionRequired`
-   **Mitigation Strategies:**
    -   Bind data handling policies to tasks and execution contexts.
    -   Enforce access control rules based on agent roles and data sensitivity.
    -   Mandate encryption for data in transit and at rest.

---

## 4. Threat Propagation Patterns

The minimal propagation model helps understand how a foundational failure can cascade:

**Semantic Misalignment** → **Task Graph Divergence** → **Delegation Ambiguity**

This progression signifies that:

1.  **Semantic inconsistency** leads to different interpretations of task decomposition.
2.  **Different task decompositions** lead to delegations to different agents or with different parameters.
3.  **Different delegations** result in misaligned authority and responsibility, potentially causing security and operational failures.

---

## Appendix: Example Scenarios

### A.1. Semantic Misalignment
-   **Scenario:** An agent in the US sends a task with `price: 1.0`, intending it as "1.0 USD". A European agent interprets it as "1.0 EUR", causing a financial discrepancy.
-   **Detection:** The receiving agent fails to find a required `currency` property alongside the `price` and rejects the task as malformed according to the shared ontology.

### A.2. Capability Misrepresentation
-   **Scenario:** A news-reading agent falsely claims it has the `writeToDatabase` capability.
-   **Impact:** A delegating agent assigns it a task to update user records, leading to data corruption.
-   **Detection:** The system checks the agent's signed capability declaration against a trusted registry and finds a mismatch.

### A.3. Identity & Delegation
-   **Scenario:** A malicious agent (`Agent C`) intercepts a delegation from `Agent A` to `Agent B` and replays it to gain access.
-   **Detection:** `Agent B` validates the delegation chain and finds that the signature is valid for `A` but the immediate sender is `C`, flagging an impersonation attempt.

### A.4. Resource Exhaustion
-   **Scenario:** An agent sends a legitimate-looking task to "analyze market data," but the provided dataset is a decompression bomb designed to consume gigabytes of memory.
-   **Detection:** The execution environment enforces a pre-defined memory limit (`ResourceConstraint`) and terminates the task before it can harm the system.
