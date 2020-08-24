import React, { useState } from 'react';
const axios = require('axios');

const Home = () => {
  const [value, setText] = useState('');
  const [bestSuggest, setSuggest] = useState({});
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const getSimilar = () => {
    const request = axios.post('localhost:3000', { query: value });
    setSuggest(request['bestSuggest']);
  };

  return (
    <div>
      <textarea
        id="in"
        rows="15"
        cols="50"
        placeholder="add your note here"
        onChange={handleChange}
      ></textarea>
      <button id="Get similar" onClick="">
        Get similar
      </button>
      <button id="Save">Save</button>
    </div>
  );
};

export default Home;
