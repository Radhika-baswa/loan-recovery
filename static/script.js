const form = document.getElementById('predict-form');
const resultArea = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const data = {};

  formData.forEach((value, key) => {
    if (!isNaN(value) && value !== '') {
      data[key] = Number(value);
    } else {
      data[key] = value;
    }
  });

  try {
    const res = await fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    const result = await res.json();

    if (res.ok) {
      resultArea.innerHTML = `
        <strong>Prediction:</strong> ${result.prediction}<br>
        <strong>Recovery Explanation:</strong> ${result.reason || 'N/A'}
      `;
    } else {
      resultArea.innerHTML = `<strong style="color:red;">Error:</strong> ${result.error}`;
    }
  } catch (err) {
    resultArea.innerHTML = `<strong style="color:red;">Failed to connect to API.</strong>`;
  }
});
