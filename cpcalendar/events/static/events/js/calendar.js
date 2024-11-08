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

    // Fonction pour récupérer la valeur d'une variable CSS
    function getCSSVariableValue(variableName) {
        return getComputedStyle(document.documentElement).getPropertyValue(variableName).trim();
    }

    var eventColors = {
        'smash': getCSSVariableValue('--smash'),            // Couleur pour Smash
        'mtg': getCSSVariableValue('--mtg'),                // Couleur pour Magic the Gathering
        'lorcana': getCSSVariableValue('--lorcana'),                // Couleur pour Lorcana
        'street_fighter': getCSSVariableValue('--street_fighter'), // Couleur pour Street Fighter
        'rpg': getCSSVariableValue('--rpg'),                // Couleur pour RPG
        'board_games': getCSSVariableValue('--board_games'), // Couleur pour Jeux de société
        'other': getCSSVariableValue('--other')             // Couleur pour Autres événements
    }

    var eventSymbols = {
        'smash': '🎮',  // Icône de manette pour Smash
        'mtg': '🃏',    // Icône de carte pour Magic
        'lorcana': '✨',           // Icône de disney pour Lorcana
        'street_fighter': '🥋',  // Icône de kimono pour Street Fighter
        'rpg': '🗡️',    // Icône d’épée pour RPG
        'board_games': '🎲',  // Icône de dé pour les jeux de société
        'other': '⭐'     // Étoile pour les autres types
    };
    
    
    

    // Initialisation du calendrier avec les événements récupérés
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',  // Vue initiale (mois)
        events: events,  // Utiliser les événements chargés dynamiquement
        eventClick: function(info) {
            if (info.event.url) {
                window.location.href = info.event.url;  // Redirige vers la page de détails
            }
            info.jsEvent.preventDefault();
        },
        eventDidMount: function(info) {
            var eventType = info.event.extendedProps.type;
            var color = eventColors[eventType] || eventColors['other'];
            info.el.style.backgroundColor = color;  // Couleur de fond des événements
            info.el.style.borderColor = color;      // Bordure des événements
            info.el.style.color = '#ffffff';            // Couleur du texte
            info.el.style.padding = '5px';              // Ajouter un peu de padding
            info.el.style.borderRadius = '5px';         // Ajouter des coins arrondis
            
            // Ajouter une info-bulle pour afficher la description de l'événement
            var tooltip = new bootstrap.Tooltip(info.el, {
                title: info.event.extendedProps.description || 'Pas de description',
                placement: 'top',
                trigger: 'hover',
                container: 'body'
            });
        },

        // Personnalisation des tailles d'affichage des événements
        // Mise à jour du contenu de l'événement avec une icône
        eventContent: function(arg) {
            var eventType = arg.event.extendedProps.type;
            var symbol = eventSymbols[eventType] || eventSymbols['other'];  // Utiliser un symbole par défaut si non spécifié

            return {
                html: `<div class="event-title">${symbol} ${arg.event.title}</div>` +
                      `<div class="event-time"></div>`
            };
        },
        eventBackgroundColor: '#f08a5d',  // Couleur par défaut des événements
        eventBorderColor: '#b83b5e',      // Couleur de la bordure des événements
        eventTextColor: '#ffffff',        // Couleur du texte dans les événe

    });

    calendar.render();
});


