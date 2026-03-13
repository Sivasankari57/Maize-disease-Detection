import React, { useState } from "react";
import "./App.css";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [prediction, setPrediction] = useState("");
  const [confidence, setConfidence] = useState("");
  const [solution, setSolution] = useState("");

  const handleChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleSubmit = async () => {
    if (!image) {
      alert("Please upload an image");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    setPrediction(data.prediction);
    setConfidence((data.confidence * 100).toFixed(2));
    setSolution(data.solution);
  };

  return (
    <div className="container">
      <div className="card">
        <h1>🌽 Maize Disease Detection</h1>

        <input type="file" onChange={handleChange} />

        {preview && <img src={preview} alt="preview" className="preview" />}

        <button onClick={handleSubmit}>Predict Disease</button>

        {prediction && (
          <div className="result">
            <h2>Disease: {prediction}</h2>
            <p>Confidence: {confidence}%</p>
            <div className="solution">
              <h3>Recommended Solution</h3>
              <p>{solution}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
