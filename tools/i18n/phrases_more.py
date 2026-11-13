# Private networks, VHF page, 404, thanks, shelf asides, split text nodes.

def entries():
    P = {}
    def a(en, ru, es, pt, ar):
        P[en] = {"ru": ru, "es": es, "pt": pt, "ar": ar}

    # split punctuation nodes
    a(" page.", ".", ".", ".", ".")
    a(" form.", ".", ".", ".", ".")
    a("form.", ".", ".", ".", ".")

    # ===== private networks =====
    a("Private radio networks",
      "Ведомственные радиосети",
      "Redes de radio privada",
      "Redes de rádio privada",
      "شبكات الراديو الخاصة")
    a("Private Radio Networks: TETRA, P25 and DMR",
      "Ведомственные радиосети: TETRA, P25 и DMR",
      "Redes de radio privada: TETRA, P25 y DMR",
      "Redes de rádio privada: TETRA, P25 e DMR",
      "شبكات الراديو الخاصة: TETRA وP25 وDMR")
    a("Public safety, utilities, transport and industrial sites run their own two-way radio (LMR / PMR) networks. Cavity filters sit at the base station and repeater sites of these networks.",
      "Службы общественной безопасности, коммунальные предприятия, транспорт и промышленные объекты эксплуатируют собственные сети профессиональной радиосвязи (LMR / PMR). Фильтры на объемных резонаторах устанавливаются на базовых станциях и ретрансляторах этих сетей.",
      "La seguridad pública, los servicios públicos, el transporte y los emplazamientos industriales operan sus propias redes de radio bidireccional (LMR / PMR). Los filtros de cavidad se instalan en las estaciones base y en los emplazamientos de repetidor de estas redes.",
      "A segurança pública, os serviços públicos, o transporte e os sítios industriais operam as suas próprias redes de rádio bidirecional (LMR / PMR). Os filtros de cavidade instalam-se nas estações de base e nos sítios de repetidor destas redes.",
      "تدير جهات السلامة العامة والمرافق والنقل والمواقع الصناعية شبكات راديو ثنائي الاتجاه خاصة بها (LMR / PMR). وتُركَّب المرشحات التجويفية في محطات القاعدة ومواقع المكررات لهذه الشبكات.")
    a("Where the systems operate",
      "Где работают эти системы",
      "Dónde operan los sistemas",
      "Onde operam os sistemas",
      "حيث تعمل الأنظمة")
    a("Frequencies are set by each country’s regulator and each licence. The usual ranges are:",
      "Частоты задаёт регулятор каждой страны и каждая лицензия. Обычно используются диапазоны:",
      "Las frecuencias las fija el regulador de cada país y cada licencia. Los rangos habituales son:",
      "As frequências são definidas pelo regulador de cada país e por cada licença. Os intervalos habituais são:",
      "تحدّد الترددات جهة التنظيم في كل بلد وكل ترخيص. والنطاقات المعتادة هي:")
    a("System", "Система", "Sistema", "Sistema", "النظام")
    a("Standard", "Стандарт", "Norma", "Norma", "المعيار")
    a("Typical bands", "Типичные диапазоны", "Bandas típicas", "Bandas típicas", "النطاقات النموذجية")
    a("380–400 MHz (public safety in many countries), 410–430 MHz, 450–470 MHz; 800 MHz in some regions",
      "380–400 MHz (общественная безопасность во многих странах), 410–430 MHz, 450–470 MHz; 800 MHz в некоторых регионах",
      "380–400 MHz (seguridad pública en muchos países), 410–430 MHz, 450–470 MHz; 800 MHz en algunas regiones",
      "380–400 MHz (segurança pública em muitos países), 410–430 MHz, 450–470 MHz; 800 MHz em algumas regiões",
      "380–400 MHz (السلامة العامة في بلدان كثيرة)، 410–430 MHz، 450–470 MHz؛ و800 MHz في بعض المناطق")
    a("VHF 136–174 MHz, UHF 380–512 MHz, 700 MHz and 800 MHz public-safety bands",
      "VHF 136–174 MHz, UHF 380–512 MHz, диапазоны общественной безопасности 700 MHz и 800 MHz",
      "VHF 136–174 MHz, UHF 380–512 MHz, bandas de seguridad pública de 700 MHz y 800 MHz",
      "VHF 136–174 MHz, UHF 380–512 MHz, bandas de segurança pública de 700 MHz e 800 MHz",
      "VHF 136–174 MHz، UHF 380–512 MHz، ونطاقات السلامة العامة عند 700 MHz و800 MHz")
    a("VHF 136–174 MHz, UHF 400–470 MHz",
      "VHF 136–174 MHz, UHF 400–470 MHz",
      "VHF 136–174 MHz, UHF 400–470 MHz",
      "VHF 136–174 MHz, UHF 400–470 MHz",
      "VHF 136–174 MHz، UHF 400–470 MHz")
    a("Repeater duplexer.",
      "Дуплексер ретранслятора.",
      "Dúplexer de repetidor.",
      "Duplexador de repetidor.",
      "دبلكسر المكرر.")
    a("Transmit and receive share one antenna. The duplexer passes each half of the pair and isolates the receiver from the transmitter at the duplex spacing.",
      "Передача и приём используют одну антенну. Дуплексер пропускает каждую половину пары и развязывает приёмник от передатчика на дуплексном разносе.",
      "Transmisión y recepción comparten una antena. El dúplexer deja pasar cada mitad del par y aísla el receptor del transmisor en el espaciado dúplex.",
      "A emissão e a receção partilham uma antena. O duplexador deixa passar cada metade do par e isola o recetor do transmissor no espaçamento dúplex.",
      "يشترك الإرسال والاستقبال في هوائي واحد. يمرّر الدبلكسر كل نصف من الزوج ويعزل المستقبل عن المرسل عند التباعد الازدواجي.")
    a("Receiver protection.",
      "Защита приёмника.",
      "Protección del receptor.",
      "Proteção do recetor.",
      "حماية المستقبل.")
    a("A bandpass cavity in front of the receiver rejects nearby transmitters on shared towers.",
      "Полосовой резонатор перед приёмником подавляет близкие передатчики на общих опорах.",
      "Una cavidad paso banda delante del receptor rechaza transmisores cercanos en torres compartidas.",
      "Uma cavidade passa-banda à frente do recetor rejeita transmissores próximos em torres partilhadas.",
      "يرفض تجويف تمرير النطاق أمام المستقبل المرسلات القريبة على الأبراج المشتركة.")
    a("Transmitter combining.",
      "Объединение передатчиков.",
      "Combinación de transmisores.",
      "Combinação de transmissores.",
      "جمع المرسلات.")
    a("Multi-channel and trunked sites combine several transmitters onto one antenna.",
      "Многоканальные и транкинговые объекты объединяют несколько передатчиков на одну антенну.",
      "Los emplazamientos multicanal y troncalizados combinan varios transmisores en una antena.",
      "Os sítios multicanal e em tronco combinam vários transmissores numa antena.",
      "تجمع المواقع متعددة القنوات والمجمَّعة عدة مرسلات على هوائي واحد.")
    a("Coexistence with cellular.",
      "Совместимость с сотовой связью.",
      "Coexistencia con la red celular.",
      "Coexistência com a rede celular.",
      "التعايش مع الشبكة الخلوية.")
    a("Band filters keep LTE and 5G energy out of the radio path, and the other way round.",
      "Полосовые фильтры удерживают энергию LTE и 5G вне радиотракта и наоборот.",
      "Los filtros de banda mantienen la energía LTE y 5G fuera de la ruta de radio, y a la inversa.",
      "Os filtros de banda mantêm a energia LTE e 5G fora do percurso de rádio, e no sentido inverso.",
      "تُبعد مرشحات النطاق طاقة LTE و5G عن المسار الراديوي، والعكس أيضًا.")
    a(": UHF cavity duplexer, 452.5–457.5 / 462.5–467.5 MHz (factory sheet).",
      ": УВЧ дуплексер на объемных резонаторах, 452.5–457.5 / 462.5–467.5 MHz (заводской лист).",
      ": dúplexer de cavidad UHF, 452.5–457.5 / 462.5–467.5 MHz (ficha de fábrica).",
      ": duplexador de cavidade UHF, 452.5–457.5 / 462.5–467.5 MHz (ficha de fábrica).",
      ": دبلكسر تجويفي UHF، 452.5–457.5 / 462.5–467.5 MHz (ورقة المصنع).")
    a(": duplexer, 135–210 / 400–500 MHz (passbands only on the quotation).",
      ": дуплексер, 135–210 / 400–500 MHz (в прайс-листе указаны только полосы пропускания).",
      ": dúplexer, 135–210 / 400–500 MHz (solo bandas de paso en la cotización).",
      ": duplexador, 135–210 / 400–500 MHz (apenas bandas de passagem na cotação).",
      ": دبلكسر، 135–210 / 400–500 MHz (نطاقات التمرير فقط في عرض السعر).")
    a("All VHF/UHF duplexers",
      "Все дуплексеры VHF/UHF",
      "Todos los dúplexers VHF/UHF",
      "Todos os duplexadores VHF/UHF",
      "جميع دبلكسرات VHF/UHF")
    a("Tx and Rx frequencies (or band and duplex spacing), channels and power per channel, the isolation or rejection you need, connector, and quantity. Use the",
      "Частоты Tx и Rx (или диапазон и дуплексный разнос), каналы и мощность на канал, требуемая развязка или подавление, разъём и количество. Воспользуйтесь формой",
      "Frecuencias Tx y Rx (o banda y espaciado dúplex), canales y potencia por canal, el aislamiento o rechazo que necesite, conector y cantidad. Use el formulario de",
      "Frequências Tx e Rx (ou banda e espaçamento dúplex), canais e potência por canal, o isolamento ou a rejeição de que necessita, conector e quantidade. Use o formulário de",
      "ترددا Tx وRx (أو النطاق والتباعد الازدواجي)، والقنوات والقدرة لكل قناة، والعزل أو الرفض المطلوب، والموصل، والكمية. استخدم نموذج")
    a("; a drawing or site plan can be attached.",
      "; можно приложить чертёж или план объекта.",
      "; se puede adjuntar un dibujo o un plano del emplazamiento.",
      "; pode anexar-se um desenho ou um plano do sítio.",
      "؛ يمكن إرفاق رسم أو مخطط للموقع.")

    # ===== VHF page =====
    a("Cavity duplexers in the VHF and UHF bands from the factory catalog. Figures below are exactly what the factory sheets state; anything else is confirmed on the quotation and the unit’s test report.",
      "Дуплексеры на объемных резонаторах в диапазонах VHF и UHF из заводского каталога. Приведённые ниже цифры — в точности то, что указано в заводских листах; всё остальное подтверждается в коммерческом предложении и в протоколе испытаний изделия.",
      "Dúplexers de cavidad en las bandas VHF y UHF del catálogo de fábrica. Las cifras siguientes son exactamente lo que indican las fichas de fábrica; cualquier otra cosa se confirma en la cotización y en el informe de ensayo de la unidad.",
      "Duplexadores de cavidade nas bandas VHF e UHF do catálogo de fábrica. As cifras abaixo são exatamente o que as fichas de fábrica indicam; qualquer outra coisa confirma-se na cotação e no relatório de ensaio da unidade.",
      "دبلكسرات تجويفية في نطاقي VHF وUHF من كتالوج المصنع. الأرقام أدناه هي تمامًا ما تذكره أوراق المصنع؛ ويُؤكَّد أي شيء آخر في عرض السعر وتقرير اختبار الوحدة.")
    a("Passbands only (quotation roster, 29 May 2026). Electrical limits are on the unit’s test report.",
      "Только полосы пропускания (прайс-лист, 29 мая 2026 г.). Электрические пределы указаны в протоколе испытаний изделия.",
      "Solo bandas de paso (lista de cotización, 29 de mayo de 2026). Los límites eléctricos figuran en el informe de ensayo de la unidad.",
      "Apenas bandas de passagem (lista da cotação, 29 de maio de 2026). Os limites elétricos constam do relatório de ensaio da unidade.",
      "نطاقات التمرير فقط (قائمة عرض الأسعار، 29 أيار/مايو 2026). الحدود الكهربائية واردة في تقرير اختبار الوحدة.")
    a("Insertion loss ≤2.2 dB, VSWR ≤1.3, ripple ≤1.9 dB, rejection ≥80 dB at the other band, isolation ≥80 dB, 50 W average, N-F / SMA-F, 177×134×73.5 mm.",
      "Вносимые потери ≤2.2 dB, VSWR ≤1.3, неравномерность ≤1.9 dB, подавление ≥80 dB в другом диапазоне, развязка ≥80 dB, средняя мощность 50 W, N-F / SMA-F, 177×134×73.5 mm.",
      "Pérdida de inserción ≤2.2 dB, VSWR ≤1.3, rizado ≤1.9 dB, rechazo ≥80 dB en la otra banda, aislamiento ≥80 dB, 50 W de media, N-F / SMA-F, 177×134×73.5 mm.",
      "Perda de inserção ≤2.2 dB, VSWR ≤1.3, ondulação ≤1.9 dB, rejeição ≥80 dB na outra banda, isolamento ≥80 dB, 50 W de média, N-F / SMA-F, 177×134×73.5 mm.",
      "فقد إدخال ≤2.2 dB، VSWR ≤1.3، تموج ≤1.9 dB، رفض ≥80 dB عند النطاق الآخر، عزل ≥80 dB، قدرة متوسطة 50 W، N-F / SMA-F، 177×134×73.5 mm.")
    a("Need another VHF or UHF Tx/Rx pair, spacing, power or connector? Send the band plan on the",
      "Нужна другая пара Tx/Rx в VHF или UHF, другой разнос, мощность или разъём? Пришлите план частот на странице",
      "¿Necesita otro par Tx/Rx de VHF o UHF, otro espaciado, potencia o conector? Envíe el plan de bandas en la página de",
      "Precisa de outro par Tx/Rx de VHF ou UHF, outro espaçamento, potência ou conector? Envie o plano de bandas na página de",
      "هل تحتاج إلى زوج Tx/Rx آخر في VHF أو UHF، أو تباعد أو قدرة أو موصل مختلف؟ أرسل خطة النطاقات في صفحة")
    a("page or write to",
      " или напишите на",
      " o escriba a",
      " ou escreva para",
      " أو راسل")
    a("VHF/UHF cavity duplexers for two-way radio (LMR) from a Shenzhen factory: KXT26065 135–210 / 400–500 MHz and KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz. Factory-sheet specifications; test report with each unit.",
      "Дуплексеры VHF/UHF на объемных резонаторах для профессиональной радиосвязи (LMR) с завода в Шэньчжэне: KXT26065 135–210 / 400–500 MHz и KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz. Характеристики по заводским листам; протокол испытаний с каждым изделием.",
      "Dúplexers de cavidad VHF/UHF para radio bidireccional (LMR) de una fábrica en Shenzhen: KXT26065 135–210 / 400–500 MHz y KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz. Especificaciones de las fichas de fábrica; informe de ensayo con cada unidad.",
      "Duplexadores de cavidade VHF/UHF para rádio bidirecional (LMR) de uma fábrica em Shenzhen: KXT26065 135–210 / 400–500 MHz e KXT-FF-09 452.5–457.5 / 462.5–467.5 MHz. Especificações das fichas de fábrica; relatório de ensaio com cada unidade.",
      "دبلكسرات تجويفية VHF/UHF للراديو ثنائي الاتجاه (LMR) من مصنع في شنجن: KXT26065 للنطاق 135–210 / 400–500 MHz وKXT-FF-09 للنطاق 452.5–457.5 / 462.5–467.5 MHz. مواصفات أوراق المصنع؛ وتقرير اختبار مع كل وحدة.")

    # application meta descriptions (from earlier extraction)
    a("Cavity bandpass filters, duplexers and combiners for in-building distributed antenna systems (DAS) and emergency responder radio coverage systems (ERCES): bands, filter positions and what to send.",
      "Полосовые фильтры, дуплексеры и комбайнеры на объемных резонаторах для внутриобъектовых распределённых антенных систем (DAS) и систем покрытия радиосвязи аварийных служб (ERCES): диапазоны, места установки фильтров и что прислать.",
      "Filtros paso banda de cavidad, dúplexers y combinadores para sistemas de antena distribuida en edificios (DAS) y sistemas de cobertura de radio de emergencias (ERCES): bandas, posiciones de los filtros y qué enviar.",
      "Filtros passa-banda de cavidade, duplexadores e combinadores para sistemas de antena distribuída em edifícios (DAS) e sistemas de cobertura de rádio de emergência (ERCES): bandas, posições dos filtros e o que enviar.",
      "مرشحات تجويفية تمرير نطاق ودبلكسرات ومجمعات لأنظمة الهوائيات الموزعة داخل المباني (DAS) وأنظمة تغطية راديو فرق الطوارئ (ERCES): النطاقات ومواضع المرشحات وما يُرسل.")
    a("Cavity duplexers, bandpass filters and combiners for TETRA, P25 and DMR private radio (LMR) base stations and repeaters. Typical bands, where the filters go, and what to send for a quotation.",
      "Дуплексеры, полосовые фильтры и комбайнеры на объемных резонаторах для базовых станций и ретрансляторов ведомственной радиосвязи TETRA, P25 и DMR (LMR). Типичные диапазоны, места установки фильтров и что прислать для коммерческого предложения.",
      "Dúplexers de cavidad, filtros paso banda y combinadores para estaciones base y repetidores de radio privada TETRA, P25 y DMR (LMR). Bandas típicas, dónde van los filtros y qué enviar para una cotización.",
      "Duplexadores de cavidade, filtros passa-banda e combinadores para estações de base e repetidores de rádio privada TETRA, P25 e DMR (LMR). Bandas típicas, onde se instalam os filtros e o que enviar para uma cotação.",
      "دبلكسرات تجويفية ومرشحات تمرير نطاق ومجمعات لمحطات القاعدة والمكررات في شبكات الراديو الخاصة TETRA وP25 وDMR (LMR). النطاقات النموذجية ومواضع المرشحات وما يُرسل للحصول على عرض سعر.")

    # ===== 404 / thanks =====
    a("The page you asked for is not here. It may have moved when the catalog was reorganized.",
      "Запрошенной страницы здесь нет. Возможно, она была перемещена при реорганизации каталога.",
      "La página que buscó no está aquí. Puede haberse movido cuando se reorganizó el catálogo.",
      "A página que pediu não está aqui. Pode ter sido movida quando o catálogo foi reorganizado.",
      "الصفحة التي طلبتها ليست هنا. ربما نُقلت عند إعادة تنظيم الكتالوج.")
    a("Looking for a model? Write to",
      "Ищете модель? Напишите на",
      "¿Busca un modelo? Escriba a",
      "Procura um modelo? Escreva para",
      "تبحث عن طراز؟ راسل")
    a("with the model number or the band plan.",
      " с номером модели или планом частот.",
      " con el número de modelo o el plan de bandas.",
      " com o número de modelo ou o plano de bandas.",
      " مع رقم الطراز أو خطة النطاقات.")
    a("Your enquiry has been sent to sales@cavityfilter.com.",
      "Ваш запрос отправлен на sales@cavityfilter.com.",
      "Su consulta se ha enviado a sales@cavityfilter.com.",
      "O seu pedido foi enviado para sales@cavityfilter.com.",
      "أُرسل استفسارك إلى sales@cavityfilter.com.")
    a("Your enquiry has been sent to sales@cavityfilter.com. We will reply by email.",
      "Ваш запрос отправлен на sales@cavityfilter.com. Мы ответим по электронной почте.",
      "Su consulta se ha enviado a sales@cavityfilter.com. Responderemos por correo.",
      "O seu pedido foi enviado para sales@cavityfilter.com. Responderemos por correio eletrónico.",
      "أُرسل استفسارك إلى sales@cavityfilter.com. سنرد بالبريد الإلكتروني.")
    a("If it is urgent, you can also reach us on",
      "Если срочно, вы также можете связаться с нами через",
      "Si es urgente, también puede contactarnos por",
      "Se for urgente, também pode contactar-nos por",
      "إذا كان الأمر عاجلًا، يمكنك أيضًا التواصل معنا عبر")
    a("or write to", "или написать на", "o escribir a", "ou escrever para", "أو الكتابة إلى")
    a("Thank you | Kangxuntong", "Спасибо | Kangxuntong", "Gracias | Kangxuntong", "Obrigado | Kangxuntong", "شكرًا لك | Kangxuntong")

    # ===== shelf asides / product side cards =====
    a("Need a different passband? Send the band plan on the",
      "Нужна другая полоса пропускания? Пришлите план частот на странице",
      "¿Necesita otra banda de paso? Envíe el plan de bandas en la página de",
      "Precisa de outra banda de passagem? Envie o plano de bandas na página de",
      "هل تحتاج إلى نطاق تمرير مختلف؟ أرسل خطة النطاقات في صفحة")
    a("This model is on the commercial shelf of the company quotation. The quotation gives the passband only, not insertion loss or rejection, and this page does not borrow electrical limits from other models. Rows marked “—” are settled on the quotation and the unit’s test report.",
      "Эта модель входит в складскую линейку корпоративного прайс-листа. В прайс-листе указана только полоса пропускания, без вносимых потерь и подавления; эта страница не заимствует электрические пределы у других моделей. Строки, отмеченные «—», уточняются в коммерческом предложении и в протоколе испытаний изделия.",
      "Este modelo está en las existencias comerciales de la cotización de la empresa. La cotización indica solo la banda de paso, no la pérdida de inserción ni el rechazo, y esta página no toma límites eléctricos de otros modelos. Las filas marcadas con «—» se resuelven en la cotización y en el informe de ensayo de la unidad.",
      "Este modelo está na prateleira comercial da cotação da empresa. A cotação indica apenas a banda de passagem, não a perda de inserção nem a rejeição, e esta página não toma limites elétricos de outros modelos. As linhas marcadas com «—» resolvem-se na cotação e no relatório de ensaio da unidade.",
      "هذا الطراز ضمن مخزون عرض أسعار الشركة التجاري. يذكر عرض السعر نطاق التمرير فقط، دون فقد الإدخال أو الرفض، ولا تستعير هذه الصفحة حدودًا كهربائية من طرازات أخرى. تُحسَم الصفوف المعلَّمة بـ «—» في عرض السعر وتقرير اختبار الوحدة.")
    a("VHF/UHF duplexers for private networks (LMR). See also",
      "Дуплексеры VHF/UHF для ведомственных сетей (LMR). См. также",
      "Dúplexers VHF/UHF para redes privadas (LMR). Véase también",
      "Duplexadores VHF/UHF para redes privadas (LMR). Ver também",
      "دبلكسرات VHF/UHF للشبكات الخاصة (LMR). انظر أيضًا")
    a("and", "и", "y", "e", "و")
    a("TETRA / P25 / DMR private networks",
      "Ведомственные сети TETRA / P25 / DMR",
      "redes privadas TETRA / P25 / DMR",
      "redes privadas TETRA / P25 / DMR",
      "شبكات TETRA / P25 / DMR الخاصة")
    a(".", ".", ".", ".", ".")

    return P
