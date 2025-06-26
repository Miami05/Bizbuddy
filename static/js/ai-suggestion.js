(function () {
  document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("ai-form");
    const keywordInput = document.getElementById("ai-keyword");
    const suggestionEl = document.getElementById("ai-suggestion");

    if (!form) return;

    form.addEventListener("submit", ev => {
      ev.preventDefault();
      const keyword = keywordInput.value.trim();
      if (!keyword) return;
      const country = form.dataset.country;
      suggestionEl.textContent = "Loading...";
      fetch("/api/suggest", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ country, keyword })
      })
        .then(res => res.json())
        .then(data => {
          suggestionEl.textContent = data.suggestion || "No suggestion.";
        })
        .catch(() => {
          suggestionEl.textContent = "Error retrieving suggestion.";
        });
    });
  });
})();
