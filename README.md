# TurboOlaf

TurboOlaf is a simple and fast cutting-edge hardware-accelerated system for selling things labeled with barcodes. It was depeloped for selling beverages in crates at the the [HaDiKO](http://hadiko.de) (more specifically, the K1 Bar), but should work just as well in many other environments.

TurboOlaf features a simple text-based interface for scanning, an advanced product dependency resolution mechanism and built-in generation of invoices and QIF files that can easily be imported into [GnuCash](http://gnucash.org). All that in little more than 200 lines of Python 3 code!

## Usage

To start TurboOlaf, run `turboolaf`. You will be greeted by an `olaf >` prompt that allows 4 types of inputs:

1. **Product identifiers** have to contain at least one letter and are usually short enough to type in manually.
2. **Barcodes** consist of 8 or more digits and is usually entered using a barcode scanner.
3. **Quantities** consist of at least 1 and at most 7 digits and increase the quantity of the previously scanned item that is added to the invoice to the given amount.
4. Simply pressing the Return key or sending an EOF sends a **termination signal** to TurboOlaf that signals the completion of the invoice creation process.

When quitting, TurboOlaf prints a string representation of the final invoice to `stdout`, writes a QIF file to `qif/[id].qif` and a JSON backup of the invoice to `invoices/[id].olaf`. The `.olaf` file can later be loaded into TurboOlaf using the `--file` command-line option.

## Product database format

TurboOlaf uses a simple JSON configuration file format. Actually, all invoices that TurboOlaf generates are clones of the original `invoice_prototype.olaf` file. This means that old invoices are always readable and editable, regardless of the current set of products configured in `invoice_prototype.olaf`.

Internally, TurboOlaf uses a dependency model to subdivide products into smaller "building blocks". Consider for example a crate of beer. This product can be subdivided into the actual liquid that is sold and the plastic crate with 24 glass bottles. This full crate can be divided into 24 single glass bottles and the plastic crate. The advantage of subdividing these products is that a meta-product for returning deposits can easily be created by creating a "Crate of Beer Deposit" product that costs nothing but dependes on "-1 times" the plastic crate with 24 glass bottles.

A product has the following attributes:

* `ids`: A list of identifiers that this product is identified by. Barcodes and human-typeable identifiers belong in this attribute.
* `name`: A human-readable name for the product that shows up on the invoice.
* `price`: A decimal representation of the value of this product.
* `dependencies`: A list of dependencies for this product. Each item in the list is a dictionary with an `id` attribute identifying the dependency and the `quantity` of the product that should be added when resolving the dependency.


