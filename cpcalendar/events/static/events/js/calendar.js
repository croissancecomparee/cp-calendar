document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var eventsData = calendarEl.getAttribute('data-events');
    
    // Vérification si l'attribut 'data-events' n'est pas vide
    if (eventsData) {
        try {
            var events = JSON.parse(eventsData);  // Parse uniquement si des données existent
        } catch (error) {
            console.error("Erreur de parsing JSON:", error);  // Gérer une erreur potentielle de parsing
            return;
        }
    } else {
        console.error("Pas d'événements disponibles");
        var events = [];
    }

    // Initialisation du calendrier avec les événements récupérés
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',  // Vue initiale (mois)
        events: events,  // Utiliser les événements chargés dynamiquement
    });

    calendar.render();
});
