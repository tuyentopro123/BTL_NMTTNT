import "./Home.css";
import React, { useState } from 'react';
import { useMutation } from "react-query";
import {convertLabel} from "../../util/function"

const Home = () => {
  const [text, setText] = useState('');
  const predictDocument  = useMutation((data) => {
    return fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    }).then((response) => response.json());
  });

  const handleClick = () => {
    predictDocument.mutate({ document: text });
  };

  const handleTextChange = (event) => {
    setText(event.target.value);
  };
  
  return (
    <main className="home">
      <div className="home_container">
        <div className="home_title">Nhập văn bản để dự đoán</div>
        <div className="home_area">
          <textarea onChange={handleTextChange} value={text} />
        </div>
        <div className="home_button">
          <button onClick={handleClick}>Dự đoán</button>
        </div>
        {predictDocument.data && predictDocument.data.err === 'false' ? (
          <div className="home_predict">
            Nhãn hệ thống dự đoán: {convertLabel(predictDocument.data?.label)}
          </div>
        )
          :
          (
            <div className="home_predict">
              {predictDocument.data?.label}
            </div>
          )
      }
      </div>
    </main>
  );
};

export default Home;
