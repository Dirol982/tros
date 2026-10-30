(function () {
  // Мобильное меню
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Копирование номера телефона
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy');
      var done = function () { var t = b.textContent; b.textContent = 'Скопировано'; setTimeout(function () { b.textContent = t; }, 1600); };
      try {
        navigator.clipboard.writeText(text).then(done, function () { selectText(b); });
      } catch (e) { selectText(b); }
    });
  });
  function selectText(b) {
    var a = b.parentNode.querySelector('a');
    if (!a) return;
    var r = document.createRange(); r.selectNodeContents(a);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }

  // Интерактивная схема троса: точки на чертеже ↔ карточки неисправностей
  var spots = document.querySelectorAll('.hotspot');
  var faults = document.querySelectorAll('.fault');
  function activate(id) {
    spots.forEach(function (s) { s.classList.toggle('is-active', s.dataset.part === id); });
    faults.forEach(function (f) {
      var on = f.dataset.part === id;
      f.classList.toggle('is-active', on);
      f.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
  }
  spots.forEach(function (s) {
    s.addEventListener('click', function () { activate(s.dataset.part); });
    s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(s.dataset.part); } });
  });
  faults.forEach(function (f) {
    f.addEventListener('click', function () { activate(f.dataset.part); });
    f.addEventListener('mouseenter', function () { activate(f.dataset.part); });
  });
  if (faults.length) activate(faults[0].dataset.part);

  // Имя выбранного фото
  document.querySelectorAll('.file-drop input').forEach(function (inp) {
    inp.addEventListener('change', function () {
      var out = inp.closest('.file-drop').querySelector('span');
      var n = inp.files ? inp.files.length : 0;
      out.textContent = n ? 'Выбрано фото: ' + n : 'Прикрепите 1–3 фото троса или кулисы';
    });
  });

  // Форма расчёта. В прототипе заявка не отправляется: на рабочем сайте
  // обработчик передаёт её на почту и в мессенджер мастера.
  document.querySelectorAll('form[data-order]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var phone = form.querySelector('input[type="tel"]');
      if (phone && phone.value.replace(/\D/g, '').length < 9) {
        phone.setCustomValidity('Укажите номер полностью, например +375 29 123-45-67');
        phone.reportValidity();
        return;
      }
      var box = form.querySelector('.form-done');
      box.hidden = false;
      box.textContent = 'Заявка сформирована. Это прототип сайта, поэтому она никуда не отправлена. На рабочем сайте мастер получит её сразу и перезвонит с расчётом.';
    });
    var tel = form.querySelector('input[type="tel"]');
    if (tel) tel.addEventListener('input', function () { tel.setCustomValidity(''); });
  });

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
