# Product-type names, specification labels and reusable title fragments.

def entries():
    P = {}
    def a(en, ru, es, pt, ar):
        P[en] = {"ru": ru, "es": es, "pt": pt, "ar": ar}

    # --- product types (title case + sentence case) ---
    types = [
        ("Cavity Bandpass Filter",
         "Полосовой фильтр на объемных резонаторах",
         "Filtro paso banda de cavidad",
         "Filtro passa-banda de cavidade",
         "مرشح تجويفي تمرير نطاق"),
        ("Cavity Duplexer",
         "Дуплексер на объемных резонаторах",
         "Dúplexer de cavidad",
         "Duplexador de cavidade",
         "دبلكسر تجويفي"),
        ("UHF Cavity Duplexer",
         "УВЧ дуплексер на объемных резонаторах",
         "Dúplexer de cavidad UHF",
         "Duplexador de cavidade UHF",
         "دبلكسر تجويفي UHF"),
        ("B3 FDD Cavity Duplexer",
         "Дуплексер B3 FDD на объемных резонаторах",
         "Dúplexer de cavidad B3 FDD",
         "Duplexador de cavidade B3 FDD",
         "دبلكسر تجويفي B3 FDD"),
        ("Dual-band Cavity Diplexer",
         "Двухдиапазонный диплексер на объемных резонаторах",
         "Diplexor de cavidad de doble banda",
         "Diplexador de cavidade de banda dupla",
         "ديبلكسر تجويفي ثنائي النطاق"),
        ("2-port Cavity Combiner",
         "Двухпортовый резонаторный комбайнер",
         "Combinador de cavidad de 2 puertos",
         "Combinador de cavidade de 2 portas",
         "مجمع تجويفي ثنائي المنافذ"),
        ("4-port Cavity Combiner",
         "Четырёхпортовый резонаторный комбайнер",
         "Combinador de cavidad de 4 puertos",
         "Combinador de cavidade de 4 portas",
         "مجمع تجويفي رباعي المنافذ"),
        ("B5 + B3 + B40 Cavity Pentaplexer",
         "Пентаплексер B5 + B3 + B40 на объемных резонаторах",
         "Pentaplexor de cavidad B5 + B3 + B40",
         "Pentaplexador de cavidade B5 + B3 + B40",
         "بنتابلكسر تجويفي B5 + B3 + B40"),
        ("Bandpass filter",
         "Полосовой фильтр",
         "Filtro paso banda",
         "Filtro passa-banda",
         "مرشح تمرير نطاق"),
        ("Bandpass filters",
         "Полосовые фильтры",
         "Filtros paso banda",
         "Filtros passa-banda",
         "مرشحات تمرير نطاق"),
        ("Duplexer",
         "Дуплексер",
         "Dúplexer",
         "Duplexador",
         "دبلكسر"),
        ("UHF cavity duplexer",
         "УВЧ дуплексер на объемных резонаторах",
         "Dúplexer de cavidad UHF",
         "Duplexador de cavidade UHF",
         "دبلكسر تجويفي UHF"),
    ]
    # N-band combiners
    nband = {
        "2": ("Двухдиапазонный резонаторный комбайнер", "Combinador de cavidad de 2 bandas", "Combinador de cavidade de 2 bandas", "مجمع تجويفي ثنائي النطاق"),
        "3": ("Трёхдиапазонный резонаторный комбайнер", "Combinador de cavidad de 3 bandas", "Combinador de cavidade de 3 bandas", "مجمع تجويفي ثلاثي النطاقات"),
        "4": ("Четырёхдиапазонный резонаторный комбайнер", "Combinador de cavidad de 4 bandas", "Combinador de cavidade de 4 bandas", "مجمع تجويفي رباعي النطاقات"),
        "5": ("Пятидиапазонный резонаторный комбайнер", "Combinador de cavidad de 5 bandas", "Combinador de cavidade de 5 bandas", "مجمع تجويفي خماسي النطاقات"),
        "6": ("Шестидиапазонный резонаторный комбайнер", "Combinador de cavidad de 6 bandas", "Combinador de cavidade de 6 bandas", "مجمع تجويفي سداسي النطاقات"),
        "7": ("Семидиапазонный резонаторный комбайнер", "Combinador de cavidad de 7 bandas", "Combinador de cavidade de 7 bandas", "مجمع تجويفي سباعي النطاقات"),
        "8": ("Восьмидиапазонный резонаторный комбайнер", "Combinador de cavidad de 8 bandas", "Combinador de cavidade de 8 bandas", "مجمع تجويفي ثماني النطاقات"),
        "9": ("Девятидиапазонный резонаторный комбайнер", "Combinador de cavidad de 9 bandas", "Combinador de cavidade de 9 bandas", "مجمع تجويفي تساعي النطاقات"),
        "10": ("Десятидиапазонный резонаторный комбайнер", "Combinador de cavidad de 10 bandas", "Combinador de cavidade de 10 bandas", "مجمع تجويفي بعشرة نطاقات"),
    }
    for n, (ru, es, pt, ar) in nband.items():
        types.append((f"{n}-band Cavity Combiner", ru, es, pt, ar))
    types += [
        ("6-band Cavity Combiner, low band",
         "Шестидиапазонный резонаторный комбайнер, нижний диапазон",
         "Combinador de cavidad de 6 bandas, banda baja",
         "Combinador de cavidade de 6 bandas, banda baixa",
         "مجمع تجويفي سداسي النطاقات، النطاق الأدنى"),
        ("8-band Cavity Combiner, mid band",
         "Восьмидиапазонный резонаторный комбайнер, средний диапазон",
         "Combinador de cavidad de 8 bandas, banda media",
         "Combinador de cavidade de 8 bandas, banda média",
         "مجمع تجويفي ثماني النطاقات، النطاق الأوسط"),
        ("2-band Cavity Combiner, high band",
         "Двухдиапазонный резонаторный комбайнер, верхний диапазон",
         "Combinador de cavidad de 2 bandas, banda alta",
         "Combinador de cavidade de 2 bandas, banda alta",
         "مجمع تجويفي ثنائي النطاق، النطاق الأعلى"),
        ("6-band Cavity Combiner (B5, B8, B28)",
         "Шестидиапазонный резонаторный комбайнер (B5, B8, B28)",
         "Combinador de cavidad de 6 bandas (B5, B8, B28)",
         "Combinador de cavidade de 6 bandas (B5, B8, B28)",
         "مجمع تجويفي سداسي النطاقات (B5, B8, B28)"),
        ("7-band Cavity Combiner (B1, B3, B40, B41, n78)",
         "Семидиапазонный резонаторный комбайнер (B1, B3, B40, B41, n78)",
         "Combinador de cavidad de 7 bandas (B1, B3, B40, B41, n78)",
         "Combinador de cavidade de 7 bandas (B1, B3, B40, B41, n78)",
         "مجمع تجويفي سباعي النطاقات (B1, B3, B40, B41, n78)"),
        ("Cavity Quadplexer",
         "Квадруплексер на объемных резонаторах",
         "Cuadriplexor de cavidad",
         "Quadriplexador de cavidade",
         "كوادربلكسر تجويفي"),
        ("Cavity Quadplexer with Coupled Port",
         "Квадруплексер на объемных резонаторах с ответвлённым портом",
         "Cuadriplexor de cavidad con puerto acoplado",
         "Quadriplexador de cavidade com porta acoplada",
         "كوادربلكسر تجويفي بمنفذ اقتران"),
    ]
    def lower_first(s):
        return s[0].lower() + s[1:] if s and s[0].isupper() else s
    for en, ru, es, pt, ar in types:
        a(en, ru, es, pt, ar)
        low = lower_first(en)
        if low != en:
            a(low, lower_first(ru), lower_first(es), lower_first(pt), ar)
        if en.lower() != en and en.lower() not in P:
            a(en.lower(), lower_first(ru), lower_first(es), lower_first(pt), ar)

    a("Specification transcribed from the factory Word file; the test report ships with the unit.",
      "Спецификация расшифрована из заводского файла Word; протокол испытаний отгружается вместе с изделием.",
      "Especificación transcrita del archivo Word de fábrica; el informe de ensayo se envía con la unidad.",
      "Especificação transcrita do ficheiro Word de fábrica; o relatório de ensaio é enviado com a unidade.",
      "نُقلت المواصفات من ملف Word الصادر عن المصنع؛ ويُشحن تقرير الاختبار مع الوحدة.")
    a("Shelf model from the 29 May 2026 quotation; 50 Ω indoor aluminum cavity. Electrical limits are on the unit’s test report.",
      "Складская модель из прайс-листа от 29 мая 2026 г.; алюминиевый резонатор 50 Ω для помещений. Электрические пределы указаны в протоколе испытаний изделия.",
      "Modelo de existencias de la cotización del 29 de mayo de 2026; cavidad de aluminio de 50 Ω para interior. Los límites eléctricos figuran en el informe de ensayo de la unidad.",
      "Modelo de prateleira da cotação de 29 de maio de 2026; cavidade de alumínio de 50 Ω para interior. Os limites elétricos constam do relatório de ensaio da unidade.",
      "طراز مخزون من عرض الأسعار المؤرخ 29 أيار/مايو 2026؛ تجويف ألومنيوم 50 Ω للتركيب الداخلي. الحدود الكهربائية واردة في تقرير اختبار الوحدة.")
    a("passband", "полоса пропускания", "banda de paso", "banda de passagem", "نطاق التمرير")
    a("Passband", "Полоса пропускания", "Banda de paso", "Banda de passagem", "نطاق التمرير")
    a("Passbands", "Полосы пропускания", "Bandas de paso", "Bandas de passagem", "نطاقات التمرير")

    # --- spec labels ---
    labels = [
        ("Electrical specification", "Электрические характеристики", "Especificación eléctrica", "Especificação elétrica", "المواصفات الكهربائية"),
        ("Rejection and isolation", "Подавление и развязка", "Rechazo y aislamiento", "Rejeição e isolamento", "الرفض والعزل"),
        ("What the quotation states", "Что указано в прайс-листе", "Lo que indica la cotización", "O que a cotação indica", "ما يذكره عرض الأسعار"),
        ("Insertion loss", "Вносимые потери", "Pérdida de inserción", "Perda de inserção", "فقد الإدخال"),
        ("Ripple", "Неравномерность", "Rizado", "Ondulação", "التموج"),
        ("VSWR", "VSWR", "VSWR", "VSWR", "VSWR"),
        ("Return loss", "Потери на отражение", "Pérdida de retorno", "Perda de retorno", "فقد الراجع"),
        ("Bandwidth", "Полоса", "Ancho de banda", "Largura de banda", "عرض النطاق"),
        ("Temperature", "Температура", "Temperatura", "Temperatura", "درجة الحرارة"),
        ("Operating temperature", "Рабочая температура", "Temperatura de funcionamiento", "Temperatura de funcionamento", "درجة حرارة التشغيل"),
        ("Storage temperature", "Температура хранения", "Temperatura de almacenamiento", "Temperatura de armazenamento", "درجة حرارة التخزين"),
        ("Impedance", "Сопротивление", "Impedancia", "Impedância", "الممانعة"),
        ("Outline", "Габариты", "Contorno", "Contorno", "الأبعاد الخارجية"),
        ("Finish", "Покрытие", "Acabado", "Acabamento", "التشطيب"),
        ("Humidity", "Влажность", "Humedad", "Humidade", "الرطوبة"),
        ("Average power", "Средняя мощность", "Potencia media", "Potência média", "القدرة المتوسطة"),
        ("Frequency", "Частота", "Frecuencia", "Frequência", "التردد"),
        ("Rejection", "Подавление", "Rechazo", "Rejeição", "الرفض"),
        ("Isolation", "Развязка", "Aislamiento", "Isolamento", "العزل"),
        ("Port", "Порт", "Puerto", "Porta", "المنفذ"),
        ("Band", "Диапазон", "Banda", "Banda", "النطاق"),
        ("Limit", "Предел", "Límite", "Limite", "الحد"),
        ("Type", "Тип", "Tipo", "Tipo", "النوع"),
        ("Type (as on the quotation)", "Тип (как в прайс-листе)", "Tipo (según la cotización)", "Tipo (como na cotação)", "النوع (كما في عرض الأسعار)"),
        ("Construction", "Конструкция", "Construcción", "Construção", "الإنشاء"),
        ("Insertion loss / ripple / rejection", "Вносимые потери / неравномерность / подавление", "Pérdida de inserción / rizado / rechazo", "Perda de inserção / ondulação / rejeição", "فقد الإدخال / التموج / الرفض"),
        ("Mounting pitch", "Шаг крепежа", "Paso de montaje", "Passo de montagem", "تباعد فتحات التثبيت"),
        ("Mounting hole", "Крепёжное отверстие", "Orificio de montaje", "Furo de montagem", "فتحة التثبيت"),
        ("RF connector", "РЧ-разъём", "Conector de RF", "Conector de RF", "موصل التردد الراديوي"),
        ("Name", "Наименование", "Nombre", "Nome", "الاسم"),  # may collide with form Name - same translation is ok for RU "Имя" vs "Наименование"
        ("Stated on the factory sheet", "Указано в заводском листе", "Indicados en la ficha de fábrica", "Indicados na ficha de fábrica", "مبيَّن في ورقة المصنع"),
        ("Channel 1 (as written)", "Канал 1 (как записано)", "Canal 1 (según está escrito)", "Canal 1 (como está escrito)", "القناة 1 (كما هو مكتوب)"),
        ("Channel 2 (as written)", "Канал 2 (как записано)", "Canal 2 (según está escrito)", "Canal 2 (como está escrito)", "القناة 2 (كما هو مكتوب)"),
        ("CH1 Passband", "CH1 Полоса пропускания", "CH1 Banda de paso", "CH1 Banda de passagem", "CH1 نطاق التمرير"),
        ("CH1 Bandwidth", "CH1 Полоса", "CH1 Ancho de banda", "CH1 Largura de banda", "CH1 عرض النطاق"),
        ("CH1 Insertion loss", "CH1 Вносимые потери", "CH1 Pérdida de inserción", "CH1 Perda de inserção", "CH1 فقد الإدخال"),
        ("CH1 Ripple", "CH1 Неравномерность", "CH1 Rizado", "CH1 Ondulação", "CH1 التموج"),
        ("CH1 VSWR", "CH1 VSWR", "CH1 VSWR", "CH1 VSWR", "CH1 VSWR"),
        ("CH1 Return loss", "CH1 Потери на отражение", "CH1 Pérdida de retorno", "CH1 Perda de retorno", "CH1 فقد الراجع"),
        ("CH2 Passband", "CH2 Полоса пропускания", "CH2 Banda de paso", "CH2 Banda de passagem", "CH2 نطاق التمرير"),
        ("CH2 Bandwidth", "CH2 Полоса", "CH2 Ancho de banda", "CH2 Largura de banda", "CH2 عرض النطاق"),
        ("CH2 Insertion loss", "CH2 Вносимые потери", "CH2 Pérdida de inserción", "CH2 Perda de inserção", "CH2 فقد الإدخال"),
        ("CH2 Ripple", "CH2 Неравномерность", "CH2 Rizado", "CH2 Ondulação", "CH2 التموج"),
        ("CH2 VSWR", "CH2 VSWR", "CH2 VSWR", "CH2 VSWR", "CH2 VSWR"),
        ("CH2 Return loss", "CH2 Потери на отражение", "CH2 Pérdida de retorno", "CH2 Perda de retorno", "CH2 فقد الراجع"),
        ("CH3 Passband", "CH3 Полоса пропускания", "CH3 Banda de paso", "CH3 Banda de passagem", "CH3 نطاق التمرير"),
        ("CH3 Bandwidth", "CH3 Полоса", "CH3 Ancho de banda", "CH3 Largura de banda", "CH3 عرض النطاق"),
        ("CH3 Insertion loss", "CH3 Вносимые потери", "CH3 Pérdida de inserción", "CH3 Perda de inserção", "CH3 فقد الإدخال"),
        ("CH3 Ripple", "CH3 Неравномерность", "CH3 Rizado", "CH3 Ondulação", "CH3 التموج"),
        ("CH3 VSWR", "CH3 VSWR", "CH3 VSWR", "CH3 VSWR", "CH3 VSWR"),
        ("CH3 Return loss", "CH3 Потери на отражение", "CH3 Pérdida de retorno", "CH3 Perda de retorno", "CH3 فقد الراجع"),
        ("CH4 Passband", "CH4 Полоса пропускания", "CH4 Banda de paso", "CH4 Banda de passagem", "CH4 نطاق التمرير"),
        ("CH4 Bandwidth", "CH4 Полоса", "CH4 Ancho de banda", "CH4 Largura de banda", "CH4 عرض النطاق"),
        ("CH4 Insertion loss", "CH4 Вносимые потери", "CH4 Pérdida de inserción", "CH4 Perda de inserção", "CH4 فقد الإدخال"),
        ("CH4 Ripple", "CH4 Неравномерность", "CH4 Rizado", "CH4 Ondulação", "CH4 التموج"),
        ("CH4 VSWR", "CH4 VSWR", "CH4 VSWR", "CH4 VSWR", "CH4 VSWR"),
        ("CH4 Return loss", "CH4 Потери на отражение", "CH4 Pérdida de retorno", "CH4 Perda de retorno", "CH4 فقد الراجع"),
        ("Port 1", "Порт 1", "Puerto 1", "Porta 1", "المنفذ 1"),
        ("Port 2", "Порт 2", "Puerto 2", "Porta 2", "المنفذ 2"),
        ("Port 3", "Порт 3", "Puerto 3", "Porta 3", "المنفذ 3"),
        ("Port 4", "Порт 4", "Puerto 4", "Porta 4", "المنفذ 4"),
        ("Port 5", "Порт 5", "Puerto 5", "Porta 5", "المنفذ 5"),
        ("Port 6", "Порт 6", "Puerto 6", "Porta 6", "المنفذ 6"),
        ("Port 7", "Порт 7", "Puerto 7", "Porta 7", "المنفذ 7"),
        ("Port 8", "Порт 8", "Puerto 8", "Porta 8", "المنفذ 8"),
        ("Port 9", "Порт 9", "Puerto 9", "Porta 9", "المنفذ 9"),
        ("Port 10", "Порт 10", "Puerto 10", "Porta 10", "المنفذ 10"),
    ]
    # Note: "Name" already in chrome as "Имя". For bilingual "名称 / Name" the English part "Name" would become "Имя" which is slightly off (should be Наименование) but acceptable in a factory header. I'll leave chrome Name as Имя for the form, and not override. First-write wins if we merge chrome first then terms... I'll skip re-adding Name here.
    for en, ru, es, pt, ar in labels:
        if en == "Name":
            continue
        a(en, ru, es, pt, ar)

    # common cell values
    a("N male or N female, specify on the order",
      "N штекер или N гнездо, указать в заказе",
      "N macho o N hembra, especificar en el pedido",
      "N macho ou N fêmea, especificar na encomenda",
      "N ذكر أو N أنثى، يُحدَّد في الطلب")
    a("Aluminum cavity, conductive oxidation, natural; black on request",
      "Алюминиевый резонатор, токопроводящее оксидирование, натуральный цвет; чёрный — по запросу",
      "Cavidad de aluminio, oxidación conductora, natural; negro bajo pedido",
      "Cavidade de alumínio, oxidação condutora, natural; preto sob pedido",
      "تجويف ألومنيوم، أكسدة موصلة، لون طبيعي؛ أسود عند الطلب")
    a("PIM3 ≤ −150 dBc @ 2×43 dBm", "PIM3 ≤ −150 dBc @ 2×43 dBm", "PIM3 ≤ −150 dBc @ 2×43 dBm", "PIM3 ≤ −150 dBc @ 2×43 dBm", "PIM3 ≤ −150 dBc @ 2×43 dBm")
    a("50 Ω (series interface)", "50 Ω (интерфейс серии)", "50 Ω (interfaz de la serie)", "50 Ω (interface da série)", "50 Ω (واجهة السلسلة)")
    a("indoor aluminum cavity (series interface)",
      "алюминиевый резонатор для помещений (интерфейс серии)",
      "cavidad de aluminio para interior (interfaz de la serie)",
      "cavidade de alumínio para interior (interface da série)",
      "تجويف ألومنيوم للتركيب الداخلي (واجهة السلسلة)")
    a("Indoor type, aluminum cavity (series interface)",
      "Исполнение для помещений, алюминиевый резонатор (интерфейс серии)",
      "Tipo de interior, cavidad de aluminio (interfaz de la serie)",
      "Tipo de interior, cavidade de alumínio (interface da série)",
      "نوع داخلي، تجويف ألومنيوم (واجهة السلسلة)")
    a("not stated on the quotation; taken from the unit’s test report",
      "в прайс-листе не указано; принимается по протоколу испытаний изделия",
      "no consta en la cotización; se toma del informe de ensayo de la unidad",
      "não consta da cotação; toma-se do relatório de ensaio da unidade",
      "غير مبيَّن في عرض الأسعار؛ يُؤخذ من تقرير اختبار الوحدة")
    a("SMA female", "SMA гнездо", "SMA hembra", "SMA fêmea", "SMA أنثى")
    a("N-F / SMA-F", "N-F / SMA-F", "N-F / SMA-F", "N-F / SMA-F", "N-F / SMA-F")

    # aria / alt prefixes
    a("Outline drawing of", "Габаритный чертёж", "Dibujo de contorno de", "Desenho de contorno de", "رسم الأبعاد الخارجية لـ")
    a("Cavity filter housings on the shelf in the Kangxuntong factory, Shenzhen",
      "Корпуса фильтров на объемных резонаторах на стеллаже завода Kangxuntong, Шэньчжэнь",
      "Carcasas de filtros de cavidad en la estantería de la fábrica Kangxuntong, Shenzhen",
      "Caixas de filtros de cavidade na prateleira da fábrica Kangxuntong, Shenzhen",
      "أغلفة مرشحات تجويفية على الرف في مصنع Kangxuntong، شنجن")
    a("Technician tuning a cavity filter on a vector network analyzer",
      "Настройка фильтра на объемных резонаторах на векторном анализаторе цепей",
      "Técnico sintonizando un filtro de cavidad en un analizador de redes vectorial",
      "Técnico a sintonizar um filtro de cavidade num analisador de redes vetorial",
      "فنّي يضبط مرشحًا تجويفيًا على محلل شبكة متجهي")
    a("Cavity combiners and bandpass filters on the factory bench",
      "Резонаторные комбайнеры и полосовые фильтры на заводском столе",
      "Combinadores de cavidad y filtros paso banda en el banco de la fábrica",
      "Combinadores de cavidade e filtros passa-banda na bancada da fábrica",
      "مجمعات تجويفية ومرشحات تمرير نطاق على طاولة المصنع")
    a("Kangxuntong cavity filter workshop in Shenzhen",
      "Цех фильтров на объемных резонаторах Kangxuntong в Шэньчжэне",
      "Taller de filtros de cavidad de Kangxuntong en Shenzhen",
      "Oficina de filtros de cavidade da Kangxuntong em Shenzhen",
      "ورشة مرشحات Kangxuntong التجويفية في شنجن")
    a("Shelf cavity hardware, photographed in the factory.",
      "Резонаторные изделия на стеллаже, снято на заводе.",
      "Hardware de cavidad en la estantería, fotografiado en la fábrica.",
      "Hardware de cavidade na prateleira, fotografado na fábrica.",
      "تجهيزات تجويفية على الرف، صُوِّرت في المصنع.")
    a("Tuning on a vector network analyzer.",
      "Настройка на векторном анализаторе цепей.",
      "Sintonización en un analizador de redes vectorial.",
      "Sintonização num analisador de redes vetorial.",
      "الضبط على محلل شبكة متجهي.")
    a("Combiners and bandpass units on the bench.",
      "Комбайнеры и полосовые фильтры на столе.",
      "Combinadores y unidades paso banda en el banco.",
      "Combinadores e unidades passa-banda na bancada.",
      "مجمعات ووحدات تمرير نطاق على الطاولة.")
    a("KXT-FF-11 outline, 215 × 184 × 44 mm",
      "Габариты KXT-FF-11, 215 × 184 × 44 mm",
      "Contorno de KXT-FF-11, 215 × 184 × 44 mm",
      "Contorno de KXT-FF-11, 215 × 184 × 44 mm",
      "أبعاد KXT-FF-11، 215 × 184 × 44 mm")
    return P
