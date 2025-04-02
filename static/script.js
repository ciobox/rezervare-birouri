document.addEventListener('DOMContentLoaded', () => {
    fetchDesks();

    document.getElementById('reservationForm').addEventListener('submit', e => {
        e.preventDefault();
        const desk = document.getElementById('desk').value;
        const name = document.getElementById('name').value;
        const date = document.getElementById('date').value;

        fetch('/api/book', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ desk, name, date })
        })
        .then(res => res.json())
        .then(() => fetchDesks());
    });
});

function fetchDesks() {
    fetch('/api/desks')
        .then(res => res.json())
        .then(data => {
            for (const [deskId, info] of Object.entries(data)) {
                const desk = document.getElementById(deskId);
                const circle = document.getElementById(deskId + '-status');
                if (info.reserved) {
                    desk.classList.add('reserved');
                    circle.classList.add('reserved');
                } else {
                    desk.classList.remove('reserved');
                    circle.classList.remove('reserved');
                }
            }
        });
}