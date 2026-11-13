# Unique page prose: home, about, quality, legal, apps, contact, custom, 404, thanks.

def entries():
    P = {}
    def a(en, ru, es, pt, ar):
        P[en] = {"ru": ru, "es": es, "pt": pt, "ar": ar}

    # ===== home =====
    a("Cavity filters · Shenzhen",
      "Фильтры на объемных резонаторах · Шэньчжэнь",
      "Filtros de cavidad · Shenzhen",
      "Filtros de cavidade · Shenzhen",
      "مرشحات تجويفية · شنجن")
    a("Cavity filters for LTE, 5G, private radio and in-building DAS.",
      "Фильтры на объемных резонаторах для LTE, 5G, ведомственной радиосвязи и внутриобъектовых DAS.",
      "Filtros de cavidad para LTE, 5G, radio privada y DAS en edificios.",
      "Filtros de cavidade para LTE, 5G, rádio privada e DAS em edifícios.",
      "مرشحات تجويفية لـ LTE و5G والراديو الخاص وأنظمة DAS داخل المباني.")
    a("Kangxuntong builds cavity bandpass filters, diplexers and multi-band combiners in Shenzhen. Documented passbands run from 135 MHz to 6 GHz. The indoor cellular line is concentrated from 700 MHz upward. Each shipment includes a network-analyzer test report.",
      "Kangxuntong производит полосовые фильтры, диплексеры и многодиапазонные комбайнеры на объемных резонаторах в Шэньчжэне. Документированные полосы пропускания — от 135 MHz до 6 GHz. Линейка для сотовой связи в помещениях сосредоточена начиная с 700 MHz. К каждой поставке прилагается протокол испытаний на анализаторе цепей.",
      "Kangxuntong fabrica en Shenzhen filtros paso banda de cavidad, diplexores y combinadores multibanda. Las bandas de paso documentadas van de 135 MHz a 6 GHz. La línea celular de interior se concentra a partir de 700 MHz. Cada envío incluye un informe de ensayo de analizador de redes.",
      "A Kangxuntong fabrica em Shenzhen filtros passa-banda de cavidade, diplexadores e combinadores multibanda. As bandas de passagem documentadas vão de 135 MHz a 6 GHz. A linha celular de interior concentra-se a partir de 700 MHz. Cada envio inclui um relatório de ensaio de analisador de redes.",
      "تُصنّع Kangxuntong في شنجن مرشحات تجويفية تمرير نطاق وديبلكسرات ومجمعات متعددة النطاقات. تمتد نطاقات التمرير الموثّقة من 135 MHz إلى 6 GHz. وتتركّز تشكيلة الاتصالات الخلوية للتركيب الداخلي ابتداءً من 700 MHz. تتضمن كل شحنة تقرير اختبار من محلل شبكة.")
    a("New:", "Новое:", "Novedad:", "Novidade:", "جديد:")
    a("VHF/UHF duplexers for private networks",
      "Дуплексеры VHF/UHF для ведомственных сетей",
      "Dúplexers VHF/UHF para redes privadas",
      "Duplexadores VHF/UHF para redes privadas",
      "دبلكسرات VHF/UHF للشبكات الخاصة")
    a("public-safety DAS",
      "DAS для служб общественной безопасности",
      "DAS de seguridad pública",
      "DAS de segurança pública",
      "DAS للسلامة العامة")
    a("Private radio and public-safety DAS",
      "Ведомственная радиосвязь и DAS общественной безопасности",
      "Radio privada y DAS de seguridad pública",
      "Rádio privada e DAS de segurança pública",
      "الراديو الخاص وDAS للسلامة العامة")
    a("Beyond LTE and 5G: duplexers for two-way radio sites and band filters for in-building emergency radio.",
      "Помимо LTE и 5G: дуплексеры для объектов профессиональной радиосвязи и полосовые фильтры для аварийного радио внутри зданий.",
      "Más allá de LTE y 5G: dúplexers para emplazamientos de radio bidireccional y filtros de banda para radio de emergencia en edificios.",
      "Além de LTE e 5G: duplexadores para sítios de rádio bidirecional e filtros de banda para rádio de emergência em edifícios.",
      "إلى جانب LTE و5G: دبلكسرات لمواقع الراديو ثنائي الاتجاه ومرشحات نطاق لراديو الطوارئ داخل المباني.")
    a("LMR · VHF / UHF", "LMR · VHF / UHF", "LMR · VHF / UHF", "LMR · VHF / UHF", "LMR · VHF / UHF")
    a("Private network / LMR duplexers",
      "Дуплексеры ведомственных сетей / LMR",
      "Dúplexers de red privada / LMR",
      "Duplexadores de rede privada / LMR",
      "دبلكسرات الشبكات الخاصة / LMR")
    a("UHF cavity duplexer KXT-FF-09 (452.5–457.5 / 462.5–467.5 MHz, isolation ≥ 80 dB, 50 W) and the 135–210 / 400–500 MHz shelf duplexer KXT26065. Other Tx/Rx pairs are built to your band plan for TETRA, P25 and DMR repeaters.",
      "УВЧ дуплексер на объемных резонаторах KXT-FF-09 (452.5–457.5 / 462.5–467.5 MHz, развязка ≥ 80 dB, 50 W) и складской дуплексер KXT26065 на 135–210 / 400–500 MHz. Другие пары Tx/Rx изготавливаются по вашему плану частот для ретрансляторов TETRA, P25 и DMR.",
      "Dúplexer de cavidad UHF KXT-FF-09 (452.5–457.5 / 462.5–467.5 MHz, aislamiento ≥ 80 dB, 50 W) y el dúplexer de existencias KXT26065 de 135–210 / 400–500 MHz. Otros pares Tx/Rx se fabrican según su plan de bandas para repetidores TETRA, P25 y DMR.",
      "Duplexador de cavidade UHF KXT-FF-09 (452.5–457.5 / 462.5–467.5 MHz, isolamento ≥ 80 dB, 50 W) e o duplexador de prateleira KXT26065 de 135–210 / 400–500 MHz. Outros pares Tx/Rx são fabricados segundo o seu plano de bandas para repetidores TETRA, P25 e DMR.",
      "دبلكسر تجويفي UHF من الطراز KXT-FF-09 (452.5–457.5 / 462.5–467.5 MHz، عزل ≥ 80 dB، 50 W) ودبلكسر المخزون KXT26065 للنطاق 135–210 / 400–500 MHz. تُصنع أزواج Tx/Rx الأخرى وفق خطة تردداتك لمكررات TETRA وP25 وDMR.")
    a("TETRA / P25 / DMR", "TETRA / P25 / DMR", "TETRA / P25 / DMR", "TETRA / P25 / DMR", "TETRA / P25 / DMR")
    a("DAS · ERCES", "DAS · ERCES", "DAS · ERCES", "DAS · ERCES", "DAS · ERCES")
    a("Public-safety DAS", "DAS общественной безопасности", "DAS de seguridad pública", "DAS de segurança pública", "DAS للسلامة العامة")
    a("Band filters and combiners for in-building DAS and emergency responder radio systems: a 758–803 MHz bandpass for the 700 MHz band, multi-band combiners from 758 MHz up, and a low-PIM order option.",
      "Полосовые фильтры и комбайнеры для внутриобъектовых DAS и систем радиосвязи аварийных служб: полосовой фильтр 758–803 MHz для диапазона 700 MHz, многодиапазонные комбайнеры начиная с 758 MHz и опция низкого PIM при заказе.",
      "Filtros de banda y combinadores para DAS en edificios y sistemas de radio de emergencias: un paso banda de 758–803 MHz para la banda de 700 MHz, combinadores multibanda desde 758 MHz y una opción de bajo PIM en el pedido.",
      "Filtros de banda e combinadores para DAS em edifícios e sistemas de rádio de emergência: um passa-banda de 758–803 MHz para a banda de 700 MHz, combinadores multibanda a partir de 758 MHz e uma opção de baixo PIM na encomenda.",
      "مرشحات نطاق ومجمعات لأنظمة DAS داخل المباني وأنظمة راديو فرق الطوارئ: مرشح تمرير نطاق 758–803 MHz لنطاق 700 MHz، ومجمعات متعددة النطاقات ابتداءً من 758 MHz، وخيار PIM منخفض عند الطلب.")
    a("In-building DAS / ERCES", "Внутриобъектовые DAS / ERCES", "DAS / ERCES en edificios", "DAS / ERCES em edifícios", "DAS / ERCES داخل المباني")
    a("Three shelf families", "Три складские линейки", "Tres familias de existencias", "Três famílias de prateleira", "ثلاث عائلات مخزون")
    a("The catalog follows the specifications already written for current products.",
      "Каталог соответствует спецификациям, уже составленным для текущих изделий.",
      "El catálogo sigue las especificaciones ya redactadas para los productos actuales.",
      "O catálogo segue as especificações já redigidas para os produtos atuais.",
      "يتبع الكتالوج المواصفات المكتوبة أصلًا للمنتجات الحالية.")
    a("Single-band cavities from 703 MHz to 3.8 GHz, plus a low-loss 2.4 GHz unit. Rejection tables are on each datasheet.",
      "Однодиапазонные резонаторы от 703 MHz до 3,8 GHz, а также малошумящий (низких потерь) блок 2,4 GHz. Таблицы подавления приведены в каждой спецификации.",
      "Cavidades de una sola banda de 703 MHz a 3,8 GHz, más una unidad de 2,4 GHz de bajas pérdidas. Las tablas de rechazo están en cada ficha técnica.",
      "Cavidades de uma só banda de 703 MHz a 3,8 GHz, mais uma unidade de 2,4 GHz de baixas perdas. As tabelas de rejeição constam de cada ficha técnica.",
      "تجاويف أحادية النطاق من 703 MHz إلى 3.8 GHz، إضافة إلى وحدة 2.4 GHz منخفضة الفقد. جداول الرفض واردة في كل ورقة مواصفات.")
    a("Two-port and four-port cavity combiners for 700 MHz through n78 and 5 GHz Wi-Fi.",
      "Двух- и четырёхпортовые резонаторные комбайнеры от 700 MHz до n78 и Wi-Fi 5 GHz.",
      "Combinadores de cavidad de dos y cuatro puertos para 700 MHz hasta n78 y Wi-Fi de 5 GHz.",
      "Combinadores de cavidade de duas e quatro portas para 700 MHz até n78 e Wi-Fi de 5 GHz.",
      "مجمعات تجويفية ثنائية ورباعية المنافذ من 700 MHz حتى n78 وWi-Fi عند 5 GHz.")
    a("5150–5370 MHz and 5450–5850 MHz in one housing, 80 dB between passbands.",
      "5150–5370 MHz и 5450–5850 MHz в одном корпусе, 80 dB между полосами пропускания.",
      "5150–5370 MHz y 5450–5850 MHz en una sola carcasa, 80 dB entre bandas de paso.",
      "5150–5370 MHz e 5450–5850 MHz numa só caixa, 80 dB entre bandas de passagem.",
      "5150–5370 MHz و5450–5850 MHz في غلاف واحد، بفصل 80 dB بين نطاقي التمرير.")
    a("What a buyer can hold us to",
      "К чему покупатель может нас обязать",
      "A qué puede atenerse un comprador",
      "A que pode um comprador exigir-nos",
      "ما يمكن للمشتري أن يحاسبنا عليه")
    a("Indoor DAS, repeater remotes, and band cleanup around LTE and 5 GHz Wi-Fi.",
      "Внутриобъектовые DAS, выносные блоки ретрансляторов и частотная очистка вокруг LTE и Wi-Fi 5 GHz.",
      "DAS de interior, remotos de repetidor y limpieza de banda en torno a LTE y Wi-Fi de 5 GHz.",
      "DAS de interior, remotos de repetidor e limpeza de banda em torno de LTE e Wi-Fi de 5 GHz.",
      "أنظمة DAS داخلية، ووحدات المكررات البعيدة، وتنظيف النطاق حول LTE وWi-Fi عند 5 GHz.")
    a("Numbers you can test",
      "Цифры, которые можно проверить",
      "Cifras que se pueden comprobar",
      "Valores que pode verificar",
      "أرقام يمكن التحقق منها")
    a("Insertion loss, ripple, VSWR and rejection on the datasheet are the limits from the factory specification for that model. Return loss is the calculated equivalent of VSWR ≤ 1.3.",
      "Вносимые потери, неравномерность, VSWR и подавление в спецификации — это пределы из заводских технических требований для данной модели. Потери на отражение — расчётный эквивалент VSWR ≤ 1.3.",
      "La pérdida de inserción, el rizado, el VSWR y el rechazo de la ficha técnica son los límites de la especificación de fábrica de ese modelo. La pérdida de retorno es el equivalente calculado de VSWR ≤ 1.3.",
      "A perda de inserção, a ondulação, o VSWR e a rejeição da ficha técnica são os limites da especificação de fábrica desse modelo. A perda de retorno é o equivalente calculado de VSWR ≤ 1.3.",
      "فقد الإدخال والتموج وVSWR والرفض في ورقة المواصفات هي الحدود الواردة في مواصفات المصنع لذلك الطراز. فقد الراجع هو المكافئ المحسوب لـ VSWR ≤ 1.3.")
    a("A test report leaves with the unit",
      "Протокол испытаний отгружается вместе с изделием",
      "Un informe de ensayo sale con la unidad",
      "Um relatório de ensaio acompanha a unidade",
      "يغادر تقرير الاختبار مع الوحدة")
    a("Tuning is done on a vector network analyzer. The report covers the electrical rows. Low PIM at ≤ −150 dBc @ 2×43 dBm is an order option, measured when it is ordered.",
      "Настройка выполняется на векторном анализаторе цепей. Протокол охватывает электрические строки. Низкий PIM при ≤ −150 dBc @ 2×43 dBm — опция заказа, измеряется при её выборе.",
      "La sintonización se hace en un analizador de redes vectorial. El informe cubre las filas eléctricas. El bajo PIM a ≤ −150 dBc @ 2×43 dBm es una opción de pedido y se mide cuando se pide.",
      "A sintonização é feita num analisador de redes vetorial. O relatório cobre as linhas elétricas. O baixo PIM a ≤ −150 dBc @ 2×43 dBm é uma opção de encomenda e mede-se quando é pedida.",
      "يُجرى الضبط على محلل شبكة متجهي. يغطي التقرير الصفوف الكهربائية. PIM المنخفض عند ≤ −150 dBc @ 2×43 dBm خيار طلب، ويُقاس عند طلبه.")
    a("Drawings, not slogans",
      "Чертежи, а не лозунги",
      "Dibujos, no eslóganes",
      "Desenhos, não slogans",
      "رسوم، لا شعارات")
    a("Outline drawings from the specification are printed on the datasheet, with mounting holes where the drawing states them.",
      "Габаритные чертежи из спецификации печатаются в паспорте изделия; крепёжные отверстия указываются там, где они есть на чертеже.",
      "Los dibujos de contorno de la especificación se imprimen en la ficha técnica, con los orificios de montaje donde el dibujo los indica.",
      "Os desenhos de contorno da especificação são impressos na ficha técnica, com os furos de montagem onde o desenho os indica.",
      "تُطبع رسوم الأبعاد الواردة في المواصفات على ورقة البيانات، مع فتحات التثبيت حيث يذكرها الرسم.")
    a("Small-batch custom bands",
      "Индивидуальные диапазоны малыми партиями",
      "Bandas a medida en lotes pequeños",
      "Bandas à medida em lotes pequenos",
      "نطاقات حسب الطلب على دفعات صغيرة")
    a("Send the band plan, rejection, power, connector and envelope. The quotation states the lead time. We do not print a universal lead time here.",
      "Пришлите план частот, подавление, мощность, разъём и габаритный конверт. Срок поставки указывается в коммерческом предложении. Универсальный срок здесь не публикуется.",
      "Envíe el plan de bandas, el rechazo, la potencia, el conector y el envolvente. La cotización indica el plazo. Aquí no publicamos un plazo universal.",
      "Envie o plano de bandas, a rejeição, a potência, o conector e o envelope. A cotação indica o prazo. Não publicamos aqui um prazo universal.",
      "أرسل خطة النطاقات والرفض والقدرة والموصل والغلاف الخارجي. يذكر عرض السعر مهلة التسليم. لا ننشر هنا مهلة تسليم عامة.")

    # ===== about =====
    a("About the factory", "О заводе", "Acerca de la fábrica", "Sobre a fábrica", "عن المصنع")
    a("Shenzhen Kangxuntong, a cavity-filter factory.",
      "Shenzhen Kangxuntong, завод фильтров на объемных резонаторах.",
      "Shenzhen Kangxuntong, una fábrica de filtros de cavidad.",
      "Shenzhen Kangxuntong, uma fábrica de filtros de cavidade.",
      "Shenzhen Kangxuntong، مصنع مرشحات تجويفية.")
    a("The company", "Компания", "La empresa", "A empresa", "الشركة")
    a("深圳市康讯通技术有限公司, in English Shenzhen Kangxuntong Technology Co., Ltd., builds cavity filters in Shenzhen. The work is bandpass filters, diplexers and multi-band combiners for LTE, 5G indoor radio and Wi-Fi cleanup.",
      "深圳市康讯通技术有限公司, в английском написании Shenzhen Kangxuntong Technology Co., Ltd., производит фильтры на объемных резонаторах в Шэньчжэне. Это полосовые фильтры, диплексеры и многодиапазонные комбайнеры для LTE, внутреннего радио 5G и очистки Wi-Fi.",
      "深圳市康讯通技术有限公司, en inglés Shenzhen Kangxuntong Technology Co., Ltd., fabrica filtros de cavidad en Shenzhen. El trabajo son filtros paso banda, diplexores y combinadores multibanda para LTE, radio 5G de interior y limpieza de Wi-Fi.",
      "深圳市康讯通技术有限公司, em inglês Shenzhen Kangxuntong Technology Co., Ltd., fabrica filtros de cavidade em Shenzhen. O trabalho são filtros passa-banda, diplexadores e combinadores multibanda para LTE, rádio 5G de interior e limpeza de Wi-Fi.",
      "深圳市康讯通技术有限公司، وبالإنجليزية Shenzhen Kangxuntong Technology Co., Ltd.، تُصنّع مرشحات تجويفية في شنجن. يشمل العمل مرشحات تمرير نطاق وديبلكسرات ومجمعات متعددة النطاقات لـ LTE والراديو الداخلي لشبكات 5G وتنظيف Wi-Fi.")
    a("The factory", "Завод", "La fábrica", "A fábrica", "المصنع")
    a("Tuning, assembly and outgoing test are done in the Shenzhen workshop. Photographs on this site are of that workshop and of current hardware.",
      "Настройка, сборка и выходной контроль выполняются в цехе в Шэньчжэне. Фотографии на этом сайте сняты в этом цехе и показывают текущие изделия.",
      "La sintonización, el montaje y el ensayo de salida se hacen en el taller de Shenzhen. Las fotografías de este sitio son de ese taller y del hardware actual.",
      "A sintonização, a montagem e o ensaio de saída são feitos na oficina de Shenzhen. As fotografias deste sítio são dessa oficina e do hardware atual.",
      "يُجرى الضبط والتجميع والاختبار النهائي في ورشة شنجن. الصور في هذا الموقع لهذه الورشة وللتجهيزات الحالية.")
    a("张体进, +86 186 8871 8926, also on WhatsApp. Trade terms on the quotation are EXW or FOB Shenzhen. Sample freight is by courier. US import duty is confirmed with the buyer and is not calculated on this site.",
      "张体进, +86 186 8871 8926, также в WhatsApp. Условия поставки в коммерческом предложении — EXW или FOB Shenzhen. Образцы отправляются курьером. Импортная пошлина США согласовывается с покупателем и на этом сайте не рассчитывается.",
      "张体进, +86 186 8871 8926, también en WhatsApp. Los términos comerciales de la cotización son EXW o FOB Shenzhen. El envío de muestras es por mensajería. El arancel de importación de EE. UU. se confirma con el comprador y no se calcula en este sitio.",
      "张体进, +86 186 8871 8926, também no WhatsApp. Os termos comerciais da cotação são EXW ou FOB Shenzhen. O envio de amostras é por courier. O direito de importação dos EUA é confirmado com o comprador e não é calculado neste sítio.",
      "张体进، +86 186 8871 8926، وأيضًا على WhatsApp. شروط التجارة في عرض السعر هي EXW أو FOB Shenzhen. شحن العينات يتم بالبريد السريع. تُؤكد رسوم الاستيراد الأمريكية مع المشتري ولا تُحسَب على هذا الموقع.")

    # ===== quality =====
    a("Quality and test", "Качество и испытания", "Calidad y ensayo", "Qualidade e ensaio", "الجودة والاختبار")
    a("VNA tuning, a report with the shipment, PIM when it is ordered.",
      "Настройка на VNA, протокол с поставкой, PIM — при заказе этой опции.",
      "Sintonización en VNA, un informe con el envío, PIM cuando se pide.",
      "Sintonização em VNA, um relatório com o envio, PIM quando é pedido.",
      "ضبط على VNA، وتقرير مع الشحنة، وقياس PIM عند طلبه.")
    a("What is measured", "Что измеряется", "Qué se mide", "O que se mede", "ما الذي يُقاس")
    a("Each unit is tuned on a vector network analyzer. The outgoing report states insertion loss, ripple, VSWR and the rejection or isolation points on the datasheet, at room temperature in a 50 Ω system.",
      "Каждое изделие настраивается на векторном анализаторе цепей. В выходном протоколе указываются вносимые потери, неравномерность, VSWR и точки подавления или развязки из спецификации, при комнатной температуре в системе 50 Ω.",
      "Cada unidad se sintoniza en un analizador de redes vectorial. El informe de salida indica la pérdida de inserción, el rizado, el VSWR y los puntos de rechazo o aislamiento de la ficha técnica, a temperatura ambiente en un sistema de 50 Ω.",
      "Cada unidade é sintonizada num analisador de redes vetorial. O relatório de saída indica a perda de inserção, a ondulação, o VSWR e os pontos de rejeição ou isolamento da ficha técnica, à temperatura ambiente num sistema de 50 Ω.",
      "تُضبط كل وحدة على محلل شبكة متجهي. يذكر تقرير الخروج فقد الإدخال والتموج وVSWR ونقاط الرفض أو العزل الواردة في ورقة المواصفات، عند درجة حرارة الغرفة في نظام 50 Ω.")
    a("Low PIM", "Низкий PIM", "Bajo PIM", "Baixo PIM", "PIM منخفض")
    a("When the order calls for the low-PIM grade, PIM3 is tested at 2×43 dBm against the ≤ −150 dBc limit and the result is on the report. Units ordered without that grade are not sold as low-PIM parts.",
      "Если в заказе указан класс низкого PIM, PIM3 испытывается при 2×43 dBm на соответствие пределу ≤ −150 dBc, результат заносится в протокол. Изделия, заказанные без этого класса, не продаются как изделия с низким PIM.",
      "Cuando el pedido exige el grado de bajo PIM, se ensaya PIM3 a 2×43 dBm frente al límite de ≤ −150 dBc y el resultado figura en el informe. Las unidades pedidas sin ese grado no se venden como piezas de bajo PIM.",
      "Quando a encomenda exige o grau de baixo PIM, o PIM3 é ensaiado a 2×43 dBm face ao limite de ≤ −150 dBc e o resultado consta do relatório. As unidades encomendadas sem esse grau não são vendidas como peças de baixo PIM.",
      "عندما يطلب الأمر درجة PIM المنخفض، يُختبر PIM3 عند 2×43 dBm مقابل حد ≤ −150 dBc ويُدرج الناتج في التقرير. الوحدات المطلوبة دون هذه الدرجة لا تُباع كقطع منخفضة PIM.")
    a("Certificates", "Сертификаты", "Certificados", "Certificados", "الشهادات")
    a("Ask us for the certificates we can share on a given order. This site does not display certification marks.",
      "Запросите сертификаты, которые мы можем предоставить по конкретному заказу. На этом сайте знаки сертификации не размещаются.",
      "Consúltenos los certificados que podemos compartir en un pedido concreto. Este sitio no muestra marcas de certificación.",
      "Peça-nos os certificados que podemos partilhar numa encomenda concreta. Este sítio não exibe marcas de certificação.",
      "اسألنا عن الشهادات التي يمكننا مشاركتها لطلب معيّن. لا يعرض هذا الموقع علامات اعتماد.")

    # ===== privacy / terms =====
    a("How this site handles an enquiry.",
      "Как этот сайт обрабатывает запрос.",
      "Cómo este sitio trata una consulta.",
      "Como este sítio trata um pedido.",
      "كيف يتعامل هذا الموقع مع الاستفسار.")
    a("When you press “Send enquiry”, the quote form sends what you typed to our sales mailbox, sales@cavityfilter.com, through the form relay service FormSubmit (formsubmit.co), which handles it under its own terms. If you choose WhatsApp or email instead, the text is sent by that service under its own terms.",
      "Когда вы нажимаете «Отправить запрос», форма коммерческого запроса передаёт введённые данные на наш почтовый ящик продаж sales@cavityfilter.com через службу пересылки FormSubmit (formsubmit.co), которая обрабатывает их на своих условиях. Если вы выбираете WhatsApp или электронную почту, текст отправляется этой службой на её условиях.",
      "Al pulsar «Enviar consulta», el formulario de cotización envía lo escrito a nuestro buzón de ventas, sales@cavityfilter.com, a través del servicio de reenvío FormSubmit (formsubmit.co), que lo trata según sus propios términos. Si elige WhatsApp o el correo, el texto lo envía ese servicio según sus términos.",
      "Ao premir «Enviar pedido», o formulário de cotação envia o que escreveu para a nossa caixa de vendas, sales@cavityfilter.com, através do serviço de reencaminhamento FormSubmit (formsubmit.co), que o trata nos seus próprios termos. Se escolher o WhatsApp ou o correio eletrónico, o texto é enviado por esse serviço nos seus termos.",
      "عند الضغط على «إرسال الاستفسار»، يُرسل نموذج التسعير ما أدخلته إلى صندوق مبيعاتنا sales@cavityfilter.com عبر خدمة الترحيل FormSubmit (formsubmit.co)، التي تعالجه وفق شروطها. إذا اخترت WhatsApp أو البريد الإلكتروني بدلًا من ذلك، يُرسل النص عبر تلك الخدمة وفق شروطها.")
    a("We use your name, company, phone number and email only to answer the enquiry. We do not sell them or pass them to third parties. To have an enquiry deleted, write to",
      "Мы используем ваше имя, компанию, номер телефона и адрес электронной почты только для ответа на запрос. Мы не продаём эти данные и не передаём их третьим лицам. Чтобы удалить запрос, напишите на",
      "Usamos su nombre, empresa, teléfono y correo solo para responder a la consulta. No los vendemos ni los cedemos a terceros. Para que se elimine una consulta, escriba a",
      "Usamos o seu nome, empresa, telefone e correio eletrónico apenas para responder ao pedido. Não os vendemos nem os cedemos a terceiros. Para eliminar um pedido, escreva para",
      "نستخدم اسمك وشركتك ورقم هاتفك وبريدك فقط للرد على الاستفسار. لا نبيعها ولا نمررها إلى أطراف ثالثة. لحذف استفسار، راسل")
    # The privacy second paragraph includes a mailto link in the middle. Text nodes are split.
    a("We use your name, company, phone number and email only to answer the enquiry. We do not sell them or pass them to third parties. To have an enquiry deleted, write to sales@cavityfilter.com.",
      "Мы используем ваше имя, компанию, номер телефона и адрес электронной почты только для ответа на запрос. Мы не продаём эти данные и не передаём их третьим лицам. Чтобы удалить запрос, напишите на sales@cavityfilter.com.",
      "Usamos su nombre, empresa, teléfono y correo solo para responder a la consulta. No los vendemos ni los cedemos a terceros. Para que se elimine una consulta, escriba a sales@cavityfilter.com.",
      "Usamos o seu nome, empresa, telefone e correio eletrónico apenas para responder ao pedido. Não os vendemos nem os cedemos a terceiros. Para eliminar um pedido, escreva para sales@cavityfilter.com.",
      "نستخدم اسمك وشركتك ورقم هاتفك وبريدك فقط للرد على الاستفسار. لا نبيعها ولا نمررها إلى أطراف ثالثة. لحذف استفسار، راسل sales@cavityfilter.com.")
    a("Commercial terms for this catalog.",
      "Коммерческие условия этого каталога.",
      "Términos comerciales de este catálogo.",
      "Termos comerciais deste catálogo.",
      "الشروط التجارية لهذا الكتالوج.")
    a("Datasheet Rev A is the catalog specification. The test report shipped with a unit is the record for that unit. Trade terms are EXW or FOB Shenzhen unless the quotation says otherwise. Lead time, price and any certificate are on the quotation. Low PIM applies only when the order selects that option.",
      "Спецификация ред. A является каталожной характеристикой. Протокол испытаний, отгруженный с изделием, является записью для данного изделия. Условия поставки — EXW или FOB Shenzhen, если в коммерческом предложении не указано иное. Срок, цена и любые сертификаты указываются в коммерческом предложении. Низкий PIM действует только при выборе этой опции в заказе.",
      "La ficha técnica Rev. A es la especificación del catálogo. El informe de ensayo enviado con una unidad es el registro de esa unidad. Los términos comerciales son EXW o FOB Shenzhen salvo que la cotización diga otra cosa. El plazo, el precio y cualquier certificado figuran en la cotización. El bajo PIM aplica solo cuando el pedido selecciona esa opción.",
      "A ficha técnica Rev. A é a especificação do catálogo. O relatório de ensaio enviado com uma unidade é o registo dessa unidade. Os termos comerciais são EXW ou FOB Shenzhen, salvo se a cotação indicar o contrário. O prazo, o preço e qualquer certificado constam da cotação. O baixo PIM aplica-se apenas quando a encomenda seleciona essa opção.",
      "ورقة المواصفات الإصدار A هي مواصفة الكتالوج. تقرير الاختبار المُشحن مع الوحدة هو السجل المعتمد لتلك الوحدة. شروط التجارة هي EXW أو FOB Shenzhen ما لم ينص عرض السعر على خلاف ذلك. مهلة التسليم والسعر وأي شهادة ترد في عرض السعر. ينطبق PIM المنخفض فقط عندما يختار الطلب هذا الخيار.")

    return P
