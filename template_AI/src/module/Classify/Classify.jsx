import "./Classify.css";
import React, { useEffect, useState } from 'react';
import { useMutation } from "react-query";
import Chart from "../../components/Chart/Chart";

const Classify = () => {
  const predictDocument  = useMutation(() => {
    return fetch('http://127.0.0.1:5000/data', {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    }).then((response) => response.json());
  });
  useEffect(() => {
    predictDocument.mutate()
  },[])

  if(predictDocument.data) {
    console.log(predictDocument.data)
  }
  return (
    <main className="classify">
      <div className="classify_container">
          <div className="classify_title">
            <h1>Thông tin dữ liệu</h1>
          </div>
        <div className="classify_training">
          <div className="classify_train">
              <div className="chart_title">
                Dữ liệu tập huấn luyện
              </div>
              {predictDocument.data && 
                  <Chart data={predictDocument.data.data1.sort((a, b) => a.name.localeCompare(b.name))}/>
              }
          </div>
          <div className="classify_test">
            <div className="chart_title">
                Dữ liệu tập test
              </div>
              {predictDocument.data && 
                  <Chart data={predictDocument.data.data2.sort((a, b) => a.name.localeCompare(b.name))}/>
              }
          </div>
        </div>
      </div>
    </main>
  );
};

export default Classify;
