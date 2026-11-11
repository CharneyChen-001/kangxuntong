(function () {
  var params = new URLSearchParams(window.location.search);
  var modelField = document.querySelector("[name=model]");
  var productField = document.querySelector("[name=product]");
  if (params.get("model")) {
    if (modelField) modelField.value = params.get("model");
    if (productField && !productField.value) productField.value = params.get("model");
  }

  var buttons = document.querySelectorAll("[data-filter]");
  var cards = document.querySelectorAll("[data-cat]");
  var search = document.querySelector("[data-search]");
  var current = "all";

  function apply() {
    var q = (search && search.value || "").trim().toLowerCase();
    cards.forEach(function (card) {
      var catOk = current === "all" || card.getAttribute("data-cat") === current;
      var text = card.textContent.toLowerCase();
      card.style.display = catOk && (!q || text.indexOf(q) !== -1) ? "" : "none";
    });
  }

  buttons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      buttons.forEach(function (b) { b.classList.remove("on"); });
      btn.classList.add("on");
      current = btn.getAttribute("data-filter");
      apply();
    });
  });
  if (search) search.addEventListener("input", apply);

  var form = document.getElementById("rfq");
  if (!form) return;
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (form.company_website && form.company_website.value) return;
    var required = ["name", "company", "email", "country", "product", "message"];
    var missing = required.filter(function (key) {
      return !form.elements[key] || !String(form.elements[key].value).trim();
    });
    var email = String(form.elements.email.value || "");
    var emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    var err = document.getElementById("form-error");
    var ok = document.getElementById("form-ok");
    if (missing.length || !emailOk) {
      err.textContent = form.getAttribute("data-error");
      ok.style.display = "none";
      return;
    }
    err.textContent = "";
    var lines = [];
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === "submit" || el.name === "company_website") return;
      if (String(el.value).trim()) lines.push(el.name + ": " + el.value.trim());
    });
    var summary = lines.join("\n");
    var pre = document.getElementById("form-summary");
    pre.textContent = summary;
    ok.style.display = "block";
    var wa = document.getElementById("wa-link");
    wa.href = "https://wa.me/8618688718926?text=" + encodeURIComponent(summary);
    form.reset();
  });
})();
