# Custom, applications, VHF, 404, thanks, contact leftovers, shelf asides.

def entries():
    P = {}
    def a(en, ru, es, pt, ar):
        P[en] = {"ru": ru, "es": es, "pt": pt, "ar": ar}

    # ===== custom =====
    a("Send the band plan. We quote from the cavity shelf.",
      "Пришлите план частот. Мы котируем исходя из резонаторной линейки.",
      "Envíe el plan de bandas. Cotizamos a partir de la línea de cavidad.",
      "Envie o plano de bandas. Cotamos a partir da linha de cavidade.",
      "أرسل خطة النطاقات. نسعّر انطلاقًا من تشكيلة التجاويف.")
    a("What to send", "Что прислать", "Qué enviar", "O que enviar", "ما الذي يُرسل")
    a("Passband, or Tx/Rx pair, in MHz",
      "Полоса пропускания или пара Tx/Rx, в MHz",
      "Banda de paso, o par Tx/Rx, en MHz",
      "Banda de passagem, ou par Tx/Rx, em MHz",
      "نطاق التمرير، أو زوج Tx/Rx، بوحدة MHz")
    a("Maximum insertion loss and ripple",
      "Максимальные вносимые потери и неравномерность",
      "Pérdida de inserción y rizado máximos",
      "Perda de inserção e ondulação máximas",
      "الحد الأقصى لفقد الإدخال والتموج")
    a("Rejection or isolation, with the frequencies that matter",
      "Подавление или развязка, с указанием значимых частот",
      "Rechazo o aislamiento, con las frecuencias que importan",
      "Rejeição ou isolamento, com as frequências que importam",
      "الرفض أو العزل، مع الترددات ذات الصلة")
    a("Average power, and whether the low-PIM option is required",
      "Средняя мощность и требуется ли опция низкого PIM",
      "Potencia media y si se requiere la opción de bajo PIM",
      "Potência média e se a opção de baixo PIM é necessária",
      "القدرة المتوسطة، وما إذا كان خيار PIM المنخفض مطلوبًا")
    a("Connector and gender, outline limit, quantity, indoor or a sealed version",
      "Разъём и пол (тип контакта), ограничение по габаритам, количество, исполнение для помещений или герметичное",
      "Conector y género, límite de contorno, cantidad, interior o una versión estanca",
      "Conector e género, limite de contorno, quantidade, interior ou uma versão estanque",
      "الموصل ونوعه (ذكر/أنثى)، حد الأبعاد، الكمية، تركيب داخلي أو نسخة محكمة")
    a("How an order moves", "Как проходит заказ", "Cómo avanza un pedido", "Como avança uma encomenda", "كيف يسير الطلب")
    a("We review the band plan, quote the model, build the sample, and ship production after the sample is accepted. Lead time is written on the quotation.",
      "Мы рассматриваем план частот, котируем модель, изготавливаем образец и отгружаем серию после приёмки образца. Срок поставки указывается в коммерческом предложении.",
      "Revisamos el plan de bandas, cotizamos el modelo, fabricamos la muestra y enviamos la producción una vez aceptada la muestra. El plazo se escribe en la cotización.",
      "Revisamos o plano de bandas, cotamos o modelo, fabricamos a amostra e enviamos a produção após a aceitação da amostra. O prazo é escrito na cotação.",
      "نراجع خطة النطاقات، ونسعّر الطراز، ونصنع العينة، ثم نشحن الإنتاج بعد قبول العينة. تُكتب مهلة التسليم في عرض السعر.")
    a("The current indoor shelf is the starting point: aluminum cavity, 50 Ω, N or SMA. A sealed outdoor version is a separate mechanical design and is quoted on its own.",
      "Отправная точка — текущая линейка для помещений: алюминиевый резонатор, 50 Ω, N или SMA. Герметичное уличное исполнение — отдельная механическая конструкция и котируется отдельно.",
      "El punto de partida es la línea de interior actual: cavidad de aluminio, 50 Ω, N o SMA. Una versión exterior estanca es un diseño mecánico aparte y se cotiza por separado.",
      "O ponto de partida é a linha de interior atual: cavidade de alumínio, 50 Ω, N ou SMA. Uma versão exterior estanque é um projeto mecânico à parte e é cotada em separado.",
      "نقطة الانطلاق هي تشكيلة التركيب الداخلي الحالية: تجويف ألومنيوم، 50 Ω، وموصل N أو SMA. النسخة الخارجية المحكمة تصميم ميكانيكي منفصل وتُسعَّر على حدة.")

    # ===== applications index =====
    a("Where these cavity filters are used.",
      "Где применяются эти фильтры на объемных резонаторах.",
      "Dónde se usan estos filtros de cavidad.",
      "Onde se usam estes filtros de cavidade.",
      "أين تُستخدم هذه المرشحات التجويفية.")
    a("Indoor DAS and multi-operator combining",
      "Внутриобъектовые DAS и объединение нескольких операторов",
      "DAS de interior y combinación multioperador",
      "DAS de interior e combinação multioperador",
      "DAS داخلي والجمع بين عدة مشغّلين")
    a("See also", "См. также", "Véase también", "Ver também", "انظر أيضًا")
    a("in-building DAS and ERCES",
      "внутриобъектовые DAS и ERCES",
      "DAS en edificios y ERCES",
      "DAS em edifícios e ERCES",
      "DAS داخل المباني وERCES")
    a("The four-port combiners put 700/900, 1800, 2100 and 2300/2600, or Band 1 with 2.6 GHz and n78, onto one antenna feed. Port isolation on those sheets is 70 dB or 80 dB in the other passbands.",
      "Четырёхпортовые комбайнеры выводят 700/900, 1800, 2100 и 2300/2600, либо Band 1 с 2,6 GHz и n78, на один фидер антенны. Развязка портов в этих листах составляет 70 dB или 80 dB в остальных полосах пропускания.",
      "Los combinadores de cuatro puertos llevan 700/900, 1800, 2100 y 2300/2600, o la Banda 1 con 2,6 GHz y n78, a una sola alimentación de antena. El aislamiento entre puertos en esas fichas es de 70 dB u 80 dB en las otras bandas de paso.",
      "Os combinadores de quatro portas levam 700/900, 1800, 2100 e 2300/2600, ou a Banda 1 com 2,6 GHz e n78, a uma só alimentação de antena. O isolamento entre portas nessas fichas é de 70 dB ou 80 dB nas outras bandas de passagem.",
      "تضع المجمعات رباعية المنافذ نطاقات 700/900 و1800 و2100 و2300/2600، أو النطاق 1 مع 2.6 GHz وn78، على تغذية هوائي واحدة. عزل المنافذ في تلك الأوراق هو 70 dB أو 80 dB في نطاقات التمرير الأخرى.")
    # The first sentence starts with a link "See also in-building..." then ". The four-port..."
    a(". The four-port combiners put 700/900, 1800, 2100 and 2300/2600, or Band 1 with 2.6 GHz and n78, onto one antenna feed. Port isolation on those sheets is 70 dB or 80 dB in the other passbands.",
      ". Четырёхпортовые комбайнеры выводят 700/900, 1800, 2100 и 2300/2600, либо Band 1 с 2,6 GHz и n78, на один фидер антенны. Развязка портов в этих листах составляет 70 dB или 80 dB в остальных полосах пропускания.",
      ". Los combinadores de cuatro puertos llevan 700/900, 1800, 2100 y 2300/2600, o la Banda 1 con 2,6 GHz y n78, a una sola alimentación de antena. El aislamiento entre puertos en esas fichas es de 70 dB u 80 dB en las otras bandas de paso.",
      ". Os combinadores de quatro portas levam 700/900, 1800, 2100 e 2300/2600, ou a Banda 1 com 2,6 GHz e n78, a uma só alimentação de antena. O isolamento entre portas nessas fichas é de 70 dB ou 80 dB nas outras bandas de passagem.",
      ". تضع المجمعات رباعية المنافذ نطاقات 700/900 و1800 و2100 و2300/2600، أو النطاق 1 مع 2.6 GHz وn78، على تغذية هوائي واحدة. عزل المنافذ في تلك الأوراق هو 70 dB أو 80 dB في نطاقات التمرير الأخرى.")
    a("Repeaters", "Ретрансляторы", "Repetidores", "Repetidores", "المكررات")
    a("Single-band cavities at 50 W and 100 W sit on the BTS or repeater port: Band 28, Band 20, Band 8, Band 5, Band 3, Band 1 and Band 7, plus n78 at 50 W.",
      "Однодиапазонные резонаторы на 50 W и 100 W устанавливаются на порт БС или ретранслятора: Band 28, Band 20, Band 8, Band 5, Band 3, Band 1 и Band 7, а также n78 на 50 W.",
      "Las cavidades de una sola banda de 50 W y 100 W se instalan en el puerto de la BTS o del repetidor: Banda 28, 20, 8, 5, 3, 1 y 7, más n78 a 50 W.",
      "As cavidades de uma só banda de 50 W e 100 W instalam-se na porta da BTS ou do repetidor: Banda 28, 20, 8, 5, 3, 1 e 7, mais n78 a 50 W.",
      "تُركَّب التجاويف أحادية النطاق بقدرة 50 W و100 W على منفذ المحطة الأساسية أو المكرر: النطاقات 28 و20 و8 و5 و3 و1 و7، إضافة إلى n78 بقدرة 50 W.")
    a("Wi-Fi cleanup", "Очистка Wi-Fi", "Limpieza de Wi-Fi", "Limpeza de Wi-Fi", "تنظيف Wi-Fi")
    a("2400–2483 MHz and 2400–2485 MHz bandpass units, and the 5 GHz two-port combiners at 5150–5350 / 5725–5875 MHz, keep cellular energy out of the Wi-Fi path. The diplexer separates the two 5 GHz passbands by 80 dB.",
      "Полосовые блоки 2400–2483 MHz и 2400–2485 MHz, а также двухпортовые комбайнеры 5 GHz на 5150–5350 / 5725–5875 MHz удерживают энергию сотовой связи вне тракта Wi-Fi. Диплексер разделяет две полосы 5 GHz на 80 dB.",
      "Las unidades paso banda de 2400–2483 MHz y 2400–2485 MHz, y los combinadores de dos puertos de 5 GHz en 5150–5350 / 5725–5875 MHz, mantienen la energía celular fuera de la ruta Wi-Fi. El diplexor separa las dos bandas de paso de 5 GHz en 80 dB.",
      "As unidades passa-banda de 2400–2483 MHz e 2400–2485 MHz, e os combinadores de duas portas de 5 GHz em 5150–5350 / 5725–5875 MHz, mantêm a energia celular fora do percurso Wi-Fi. O diplexador separa as duas bandas de passagem de 5 GHz em 80 dB.",
      "وحدات تمرير النطاق 2400–2483 MHz و2400–2485 MHz، والمجمعات ثنائية المنافذ عند 5 GHz للنطاق 5150–5350 / 5725–5875 MHz، تُبعد طاقة الاتصالات الخلوية عن مسار Wi-Fi. ويفصل الديبلكسر نطاقي التمرير عند 5 GHz بمقدار 80 dB.")
    a("VHF and UHF", "VHF и UHF", "VHF y UHF", "VHF e UHF", "VHF وUHF")
    a("The factory-file section includes a",
      "В разделе заводских файлов есть",
      "La sección de archivos de fábrica incluye un",
      "A secção de ficheiros de fábrica inclui um",
      "يتضمن قسم ملفات المصنع")
    a("400 MHz duplexer", "дуплексер 400 MHz", "dúplexer de 400 MHz", "duplexador de 400 MHz", "دبلكسر 400 MHz")
    a("with full electrical limits, and the quotation roster lists a",
      "с полными электрическими пределами, а в прайс-листе указан",
      "con límites eléctricos completos, y la lista de la cotización incluye un",
      "com limites elétricos completos, e a lista da cotação inclui um",
      "بحدود كهربائية كاملة، وتدرج قائمة عرض الأسعار")
    a("135–210 / 400–500 MHz duplexer",
      "дуплексер 135–210 / 400–500 MHz",
      "dúplexer de 135–210 / 400–500 MHz",
      "duplexador de 135–210 / 400–500 MHz",
      "دبلكسر 135–210 / 400–500 MHz")
    a("by passband only. Both are on the",
      "только с указанием полос пропускания. Оба приведены на странице",
      "solo por banda de paso. Ambos están en la página de",
      "apenas por banda de passagem. Ambos estão na página de",
      "بنطاق التمرير فقط. وكلاهما في صفحة")
    a("VHF/UHF duplexers", "Дуплексеры VHF/UHF", "dúplexers VHF/UHF", "duplexadores VHF/UHF", "دبلكسرات VHF/UHF")
    a("page.", " .", ".", ".", ".")
    a("Private radio networks: TETRA, P25, DMR",
      "Ведомственные радиосети: TETRA, P25, DMR",
      "Redes de radio privada: TETRA, P25, DMR",
      "Redes de rádio privada: TETRA, P25, DMR",
      "شبكات الراديو الخاصة: TETRA وP25 وDMR")
    a("Repeater duplexers, receiver filters and transmitter combiners for two-way radio sites.",
      "Дуплексеры ретрансляторов, фильтры приёмника и комбайнеры передатчиков для объектов профессиональной радиосвязи.",
      "Dúplexers de repetidor, filtros de receptor y combinadores de transmisor para emplazamientos de radio bidireccional.",
      "Duplexadores de repetidor, filtros de recetor e combinadores de transmissor para sítios de rádio bidirecional.",
      "دبلكسرات المكررات ومرشحات المستقبل ومجمعات المرسل لمواقع الراديو ثنائي الاتجاه.")
    a("Bands and filter positions →",
      "Диапазоны и места установки фильтров →",
      "Bandas y posiciones de los filtros →",
      "Bandas e posições dos filtros →",
      "النطاقات ومواضع المرشحات →")
    a("In-building DAS and emergency responder radio (ERCES)",
      "Внутриобъектовые DAS и радиосвязь аварийных служб (ERCES)",
      "DAS en edificios y radio de emergencias (ERCES)",
      "DAS em edifícios e rádio de emergência (ERCES)",
      "DAS داخل المباني وراديو فرق الطوارئ (ERCES)")
    a("Band filters, POI combiners and low-PIM parts for public-safety and cellular DAS.",
      "Полосовые фильтры, комбайнеры точки сопряжения (POI) и изделия с низким PIM для DAS общественной безопасности и сотовой связи.",
      "Filtros de banda, combinadores de POI y piezas de bajo PIM para DAS de seguridad pública y celular.",
      "Filtros de banda, combinadores de POI e peças de baixo PIM para DAS de segurança pública e celular.",
      "مرشحات نطاق ومجمعات نقطة الواجهة (POI) وقطع منخفضة PIM لأنظمة DAS للسلامة العامة والاتصالات الخلوية.")

    # ===== DAS / ERCES =====
    a("In-building DAS and ERCES",
      "Внутриобъектовые DAS и ERCES",
      "DAS en edificios y ERCES",
      "DAS em edifícios e ERCES",
      "DAS داخل المباني وERCES")
    a("In-building DAS and Emergency Responder Radio (ERCES)",
      "Внутриобъектовые DAS и радиосвязь аварийных служб (ERCES)",
      "DAS en edificios y radio de emergencias (ERCES)",
      "DAS em edifícios e rádio de emergência (ERCES)",
      "DAS داخل المباني وراديو فرق الطوارئ (ERCES)")
    a("A distributed antenna system (DAS) carries cellular and public-safety radio signals inside a building. Cavity filters decide which bands enter it and keep them apart.",
      "Распределённая антенная система (DAS) передаёт сигналы сотовой связи и радиосвязи общественной безопасности внутри здания. Фильтры на объемных резонаторах определяют, какие диапазоны в неё входят, и разделяют их.",
      "Un sistema de antena distribuida (DAS) transporta señales celulares y de radio de seguridad pública dentro de un edificio. Los filtros de cavidad deciden qué bandas entran y las mantienen separadas.",
      "Um sistema de antena distribuída (DAS) transporta sinais celulares e de rádio de segurança pública dentro de um edifício. Os filtros de cavidade decidem que bandas entram e mantêm-nas separadas.",
      "ينقل نظام الهوائيات الموزعة (DAS) إشارات الاتصالات الخلوية وراديو السلامة العامة داخل المبنى. وتقرر المرشحات التجويفية أي النطاقات تدخله وتُبقيها منفصلة.")
    a("Emergency responder radio coverage",
      "Покрытие радиосвязи аварийных служб",
      "Cobertura de radio de emergencias",
      "Cobertura de rádio de emergência",
      "تغطية راديو فرق الطوارئ")
    a("In the United States many jurisdictions require in-building coverage for fire and police radio. The requirement comes from the International Fire Code (section 510) and NFPA 1225, as adopted locally. The authority having jurisdiction (AHJ) sets the frequencies, the coverage targets and the acceptance test. System listings and acceptance are handled by the system integrator with the AHJ.",
      "В США многие юрисдикции требуют внутриобъектового покрытия для радиосвязи пожарных и полиции. Требование исходит из International Fire Code (раздел 510) и NFPA 1225 в местной редакции. Орган, обладающий юрисдикцией (AHJ), задаёт частоты, цели покрытия и приёмочные испытания. Перечень систем и приёмка ведутся системным интегратором совместно с AHJ.",
      "En Estados Unidos muchas jurisdicciones exigen cobertura en el edificio para la radio de bomberos y policía. El requisito proviene del International Fire Code (sección 510) y de la NFPA 1225, según se adopten localmente. La autoridad competente (AHJ) fija las frecuencias, los objetivos de cobertura y el ensayo de aceptación. Las listas de sistemas y la aceptación las gestiona el integrador con la AHJ.",
      "Nos Estados Unidos muitas jurisdições exigem cobertura no edifício para o rádio de bombeiros e polícia. O requisito provém do International Fire Code (secção 510) e da NFPA 1225, conforme adotados localmente. A autoridade competente (AHJ) define as frequências, os objetivos de cobertura e o ensaio de aceitação. As listas de sistemas e a aceitação são tratadas pelo integrador com a AHJ.",
      "في الولايات المتحدة تشترط كثير من الولايات القضائية تغطية داخل المباني لراديو الإطفاء والشرطة. وينبع هذا الشرط من المدونة الدولية للحريق (القسم 510) ومن NFPA 1225 بحسب ما يُعتمد محليًا. تحدّد السلطة ذات الاختصاص (AHJ) الترددات وأهداف التغطية واختبار القبول. ويتولى مُكامل النظام قوائم الأنظمة والقبول مع الـ AHJ.")
    a("Bands commonly carried",
      "Типично передаваемые диапазоны",
      "Bandas habitualmente transportadas",
      "Bandas habitualmente transportadas",
      "النطاقات المنقولة عادة")
    a("Service", "Служба", "Servicio", "Serviço", "الخدمة")
    a("Typical frequencies", "Типичные частоты", "Frecuencias típicas", "Frequências típicas", "الترددات النموذجية")
    a("VHF / UHF public safety",
      "VHF / UHF общественной безопасности",
      "Seguridad pública VHF / UHF",
      "Segurança pública VHF / UHF",
      "السلامة العامة VHF / UHF")
    a("700 MHz public safety, incl. FirstNet Band 14",
      "Общественная безопасность 700 MHz, включая FirstNet Band 14",
      "Seguridad pública de 700 MHz, incl. FirstNet Banda 14",
      "Segurança pública de 700 MHz, incl. FirstNet Banda 14",
      "السلامة العامة عند 700 MHz، بما في ذلك FirstNet النطاق 14")
    a("800 MHz public safety",
      "Общественная безопасность 800 MHz",
      "Seguridad pública de 800 MHz",
      "Segurança pública de 800 MHz",
      "السلامة العامة عند 800 MHz")
    a("Cellular DAS", "Сотовая DAS", "DAS celular", "DAS celular", "DAS خلوي")
    a("LTE and 5G bands of the operators served, e.g. Band 28, 20, 8, 3, 1, 7 and n78",
      "Диапазоны LTE и 5G обслуживаемых операторов, например Band 28, 20, 8, 3, 1, 7 и n78",
      "Bandas LTE y 5G de los operadores servidos, p. ej. Banda 28, 20, 8, 3, 1, 7 y n78",
      "Bandas LTE e 5G dos operadores servidos, p. ex. Banda 28, 20, 8, 3, 1, 7 e n78",
      "نطاقات LTE و5G للمشغّلين المخدومين، مثل النطاقات 28 و20 و8 و3 و1 و7 وn78")
    a("Where cavity filters go",
      "Куда ставятся фильтры на объемных резонаторах",
      "Dónde van los filtros de cavidad",
      "Onde se instalam os filtros de cavidade",
      "أين تُوضع المرشحات التجويفية")
    a("Signal booster / BDA band selection.",
      "Выбор диапазона усилителя сигнала / BDA.",
      "Selección de banda del repetidor / BDA.",
      "Seleção de banda do reforçador de sinal / BDA.",
      "اختيار نطاق معزّز الإشارة / BDA.")
    a("Pass the licensed channels, reject adjacent services.",
      "Пропускать лицензированные каналы, подавлять соседние службы.",
      "Dejar pasar los canales licenciados y rechazar los servicios adyacentes.",
      "Deixar passar os canais licenciados e rejeitar os serviços adjacentes.",
      "تمرير القنوات المرخّصة ورفض الخدمات المجاورة.")
    a("Point of interface (POI).",
      "Точка сопряжения (POI).",
      "Punto de interfaz (POI).",
      "Ponto de interface (POI).",
      "نقطة الواجهة (POI).")
    a("Band combiners and duplexers join several operators’ signal sources onto the DAS.",
      "Диапазонные комбайнеры и дуплексеры объединяют источники сигнала нескольких операторов на DAS.",
      "Los combinadores de banda y los dúplexers reúnen las fuentes de señal de varios operadores en el DAS.",
      "Os combinadores de banda e os duplexadores reúnem as fontes de sinal de vários operadores no DAS.",
      "تجمع مجمعات النطاق والدبلكسرات مصادر إشارة عدة مشغّلين على نظام DAS.")
    a("Shared cabling.",
      "Совместная кабельная инфраструктура.",
      "Cableado compartido.",
      "Cablagem partilhada.",
      "كابلات مشتركة.")
    a("Combiners and diplexers separate public-safety and cellular systems on one riser.",
      "Комбайнеры и диплексеры разделяют системы общественной безопасности и сотовой связи на одном стояке.",
      "Los combinadores y diplexores separan los sistemas de seguridad pública y celular en un mismo montante.",
      "Os combinadores e diplexadores separam os sistemas de segurança pública e celular num mesmo montante.",
      "تفصل المجمعات والديبلكسرات أنظمة السلامة العامة والأنظمة الخلوية على عمود صاعد واحد.")
    a("Passive intermodulation from strong downlink carriers can land in uplink bands, so low-PIM parts matter at the POI. Low PIM is an order option on our datasheets.",
      "Пассивная интермодуляция от мощных несущих линии вниз может попадать в полосы линии вверх, поэтому изделия с низким PIM важны в точке сопряжения. Низкий PIM — опция заказа в наших спецификациях.",
      "La intermodulación pasiva de portadoras fuertes de enlace descendente puede caer en bandas de enlace ascendente, por lo que las piezas de bajo PIM importan en el POI. El bajo PIM es una opción de pedido en nuestras fichas técnicas.",
      "A intermodulação passiva de portadoras fortes de downlink pode cair em bandas de uplink, pelo que as peças de baixo PIM importam no POI. O baixo PIM é uma opção de encomenda nas nossas fichas técnicas.",
      "يمكن للتضمين البيني السلبي الصادر عن حاملات الوصلة الهابطة القوية أن يقع في نطاقات الوصلة الصاعدة، لذا تهمّ القطع منخفضة PIM عند نقطة الواجهة. PIM المنخفض خيار طلب في أوراق مواصفاتنا.")
    a("Related products", "Связанные изделия", "Productos relacionados", "Produtos relacionados", "منتجات ذات صلة")
    a(": bandpass, 758–803 MHz.",
      ": полосовой фильтр, 758–803 MHz.",
      ": paso banda, 758–803 MHz.",
      ": passa-banda, 758–803 MHz.",
      ": تمرير نطاق، 758–803 MHz.")
    a(": 4-port combiner, 758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz.",
      ": четырёхпортовый комбайнер, 758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz.",
      ": combinador de 4 puertos, 758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz.",
      ": combinador de 4 portas, 758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz.",
      ": مجمع رباعي المنافذ، 758–960 / 1805–1920 / 2010–2170 / 2310–2675 MHz.")
    a("for the public-safety radio side.",
      "для стороны радиосвязи общественной безопасности.",
      "para el lado de radio de seguridad pública.",
      "para o lado de rádio de segurança pública.",
      "لجانب راديو السلامة العامة.")
    a("Cellular bandpass filters and combiners",
      "Сотовые полосовые фильтры и комбайнеры",
      "Filtros paso banda y combinadores celulares",
      "Filtros passa-banda e combinadores celulares",
      "مرشحات تمرير نطاق ومجمعات خلوية")
    a("What to send for a quotation",
      "Что прислать для коммерческого предложения",
      "Qué enviar para una cotización",
      "O que enviar para uma cotação",
      "ما الذي يُرسل للحصول على عرض سعر")
    a("The band plan for each system, the rejection or isolation between them, power at the filter, connector, and quantity. A riser diagram or POI drawing can be attached on the",
      "План частот каждой системы, подавление или развязка между ними, мощность на фильтре, разъём и количество. Схему стояка или чертёж точки сопряжения можно приложить в форме",
      "El plan de bandas de cada sistema, el rechazo o aislamiento entre ellos, la potencia en el filtro, el conector y la cantidad. Un diagrama de montante o un dibujo de POI puede adjuntarse en el formulario de",
      "O plano de bandas de cada sistema, a rejeição ou o isolamento entre eles, a potência no filtro, o conector e a quantidade. Um diagrama de montante ou um desenho de POI pode anexar-se no formulário de",
      "خطة النطاقات لكل نظام، والرفض أو العزل بينها، والقدرة عند المرشح، والموصل، والكمية. يمكن إرفاق مخطط العمود الصاعد أو رسم نقطة الواجهة في نموذج")
    a("form.", " .", ".", ".", ".")
    a("custom design", "индивидуального проектирования", "diseño a medida", "projeto à medida", "التصميم حسب الطلب")

    return P
