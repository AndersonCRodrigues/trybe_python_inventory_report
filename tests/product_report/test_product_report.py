from inventory_report.product import Product


def test_product_report() -> None:
    product = Product(
        "123",
        "Test Product",
        "Test Company",
        "2023-01-01",
        "2023-12-31",
        "ABC123",
        "Store in a cool and dry place",
    )
    expected_string = (
        "The product 123 - Test Product "
        "with serial number ABC123 "
        "manufactured on 2023-01-01 "
        "by the company Test Company "
        "valid until 2023-12-31 "
        "must be stored according to the following instructions: "
        "Store in a cool and dry place."
    )

    actual_string = str(product)

    assert actual_string == expected_string
