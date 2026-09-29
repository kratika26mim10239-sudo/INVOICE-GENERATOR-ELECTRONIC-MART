import os
import unittest
from src.invoice_generator import generate_pdf_receipt

class TestInvoiceGeneration(unittest.TestCase):

    def setUp(self):
        self.test_filename = "test_receipt.pdf"
        self.cust_name = "Jane Doe"
        self.cust_phone = "555-0199"
        self.items = [
            {"description": "Wireless Mouse", "qty": 2, "price": 25.0, "total": 50.0},
            {"description": "Mechanical Keyboard", "qty": 1, "price": 120.0, "total": 120.0}
        ]

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_grand_total_calculation(self):
        grand_total = sum(item["total"] for item in self.items)
        self.assertEqual(grand_total, 170.0)

    def test_pdf_creation(self):
        output_path = generate_pdf_receipt(
            self.test_filename,
            self.cust_name,
            self.cust_phone,
            self.items
        )
        self.assertTrue(os.path.exists(output_path))
        self.assertGreater(os.path.getsize(output_path), 0)

if __name__ == "__main__":
    unittest.main()
