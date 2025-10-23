import React, { useState } from 'react';
import { Upload, CreditCard, AlertCircle, CheckCircle, Download, Loader } from 'lucide-react';
import axios from 'axios';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError(null);
      setResult(null);
    } else {
      setError('Please select a valid PDF file');
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file first');
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${API_URL}/api/parse`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setResult(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to parse statement');
    } finally {
      setLoading(false);
    }
  };

  const exportJSON = () => {
    if (!result) return;
    const dataStr = JSON.stringify(result, null, 2);
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'parsed_statement.json';
    link.click();
  };

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <CreditCard size={48} />
          <h1>Credit Card Statement Parser</h1>
          <p>Extract data from HDFC, ICICI, SBI, Axis & AmEx statements</p>
        </header>

        <div className="upload-section">
          <div className="upload-box">
            <input
              type="file"
              accept=".pdf"
              onChange={handleFileChange}
              id="file-input"
              style={{ display: 'none' }}
            />
            <label htmlFor="file-input" className="upload-label">
              <Upload size={48} />
              <p>{file ? file.name : 'Click to upload PDF'}</p>
            </label>
          </div>
          
          <button 
            onClick={handleUpload} 
            disabled={!file || loading}
            className="parse-btn"
          >
            {loading ? <Loader className="spin" size={20} /> : 'Parse Statement'}
          </button>
        </div>

        {error && (
          <div className="alert error">
            <AlertCircle size={20} />
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="result-section">
            <div className="result-header">
              <div className="flex-center">
                <CheckCircle size={24} color="#10b981" />
                <h2>Extracted Data</h2>
              </div>
              <button onClick={exportJSON} className="export-btn">
                <Download size={16} />
                Export JSON
              </button>
            </div>

            <div className="data-grid">
              <DataCard label="Issuer" value={result.issuer} />
              <DataCard label="Card Last 4 Digits" value={result.cardLast4} />
              <DataCard label="Statement Period" value={result.statementPeriod} />
              <DataCard label="Due Date" value={result.dueDate} />
              <DataCard label="Total Due" value={result.totalDue} />
              <DataCard label="Previous Balance" value={result.previousBalance} />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

const DataCard = ({ label, value }) => (
  <div className="data-card">
    <p className="label">{label}</p>
    <p className="value">{value}</p>
  </div>
);

export default App;