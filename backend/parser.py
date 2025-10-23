import pdfplumber
import re
from datetime import datetime

def parse_credit_card_statement(filepath):
    """
    Parse credit card statement and extract 5 key data points
    """
    try:
        with pdfplumber.open(filepath) as pdf:
            # Extract text from first 3 pages
            text = ""
            for page in pdf.pages[:3]:
                text += page.extract_text() + "\n"
        
        result = {
            "issuer": detect_issuer(text),
            "cardLast4": extract_card_number(text),
            "statementPeriod": extract_statement_period(text),
            "dueDate": extract_due_date(text),
            "totalDue": extract_total_due(text),
            "previousBalance": extract_previous_balance(text)
        }
        
        return result
    
    except Exception as e:
        raise Exception(f"Error parsing PDF: {str(e)}")

def detect_issuer(text):
    """Detect credit card issuer"""
    issuers = {
        r'HDFC\s*BANK': 'HDFC Bank',
        r'ICICI\s*BANK': 'ICICI Bank',
        r'SBI\s*CARD': 'SBI Card',
        r'AXIS\s*BANK': 'Axis Bank',
        r'AMERICAN\s*EXPRESS': 'American Express'
    }
    
    for pattern, name in issuers.items():
        if re.search(pattern, text, re.IGNORECASE):
            return name
    
    return "Unknown"

def extract_card_number(text):
    """Extract last 4 digits of card"""
    patterns = [
        r'(?:Card(?:\s+No\.?|\s+Number)?|Account)\s*[:\s]*(?:XXXX\s*)?(\d{4})',
        r'ending\s+(?:in\s+)?(\d{4})',
        r'\*+\s*(\d{4})',
        r'Card\s*:\s*\*+(\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return "N/A"

def extract_statement_period(text):
    """Extract billing cycle/statement period"""
    patterns = [
        r'Statement\s+(?:Period|Date)[\s:]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\s*(?:to|-)?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'Billing\s+(?:Period|Cycle)[\s:]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\s*(?:to|-)?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'(?:From|Period)[\s:]*(\d{1,2}\s+[A-Z][a-z]+\s+\d{4})\s+to\s+(\d{1,2}\s+[A-Z][a-z]+\s+\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return f"{match.group(1)} to {match.group(2)}"
    
    return "N/A"

def extract_due_date(text):
    """Extract payment due date"""
    patterns = [
        r'(?:Payment\s+)?Due\s+(?:Date|By)[\s:]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'(?:Pay\s+by|Payment\s+due)[\s:]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'Due\s+Date[\s:]*(\d{1,2}\s+[A-Z][a-z]+\s+\d{4})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)
    
    return "N/A"

def extract_total_due(text):
    """Extract total amount due"""
    patterns = [
        r'Total\s+(?:Amount\s+)?Due[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)',
        r'(?:Payment\s+Due|Amount\s+Due)[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)',
        r'Minimum\s+(?:Amount\s+)?Due[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)',
        r'Total\s+Outstanding[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return f"₹{match.group(1)}"
    
    return "N/A"

def extract_previous_balance(text):
    """Extract previous balance"""
    patterns = [
        r'Previous\s+(?:Balance|Outstanding)[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)',
        r'Opening\s+Balance[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)',
        r'Last\s+Statement\s+Balance[\s:]*(?:Rs\.?|INR|₹)?\s*([\d,]+\.?\d*)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return f"₹{match.group(1)}"
    
    return "N/A"