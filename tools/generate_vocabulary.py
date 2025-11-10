import os
from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS, OWL, DCTERMS

def generate_vocabulary_docs():
    """
    Generates Markdown documentation for ontology modules from TTL files.
    """
    ontologies_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ontologies'))
    specs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'specs', 'vocabulary'))
    
    if not os.path.exists(specs_dir):
        os.makedirs(specs_dir)

    for filename in os.listdir(ontologies_dir):
        if filename.endswith(".ttl"):
            ttl_path = os.path.join(ontologies_dir, filename)
            g = Graph()
            g.parse(ttl_path, format="turtle")

            ontology_uri = None
            for s, p, o in g.triples((None, RDF.type, OWL.Ontology)):
                ontology_uri = s
                break

            if not ontology_uri:
                continue

            title = g.value(ontology_uri, DCTERMS.title)
            description = g.value(ontology_uri, DCTERMS.description)
            
            module_name = os.path.splitext(filename)[0]
            md_path = os.path.join(specs_dir, f"{module_name}-vocabulary.md")

            with open(md_path, "w") as f:
                f.write(f"# {title} Vocabulary\n\n")
                f.write(f"**Namespace:** `{ontology_uri}`\n\n")
                f.write(f"{description}\n\n")

                f.write("## Classes\n\n")
                classes = sorted(g.subjects(RDF.type, OWL.Class))
                for c in classes:
                    label = g.value(c, RDFS.label)
                    comment = g.value(c, RDFS.comment)
                    if label and comment:
                        f.write(f"### `{label}`\n\n")
                        f.write(f"**IRI:** `{c}`\n\n")
                        f.write(f"{comment}\n\n")

                f.write("## Properties\n\n")
                properties = sorted(g.subjects(RDF.type, OWL.ObjectProperty))
                properties.extend(sorted(g.subjects(RDF.type, OWL.DatatypeProperty)))
                for p in properties:
                    label = g.value(p, RDFS.label)
                    comment = g.value(p, RDFS.comment)
                    domain = g.value(p, RDFS.domain)
                    range = g.value(p, RDFS.range)
                    if label and comment:
                        f.write(f"### `{label}`\n\n")
                        f.write(f"**IRI:** `{p}`\n\n")
                        if domain:
                            f.write(f"**Domain:** `{domain}`\n\n")
                        if range:
                            f.write(f"**Range:** `{range}`\n\n")
                        f.write(f"{comment}\n\n")

    print("Vocabulary documentation generated successfully.")

if __name__ == "__main__":
    generate_vocabulary_docs()
