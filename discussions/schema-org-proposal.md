# Proposal for Hosted Extension: Agent Ontology

## 1. Motivation

This proposal suggests the inclusion of the **Agent Ontology** as a hosted extension to Schema.org. The Agent Ontology is a project by the [W3C Semantic Agent Communication Community Group (SAC-CG)](https://www.w3.org/community/s-agent-comm/), designed to provide a standard, interoperable vocabulary for describing the identity, capabilities, and operational semantics of AI Agents.

As AI agents become more prevalent on the web, there is a growing need for a standardized way to describe them. This allows for:
- **Enhanced Discoverability**: Search engines can understand what an AI Agent is, what it can do, and how to interact with it, leading to richer search results and better user experiences.
- **Interoperability**: A common vocabulary enables different agent platforms, marketplaces, and tools to seamlessly exchange information about agents.
- **Trust and Accountability**: Standardized descriptions of an agent's identity, ownership, and capabilities are foundational for building trustworthy and accountable AI systems.

By integrating with Schema.org, the Agent Ontology can leverage the vast existing ecosystem of tools and platforms, making it easier for developers to adopt and for search engines to consume.

## 2. Link to Ontology and Documentation

- **Stable Namespace URI**: `https://w3id.org/agent-ontology/`
- **GitHub Repository (Source of Truth)**: [https://github.com/w3c-cg/agent-ontology](https://github.com/w3c-cg/agent-ontology)
- **Human-Readable Documentation (Generated)**: [https://s-agent-comm.github.io/agent-ontology/](https://s-agent-comm.github.io/agent-ontology/)

The ontology is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), which is compatible with Schema.org's terms.

## 3. Core Concepts

The Agent Ontology defines several core concepts:

- **Agent (`agent:Agent`)**: An autonomous entity with a verifiable identity (e.g., DID) that can perform actions. Mapped as a subclass of `schema:SoftwareApplication` and `schema:Service`.
- **Person (`agent:Person`)**: Represents a human agent. Mapped as a subclass of `schema:Person`.
- **Organization (`agent:Organization`)**: Represents an organizational agent. Mapped as a subclass of `schema:Organization`.
- **Capability (`cap:Capability`)**: A high-level, semantic description of a function an agent can perform (e.g., "book a flight"). Mapped as a subclass of `schema:Action`. The property `core:hasCapability` is mapped as a subproperty of `schema:potentialAction`.
- **Skill (`cap:Skill`)**: A specific, machine-executable operation that implements a capability, with defined parameters (e.g., an API call). Mapped as a subclass of `schema:Action`.
- **Intent (`intent:Intent`)**: A semantic expression of purpose or a goal that an agent aims to achieve. Mapped as a subclass of `schema:Intent`.
- **Core Action (`core:Action`)**: A general action performed by an agent. Mapped as a subclass of `schema:Action`.
- **Agent Relationship (`del:AgentRelationship`)**: Describes a relationship or delegation between agents. Mapped as a subclass of `schema:Role`.
- **Contract (`contract:Contract`)**: Represents a formal agreement between agents. Mapped as a subclass of `schema:Contract`.
- **Ledger Event (`ledger:LedgerEvent`)**: An event recorded on a ledger. Mapped as a subclass of `schema:Event`.
- **Agent Objective (`agent:objective`)**: The purpose or goal of an agent. Mapped as a subproperty of `schema:description`.
- **Identity Title (`id:title`)**: A title or name associated with an agent's identity. Mapped as a subproperty of `schema:name`.

## 4. Example Usage (JSON-LD)

Here is a practical example of how a developer could use the combined vocabularies to describe a "Travel Agent Bot" on their website.

```html
<script type="application/ld+json">
{
  "@context": {
    "schema": "http://schema.org/",
    "agent": "https://w3id.org/agent-ontology/agent#",
    "cap": "https://w3id.org/agent-ontology/capability#",
    "id": "https://w3id.org/agent-ontology/identity#"
  },
  "@type": ["schema:SoftwareApplication", "agent:Agent"],
  "schema:name": "Travel Agent Bot",
  "schema:description": "An AI-powered assistant to help you find and book flights and hotels.",
  "schema:author": {
    "@type": "schema:Organization",
    "schema:name": "Global Travel Inc."
  },
  "agent:hasIdentity": {
    "@type": "id:AgentIdentity",
    "id:did": "did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH",
    "id:title": "Travel Agent Bot Identity"
  },
  "agent:purposeAndRole": {
    "@type": "agent:PurposeRole",
    "agent:objective": "Facilitate travel bookings for users."
  },
  "core:hasCapability": [
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Find and book flights",
      "cap:hasSkill": [
        {
          "@type": "cap:Skill",
          "cap:skillId": "api.travel.searchFlights",
          "cap:description": "Searches for available flights between two cities on a given date.",
          "cap:hasParameter": [
            { "cap:parameterName": "origin", "cap:parameterType": "schema:City" },
            { "cap:parameterName": "destination", "cap:parameterType": "schema:City" },
            { "cap:parameterName": "departureDate", "cap:parameterType": "schema:Date" }
          ]
        }
      ]
    },
    {
      "@type": "cap:Capability",
      "cap:capabilityExpression": "Find hotel accommodations"
    }
  ]
}
</script>

This example demonstrates how `schema.org` properties (`name`, `description`, `author`) can be used for general description, while the `agent-ontology` vocabulary provides the specialized, structured details about the agent's identity and functional capabilities.

## 5. Relationship with Technical Specifications (e.g., OpenAPI)

It is important to clarify that the Agent Ontology provides a **semantic description** of AI Agents and their capabilities, rather than a direct technical specification for API implementation.

-   **Agent Ontology (Semantic Layer)**: Defines *what* an Agent is, *what* its capabilities are, and *why* it performs certain actions. It establishes a common, machine-readable vocabulary for high-level understanding, discoverability, and interoperability across different agent systems. This is akin to a "menu" describing available services.
-   **OpenAPI (Technical Implementation Layer)**: Defines *how* a specific `cap:Skill` or action is technically implemented and executed. This includes details like API endpoints, request/response formats, authentication, and data schemas. This is akin to a "recipe" or "technical manual" for executing a specific task.

The two are complementary: the Agent Ontology provides the semantic context that allows systems to discover and understand an agent's potential, while OpenAPI (or similar specifications like AsyncAPI, GraphQL schemas) provides the precise technical instructions for interacting with that agent's underlying services. The ontology does not directly generate OpenAPI specifications but provides the semantic hooks (e.g., `cap:skillId`) that can be used to link to such technical documentation.

## 6. Community and Maintenance

The Agent Ontology is actively maintained by the W3C Semantic Agent Communication Community Group. We are committed to the long-term stability and evolution of this vocabulary in alignment with the needs of the AI and web developer communities.

We believe that making the Agent Ontology a hosted extension of Schema.org will be a significant step towards a more interoperable and discoverable ecosystem of AI agents on the web. We welcome feedback and are happy to answer any questions.