
document.addEventListener(DOMContentLoaded, () => {
	const tipsContainer = document.getElementById("tips-container")
	const searchInput = document.getElementById("search-input")
	const filter = document.getElementById("category-filter")
	const countryId = window.location.pathname.split("/").pop()

	function fetchTips() {
		fetch(`/api/tips/${countryId}`)
			.then(res => res.json())
			.then(tips => {
				const filtered = tips.filter(
					t =>
						t.content.toLowerCase().includes(searchInput.value.toLowerCase()) &&
						(filter.value === "" || t.category === filter.value)
				);
				if (filtered.length === 0) {
					tipsContainer.innerHTML = `
						<div class="p-4 text-gray-600 italic">
							🚫 No startup tips found. Try changing your search or category.
						</div> 
					`;
				} else {
					tipsContainer.innerHTML = filtered
						.map(
							t => `
								<div class="p-4 border rounded shadow bg-white">
									<p>${t.content}</p>
									<button class="bookmark-btn mt-2 text-blue-600 underline"
										data-id="${t.id}">Bookmark</button>
								</div>
							`
						)
						.join("");
				}
				document.querySelectorAll(".bookmark-btn").forEach(btn => {
					btn.addEventListener("click", () => {
						fetch("/api/bookmark", {
							method: "POST",
							headers: { "Content-Type": "application/json" },
							body: JSON.stringify({ tip_id: btn.dataset.id }),
						});
					});
				});
			});
	}
	searchInput.addEventListener("input", fetchTips);
	filter.addEventListener("change", fetchTips);
	fetchTips();
});
