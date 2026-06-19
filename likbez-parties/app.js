const tableBody = document.querySelector("#party-table");
const cardsRoot = document.querySelector("#party-cards");
const filters = document.querySelectorAll(".filter");
const currentNewsList = document.querySelector("#current-news-list");
const currentNewsSource = document.querySelector("#current-news-source");

function renderCurrentNews() {
  if (!currentNewsList || !window.CURRENT_NEWS) return;

  currentNewsList.innerHTML = window.CURRENT_NEWS.items.map((item) => `
    <li>${item}</li>
  `).join("");

  if (currentNewsSource) {
    const sourceUrl = window.CURRENT_NEWS.sourceUrl;
    const source = sourceUrl
      ? `<a href="${sourceUrl}" rel="noopener">${window.CURRENT_NEWS.source}</a>`
      : window.CURRENT_NEWS.source;
    currentNewsSource.innerHTML = `Источник: ${source} · обновлено: ${window.CURRENT_NEWS.updatedAt}`;
  }
}

function renderParties(filter = "all") {
  const parties = window.PARTIES.filter((party) => {
    return filter === "all" || party.tags.includes(filter);
  });

  tableBody.innerHTML = parties.map((party) => `
    <tr>
      <td><a href="#${party.id}">${party.name}</a><small>${party.hebrew}</small></td>
      <td>${party.leader}</td>
      <td>${party.camp}</td>
      <td>${party.topic}</td>
      <td>${party.short}</td>
    </tr>
  `).join("");

  cardsRoot.innerHTML = parties.map((party) => `
    <article class="party-card" id="${party.id}">
      <div class="party-card-head">
        <div>
          <p class="party-hebrew">${party.hebrew}</p>
          <h3>${party.name}</h3>
        </div>
        <span>${party.camp}</span>
      </div>
      <dl>
        <div>
          <dt>Лидер</dt>
          <dd>${party.leader}</dd>
        </div>
        <div>
          <dt>Кому говорит</dt>
          <dd>${party.audience}</dd>
        </div>
        <div>
          <dt>Коалиционная логика</dt>
          <dd>${party.coalition}</dd>
        </div>
      </dl>
      <p>${party.explain}</p>
      <p class="party-note">${party.note}</p>
    </article>
  `).join("");
}

filters.forEach((button) => {
  button.addEventListener("click", () => {
    filters.forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    renderParties(button.dataset.filter);
  });
});

renderCurrentNews();
renderParties();
