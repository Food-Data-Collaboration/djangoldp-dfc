import re
import requests

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

        # Tests the assumptions of this script to check for changes in the ontology format.
        self.report_error_checking(product_types)

    def gather_product_types(self):
        # Download the published dfc-pt ontology.
        g = Graph()
        g.parse(DFC_PT_URL, format="xml")

        # Product type candidates are gathered from the SKOS properties that are used for them.
        product_types = set()
        for s in g.subjects(SKOS.hasTopConcept, None):
            for top_concept in g.objects(s, SKOS.hasTopConcept):
                product_types.add(str(top_concept))

        for s in g.subjects(SKOS.narrower, None):
            for concept in g.objects(s, SKOS.narrower):
                product_types.add(str(concept))

        return product_types

    def report_error_checking(self, product_types):
        print(
            "\n-------------------------------------------\n"
            "Conducting error checking. The script will now test its own assumptions by"
            " looking for possible changes in the ontology schema"
        )

        # Read the content of the ontology into a string.
        response = requests.get(DFC_PT_URL)
        response.raise_for_status()
        content = response.text

        # Run a simple regex to check for all unique product type candidates.
        pattern = re.compile(
            r'"https:\/\/github.com\/datafoodconsortium\/taxonomies\/releases\/latest\/download\/productTypes.rdf#[\S]+"'
        )
        matches = {m.replace('"', "") for m in set(pattern.findall(content))}

        # Compare the set of matches with those handled by the script, and report any inconsistencies.
        diff = matches.difference(product_types).difference(set(ProductType.values))
        error_count = len(diff)

        if error_count > 0:
            print(
                f"{error_count} possible product types were found which were not identified by the script,"
                " probably due to the predicate where the URI was found"
            )
            print("These are as follows")
            for error in diff:
                print(f" - {error}")

        diff = product_types.difference(matches)
        if len(diff) > 0:
            print(
                f"{len(diff)} product types were identified by the script which have an unexpected URI structure"
            )
            print("These are as follows")
            for error in diff:
                print(f" - {error}")

        error_count += len(diff)
        if error_count == 0:
            print("Check complete. No errors were found.")
        else:
            print(
                f"Check complete. {error_count} possible errors found. Please review them for validity."
            )
