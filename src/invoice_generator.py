from datetime import datetime
import os
import tkinter as tk
from tkinter import messagebox, ttk
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def generate_pdf_receipt(filename, cust_name, cust_phone, items):
    """
    Generates a PDF invoice file using ReportLab.
    
    :param filename: Target output PDF filename.
    :param cust_name: Customer Name.
    :param cust_phone: Customer Phone Number.
    :param items: List of dicts with keys 'description', 'qty', 'price', 'total'.
    :return: Absolute file path of generated PDF.
    """
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    elements = []
    styles = getSampleStyleSheet()

    # Document Styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        textColor=colors.HexColor('#1A237E'),
        spaceAfter=12
    )
    normal_style = styles['Normal']

    # Header Section
    elements.append(Paragraph("TECH ZONE ELECTRONICS MARKET", title_style))
    elements.append(Paragraph("123 Tech Plaza, Electronics Street, City", normal_style))
    elements.append(Paragraph("Phone: +1 800-555-0199 | Email: sales@techzone.com", normal_style))
    elements.append(Spacer(1, 15))

    # Receipt & Customer Details
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    info_data = [
        [f"Invoice Date: {date_str}", f"Customer: {cust_name}"],
        [f"Invoice No: INV-{timestamp}", f"Phone: {cust_phone}"]
    ]
    info_table = Table(info_data, colWidths=[270, 270])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F5F5F5')),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 15))

    # Items Table
    table_data = [["Item Description", "Qty", "Unit Price", "Total"]]
    for item in items:
        table_data.append([
            item["description"],
            str(item["qty"]),
            f"${item['price']:.2f}",
            f"${item['total']:.2f}"
        ])

    grand_total = sum(item["total"] for item in items)
    table_data.append(["", "", "Grand Total:", f"${grand_total:.2f}"])

    items_table = Table(table_data, colWidths=[260, 60, 110, 110])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1A237E')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -2), colors.HexColor('#FAFAFA')),
        ('GRID', (0, 0), (-1, -2), 0.5, colors.HexColor('#E0E0E0')),
        ('FONTNAME', (-2, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (-2, -1), (-1, -1), 11),
        ('ALIGN', (-2, -1), (-1, -1), 'RIGHT'),
    ]))

    elements.append(items_table)
    elements.append(Spacer(1, 20))

    # Footer
    elements.append(Paragraph("Thank you for shopping with us! Standard 1-year warranty applies to all electronic items.", normal_style))

    doc.build(elements)
    return os.path.abspath(filename)


class ElectronicsInvoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Electronics Store Invoice Generator")
        self.root.geometry("800x650")

        self.items = []

        self.create_widgets()

    def create_widgets(self):
        # Header Title
        title_label = tk.Label(
            self.root,
            text="Electronics Store Invoice System",
            font=("Helvetica", 16, "bold"),
        )
        title_label.pack(pady=10)

        # Customer Information Frame
        cust_frame = tk.LabelFrame(
            self.root, text="Customer Details", font=("Helvetica", 11, "bold")
        )
        cust_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(cust_frame, text="Customer Name:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        self.cust_name_entry = tk.Entry(cust_frame, width=30)
        self.cust_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(cust_frame, text="Phone Number:").grid(
            row=0, column=2, padx=5, pady=5, sticky="e"
        )
        self.cust_phone_entry = tk.Entry(cust_frame, width=25)
        self.cust_phone_entry.grid(row=0, column=3, padx=5, pady=5)

        # Product Entry Frame
        prod_frame = tk.LabelFrame(
            self.root, text="Add Electronics Item", font=("Helvetica", 11, "bold")
        )
        prod_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(prod_frame, text="Item Description:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        self.item_name_entry = tk.Entry(prod_frame, width=25)
        self.item_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(prod_frame, text="Qty:").grid(
            row=0, column=2, padx=5, pady=5, sticky="e"
        )
        self.item_qty_entry = tk.Entry(prod_frame, width=8)
        self.item_qty_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(prod_frame, text="Unit Price ($):").grid(
            row=0, column=4, padx=5, pady=5, sticky="e"
        )
        self.item_price_entry = tk.Entry(prod_frame, width=10)
        self.item_price_entry.grid(row=0, column=5, padx=5, pady=5)

        add_btn = tk.Button(
            prod_frame,
            text="Add Item",
            command=self.add_item,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 10, "bold"),
        )
        add_btn.grid(row=0, column=6, padx=10, pady=5)

        # Item List Table
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=15, pady=5)

        columns = ("Description", "Quantity", "Unit Price", "Total")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings")

        self.tree.heading("Description", text="Item Description")
        self.tree.heading("Quantity", text="Qty")
        self.tree.heading("Unit Price", text="Unit Price ($)")
        self.tree.heading("Total", text="Total Amount ($)")

        self.tree.column("Description", width=300)
        self.tree.column("Quantity", width=80, anchor="center")
        self.tree.column("Unit Price", width=120, anchor="e")
        self.tree.column("Total", width=120, anchor="e")

        self.tree.pack(fill="both", expand=True)

        # Total & PDF Export Frame
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill="x", padx=15, pady=10)

        self.total_label = tk.Label(
            bottom_frame,
            text="Grand Total: $0.00",
            font=("Helvetica", 12, "bold"),
            fg="navy",
        )
        self.total_label.pack(side="left")

        export_btn = tk.Button(
            bottom_frame,
            text="Export PDF Receipt",
            command=self.generate_pdf,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 11, "bold"),
            padx=10,
        )
        export_btn.pack(side="right")

    def add_item(self):
        desc = self.item_name_entry.get().strip()
        qty_str = self.item_qty_entry.get().strip()
        price_str = self.item_price_entry.get().strip()

        if not desc or not qty_str or not price_str:
            messagebox.showerror("Input Error", "Please fill in all item details.")
            return

        try:
            qty = int(qty_str)
            price = float(price_str)
            if qty <= 0 or price < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Input Error", "Quantity must be a positive integer and price a non-negative number."
            )
            return

        line_total = qty * price
        self.items.append(
            {"description": desc, "qty": qty, "price": price, "total": line_total}
        )

        self.tree.insert(
            "",
            "end",
            values=(
                desc,
                qty,
                f"${price:.2f}",
                f"${line_total:.2f}",
            ),
        )

        self.item_name_entry.delete(0, tk.END)
        self.item_qty_entry.delete(0, tk.END)
        self.item_price_entry.delete(0, tk.END)

        self.update_total()

    def update_total(self):
        grand_total = sum(item["total"] for item in self.items)
        self.total_label.config(text=f"Grand Total: ${grand_total:.2f}")

    def generate_pdf(self):
        cust_name = self.cust_name_entry.get().strip()
        cust_phone = self.cust_phone_entry.get().strip()

        if not cust_name:
            messagebox.showerror("Error", "Customer name is required.")
            return

        if not self.items:
            messagebox.showerror("Error", "Please add at least one item to the invoice.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"invoice_{timestamp}.pdf"

        try:
            full_path = generate_pdf_receipt(filename, cust_name, cust_phone, self.items)
            messagebox.showinfo("Success", f"Invoice saved successfully as:\n{full_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")
