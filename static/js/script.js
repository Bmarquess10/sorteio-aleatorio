async function sortear() {
  document.getElementById("erro").textContent = "";
  document.getElementById("resultado").textContent = "";

  const totalNumeros = document.getElementById("totalNumeros").value;
  const numerosSorteados = document.getElementById("numerosSorteados").value;

  try {
    const response = await fetch("/sortear", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `total_numeros=${totalNumeros}&numeros_sorteados=${numerosSorteados}`,
    });
    const data = await response.json();

    if (data.erro) {
      document.getElementById("erro").textContent = data.erro;
    } else {
      document.getElementById("resultado").textContent =
        "Números sorteados: " + data.resultado.join(", ");
    }
  } catch (e) {
    document.getElementById("erro").textContent =
      "Ocorreu um erro. Tente novamente.";
  }
}
