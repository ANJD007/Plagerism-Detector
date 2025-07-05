document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);

  const res = await fetch("/compare", {
    method: "POST",
    body: formData,
  });

  const data = await res.json();
  document.getElementById("resultBox").textContent = `Similarity: ${data.similarity}%`;
});
