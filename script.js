fetch("data/notices.json")
  .then(response => response.json())
  .then(data => {
    const notices = document.getElementById("notices");

    data.forEach(item => {
      notices.innerHTML += `
        <p>
          <a href="${item.link}" target="_blank">
            ${item.title}
          </a>
        </p>
      `;
    });
  });
