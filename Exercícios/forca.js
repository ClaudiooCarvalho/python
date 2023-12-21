<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Forca com Palavras Matemáticas</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 50px;
    }

    #forca {
      font-family: monospace;
    }
  </style>
</head>
<body>

<h1>Bem-vindo ao Jogo da Forca com Palavras Matemáticas!</h1>
<div id="forca"></div>
<div id="palavra-atual"></div>
<div id="letras-incorretas"></div>
<input type="text" id="tentativa" placeholder="Digite uma letra">
<button onclick="fazerTentativa()">Tentar</button>
<button onclick="iniciarJogo()">Novo Jogo</button>

<script>
  let palavra, letrasDescobertas, tentativas, maxTentativas, erros, temporizador;

  function escolherPalavra() {
    const palavrasMatematicas = ["derivada", "integral", "equacao", "matriz", "logaritmo"];
    return palavrasMatematicas[Math.floor(Math.random() * palavrasMatematicas.length)];
  }

  function exibirForca(erros) {
    const forca = [
      `
           -----
           |   |
               |
               |
               |
               |
        ----------`,
      `
           -----
           |   |
           O   |
               |
               |
               |
        ----------`,
      `
           -----
           |   |
           O   |
           |   |
               |
               |
        ----------`,
      `
           -----
           |   |
           O   |
          /|   |
               |
               |
        ----------`,
      `
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ----------`,
      `
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ----------`,
      `
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ----------`
    ];
    return forca[erros];
  }

  function iniciarJogo() {
    palavra = escolherPalavra().toUpperCase();
    letrasDescobertas = new Set();
    tentativas = 0;
    maxTentativas = palavra.length + 2;
    erros = 0;

    document.getElementById('forca').innerHTML = '';
    document.getElementById('palavra-atual').innerHTML = '';
    document.getElementById('letras-incorretas').innerHTML = '';
    document.getElementById('tentativa').value = '';

    mostrarForca();
    mostrarPalavraAtual();
  }

  function mostrarForca() {
    document.getElementById('forca').innerHTML = exibirForca(erros);
  }

  function mostrarPalavraAtual() {
    const palavraAtual = palavra.split('').map(letra => letrasDescobertas.has(letra) ? letra : '_').join('');
    document.getElementById('palavra-atual').innerHTML = 'Palavra: ' + palavraAtual;
  }

  function mostrarLetrasIncorretas() {
    const letrasIncorretas = Array.from(new Set(palavra.split('') - letrasDescobertas)).join(', ');
    document.getElementById('letras-incorretas').innerHTML = 'Letras incorretas: ' + letrasIncorretas;
  }

  function fazerTentativa() {
    const tentativaInput = document.getElementById('tentativa');
    const tentativa = tentativaInput.value.toUpperCase();

    if (tentativa.length === 1 && tentativa.match(/[A-Z]/)) {
      if (letrasDescobertas.has(tentativa)) {
        alert("Você já tentou essa letra. Tente novamente.");
      } else if (palavra.includes(tentativa)) {
        letrasDescobertas.add(tentativa);
        mostrarPalavraAtual();
        if (palavra.split('').every(letra => letrasDescobertas.has(letra))) {
          alert("Parabéns! Você venceu!");
          iniciarJogo();
        }
      } else {
        erros++;
        mostrarForca();
        if (erros === maxTentativas) {
          alert("Você perdeu! A palavra era: " + palavra);
          iniciarJogo();
        }
      }

      mostrarLetrasIncorretas();
    } else {
      alert("Por favor, digite uma única letra válida.");
    }

    tentativaInput.value = '';
  }

  function configurarTemporizador() {
    temporizador = parseInt(prompt("Digite o tempo máximo para o jogo (em segundos): "));
    alert("Você tem " + temporizador + " segundos para adivinhar a palavra.");
    setTimeout(() => {
      alert("Tempo esgotado! Você demorou muito. A palavra era: " + escolherPalavra().toUpperCase());
      iniciarJogo();
    }, temporizador * 1000);
  }

  configurarTemporizador();
  iniciarJogo();
</script>

</body>
</html>
