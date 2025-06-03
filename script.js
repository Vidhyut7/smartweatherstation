async function fetchReadings() {
    try {
        const response = await fetch('/readings/');
        const readings = await response.json();
        const readingsBody = document.getElementById('readingsBody');
        readingsBody.innerHTML = '';

        readings.forEach(reading => {
            const row = `<tr>
                <td>${reading.temperature}</td>
                 <td>${reading.pressure}</td>
                <td>${reading.altitude}</td>
                <td>${reading.timestamp}</td>
            </tr>`;
            readingsBody.innerHTML += row;
        });
    } catch (error) {
        console.error('Error fetching readings:', error);
    }
}

// Initial fetch
fetchReadings();

// Set up refresh button
document.getElementById('refreshButton').addEventListener('click', fetchReadings);
