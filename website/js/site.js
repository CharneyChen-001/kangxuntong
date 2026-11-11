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

  // ---- RFQ form: posts to FormSubmit (sales@cavityfilter.com); WhatsApp and email are alternatives.
  var form = document.getElementById("rfq");
  if (!form) return;
  var err = document.getElementById("form-error");
  var wa = document.getElementById("wa-link");
  var mail = document.getElementById("mail-link");
  var waNumber = form.getAttribute("data-wa");
  var mailBase = mail ? mail.getAttribute("href").split("?")[0] : "";
  var required = Array.prototype.map.call(form.querySelectorAll("[required]"), function (el) { return el.name; });
  var fileInput = form.querySelector("input[type=file]");

  function summary() {
    var lines = [];
    Array.prototype.forEach.call(form.elements, function (el) {
      if (!el.name || el.type === "submit" || el.type === "hidden" || el.type === "file" || el.name.charAt(0) === "_") return;
      if (String(el.value).trim()) lines.push(el.name + ": " + String(el.value).trim());
    });
    return lines.join("\n");
  }
  function refreshLinks() {
    var text = summary();
    if (wa) wa.href = "https://wa.me/" + waNumber + (text ? "?text=" + encodeURIComponent(text) : "");
    if (mail) mail.href = mailBase + "?subject=" + encodeURIComponent("RFQ " + (form.elements.model && form.elements.model.value || form.elements.product.value || "")) +
      (text ? "&body=" + encodeURIComponent(text) : "");
  }
  form.addEventListener("input", refreshLinks);
  form.addEventListener("change", refreshLinks);
  refreshLinks();

  function valid() {
    var missing = required.filter(function (key) {
      return !form.elements[key] || !String(form.elements[key].value).trim();
    });
    var emailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(form.elements.email.value || ""));
    var size = 0;
    if (fileInput && fileInput.files) Array.prototype.forEach.call(fileInput.files, function (f) { size += f.size; });
    return !missing.length && emailOk && size <= 10 * 1024 * 1024;
  }

  form.addEventListener("submit", function (e) {
    if (form._honey && form._honey.value) { e.preventDefault(); return; }
    if (!valid()) {
      e.preventDefault();
      err.textContent = form.getAttribute("data-error");
      return;
    }
    err.textContent = "";
    if (!window.fetch || !window.FormData) return; // normal POST to FormSubmit, which redirects to _next
    if (fileInput && fileInput.files && fileInput.files.length) return; // attachments go by normal multipart POST (not AJAX)
    e.preventDefault();
    var btn = form.querySelector("button[type=submit]");
    var label = btn.textContent;
    btn.disabled = true;
    btn.textContent = form.getAttribute("data-sending");
    fetch(form.getAttribute("data-ajax"), { method: "POST", headers: { Accept: "application/json" }, body: new FormData(form) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (res.ok && String(res.j.success) !== "false") {
          window.location.href = form.elements._next.value;
        } else {
          throw new Error(res.j && res.j.message || "send failed");
        }
      })
      .catch(function () {
        btn.disabled = false;
        btn.textContent = label;
        err.textContent = form.getAttribute("data-fail");
      });
  });
})();
