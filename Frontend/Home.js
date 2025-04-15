import React from "react";
import "./Home.css";

const Home = () => {
    return (
        <section id="home" className="home-section">
            <div className="section-container">
                <div className="intro-card">
                    <h2>Understanding Skin Cancer</h2>
                    <p>
                        Skin cancer is the abnormal growth of skin cells, most often developing on sun-exposed skin.
                        Early detection through regular screening significantly improves treatment outcomes.
                    </p>
                </div>

                <div className="info-grid">
                    <div className="info-card prevention-card">
                        <h3>Prevention Strategies</h3>
                        <ul>
                            <li>Use SPF 30+ sunscreen daily</li>
                            <li>Wear protective clothing</li>
                            <li>Avoid peak sun hours</li>
                            <li>Regular self-examinations</li>
                        </ul>
                    </div>

                    <div className="info-card detection-card">
                        <h3>Detection Guide</h3>
                        <div className="abcde-rule">
                            <div>
                                <h4>A - Asymmetry</h4>
                                <p>Uneven shape</p>
                            </div>
                            <div>
                                <h4>B - Border</h4>
                                <p>Irregular edges</p>
                            </div>
                            <div>
                                <h4>C - Color</h4>
                                <p>Multiple colors</p>
                            </div>
                            <div>
                                <h4>D - Diameter</h4>
                                <p>Larger than 6mm</p>
                            </div>
                            <div>
                                <h4>E - Evolving</h4>
                                <p>Changing over time</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="tech-card">
                    <h3>Our AI Technology</h3>
                    <p>
                        Using deep learning trained on thousands of dermatologist-verified images, our system
                        identifies suspicious patterns with over 90% accuracy compared to clinical diagnosis.
                    </p>
                </div>
            </div>
        </section>
    );
};

export default Home;