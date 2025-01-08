import { API_BASE_URL } from "./config.js";

async function testAPIConnection() {
    try {
        const response = await fetch(`${API_BASE_URL}/utils/test_crewai_db`);
        const data = await response.json();
        console.log("Resposta da API:", data); // Log da resposta para depuração

        if (data.status === "success") {
            document.getElementById("api-status").textContent = "Conexão com a API bem-sucedida!";
        } else {
            document.getElementById("api-status").textContent = `Erro: ${data.message || "Resposta inesperada"}`;
        }
    } catch (error) {
        console.error("Erro ao conectar à API:", error);
        document.getElementById("api-status").textContent = "Erro ao conectar à API!";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    testAPIConnection();
});
