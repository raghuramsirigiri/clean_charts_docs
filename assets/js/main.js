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

  // ─── Mobile Sidebar Toggle ───
  const sidebar = document.querySelector(".docs-sidebar");
  const toggleBtn = document.querySelector(".sidebar-toggle");

  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener("click", () => {
      const isOpen = sidebar.classList.toggle("open");
      toggleBtn.setAttribute("aria-expanded", isOpen);
    });
  }

  // Auto-close sidebar when a nav link is tapped (mobile)
  document.querySelectorAll(".nav-link").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth <= 900 && sidebar && sidebar.classList.contains("open")) {
        sidebar.classList.remove("open");
        if (toggleBtn) toggleBtn.setAttribute("aria-expanded", "false");
      }
    });
  });
});
