const form = document.getElementById('predict-form');
const resultArea = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(form);
  const data = {};

  formData.forEach((value, key) => {
    // Convert to number if numeric field
    if (!isNaN(value) && value !== '') {
      data[key] = Number(value);
    } else {
      data[key] = value;
    }
  });

  try {
    const res = await fetch('https://loan-recovery-5.onrender.com'
, {
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
    console.error("JS Error:", err);
    resultArea.innerHTML = `<strong style="color:red;">Failed to connect to API.</strong>`;
  }
});
