import React, { useState } from 'react';

function Calculator() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [operator, setOperator] = useState('');
  const [result, setResult] = useState('');

  const handleCalculate = () => {
    if (num1 !== '' && num2 !== '' && operator !== '') {
      fetch({
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ num1, num2, operator }),
      })
        .then(response => response.json())
        .then(data => setResult(data.result))
        .catch(error => console.error('Error:', error));
    }
  };

  return (
    <div>
      <h1>Simple Calculator</h1>
      <input
        type="number"
        value={num1}
        onChange={e => setNum1(e.target.value)}
        placeholder="Enter first number"
      />
      <input
        type="number"
        value={num2}
        onChange={e => setNum2(e.target.value)}
        placeholder="Enter second number"
      />
      <input
        type="text"
        value={operator}
        onChange={e => setOperator(e.target.value)}
        placeholder="Enter operator"
      />
      <button onClick={handleCalculate}>Calculate</button>
      <div>
        Result: <span>{result}</span>
      </div>
    </div>
  );
}

export default Calculator;
