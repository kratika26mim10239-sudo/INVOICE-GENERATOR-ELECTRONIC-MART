# Initializes the src package
from .invoice_generator import ElectronicsInvoiceApp, generate_pdf_receipt

__all__ = ["ElectronicsInvoiceApp", "generate_pdf_receipt"]
