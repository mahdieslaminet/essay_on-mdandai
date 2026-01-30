const form = document.getElementById("analyzeForm");
const loader = document.getElementById("loader");
const result = document.getElementById("result");
const answer = document.getElementById("answer");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  loader.classList.remove("hidden");
  result.classList.add("hidden");

  const image = document.getElementById("image").files[0];
  const prompt = document.getElementById("prompt").value;

  const formData = new FormData();
  formData.append("image", image);
  formData.append("prompt", prompt);

  try {
    const response = await fetch("http://localhost:8000/infer", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    answer.innerText = data.answer;
    result.classList.remove("hidden");
  } catch (err) {
    alert("خطا در ارتباط با سرور");
  } finally {
    loader.classList.add("hidden");
  }
});
