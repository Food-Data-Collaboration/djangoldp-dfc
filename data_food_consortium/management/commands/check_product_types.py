from django.core.management.base import BaseCommand

from data_food_consortium.enums import DFC_PT_URL, ProductType
from rdflib import Graph
from rdflib.namespace import SKOS


class Command(BaseCommand):
    help = "Compares the ProductType enumeration in this package with the published ontology, and suggests changes"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Gather all product type candidates.
        product_types = self.gather_product_types()

        # Remove all product type candidates that are already configured on the existing enum.
        new_product_types = list(product_types.difference(set(ProductType.values)))
        new_product_types.sort()
        if len(new_product_types):
            print(
                f"{len(new_product_types)} new produdct types found. Please copy the following values into the TextChoices"
            )
            print("-------------------------")
        else:
            print("No new product types found.")

        # Format the product type candidates as an enum.
        for pt in new_product_types:
            choice_name = pt.split("#")[-1]
            print(
                f'    {choice_name.replace("-", "_").upper()} = ("{pt}", "{choice_name.replace("-", " ").capitalize()}")'
            )

    def treat_concept_name(self, concept_name: str):
        # ProductType ontology contains uppercase, camel case and lowercase variants of the same product types,
        # labelled as exact matches of one another. We treat only the lowercase variant, for simplicity.
        # Likewise, we do not store duplicate product types for HTTP or HTTPS scheme URIs.
        concept_args = concept_name.split("#")
        return (
            concept_args[0].replace("http://", "https://")
            + "#"
            + concept_args[1].lower()
        )

    def gather_product_types(self):
        # Download the published dfc-pt ontology.
        g = Graph()
        g.parse(DFC_PT_URL, format="xml")

        # Product type candidates are gathered from the SKOS properties that are used for them.
        product_types = set()
        for s in g.subjects(SKOS.hasTopConcept, None):
            for top_concept in g.objects(s, SKOS.hasTopConcept):
                product_types.add(self.treat_concept_name(str(top_concept)))

        for s in g.subjects(SKOS.narrower, None):
            for concept in g.objects(s, SKOS.narrower):
                product_types.add(self.treat_concept_name(str(concept)))

        return product_types
