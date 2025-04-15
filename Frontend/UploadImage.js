import React, { useState } from "react";
import axios from "axios";
import "./UploadImage.css";

const UploadImage = () => {
    const [selectedFile, setSelectedFile] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [preview, setPreview] = useState(null);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedFile(file);
            setError(null);
            setResult(null);
            
            // Create preview
            const reader = new FileReader();
            reader.onloadend = () => {
                setPreview(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            setError("Please select an image first");
            return;
        }

        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            setLoading(true);
            const response = await axios.post("http://localhost:5000/predict", formData, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            });

            if (response.data && response.data.success) {
                setResult(response.data);
            } else {
                setError(response.data.error || "Invalid response from server");
            }
        } catch (err) {
            console.error("Error uploading file:", err);
            setError(err.response?.data?.error || "Unable to process the image");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="upload-container">
            <div className="upload-box">
                {preview ? (
                    <div className="image-preview">
                        <img src={preview} alt="Preview" className="preview-image" />
                        <button 
                            onClick={() => {
                                setSelectedFile(null);
                                setPreview(null);
                            }} 
                            className="clear-button"
                        >
                            ×
                        </button>
                    </div>
                ) : (
                    <div className="upload-area">
                        <label className="file-input-label">
                            <input 
                                type="file" 
                                onChange={handleFileChange} 
                                accept="image/jpeg, image/png"
                                className="file-input"
                            />
                            <div className="upload-icon">📁</div>
                            <p>Choose an image</p>
                            <p className="file-types">JPG, PNG (max 5MB)</p>
                        </label>
                    </div>
                )}

                <button 
                    onClick={handleUpload} 
                    disabled={loading || !selectedFile}
                    className={`analyze-button ${loading ? 'loading' : ''}`}
                >
                    {loading ? (
                        <>
                            <span className="spinner"></span>
                            Analyzing...
                        </>
                    ) : (
                        'Analyze Image'
                    )}
                </button>
            </div>

            {error && <div className="error-message">{error}</div>}

            {result && (
                <div className={`result-box ${result.status === "Cancer Detected" ? 'cancer' : 'no-cancer'}`}>
                    <h3>Detection Result</h3>
                    <div className="result-content">
                        {result.status === "Cancer Detected" ? (
                            <div className="result-alert">
                                <span className="alert-icon">⚠️</span>
                                <div>
                                    <p className="result-title">Cancer Detected: {result.type}</p>
                                    <p className="result-confidence">Confidence: {result.confidence}</p>
                                </div>
                            </div>
                        ) : (
                            <div className="result-alert">
                                <span className="alert-icon">✅</span>
                                <div>
                                    <p className="result-title">No Cancer Detected: {result.type}</p>
                                    <p className="result-confidence">Confidence: {result.confidence}</p>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

export default UploadImage;