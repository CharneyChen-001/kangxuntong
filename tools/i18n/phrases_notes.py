# Product footnotes, typo explanations and remaining cell phrases. Faithful to the EN/ZH notes.

def entries():
    P = {}
    def a(en, ru, es, pt, ar):
        P[en] = {"ru": ru, "es": es, "pt": pt, "ar": ar}

    a("The source sheet gave insertion loss and ripple without a symbol. This revision states them as maximum values (≤).",
      "В исходном листе вносимые потери и неравномерность указаны без знака. В этой редакции они приведены как максимальные значения (≤).",
      "La ficha de origen indicaba la pérdida de inserción y el rizado sin un símbolo. Esta revisión los expresa como valores máximos (≤).",
      "A ficha de origem indicava a perda de inserção e a ondulação sem um símbolo. Esta revisão expressa-os como valores máximos (≤).",
      "ذكرت ورقة المصدر فقد الإدخال والتموج دون رمز. ويذكرهما هذا التنقيح كقيم قصوى (≤).")
    a("Return loss is calculated from VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
      "Потери на отражение рассчитаны из VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
      "La pérdida de retorno se calcula a partir de VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
      "A perda de retorno calcula-se a partir de VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.",
      "يُحسَب فقد الراجع من VSWR ≤ 1.3: RL = −20 log10((VSWR−1)/(VSWR+1)) ≈ 17.7 dB.")
    a("Rejection figures are the discrete points written in the source sheet.",
      "Значения подавления — дискретные точки, записанные в исходном листе.",
      "Las cifras de rechazo son los puntos discretos escritos en la ficha de origen.",
      "As cifras de rejeição são os pontos discretos escritos na ficha de origem.",
      "أرقام الرفض هي النقاط المنفصلة المكتوبة في ورقة المصدر.")
    a("The connector was written ISMA-F and is corrected to SMA-F.",
      "Разъём был записан как ISMA-F и исправлен на SMA-F.",
      "El conector estaba escrito ISMA-F y se corrige a SMA-F.",
      "O conector estava escrito ISMA-F e corrige-se para SMA-F.",
      "كُتب الموصل ISMA-F وصُحِّح إلى SMA-F.")
    a("The outline was written 228**144×45.5 mm and is corrected to 228×144×45.5 mm.",
      "Габариты были записаны как 228**144×45.5 mm и исправлены на 228×144×45.5 mm.",
      "El contorno estaba escrito 228**144×45.5 mm y se corrige a 228×144×45.5 mm.",
      "O contorno estava escrito 228**144×45.5 mm e corrige-se para 228×144×45.5 mm.",
      "كُتبت الأبعاد 228**144×45.5 mm وصُحِّحت إلى 228×144×45.5 mm.")
    a("The source table is laid out with items in columns; it is shown here row by row. No number is changed.",
      "Исходная таблица расположена по столбцам; здесь она показана построчно. Ни одно число не изменено.",
      "La tabla de origen está dispuesta con los ítems en columnas; aquí se muestra fila a fila. No se cambia ningún número.",
      "A tabela de origem está disposta com os itens em colunas; aqui mostra-se linha a linha. Nenhum número é alterado.",
      "جدول المصدر مرتّب ببنود في أعمدة؛ ويُعرض هنا صفًا بصف. لم يُغيَّر أي رقم.")
    a("The source frequency cell is blank; the passband is only in the table header. This page copies it into the frequency row.",
      "Ячейка частоты в исходнике пуста; полоса пропускания указана только в заголовке таблицы. Эта страница копирует её в строку частоты.",
      "La celda de frecuencia de origen está en blanco; la banda de paso solo está en el encabezado de la tabla. Esta página la copia en la fila de frecuencia.",
      "A célula de frequência de origem está em branco; a banda de passagem está apenas no cabeçalho da tabela. Esta página copia-a para a linha de frequência.",
      "خلية التردد في المصدر فارغة؛ ونطاق التمرير موجود فقط في رأس الجدول. تنسخه هذه الصفحة إلى صف التردد.")
    a("The factory Word heading said 中频段8频合路器规格书; it is corrected to 低频段6频合路器规格书 to match the filename and the 6-port table.",
      "В заголовке заводского файла Word было указано 中频段8频合路器规格书; исправлено на 低频段6频合路器规格书, чтобы соответствовать имени файла и таблице на 6 портов.",
      "El encabezado del Word de fábrica decía 中频段8频合路器规格书; se corrige a 低频段6频合路器规格书 para coincidir con el nombre de archivo y la tabla de 6 puertos.",
      "O cabeçalho do Word de fábrica dizia 中频段8频合路器规格书; corrige-se para 低频段6频合路器规格书 para coincidir com o nome do ficheiro e a tabela de 6 portas.",
      "كان عنوان ملف Word الصادر عن المصنع 中频段8频合路器规格书؛ وصُحِّح إلى 低频段6频合路器规格书 ليطابق اسم الملف وجدول المنافذ الستة.")
    a("†† Port 2 rejection was written 90@22620-2690 on the source sheet; every other port uses 2620-2690. Printed as 2620-2690, marked *.",
      "†† Подавление порта 2 было записано как 90@22620-2690 в исходном листе; все остальные порты используют 2620-2690. Напечатано как 2620-2690, отмечено *.",
      "†† El rechazo del puerto 2 estaba escrito 90@22620-2690 en la ficha de origen; los demás puertos usan 2620-2690. Impreso como 2620-2690, marcado *.",
      "†† A rejeição da porta 2 estava escrita 90@22620-2690 na ficha de origem; as outras portas usam 2620-2690. Impresso como 2620-2690, marcado *.",
      "†† كُتب رفض المنفذ 2 على ورقة المصدر 90@22620-2690؛ وتستخدم بقية المنافذ 2620-2690. طُبع كـ 2620-2690، مع علامة *.")
    a("On CH3 and CH4 the source repeated 1920–1980 MHz and omitted 2110–2170 MHz; isolation is filled as ≥80 dB to match the rest of the sheet.",
      "На CH3 и CH4 исходник повторял 1920–1980 MHz и пропускал 2110–2170 MHz; развязка заполнена как ≥80 dB для соответствия остальному листу.",
      "En CH3 y CH4 el origen repetía 1920–1980 MHz y omitía 2110–2170 MHz; el aislamiento se completa como ≥80 dB para coincidir con el resto de la ficha.",
      "Em CH3 e CH4 a origem repetia 1920–1980 MHz e omitia 2110–2170 MHz; o isolamento preenche-se como ≥80 dB para coincidir com o resto da ficha.",
      "في CH3 وCH4 كرّر المصدر 1920–1980 MHz وأغفل 2110–2170 MHz؛ ويُملأ العزل بـ ≥80 dB ليطابق بقية الورقة.")
    a("Transcribed from the factory Word file, including the mechanical drawing on page 2 of that file. A † marks a merged cell copied onto a blank port.",
      "Расшифровано из заводского файла Word, включая механический чертёж на странице 2 этого файла. Знак † отмечает объединённую ячейку, скопированную на пустой порт.",
      "Transcrito del archivo Word de fábrica, incluido el dibujo mecánico de la página 2 de ese archivo. Un † marca una celda combinada copiada a un puerto en blanco.",
      "Transcrito do ficheiro Word de fábrica, incluindo o desenho mecânico da página 2 desse ficheiro. Um † marca uma célula unida copiada para uma porta em branco.",
      "نُقل من ملف Word الصادر عن المصنع، بما في ذلك الرسم الميكانيكي في الصفحة 2 من ذلك الملف. علامة † تشير إلى خلية مدمجة نُسخت إلى منفذ فارغ.")
    a("Transcribed from the factory Word file. Typos named on the PDF are corrected. Every other number is unchanged. A † marks a merged cell copied onto a blank port.",
      "Расшифровано из заводского файла Word. Опечатки, названные в PDF, исправлены. Все остальные числа не изменены. Знак † отмечает объединённую ячейку, скопированную на пустой порт.",
      "Transcrito del archivo Word de fábrica. Las erratas indicadas en el PDF están corregidas. Cualquier otro número no se modifica. Un † marca una celda combinada copiada a un puerto en blanco.",
      "Transcrito do ficheiro Word de fábrica. Os erros tipográficos indicados no PDF estão corrigidos. Qualquer outro número permanece inalterado. Um † marca uma célula unida copiada para uma porta em branco.",
      "نُقل من ملف Word الصادر عن المصنع. صُحِّحت الأخطاء الإملائية المذكورة في ملف PDF. ولم يُغيَّر أي رقم آخر. علامة † تشير إلى خلية مدمجة نُسخت إلى منفذ فارغ.")
    a("A dangling “≥” at the end of the port 2 rejection list is not treated as a limit. Port 2 VSWR is a merged cell, copied from port 1 as ≤1.3, marked †.",
      "Свободный знак «≥» в конце списка подавления порта 2 не рассматривается как предел. VSWR порта 2 — объединённая ячейка, скопированная с порта 1 как ≤1.3, отмечено †.",
      "Un «≥» suelto al final de la lista de rechazo del puerto 2 no se trata como un límite. El VSWR del puerto 2 es una celda combinada, copiada del puerto 1 como ≤1.3, marcada †.",
      "Um «≥» solto no fim da lista de rejeição da porta 2 não é tratado como um limite. O VSWR da porta 2 é uma célula unida, copiada da porta 1 como ≤1.3, marcada †.",
      "علامة «≥» المعلّقة في نهاية قائمة رفض المنفذ 2 لا تُعامَل كحد. VSWR للمنفذ 2 خلية مدمجة، نُسخت من المنفذ 1 كـ ≤1.3، مع علامة †.")
    a("The factory file was named 9频合路器技术规格书, but the table has 8 ports (port 4 carries two passbands 1887.5-1915 / 2010-2025), so the published title is 8-band.",
      "Заводской файл был назван 9频合路器技术规格书, но в таблице 8 портов (порт 4 несёт две полосы 1887.5-1915 / 2010-2025), поэтому опубликованное название — 8-диапазонный.",
      "El archivo de fábrica se llamaba 9频合路器技术规格书, pero la tabla tiene 8 puertos (el puerto 4 lleva dos bandas de paso 1887.5-1915 / 2010-2025), así que el título publicado es de 8 bandas.",
      "O ficheiro de fábrica chamava-se 9频合路器技术规格书, mas a tabela tem 8 portas (a porta 4 transporta duas bandas de passagem 1887.5-1915 / 2010-2025), pelo que o título publicado é de 8 bandas.",
      "سُمِّي ملف المصنع 9频合路器技术规格书، لكن الجدول يضم 8 منافذ (المنفذ 4 يحمل نطاقي تمرير 1887.5-1915 / 2010-2025)، لذا فإن العنوان المنشور هو 8 نطاقات.")
    a("CH2–CH4 source omitted isolation to 758–960 MHz; filled as ≥70 dB to match the rest of the sheet. A truncated «1805-1920MH» on CH4 is read as 1805–1920 MHz.",
      "В исходнике для CH2–CH4 была пропущена развязка к 758–960 MHz; заполнена как ≥70 dB для соответствия остальному листу. Усечённая запись «1805-1920MH» на CH4 читается как 1805–1920 MHz.",
      "El origen de CH2–CH4 omitía el aislamiento a 758–960 MHz; se completa como ≥70 dB para coincidir con el resto de la ficha. Un «1805-1920MH» truncado en CH4 se lee como 1805–1920 MHz.",
      "A origem de CH2–CH4 omitia o isolamento a 758–960 MHz; preenche-se como ≥70 dB para coincidir com o resto da ficha. Um «1805-1920MH» truncado em CH4 lê-se como 1805–1920 MHz.",
      "أغفل مصدر CH2–CH4 العزل إلى 758–960 MHz؛ ويُملأ بـ ≥70 dB ليطابق بقية الورقة. وتُقرأ الصيغة المقطوعة «1805-1920MH» في CH4 على أنها 1805–1920 MHz.")
    a("The source heading says duplexer; the file name says filter. This sheet is issued as a two-passband diplexer. Bandwidths 220 MHz and 400 MHz are from the source.",
      "В заголовке исходника указан дуплексер; в имени файла — фильтр. Этот лист выпущен как диплексер с двумя полосами пропускания. Полосы 220 MHz и 400 MHz взяты из исходника.",
      "El encabezado de origen dice dúplexer; el nombre de archivo dice filtro. Esta ficha se emite como un diplexor de dos bandas de paso. Los anchos de banda de 220 MHz y 400 MHz proceden del origen.",
      "O cabeçalho de origem diz duplexador; o nome do ficheiro diz filtro. Esta ficha é emitida como um diplexador de duas bandas de passagem. As larguras de banda de 220 MHz e 400 MHz provêm da origem.",
      "يقول عنوان المصدر إنه دبلكسر؛ واسم الملف يقول إنه مرشح. تُصدر هذه الورقة كديبلكسر بنطاقي تمرير. عرضا النطاق 220 MHz و400 MHz مأخوذان من المصدر.")
    a("* The source PIM level is ≤−145 dBc. The test condition was written “43dBC”; this page reads it as the industry-standard two-tone PIM3 test at 2×43 dBm. Marked * and pending written factory confirmation.",
      "* Уровень PIM в исходнике — ≤−145 dBc. Условие испытания было записано как «43dBC»; эта страница читает его как стандартное двухтоновое испытание PIM3 при 2×43 dBm. Отмечено * и ожидает письменного подтверждения завода.",
      "* El nivel de PIM de origen es ≤−145 dBc. La condición de ensayo estaba escrita «43dBC»; esta página la interpreta como el ensayo PIM3 de dos tonos habitual en la industria a 2×43 dBm. Marcado * y pendiente de confirmación escrita de fábrica.",
      "* O nível de PIM de origem é ≤−145 dBc. A condição de ensaio estava escrita «43dBC»; esta página interpreta-a como o ensaio PIM3 de dois tons habitual na indústria a 2×43 dBm. Marcado * e pendente de confirmação escrita da fábrica.",
      "* مستوى PIM في المصدر هو ≤−145 dBc. كُتب شرط الاختبار «43dBC»؛ وتقرأه هذه الصفحة على أنه اختبار PIM3 القياسي ذي النغمتين عند 2×43 dBm. مُعلَّم بـ * وبانتظار تأكيد كتابي من المصنع.")
    a("The source is one two-channel table; the first transcription split it into four “ports” by mistake and is replaced by the table above. Mechanical rows are merged cells shared by both channels. The source title and “model” cell read SGQ-1.8G-75M-19088-ZTJ and are shown as written; the catalogue number is KXT-FF-23.",
      "Исходник — одна двухканальная таблица; первая расшифровка по ошибке разбила её на четыре «порта» и заменена таблицей выше. Механические строки — объединённые ячейки, общие для обоих каналов. Заголовок исходника и ячейка «модель» читаются SGQ-1.8G-75M-19088-ZTJ и приведены как записано; каталожный номер — KXT-FF-23.",
      "El origen es una sola tabla de dos canales; la primera transcripción la dividió por error en cuatro «puertos» y se sustituye por la tabla anterior. Las filas mecánicas son celdas combinadas compartidas por ambos canales. El título de origen y la celda «modelo» dicen SGQ-1.8G-75M-19088-ZTJ y se muestran tal como están escritos; el número de catálogo es KXT-FF-23.",
      "A origem é uma só tabela de dois canais; a primeira transcrição dividiu-a por engano em quatro «portas» e é substituída pela tabela acima. As linhas mecânicas são células unidas partilhadas por ambos os canais. O título de origem e a célula «modelo» dizem SGQ-1.8G-75M-19088-ZTJ e mostram-se como estão escritos; o número de catálogo é KXT-FF-23.",
      "المصدر جدول واحد بقناتين؛ أما النقل الأول فقسمه خطأً إلى أربعة «منافذ» واستُبدل بالجدول أعلاه. الصفوف الميكانيكية خلايا مدمجة مشتركة بين القناتين. يقرأ عنوان المصدر وخلية «الطراز» SGQ-1.8G-75M-19088-ZTJ ويُعرضان كما كُتبا؛ ورقم الكتالوج هو KXT-FF-23.")
    a("* The source table writes 1802–1833 MHz (the Word display matches the XML; the cell is wide, so this is not overflow). The file name (1802-1883滤波器技术规格书.docx) and the model number KXT-BF-18021883 are 1802–1883. This page prints the table value 1802–1833 MHz (bandwidth 31 MHz), marked *. The catalog model number is unchanged.",
      "* В исходной таблице указано 1802–1833 MHz (отображение Word совпадает с XML; ячейка широкая, это не переполнение). Имя файла (1802-1883滤波器技术规格书.docx) и номер модели KXT-BF-18021883 — 1802–1883. Эта страница печатает табличное значение 1802–1833 MHz (полоса 31 MHz), отмечено *. Каталожный номер модели не изменён.",
      "* La tabla de origen escribe 1802–1833 MHz (la vista de Word coincide con el XML; la celda es ancha, así que no es un desbordamiento). El nombre de archivo (1802-1883滤波器技术规格书.docx) y el número de modelo KXT-BF-18021883 son 1802–1883. Esta página imprime el valor de la tabla 1802–1833 MHz (ancho de banda 31 MHz), marcado *. El número de modelo del catálogo no cambia.",
      "* A tabela de origem escreve 1802–1833 MHz (a vista do Word coincide com o XML; a célula é larga, pelo que não é um transbordo). O nome do ficheiro (1802-1883滤波器技术规格书.docx) e o número de modelo KXT-BF-18021883 são 1802–1883. Esta página imprime o valor da tabela 1802–1833 MHz (largura de banda 31 MHz), marcado *. O número de modelo do catálogo não se altera.",
      "* يكتب جدول المصدر 1802–1833 MHz (عرض Word يطابق XML؛ والخلية واسعة، لذا فهذا ليس فيضانًا). اسم الملف (1802-1883滤波器技术规格书.docx) ورقم الطراز KXT-BF-18021883 هما 1802–1883. تطبع هذه الصفحة قيمة الجدول 1802–1833 MHz (عرض نطاق 31 MHz)، مع علامة *. رقم طراز الكتالوج دون تغيير.")
    a("* Port 3 VSWR is written ≤0.9 on the source sheet (VSWR cannot be below 1; the cell is wide, and the Word display matches the XML, so this is not an overflow. It may be a typo for 1.9, or a return-loss figure written as VSWR). This page prints ≤0.9 as written, marked *, and does not rewrite it. Ports 1 and 2 are ≤1.3 as written. Pending written factory confirmation.",
      "* VSWR порта 3 записан как ≤0.9 в исходном листе (VSWR не может быть меньше 1; ячейка широкая, отображение Word совпадает с XML, это не переполнение. Возможно, опечатка вместо 1.9 либо величина потерь на отражение, записанная как VSWR). Эта страница печатает ≤0.9 как записано, отмечено *, и не переписывает его. Порты 1 и 2 — ≤1.3 как записано. Ожидается письменное подтверждение завода.",
      "* El VSWR del puerto 3 está escrito ≤0.9 en la ficha de origen (el VSWR no puede ser inferior a 1; la celda es ancha y la vista de Word coincide con el XML, así que no es un desbordamiento. Puede ser una errata por 1.9, o una cifra de pérdida de retorno escrita como VSWR). Esta página imprime ≤0.9 tal como está escrito, marcado *, y no lo reescribe. Los puertos 1 y 2 son ≤1.3 tal como están escritos. Pendiente de confirmación escrita de fábrica.",
      "* O VSWR da porta 3 está escrito ≤0.9 na ficha de origem (o VSWR não pode ser inferior a 1; a célula é larga e a vista do Word coincide com o XML, pelo que não é um transbordo. Pode ser um erro tipográfico por 1.9, ou uma cifra de perda de retorno escrita como VSWR). Esta página imprime ≤0.9 como está escrito, marcado *, e não o reescreve. As portas 1 e 2 são ≤1.3 como estão escritas. Pendente de confirmação escrita da fábrica.",
      "* كُتب VSWR للمنفذ 3 على ورقة المصدر ≤0.9 (لا يمكن أن يكون VSWR أقل من 1؛ والخلية واسعة، وعرض Word يطابق XML، لذا فهذا ليس فيضانًا. قد يكون خطأً مطبعيًا بدل 1.9، أو رقم فقد راجع كُتب على أنه VSWR). تطبع هذه الصفحة ≤0.9 كما هو مكتوب، مع علامة *، ولا تعيد كتابته. المنفذان 1 و2 هما ≤1.3 كما هو مكتوب. بانتظار تأكيد كتابي من المصنع.")

    # ordering lines / mechanical notes
    a("+ connector + finish + low-PIM option + quantity",
      "+ разъём + покрытие + опция низкого PIM + количество",
      "+ conector + acabado + opción de bajo PIM + cantidad",
      "+ conector + acabamento + opção de baixo PIM + quantidade",
      "+ الموصل + التشطيب + خيار PIM المنخفض + الكمية")
    a("+ connector + power + low-PIM option + quantity",
      "+ разъём + мощность + опция низкого PIM + количество",
      "+ conector + potencia + opción de bajo PIM + cantidad",
      "+ conector + potência + opção de baixo PIM + quantidade",
      "+ الموصل + القدرة + خيار PIM المنخفض + الكمية")
    a("Mounting-hole pitch 82.4 × 82.4 mm, hole Ø3.2 mm.",
      "Шаг крепёжных отверстий 82.4 × 82.4 mm, отверстие Ø3.2 mm.",
      "Paso de orificios de montaje 82.4 × 82.4 mm, orificio Ø3.2 mm.",
      "Passo dos furos de montagem 82.4 × 82.4 mm, furo Ø3.2 mm.",
      "تباعد فتحات التثبيت 82.4 × 82.4 mm، فتحة Ø3.2 mm.")

    a("Indoor, aluminum cavity (series interface)",
      "Исполнение для помещений, алюминиевый резонатор (интерфейс серии)",
      "Interior, cavidad de aluminio (interfaz de la serie)",
      "Interior, cavidade de alumínio (interface da série)",
      "داخلي، تجويف ألومنيوم (واجهة السلسلة)")
    a("Not stated on the quotation; on the unit’s factory test report",
      "В прайс-листе не указано; см. заводской протокол испытаний изделия",
      "No consta en la cotización; figura en el informe de ensayo de fábrica de la unidad",
      "Não consta da cotação; consta do relatório de ensaio de fábrica da unidade",
      "غير مبيَّن في عرض السعر؛ وارد في تقرير اختبار المصنع للوحدة")
    a("Order option, confirmed on the quotation",
      "Опция заказа, подтверждается в коммерческом предложении",
      "Opción de pedido, confirmada en la cotización",
      "Opção de encomenda, confirmada na cotação",
      "خيار طلب، يُؤكَّد في عرض السعر")
    a("A duplexer for VHF/UHF private radio (LMR). See also",
      "Дуплексер для ведомственной радиосвязи VHF/UHF (LMR). См. также",
      "Un dúplexer para radio privada VHF/UHF (LMR). Véase también",
      "Um duplexador para rádio privada VHF/UHF (LMR). Ver também",
      "دبلكسر لراديو خاص VHF/UHF (LMR). انظر أيضًا")
    a("TETRA / P25 / DMR networks",
      "сети TETRA / P25 / DMR",
      "redes TETRA / P25 / DMR",
      "redes TETRA / P25 / DMR",
      "شبكات TETRA / P25 / DMR")
    a("VHF/UHF duplexers",
      "дуплексеры VHF/UHF",
      "dúplexers VHF/UHF",
      "duplexadores VHF/UHF",
      "دبلكسرات VHF/UHF")

    a("The source sheet leaves the outline as TBD.",
      "В исходном листе габариты указаны как TBD.",
      "La ficha de origen deja el contorno como TBD.",
      "A ficha de origem deixa o contorno como TBD.",
      "تترك ورقة المصدر الأبعاد كـ TBD.")
    a("技术指标 Technical",
      "技术指标 Технические характеристики",
      "技术指标 Técnico",
      "技术指标 Técnico",
      "技术指标 تقني")
    a("指标项目 Item",
      "指标项目 Позиция",
      "指标项目 Ítem",
      "指标项目 Item",
      "指标项目 البند")
    a("黑色 Black",
      "黑色 Чёрный",
      "黑色 Negro",
      "黑色 Preto",
      "黑色 أسود")
    a("About the factory | Kangxuntong",
      "О заводе | Kangxuntong",
      "Acerca de la fábrica | Kangxuntong",
      "Sobre a fábrica | Kangxuntong",
      "عن المصنع | Kangxuntong")
    return P
