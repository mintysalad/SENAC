// JavaScript (portfolio.js)
// Esse arquivo pode ser usado para adicionar interatividade ao seu portfólio.

document.addEventListener("DOMContentLoaded", () => {
    console.log("Página carregada com sucesso!");
  
    // Exemplo de evento de clique nos links do menu
    const navLinks = document.querySelectorAll("header nav ul li a");
    navLinks.forEach(link => {
      link.addEventListener("click", event => {
        event.preventDefault();
        const targetId = link.getAttribute("href").substring(1);
        const targetSection = document.getElementById(targetId);
  
        if (targetSection) {
          window.scrollTo({
            top: targetSection.offsetTop,
            behavior: "smooth",
          });
        }
      });
    });
  
    // Gerar novos corações animados periodicamente
    const heartContainer = document.body;
    setInterval(() => {
      const heart = document.createElement("div");
      heart.classList.add("heart");
      heart.style.left = `${Math.random() * 100}%`;
      heart.style.animationDelay = `${Math.random() * 5}s`;
      heartContainer.appendChild(heart);
  
      setTimeout(() => {
        heart.remove();
      }, 5000);
    }, 1000);
  });