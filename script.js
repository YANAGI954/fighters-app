Promise.all([
  fetch("fighters_news.json").then(res => res.json()),
  fetch("fighters_standings.json").then(res => res.json())
]).then(([newsData, standingsData]) => {
  const newsList = document.getElementById("news-list");
  newsData.news.forEach(n => {
    const li = document.createElement("li");
    li.innerHTML = `<a href="${n.link}" target="_blank">${n.title}</a>`;
    newsList.appendChild(li);
  });

  const standingsTbody = document.querySelector("#standings-table tbody");
  standingsData.standings.forEach(t => {
    const tr = document.createElement("tr");
    tr.innerHTML = `<td>${t.team}</td><td>${t.wins}</td><td>${t.losses}</td><td>${t.draws}</td><td>${t.win_pct}</td>`;
    standingsTbody.appendChild(tr);
  });
});
