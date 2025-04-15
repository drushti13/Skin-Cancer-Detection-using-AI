import React from "react";
import Header from "./components/Header";
import Home from "./components/Home";
import SkinCancerDetection from "./components/SkinCancerDetection";
import Experts from "./components/Experts";
import Contact from "./components/Contact";
import "./styles.css";

const App = () => {
    return (
        <div className="app">
            <Header />
            
            <main>
                <section id="home">
                    <Home />
                </section>
                
                <section id="detection">
                    <SkinCancerDetection />
                </section>
                
                <section id="experts">
                    <Experts />
                </section>
                
                <section id="contact">
                    <Contact />
                </section>
            </main>
        </div>
    );
};

export default App;