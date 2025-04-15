import React, { useState } from "react";
import axios from "axios";

function URLInput({ setResult }) {
  const [url, setUrl] = useState("");

  const handleDetect = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/predict-url", { url });
      setResult(response.data.result); // Updates Result.js component
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <h2>Enter image URL:</h2>
      <input
        type="text"
        placeholder="https://example.com/image.jpg"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button onClick={handleDetect}>Detect</button>
    </div>
  );
}

export default URLInput;
