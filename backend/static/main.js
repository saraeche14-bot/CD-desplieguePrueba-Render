// Por defecto usaremos la misma URL de origen (misma máquina / dominio)
const API_BASE = ""; // si el backend está en el mismo dominio

async function loadGames() {
  const statusEl = document.getElementById("status");
  const listEl = document.getElementById("game-list");

  statusEl.textContent = "Cargando juegos...";
  listEl.innerHTML = "";

  try {
    const response = await fetch(`${API_BASE}/api/games`);
    if (!response.ok) {
      throw new Error(`Error HTTP: ${response.status}`);
    }

    const games = await response.json();
    statusEl.textContent = `Se han cargado ${games.length} juegos:`;

    games.forEach(game => {
      const li = document.createElement("li");
      li.textContent = `${game.title} (${game.year}) – ${game.genre}`;
      listEl.appendChild(li);
    });
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error al cargar los juegos. Revisa la consola.";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("reload-btn");
  btn.addEventListener("click", loadGames);
  loadGames();
});
