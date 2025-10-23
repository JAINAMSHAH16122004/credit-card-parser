"""
Dummy Credit Card Statement Generator
Creates sample PDF statements for testing
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os

def create_hdfc_statement():
    """Generate HDFC Bank dummy statement"""
    filename = "HDFC_Sample_Statement.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, height - 1*inch, "HDFC BANK")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.3*inch, "Credit Card Statement")
    
    # Card Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 2*inch, "Card Number: XXXX XXXX XXXX 5678")
    c.drawString(1*inch, height - 2.3*inch, "Cardholder: John Doe")
    
    # Statement Period
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 2.8*inch, "Statement Period: 01/10/2024 to 31/10/2024")
    c.drawString(1*inch, height - 3.1*inch, "Payment Due Date: 20/11/2024")
    
    # Amounts
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 3.6*inch, "Previous Balance: Rs. 12,500.00")
    c.drawString(1*inch, height - 3.9*inch, "Total Amount Due: Rs. 18,750.00")
    c.drawString(1*inch, height - 4.2*inch, "Minimum Amount Due: Rs. 1,875.00")
    
    # Transactions
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 4.8*inch, "Transactions:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, height - 5.1*inch, "05/10/2024  Amazon Purchase        Rs. 2,450.00")
    c.drawString(1*inch, height - 5.3*inch, "12/10/2024  Restaurant              Rs. 1,200.00")
    c.drawString(1*inch, height - 5.5*inch, "18/10/2024  Fuel Station            Rs. 3,500.00")
    c.drawString(1*inch, height - 5.7*inch, "25/10/2024  Online Shopping         Rs. 4,600.00")
    
    c.save()
    print(f"✅ Created: {filename}")

def create_icici_statement():
    """Generate ICICI Bank dummy statement"""
    filename = "ICICI_Sample_Statement.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, height - 1*inch, "ICICI BANK")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.3*inch, "Credit Card Monthly Statement")
    
    # Card Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 2*inch, "Account Number: XXXX-XXXX-XXXX-4321")
    c.drawString(1*inch, height - 2.3*inch, "Name: Jane Smith")
    
    # Statement Period
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 2.8*inch, "Billing Cycle: 01/09/2024 to 30/09/2024")
    c.drawString(1*inch, height - 3.1*inch, "Due Date: 15/10/2024")
    
    # Amounts
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 3.6*inch, "Opening Balance: Rs. 8,200.00")
    c.drawString(1*inch, height - 3.9*inch, "Total Outstanding: Rs. 15,600.00")
    c.drawString(1*inch, height - 4.2*inch, "Payment Due: Rs. 15,600.00")
    
    # Transactions
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 4.8*inch, "Transaction Details:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, height - 5.1*inch, "03/09/2024  Grocery Store          Rs. 3,200.00")
    c.drawString(1*inch, height - 5.3*inch, "10/09/2024  Movie Tickets          Rs. 800.00")
    c.drawString(1*inch, height - 5.5*inch, "15/09/2024  Electronics            Rs. 5,400.00")
    c.drawString(1*inch, height - 5.7*inch, "22/09/2024  Travel Booking         Rs. 8,000.00")
    
    c.save()
    print(f"✅ Created: {filename}")

def create_sbi_statement():
    """Generate SBI Card dummy statement"""
    filename = "SBI_Sample_Statement.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, height - 1*inch, "SBI CARD")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.3*inch, "Statement of Account")
    
    # Card Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 2*inch, "Card: ****9012")
    c.drawString(1*inch, height - 2.3*inch, "Customer: Raj Kumar")
    
    # Statement Period
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 2.8*inch, "Statement Period: 15/08/2024 to 14/09/2024")
    c.drawString(1*inch, height - 3.1*inch, "Payment Due By: 05/10/2024")
    
    # Amounts
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 3.6*inch, "Previous Balance: Rs. 5,400.00")
    c.drawString(1*inch, height - 3.9*inch, "Total Amount Due: Rs. 22,300.00")
    c.drawString(1*inch, height - 4.2*inch, "Minimum Due: Rs. 2,230.00")
    
    # Transactions
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 4.8*inch, "Transaction Summary:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, height - 5.1*inch, "20/08/2024  Flipkart              Rs. 6,500.00")
    c.drawString(1*inch, height - 5.3*inch, "25/08/2024  Restaurant            Rs. 2,400.00")
    c.drawString(1*inch, height - 5.5*inch, "01/09/2024  Petrol Pump           Rs. 4,000.00")
    c.drawString(1*inch, height - 5.7*inch, "10/09/2024  Medical Store         Rs. 3,900.00")
    
    c.save()
    print(f"✅ Created: {filename}")

def create_axis_statement():
    """Generate Axis Bank dummy statement"""
    filename = "Axis_Sample_Statement.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, height - 1*inch, "AXIS BANK")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.3*inch, "Credit Card Statement")
    
    # Card Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 2*inch, "Card No: XXXX XXXX XXXX 7890")
    c.drawString(1*inch, height - 2.3*inch, "Name: Priya Sharma")
    
    # Statement Period
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 2.8*inch, "Billing Period: 01/11/2024 to 30/11/2024")
    c.drawString(1*inch, height - 3.1*inch, "Due Date: 18/12/2024")
    
    # Amounts
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 3.6*inch, "Previous Balance: Rs. 9,800.00")
    c.drawString(1*inch, height - 3.9*inch, "Total Amount Due: Rs. 28,450.00")
    c.drawString(1*inch, height - 4.2*inch, "Minimum Payment Due: Rs. 2,845.00")
    
    # Transactions
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 4.8*inch, "Recent Transactions:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, height - 5.1*inch, "05/11/2024  Zomato               Rs. 1,200.00")
    c.drawString(1*inch, height - 5.3*inch, "12/11/2024  Myntra               Rs. 5,600.00")
    c.drawString(1*inch, height - 5.5*inch, "20/11/2024  Uber                 Rs. 850.00")
    c.drawString(1*inch, height - 5.7*inch, "28/11/2024  BookMyShow           Rs. 1,200.00")
    
    c.save()
    print(f"✅ Created: {filename}")

def create_amex_statement():
    """Generate American Express dummy statement"""
    filename = "AmEx_Sample_Statement.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1*inch, height - 1*inch, "AMERICAN EXPRESS")
    c.setFont("Helvetica", 12)
    c.drawString(1*inch, height - 1.3*inch, "Account Statement")
    
    # Card Details
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 2*inch, "Card ending in 3456")
    c.drawString(1*inch, height - 2.3*inch, "Member: Alex Johnson")
    
    # Statement Period
    c.setFont("Helvetica", 10)
    c.drawString(1*inch, height - 2.8*inch, "Statement Date: 01/12/2024 to 31/12/2024")
    c.drawString(1*inch, height - 3.1*inch, "Payment Due Date: 25/01/2025")
    
    # Amounts
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 3.6*inch, "Previous Balance: INR 15,000.00")
    c.drawString(1*inch, height - 3.9*inch, "Total Amount Due: INR 32,500.00")
    c.drawString(1*inch, height - 4.2*inch, "Minimum Due: INR 3,250.00")
    
    # Transactions
    c.setFont("Helvetica-Bold", 11)
    c.drawString(1*inch, height - 4.8*inch, "Activity Summary:")
    c.setFont("Helvetica", 9)
    c.drawString(1*inch, height - 5.1*inch, "10/12/2024  Apple Store          INR 8,500.00")
    c.drawString(1*inch, height - 5.3*inch, "15/12/2024  Hotel Booking        INR 12,000.00")
    c.drawString(1*inch, height - 5.5*inch, "22/12/2024  Shopping Mall        INR 6,200.00")
    c.drawString(1*inch, height - 5.7*inch, "28/12/2024  Restaurant           INR 3,300.00")
    
    c.save()
    print(f"✅ Created: {filename}")

if __name__ == "__main__":
    print("\n🏦 Generating Dummy Credit Card Statements...\n")
    
    create_hdfc_statement()
    create_icici_statement()
    create_sbi_statement()
    create_axis_statement()
    create_amex_statement()
    
    print("\n✅ All dummy statements created successfully!")
    print("📁 Files created in current directory:")
    print("   - HDFC_Sample_Statement.pdf")
    print("   - ICICI_Sample_Statement.pdf")
    print("   - SBI_Sample_Statement.pdf")
    print("   - Axis_Sample_Statement.pdf")
    print("   - AmEx_Sample_Statement.pdf")
    print("\n🧪 Ready for testing!")