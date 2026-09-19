const textInput = document.querySelector("#teacherText");
const processButton = document.querySelector("#processButton");
const recordButton = document.querySelector("#recordButton");
const status = document.querySelector("#status");
const cards = document.querySelector("#flashcards");

function renderCards(items) {
  cards.replaceChildren();
  const template = document.querySelector("#flashcardTemplate");
  items.forEach((item) => {
    const card = template.content.cloneNode(true);
    card.querySelector(".emoji").textContent = item.emoji;
    card.querySelector(".hindi").textContent = item.hindi;
    card.querySelector(".santali-word").textContent = item.santali;
    cards.append(card);
  });
}

async function createLearningCards() {
  const text = textInput.value.trim();
  if (!text) { status.textContent = "Please add a short Hindi explanation first."; return; }
  processButton.disabled = true;
  processButton.innerHTML = "Making cards…";
  status.textContent = "Working locally with the lesson pack…";
  try {
    const response = await fetch("/api/process-lesson", {
      method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ text, grade: 2, lesson_id: "plants" })
    });
    if (!response.ok) throw new Error("The local learning service is unavailable.");
    const result = await response.json();
    document.querySelector("#santaliText").textContent = result.translation.translated_text;
    document.querySelector("#translationWarning").textContent = result.translation.warning || "Local learning pack output.";
    document.querySelector("#simpleText").textContent = result.simple_explanation;
    renderCards(result.flashcards);
    status.textContent = "Learning cards are ready — no network was used.";
  } catch (error) {
    status.textContent = `${error.message} Start the local backend, then try again.`;
  } finally {
    processButton.disabled = false;
    processButton.innerHTML = "Create learning cards <b>→</b>";
  }
}

let recognition;
if ("webkitSpeechRecognition" in window) {
  recognition = new webkitSpeechRecognition();
  recognition.lang = "hi-IN";
  recognition.interimResults = false;
  recognition.onresult = (event) => { textInput.value = event.results[0][0].transcript; status.textContent = "Voice captured. Create the learning cards when ready."; };
  recognition.onend = () => { recordButton.classList.remove("active"); recordButton.setAttribute("aria-pressed", "false"); };
}
recordButton.addEventListener("click", () => {
  if (!recognition) { status.textContent = "Live browser speech recognition is not available here. The final tablet app uses local ASR; type the demo text for now."; return; }
  recordButton.classList.add("active"); recordButton.setAttribute("aria-pressed", "true"); recognition.start(); status.textContent = "Listening…";
});
processButton.addEventListener("click", createLearningCards);
document.querySelector("#listenButton").addEventListener("click", () => {
  const utterance = new SpeechSynthesisUtterance(document.querySelector("#santaliText").textContent);
  speechSynthesis.cancel(); speechSynthesis.speak(utterance); status.textContent = "Playing device speech. A verified Santali voice pack is still required for deployment.";
});
renderCards([
  { emoji: "💧", hindi: "पानी", santali: "dak" }, { emoji: "☀️", hindi: "सूरज की धूप", santali: "singi marsal" }, { emoji: "💨", hindi: "हवा", santali: "hawa" }, { emoji: "🟫", hindi: "मिट्टी", santali: "hasa" }
]);
