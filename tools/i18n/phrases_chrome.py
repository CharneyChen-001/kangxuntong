# Chrome, forms, shared UI and RF glossary terms.
# Keys are English source strings (whitespace-normalized on lookup).

def entries():
    P = {}
    def a(en, ru, es, pt, ar):
        P[en] = {"ru": ru, "es": es, "pt": pt, "ar": ar}
    # --- language switcher / chrome ---
    a("Menu", "Меню", "Menú", "Menu", "القائمة")
    a("Language", "Язык", "Idioma", "Idioma", "اللغة")
    a("Home", "Главная", "Inicio", "Início", "الرئيسية")
    a("Products", "Продукция", "Productos", "Produtos", "المنتجات")
    a("Applications", "Применения", "Aplicaciones", "Aplicações", "التطبيقات")
    a("Custom design", "Индивидуальное проектирование", "Diseño a medida", "Projeto à medida", "تصميم حسب الطلب")
    a("Quality", "Качество", "Calidad", "Qualidade", "الجودة")
    a("About", "О компании", "Acerca de", "Sobre nós", "من نحن")
    a("Contact", "Контакты", "Contacto", "Contacto", "اتصل بنا")
    a("Request a quote", "Запросить предложение", "Solicitar una cotización", "Pedir uma cotação", "طلب عرض سعر")
    a("Privacy", "Конфиденциальность", "Privacidad", "Privacidade", "الخصوصية")
    a("Terms", "Условия", "Términos", "Termos", "الشروط")
    a("Pages", "Страницы", "Páginas", "Páginas", "الصفحات")
    a("Rev A", "Ред. A", "Rev. A", "Rev. A", "الإصدار A")
    a("Catalog index PDF", "PDF указателя каталога", "PDF del índice del catálogo", "PDF do índice do catálogo", "فهرس الكتالوج PDF")
    a("12-model roster PDF", "PDF списка из 12 моделей", "PDF de la lista de 12 modelos", "PDF da lista de 12 modelos", "قائمة 12 طرازاً PDF")
    a("Shenzhen factory · Indoor cavity filters, duplexers and combiners · EXW or FOB Shenzhen",
      "Завод в Шэньчжэне · Внутренние фильтры, дуплексеры и комбайнеры на объемных резонаторах · EXW или FOB Shenzhen",
      "Fábrica en Shenzhen · Filtros, dúplexers y combinadores de cavidad para interior · EXW o FOB Shenzhen",
      "Fábrica em Shenzhen · Filtros, duplexadores e combinadores de cavidade para interior · EXW ou FOB Shenzhen",
      "مصنع شنجن · مرشحات ودبلكسرات ومجمعات تجويفية للتركيب الداخلي · EXW أو FOB Shenzhen")
    a("Shenzhen Kangxuntong Technology Co., Ltd. makes cavity filters. The English name is the standard rendering of the registered Chinese name.",
      "Shenzhen Kangxuntong Technology Co., Ltd. производит фильтры на объемных резонаторах. Английское название — стандартная передача зарегистрированного китайского наименования.",
      "Shenzhen Kangxuntong Technology Co., Ltd. fabrica filtros de cavidad. El nombre en inglés es la forma estándar del nombre chino registrado.",
      "A Shenzhen Kangxuntong Technology Co., Ltd. fabrica filtros de cavidade. O nome em inglês é a forma padrão do nome chinês registado.",
      "تُصنّع Shenzhen Kangxuntong Technology Co., Ltd. مرشحات تجويفية. الاسم الإنجليزي هو الصيغة المعتمدة للاسم الصيني المسجّل.")
    a("Shenzhen, Guangdong, China", "Шэньчжэнь, провинция Гуандун, Китай", "Shenzhen, Guangdong, China", "Shenzhen, Guangdong, China", "شنجن، غوانغدونغ، الصين")
    a("EXW / FOB Shenzhen", "EXW / FOB Shenzhen", "EXW / FOB Shenzhen", "EXW / FOB Shenzhen", "EXW / FOB Shenzhen")
    a("Specifications follow Rev A datasheets. The factory test report shipped with the goods is the record for that serial.",
      "Характеристики соответствуют спецификациям ред. A. Заводской протокол испытаний, отгружаемый с изделием, является записью для данного серийного номера.",
      "Las especificaciones siguen las fichas técnicas Rev. A. El informe de ensayo de fábrica que se envía con el equipo es el registro de ese número de serie.",
      "As especificações seguem as fichas técnicas Rev. A. O relatório de ensaio de fábrica enviado com o equipamento é o registo desse número de série.",
      "تتبع المواصفات أوراق البيانات الإصدار A. تقرير الاختبار الصادر من المصنع والمُرفق بالشحنة هو السجل المعتمد لذلك الرقم التسلسلي.")
    a("WhatsApp · 张体进", "WhatsApp · 张体进", "WhatsApp · 张体进", "WhatsApp · 张体进", "WhatsApp · 张体进")

    # --- forms ---
    a("Fill in every required field (name, company, a valid email, country, product, message; quantity on the custom page).",
      "Заполните все обязательные поля (имя, компания, действительный адрес электронной почты, страна, изделие, сообщение; на странице индивидуального проектирования также количество).",
      "Rellene todos los campos obligatorios (nombre, empresa, un correo electrónico válido, país, producto, mensaje; la cantidad en la página de diseño a medida).",
      "Preencha todos os campos obrigatórios (nome, empresa, um correio eletrónico válido, país, produto, mensagem; a quantidade na página de projeto à medida).",
      "يُرجى تعبئة جميع الحقول الإلزامية (الاسم، الشركة، بريد إلكتروني صالح، البلد، المنتج، الرسالة؛ والكمية في صفحة التصميم حسب الطلب).")
    a("Name", "Имя", "Nombre", "Nome", "الاسم")
    a("Company", "Компания", "Empresa", "Empresa", "الشركة")
    a("Work email", "Рабочая почта", "Correo de trabajo", "Correio de trabalho", "البريد المهني")
    a("Country", "Страна", "País", "País", "البلد")
    a("Phone / WhatsApp", "Телефон / WhatsApp", "Teléfono / WhatsApp", "Telefone / WhatsApp", "الهاتف / WhatsApp")
    a("Product or model", "Изделие или модель", "Producto o modelo", "Produto ou modelo", "المنتج أو الطراز")
    a("Model", "Модель", "Modelo", "Modelo", "الطراز")
    a("Quantity", "Количество", "Cantidad", "Quantidade", "الكمية")
    a("Frequency plan", "План частот", "Plan de frecuencias", "Plano de frequências", "خطة الترددات")
    a("Power", "Мощность", "Potencia", "Potência", "القدرة")
    a("Connector", "Разъём", "Conector", "Conector", "الموصل")
    a("Low-PIM option", "Опция низкого PIM", "Opción de bajo PIM", "Opção de baixo PIM", "خيار PIM المنخفض")
    a("Not required", "Не требуется", "No se requiere", "Não necessária", "غير مطلوب")
    a("Required, ≤ −150 dBc", "Требуется, ≤ −150 dBc", "Requerido, ≤ −150 dBc", "Necessário, ≤ −150 dBc", "مطلوب، ≤ −150 dBc")
    a("Message", "Сообщение", "Mensaje", "Mensagem", "الرسالة")
    a("Send enquiry", "Отправить запрос", "Enviar consulta", "Enviar pedido", "إرسال الاستفسار")
    a("Drawing or band plan (optional)", "Чертёж или план частот (необязательно)", "Plano o plano de bandas (opcional)", "Desenho ou plano de bandas (opcional)", "رسم أو خطة نطاقات (اختياري)")
    a("PDF, DWG, DXF, STEP, JPG or PNG, 10 MB in total. Email larger files.",
      "PDF, DWG, DXF, STEP, JPG или PNG, всего не более 10 МБ. Файлы большего размера отправьте по электронной почте.",
      "PDF, DWG, DXF, STEP, JPG o PNG, 10 MB en total. Envíe los archivos más grandes por correo.",
      "PDF, DWG, DXF, STEP, JPG ou PNG, 10 MB no total. Envie ficheiros maiores por correio eletrónico.",
      "PDF أو DWG أو DXF أو STEP أو JPG أو PNG، بما لا يتجاوز 10 ميغابايت إجمالاً. أرسل الملفات الأكبر بالبريد الإلكتروني.")
    a("Or:", "Или:", "O:", "Ou:", "أو:")
    a("Send on WhatsApp", "Отправить в WhatsApp", "Enviar por WhatsApp", "Enviar pelo WhatsApp", "إرسال عبر WhatsApp")
    a("Email sales@cavityfilter.com", "Написать на sales@cavityfilter.com", "Correo a sales@cavityfilter.com", "Correio para sales@cavityfilter.com", "البريد إلى sales@cavityfilter.com")
    a("The enquiry goes straight to sales@cavityfilter.com and we reply by email. The form is relayed by FormSubmit (formsubmit.co); see the",
      "Запрос направляется напрямую на sales@cavityfilter.com, мы отвечаем по электронной почте. Форма пересылается службой FormSubmit (formsubmit.co); см.",
      "La consulta se envía directamente a sales@cavityfilter.com y respondemos por correo. El formulario lo reenvía FormSubmit (formsubmit.co); véase la",
      "O pedido é enviado diretamente para sales@cavityfilter.com e respondemos por correio eletrónico. O formulário é reencaminhado pelo FormSubmit (formsubmit.co); consulte a",
      "يُرسل الاستفسار مباشرة إلى sales@cavityfilter.com ونرد بالبريد الإلكتروني. يُرحَّل النموذج عبر FormSubmit (formsubmit.co)؛ انظر")
    a("privacy note", "уведомление о конфиденциальности", "nota de privacidad", "nota de privacidade", "ملاحظة الخصوصية")
    a("Sending…", "Отправка…", "Enviando…", "A enviar…", "جارٍ الإرسال…")
    a("Sending failed. Please use email or WhatsApp instead; your text is still in the form.",
      "Отправка не удалась. Воспользуйтесь электронной почтой или WhatsApp; текст сохранён в форме.",
      "El envío ha fallado. Use el correo o WhatsApp; el texto sigue en el formulario.",
      "O envio falhou. Utilize o correio eletrónico ou o WhatsApp; o texto permanece no formulário.",
      "فشل الإرسال. يُرجى استخدام البريد الإلكتروني أو WhatsApp؛ يبقى النص في النموذج.")
    a("New RFQ · cavityfilter.com", "Новый запрос · cavityfilter.com", "Nueva RFQ · cavityfilter.com", "Novo RFQ · cavityfilter.com", "طلب تسعير جديد · cavityfilter.com")
    a("New RFQ · cavityfilter.com (Russian)", "Новый запрос · cavityfilter.com (русская версия)", "Nueva RFQ · cavityfilter.com (ruso)", "Novo RFQ · cavityfilter.com (russo)", "طلب تسعير جديد · cavityfilter.com (الروسية)")
    # subject lines set in form_html, not these
    a("Tell us the model, the band and the quantity.",
      "Укажите модель, диапазон и количество.",
      "Indíquenos el modelo, la banda y la cantidad.",
      "Indique-nos o modelo, a banda e a quantidade.",
      "أخبرنا بالطراز والنطاق والكمية.")

    # --- common actions / catalog ---
    a("Browse the catalog", "Смотреть каталог", "Ver el catálogo", "Ver o catálogo", "تصفح الكتالوج")
    a("Open", "Открыть", "Abrir", "Abrir", "فتح")
    a("All", "Все", "Todos", "Todos", "الكل")
    a("Bandpass", "Полосовые", "Paso banda", "Passa-banda", "تمرير نطاق")
    a("Combiners", "Комбайнеры", "Combinadores", "Combinadores", "المجمعات")
    a("Diplexer", "Диплексер", "Diplexor", "Diplexador", "ديبلكسر")
    a("PDF", "PDF", "PDF", "PDF", "PDF")
    a("Download datasheet PDF", "Скачать спецификацию PDF", "Descargar ficha técnica PDF", "Descarregar ficha técnica PDF", "تنزيل ورقة المواصفات PDF")
    a("Shelf model list PDF", "PDF списка складских моделей", "PDF de la lista de modelos de existencias", "PDF da lista de modelos de prateleira", "قائمة طرازات المخزون PDF")
    a("Roster PDF", "PDF списка", "PDF de la lista", "PDF da lista", "قائمة PDF")
    a("Model page", "Страница модели", "Página del modelo", "Página do modelo", "صفحة الطراز")
    a("Specification", "Спецификация", "Especificación", "Especificação", "المواصفات")
    a("Quote", "Запрос", "Cotización", "Cotação", "عرض سعر")
    a("Catalog", "Каталог", "Catálogo", "Catálogo", "الكتالوج")
    a("Full catalog", "Весь каталог", "Catálogo completo", "Catálogo completo", "الكتالوج الكامل")
    a("Product catalog", "Каталог продукции", "Catálogo de productos", "Catálogo de produtos", "كتالوج المنتجات")
    a("Back to the catalog", "Вернуться в каталог", "Volver al catálogo", "Voltar ao catálogo", "العودة إلى الكتالوج")
    a("Send a band plan", "Отправить план частот", "Enviar un plan de bandas", "Enviar um plano de bandas", "إرسال خطة نطاقات")
    a("Send the band plan", "Отправить план частот", "Enviar el plan de bandas", "Enviar o plano de bandas", "إرسال خطة النطاقات")
    a("All applications", "Все применения", "Todas las aplicaciones", "Todas as aplicações", "جميع التطبيقات")
    a("All remaining factory Word sheets", "Все остальные заводские файлы Word", "El resto de las fichas Word de fábrica", "As restantes fichas Word de fábrica", "بقية ملفات Word الصادرة عن المصنع")
    a("Specifications", "Спецификации", "Especificaciones", "Especificações", "المواصفات")
    a("Search 1800, n78, KXT…", "Поиск 1800, n78, KXT…", "Buscar 1800, n78, KXT…", "Pesquisar 1800, n78, KXT…", "بحث 1800، n78، KXT…")
    a("Thank you", "Спасибо", "Gracias", "Obrigado", "شكرًا لك")
    a("Page not found", "Страница не найдена", "Página no encontrada", "Página não encontrada", "الصفحة غير موجودة")
    a("Page not found.", "Страница не найдена.", "Página no encontrada.", "Página não encontrada.", "الصفحة غير موجودة.")
    a("Page not found | Kangxuntong", "Страница не найдена | Kangxuntong", "Página no encontrada | Kangxuntong", "Página não encontrada | Kangxuntong", "الصفحة غير موجودة | Kangxuntong")
    a("Sales", "Продажи", "Ventas", "Vendas", "المبيعات")
    a("Ordering", "Заказ", "Pedido", "Encomenda", "الطلب")
    a("IL", "IL", "IL", "IL", "IL")
    a("Item", "Позиция", "Ítem", "Item", "البند")
    a("Technical", "Технические", "Técnico", "Técnico", "تقني")
    a("Black", "Чёрный", "Negro", "Preto", "أسود")
    a("—, contact us", "—, свяжитесь с нами", "—, contáctenos", "—, contacte-nos", "—، اتصل بنا")
    a("—, state it on the enquiry", "—, укажите в запросе", "—, indíquelo en la consulta", "—, indique-o no pedido", "—، بيّنه في الاستفسار")
    a("Outline as drawn.", "Габариты — по чертежу.", "Contorno según el dibujo.", "Contorno conforme o desenho.", "الأبعاد حسب الرسم.")
    a("N and SMA ports", "Разъёмы N и SMA", "Puertos N y SMA", "Portas N e SMA", "منافذ N وSMA")
    a("Documented passbands", "Документированные полосы пропускания", "Bandas de paso documentadas", "Bandas de passagem documentadas", "نطاقات التمرير الموثّقة")
    a("Datasheets in this catalog", "Спецификации в этом каталоге", "Fichas técnicas de este catálogo", "Fichas técnicas deste catálogo", "أوراق المواصفات في هذا الكتالوج")
    a("Test report with shipment", "Протокол испытаний с поставкой", "Informe de ensayo con el envío", "Relatório de ensaio com o envio", "تقرير اختبار مع الشحنة")
    a("Datasheets issued from the current specification set. Filter by family or search a frequency. Further factory Word sheets are transcribed on the next page.",
      "Спецификации составлены по действующему комплекту технических требований. Фильтруйте по семейству или ищите частоту. Остальные заводские файлы Word расшифрованы на следующей странице.",
      "Fichas técnicas emitidas a partir del conjunto de especificaciones vigente. Filtre por familia o busque una frecuencia. El resto de las fichas Word de fábrica están transcritas en la página siguiente.",
      "Fichas técnicas emitidas a partir do conjunto de especificações vigente. Filtre por família ou pesquise uma frequência. As restantes fichas Word de fábrica estão transcritas na página seguinte.",
      "أُصدرت أوراق المواصفات من مجموعة المواصفات الحالية. صفِّ حسب العائلة أو ابحث عن تردد. نُقلت بقية ملفات Word الصادرة عن المصنع في الصفحة التالية.")
    a("Factory specification files", "Заводские файлы спецификаций", "Fichas de especificación de fábrica", "Ficheiros de especificação de fábrica", "ملفات مواصفات المصنع")
    a("These sheets are transcribed from the remaining factory Word files. Duplicate files with the same table are listed once.",
      "Эти листы расшифрованы из остальных заводских файлов Word. Повторяющиеся файлы с одной и той же таблицей указаны один раз.",
      "Estas fichas se transcriben de los archivos Word de fábrica restantes. Los archivos duplicados con la misma tabla se listan una sola vez.",
      "Estas fichas são transcritas a partir dos restantes ficheiros Word de fábrica. Ficheiros duplicados com a mesma tabela figuram uma só vez.",
      "نُقلت هذه الأوراق من بقية ملفات Word الصادرة عن المصنع. تُدرج الملفات المكررة ذات الجدول نفسه مرة واحدة.")
    a("Quotation shelf, 29 May 2026", "Складские позиции прайс-листа, 29 мая 2026 г.", "Existencias de la cotización, 29 de mayo de 2026", "Prateleira da cotação, 29 de maio de 2026", "مخزون عرض الأسعار، 29 أيار/مايو 2026")
    a("Passbands only. Electrical limits for these twelve models are on each unit’s test report.",
      "Только полосы пропускания. Электрические пределы этих двенадцати моделей указаны в протоколе испытаний каждого изделия.",
      "Solo bandas de paso. Los límites eléctricos de estos doce modelos figuran en el informe de ensayo de cada unidad.",
      "Apenas bandas de passagem. Os limites elétricos destes doze modelos constam do relatório de ensaio de cada unidade.",
      "نطاقات التمرير فقط. الحدود الكهربائية لهذه الطرازات الاثني عشر واردة في تقرير اختبار كل وحدة.")
    a("VHF/UHF Duplexers for Two-way Radio / LMR →",
      "Дуплексеры VHF/UHF для профессиональной радиосвязи / LMR →",
      "Dúplexers VHF/UHF para radio bidireccional / LMR →",
      "Duplexadores VHF/UHF para rádio bidirecional / LMR →",
      "دبلكسرات VHF/UHF للراديو ثنائي الاتجاه / LMR →")
    a("VHF/UHF Duplexers for Two-way Radio / LMR",
      "Дуплексеры VHF/UHF для профессиональной радиосвязи / LMR",
      "Dúplexers VHF/UHF para radio bidireccional / LMR",
      "Duplexadores VHF/UHF para rádio bidirecional / LMR",
      "دبلكسرات VHF/UHF للراديو ثنائي الاتجاه / LMR")
    a("VHF/UHF Duplexers for Two-way Radio / LMR | Kangxuntong",
      "Дуплексеры VHF/UHF для профессиональной радиосвязи / LMR | Kangxuntong",
      "Dúplexers VHF/UHF para radio bidireccional / LMR | Kangxuntong",
      "Duplexadores VHF/UHF para rádio bidirecional / LMR | Kangxuntong",
      "دبلكسرات VHF/UHF للراديو ثنائي الاتجاه / LMR | Kangxuntong")
    a("Products | Kangxuntong", "Продукция | Kangxuntong", "Productos | Kangxuntong", "Produtos | Kangxuntong", "المنتجات | Kangxuntong")
    a("Kangxuntong | Cavity Filters", "Kangxuntong | Фильтры на объемных резонаторах", "Kangxuntong | Filtros de cavidad", "Kangxuntong | Filtros de cavidade", "Kangxuntong | مرشحات تجويفية")
    return P
