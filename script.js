fetch("./data/notices.json")
  .then(r => r.json())
  .then(data => {
    const notices = document.getElementById("notices");

    data.forEach(item => {
      const p = document.createElement("p");

      p.innerHTML =
        `<a href="${item.link}" target="_blank">${item.title}</a>`;

      notices.appendChild(p);
    });
  })
  .catch(err => {
    document.getElementById("notices").innerHTML =
      "<p>Error loading notices.</p>";
    console.error(err);
  });
