import React from "react";
import UploadImage from "./UploadImage";
import "./SkinCancerDetection.css";

const SkinCancerDetection = () => {
    return (
        <section id="detection" className="detection-section">
            <div className="section-container">
                <div className="section-header">
                    <h2>AI Skin Cancer Detection</h2>
                    <p className="subtitle">
                        Get instant analysis of suspicious skin lesions with our clinically-validated AI
                    </p>
                </div>

                <div className="detection-grid">
                    <div className="upload-card">
                        <h3>Upload Your Image</h3>
                        <p className="instruction">
                            Take or upload a clear photo of the skin area you're concerned about
                        </p>
                        <UploadImage />
                    </div>

                    <div className="features-grid">
                        <div className="feature-card">
                            <div className="feature-icon">📸</div>
                            <h4>Image Guidelines</h4>
                            <ul>
                                <li>High-resolution images</li>
                                <li>Neutral background</li>
                                <li>Good lighting</li>
                                <li>Multiple angles</li>
                            </ul>
                        </div>

                        <div className="feature-card">
                            <div className="feature-icon">⚡</div>
                            <h4>Fast Results</h4>
                            <ul>
                                <li>30-second analysis</li>
                                <li>Visual explanations</li>
                                <li>Confidence scores</li>
                                <li>Case comparisons</li>
                            </ul>
                        </div>

                        <div className="feature-card">
                            <div className="feature-icon">🩺</div>
                            <h4>Next Steps</h4>
                            <ul>
                                <li>Doctor referrals</li>
                                <li>Downloadable report</li>
                                <li>Telemedicine options</li>
                                <li>Follow-up reminders</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div className="disclaimer">
                    <p>⚠️ This tool is for informational purposes only and does not replace professional medical diagnosis.</p>
                </div>
            </div>
        </section>
    );
};

export default SkinCancerDetection;