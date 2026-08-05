document.addEventListener("DOMContentLoaded", () => {
  // Accordion Section Toggle Logic
  const groupButtons = document.querySelectorAll(".nav-group-title");

  groupButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const isExpanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", !isExpanded);

      const navList = button.nextElementSibling;
      if (navList) {
        navList.style.display = isExpanded ? "none" : "block";
      }
    });
  });

  // Automatically Expand Section of Active Link
  const activeLink = document.querySelector(".nav-link.active");
  if (activeLink) {
    const parentGroup = activeLink.closest(".nav-group");
    if (parentGroup) {
      const btn = parentGroup.querySelector(".nav-group-title");
      if (btn) btn.setAttribute("aria-expanded", "true");
    }
    // Smooth scroll into view inside sidebar
    activeLink.scrollIntoView({ block: "nearest" });
  }
});
