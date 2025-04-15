import React from "react";

function Result({ result }) {
    if (!result) return null;

    return (
        <div className={`result-container ${
            result.status === "Cancer Detected" 
                ? "result-cancer" 
                : "result-no-cancer"
        }`}>
            <h3>Detection Result</h3>
            {result.status === "Cancer Detected" ? (
                <div>
                    <p style={{ color: "#f44336" }}>
                        ⚠️ <strong>Cancer Detected:</strong> {result.type}
                    </p>
                    <p>Confidence: {result.confidence}</p>
                    <p className="warning-message">
                        Please consult a dermatologist immediately for further evaluation.
                    </p>
                </div>
            ) : (
                <div>
                    <p style={{ color: "#4caf50" }}>
                        ✅ <strong>No Cancer Detected:</strong> {result.type}
                    </p>
                    <p>Confidence: {result.confidence}</p>
                </div>
            )}
        </div>
    );
}

export default Result;