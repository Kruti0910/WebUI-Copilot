import React, { useState } from 'react';
import axios from 'axios';
import './QueryForm.css';

const QueryForm = () => {
    const [question, setQuestion] = useState('');
    const [response, setResponse] = useState('');
    const [agent, setAgent] = useState('clinical');  // Default to 'clinical'

    const handleQuery = async () => {
        try {
            const result = await axios.post(`http://127.0.0.1:8000/${agent}`, { question });
            setResponse(result.data.response || "No response from the server.");
        } catch (error) {
            setResponse("Error connecting to backend. Make sure FastAPI server is running.");
            console.error(error);
        }
    };

    return (
        <div className="query-form">
            <textarea
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                rows="4"
                cols="50"
                placeholder="Type your question here..."
            />

            <div className="buttons">
                <button onClick={() => setAgent('clinical')}>Clinical Agent</button>
                <button onClick={() => setAgent('food_security')}>Food Security Agent</button>
            </div>

            <div>
                <button onClick={handleQuery}>Ask Agent</button>
            </div>

            {response && (
                <div className="response">
                    <h2>Response:</h2>
                    <p>{response}</p>
                </div>
            )}
        </div>
    );
};

export default QueryForm;
