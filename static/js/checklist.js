document.addEventListener("DOMContentLoaded", () => {
	const checklist = document.getElementById("checklist")
	const country_id = window.location.pathname.split("/").pop()
	fetch(`/api/checklist/${country_id}`)
		.then(res => res.json())
		.then(steps => {
			checklist.innerHTML = steps
				.map(
					s => `<li class="flex item-center space-x-2">
						<input type="checkbox", onchange="saveChecklist(${s.id}, this.checked)"/>
						<span>${s.step_number}. ${s.content}</span>
				</li>`
				)
				.join("")
		});
});

function saveChecklist(stepId, completed) {
	fetch("/api/checklist-progress", {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify({ step_id: stepId, completed }),
	});
}
