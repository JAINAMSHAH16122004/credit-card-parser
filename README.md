# Credit Card Statement Parser

Extract key information from credit card statements across 5 major Indian banks.

## 🏦 Supported Banks
- HDFC Bank
- ICICI Bank
- SBI Card
- Axis Bank
- American Express

## 📊 Extracted Data Points
1. Card Issuer
2. Card Last 4 Digits
3. Statement Period
4. Payment Due Date
5. Total Amount Due
6. Previous Balance

## 🛠️ Tech Stack
- **Backend**: Python + Flask + pdfplumber
- **Frontend**: React + Axios
- **Deployment**: Railway (Backend) + Vercel (Frontend)

## 🚀 Live Demo
- Frontend: https://credit-card-parser-lyc9o1ewa-jainam-shahs-projects.vercel.app/
- Backend API: https://credit-card-parser-backend.onrender.com/health

## 💻 Local Development

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure
```
credit-card-parser/
├── backend/
│   ├── app.py              # Flask API
│   ├── parser.py           # PDF parsing logic
│   ├── requirements.txt    # Python dependencies
│   └── Procfile           # Railway config
├── frontend/
│   ├── src/
│   │   ├── App.js         # React main component
│   │   └── App.css        # Styles
│   └── package.json       # NPM dependencies
└── README.md              # This file
```

## 🧪 Testing
Generate dummy statements:
```bash
cd backend
pip install reportlab
python generate_dummy_statements.py
```

## 📡 API Endpoints

### Health Check
```bash
GET /health
Response: {"status": "healthy"}
```

### Parse Statement
```bash
POST /api/parse
Content-Type: multipart/form-data
Body: file=@statement.pdf

Response:
{
  "issuer": "HDFC Bank",
  "cardLast4": "1234",
  "statementPeriod": "01/10/2024 to 31/10/2024",
  "dueDate": "20/11/2024",
  "totalDue": "₹15,000",
  "previousBalance": "₹10,000"
}
```

## 👤 Author
Jainam Mukesh Shah
60004220085
Dj Sanghvi College of Engineering
Computer Engineering
