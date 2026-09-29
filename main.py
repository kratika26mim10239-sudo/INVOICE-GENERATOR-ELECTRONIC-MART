import tkinter as tk
from src.invoice_generator import ElectronicsInvoiceApp

def main():
    root = tk.Tk()
    app = ElectronicsInvoiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
