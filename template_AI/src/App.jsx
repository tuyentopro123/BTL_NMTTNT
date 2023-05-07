import "./App.css";
import React, { useRef, useState, useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./module/Home/Home";
import Header from "./module/Header/Header";
import Classify from "./module/Classify/Classify";
function App() {
  // const location = useLocation()

  return (
    <div className="App">
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/classify" element={<Classify />} />
          {/* <Route path="/program" element={<Blog fields="program" />} />
          <Route path="/life" element={<Blog fields="life" />} />
          <Route path="/about" element={<About />} /> */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}
export default App;
