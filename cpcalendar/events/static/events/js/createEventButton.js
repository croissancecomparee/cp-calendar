function openFormInModal(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById("formContent").innerHTML = html;
        })
        .catch(error => console.error("Erreur lors du chargement du formulaire :", error));
}