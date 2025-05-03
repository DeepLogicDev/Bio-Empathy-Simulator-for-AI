import React, { useRef, useState } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

const App = () => {
  const webcamRef = useRef(null);
  const [emotion, setEmotion] = useState('');

  const capture = async () => {
    const imageSrc = webcamRef.current.getScreenshot();
    const res = await axios.post('http://localhost:5000/predict', {
      image: imageSrc,
    });
    setEmotion(res.data.emotion);
  };

  return (
    <div className="App">
      <h1>Bio Empathy Simulator</h1>
      <Webcam audio={false} ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={capture}>Detect Emotion</button>
      {emotion && <h2>Detected Emotion: {emotion}</h2>}
    </div>
  );
};

export default App;
