document.addEventListener('DOMContentLoaded', function() {
    const tools = document.querySelectorAll('.tool');

    tools.forEach(tool => {
        tool.addEventListener('click', function() {
            const description = tool.getAttribute('data-description');
            const link = tool.getAttribute('data-link');
            const descriptionContainer = tool.querySelector('.description-container');
            const descriptionText = descriptionContainer.querySelector('.description-text');
            const descriptionLink = descriptionContainer.querySelector('.description-link');

            descriptionText.textContent = description;
            descriptionLink.href = link;

            // Ocultar todas las descripciones y quitar la clase 'selected'
            document.querySelectorAll('.description-container').forEach(container => {
                container.style.display = 'none';
            });
            document.querySelectorAll('.tool').forEach(t => {
                t.classList.remove('selected');
            });

            // Mostrar la descripción de la herramienta seleccionada y añadir la clase 'selected'
            descriptionContainer.style.display = 'block';
            tool.classList.add('selected');
        });
    });
});