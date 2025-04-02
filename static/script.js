document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/desks')
        .then(res => res.json())
        .then(updateDesks);

    function updateDesks(data) {
        for (const [deskId, reserved] of Object.entries(data)) {
            const desk = document.getElementById(deskId);
            const circle = document.getElementById(deskId + '-status');
            if (reserved) {
                desk.classList.add('reserved');
                circle.classList.add('reserved');
            } else {
                desk.classList.remove('reserved');
                circle.classList.remove('reserved');
            }
        }
    }

    document.querySelectorAll('.desk').forEach(desk => {
        desk.addEventListener('click', () => {
            fetch(`/api/book/${desk.id}`, { method: 'POST' })
                .then(res => res.json())
                .then(() => fetch('/api/desks').then(res => res.json()).then(updateDesks));
        });
    });
});