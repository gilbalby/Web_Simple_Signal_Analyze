document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const signalInput = document.getElementById('signal');
    const resultDiv = document.getElementById('result');

    // Regex validation for comma-separated numbers
    signalInput.addEventListener('input', (e) => {
        const value = e.target.value;
        if (!/^[\d,]*$/.test(value)) {
            e.target.value = value.replace(/[^\d,]/g, '');
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const signalValues = signalInput.value.split(',').map(Number);

        if (!isValidSignal(signalValues)) {
            alert('Por favor, insira números válidos separados por vírgula');
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ signal: signalValues })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            displayResults(data);
        } catch (error) {
            console.error('Erro na análise:', error);
            resultDiv.innerHTML = '<h2>Erro</h2><p>Ocorreu um erro durante a análise.</p>';
        }
    });

    function isValidSignal(values) {
        return values.length > 0 && values.every(num => !isNaN(num));
    }

    function displayResults(data) {
        const html = `
            <h2>Resultados da Análise</h2>
            <ul>
                <li><strong>Média:</strong> ${data.mean.toFixed(2)}</li>
                <li><strong>Valor Mínimo:</strong> ${data.min}</li>
                <li><strong>Valor Máximo:</strong> ${data.max}</li>
                <li><strong>Tendência:</strong> ${data.trend}</li>
            </ul>
        `;
        resultDiv.innerHTML = html;
    }
});