from decimal import Decimal
import copy

class Invoice(dict):
    def get_product(self, identifier):
        """
        Return a product matching the given identifier.
        """
        # try to find an id corresponding to the code
        for p in self['products']:
            if identifier in p.get('ids', []):
                return p
        # if no product associated with the code found, return None
        return None

    def product_dependencies_are_resolvable(self, product):
        """
        Checks if the product is a top-level item in the dependency tree.
        """
        for v in self['products']:
            for identifier in product['ids']:
                if identifier in map(lambda dep: dep['id'], v.get('dependencies', [])):
                    return False
        return True

    def get_copy_with_resolved_dependencies(self):
        """
        Return a deep copy of this instance with resolved dependencies.
        """
        invoice_copy = copy.deepcopy(self)
        changes = 1
        while changes > 0:
            changes = 0
            for product in invoice_copy['products']:
                # if any other products depend on this product, don't try to resolve it
                if not invoice_copy.product_dependencies_are_resolvable(product):
                    continue
                for dependency in product.get('dependencies', []):
                    changes += 1
                    # add the required quantity to the dependencies
                    invoice_copy.get_product(dependency['id'])['quantity'] += product['quantity'] * dependency.get('quantity', 1)
                    # mark the dependency as resolved by removing it
                    product['dependencies'].remove(dependency)
        return invoice_copy

    def get_total_price(self):
        """
        Get the total price for all products on the invoice.
        """
        i = self.get_copy_with_resolved_dependencies()
        total_price = Decimal(0)
        for product in i['products']:
            billed_price = Decimal(str(product.get('price', 0))) * Decimal(str(product.get('quantity')))
            total_price += billed_price
        return total_price
