"""Write verified verbatim transcriptions (pNNNN.txt) and faithful Turkish translations (pNNNN.tr.txt)
for pages 3–16 of the 1960–1961 Republic of Cyprus House of Representatives PDF
(A Vouleftiki periodos - Synodos A - 16.08.1960 - 07.08.1961):
  - Birleşim 1: 16 Ağustos 1960 (s. 3–4, tam metin)
  - Birleşim 2: 29 Ağustos 1960 (s. 5–14, tam metin)
  - Birleşim 3: 16 Eylül 1960 (s. 15–16, açılış ve yazılı/sözlü sorular)

Originally Turkish speeches are preserved verbatim as printed in 1960; Greek speeches carry both
their verbatim original Greek (in pNNNN.txt) and faithful Turkish translation (in pNNNN.tr.txt).
"""

from pathlib import Path

VOL_ID = "KC_D1_S1_1960-08-16"
OUT_DIR = Path("data/reocr") / VOL_ID

PAGES: dict[int, tuple[str, str]] = {
    3: (
        """Πρακτικὰ τῆς Βουλῆς τῶν Ἀντιπροσώπων
Α' ΣΥΝΟΔΟΣ
ΣΥΝΕΔΡΙΑΣΙΣ 16ης ΑΥΓΟΥΣΤΟΥ 1960
(Ὥρα Ἐνάρξεως 10 π.μ.)

Temsilciler Meclisi Zabıtları
BİRİNCİ İÇTİMA
16 AĞUSTOS 1960 TARİHLİ TOPLANTI
(Başlangıç saati : ö.e. 10.00)

GEÇİCİ MECLİS REİSİ BAY H. HACIHAROS :
Elen Temsilciler, isimlerinizi lütfen söylermisiniz ?

GEÇİCİ REİS VEKİLİ DR. NİYAZİ MANYERA :
Türk Temsilciler, isimlerinizi lütfen söylermisiniz ?

GEÇİCİ MECLİS REİSİ :
Bugünkü gündem aşağıdakilerden ibarettir :
(1) Temsilcilerin söz vermesi.
(2) Meclis Reis ve Reis Vekili seçimi.
(3) Meclis Kâtipleri ve İdare Âmirlerinin seçimi.
(4) Cumhurbaşkanı ve Cumhurbaşkan Muavininin söz vermesi.

Kıbrıs Cumhuriyetinin, Anayasasına ve buna uygun olarak yapılmış kanunlara, bağımsızlığının ve toprak bütünlüğünün korunmasına, iman ve riayet edeceğime söz veririm.

BAY MİHAİLİDİS SAVVİDİS :
Bay Glafkos Kliridis'i Meclis Reisi adaylığına teklif ediyorum.

BAY STELYOS MİHAİLİDİS :
Mihailidis Savvidis'in teklifini teyit ederim.

BAY EZEKİAS PAPAYUANNU :
Meclis Reisi adayı olarak gösterilen şahsın, görevlerini sadakat ve hakkaniyetle yapacağı ve demokratik prensiplerin geliştirilmesi ve Kıbrıs halkının birliği için çalışacağı ümidiyle Akel Meclis Üyeleri, Bay Glafkos Kliridis'in adaylığını destekler ve bu suretle de halkın birliğinin geliştirilmesine yardım eder.

GEÇİCİ MECLİS REİSİ :
Başka aday olmadığından, Bay Glafkos Kliridis Meclis Reisliğine seçilmiştir. Bay Kliridis'i yerini almağa davet ederim.

GLAFKOS KLİRİDİS :
Sayın Üye Arkadaşlar,
Hür Kıbrıs'ın Birinci Meclisinin Reisliğini şahsıma emanet etmek suretiyle, bana vermiş olduğunuz şerefi kabul etmekle mütehassisim. Burada, hepimizin birlikte kabul ettiğimiz sorumluluğu tamamen müdrik olarak Kıbrıs Temsilciler Meclisini hür düşünce ve ifade ve insan hak ve hürriyetlerini muhafaza edecek örnek bir yer yapmamız için sizlerle çalışacağıma söz veririm.
Ümit ederim ki, işbirliğimiz, pek yakında hürriyetin nimetlerini elde etmeleri için dua ettiğimiz bütün esir insan topluluklarına bir örnek olacaktır. Anayasa hükümlerine dayanarak Bay Lellos Dimitriadis ile Bay Petros Stilyanu'yu Meclis Sekreteri; Bay Titos Fanos ile Bay Nikos Koşis'i de Meclis İdare Âmiri tâyin ederim.
""",
        """Temsilciler Meclisi Zabıtları
BİRİNCİ İÇTİMA
16 AĞUSTOS 1960 TARİHLİ TOPLANTI
(Başlangıç saati : ö.e. 10.00)

GEÇİCİ MECLİS REİSİ BAY H. HACIHAROS :
Elen Temsilciler, isimlerinizi lütfen söylermisiniz ?

GEÇİCİ REİS VEKİLİ DR. NİYAZİ MANYERA :
Türk Temsilciler, isimlerinizi lütfen söylermisiniz ?

GEÇİCİ MECLİS REİSİ BAY H. HACIHAROS :
Bugünkü gündem aşağıdakilerden ibarettir :
(1) Temsilcilerin söz vermesi.
(2) Meclis Reis ve Reis Vekili seçimi.
(3) Meclis Kâtipleri ve İdare Âmirlerinin seçimi.
(4) Cumhurbaşkanı ve Cumhurbaşkan Muavininin söz vermesi.
(Geçici Meclis Reisi ayağa kalkarak ve sağ kolunu kaldırarak Anayasanın 69'uncu maddesi gereğince aşağıdaki sözü verdi; bütün Elen Temsilciler ve Geçici Reis Vekili Dr. Niyazi Manyera ile bütün Türk Temsilciler aynı sözü tekrarladı:)
"Kıbrıs Cumhuriyetinin, Anayasasına ve buna uygun olarak yapılmış kanunlara, bağımsızlığının ve toprak bütünlüğünün korunmasına, iman ve riayet edeceğime söz veririm."

BAY MİHAİLİDİS SAVVİDİS :
Bay Glafkos Kliridis'i Meclis Reisi adaylığına teklif ediyorum.

BAY STELYOS MİHAİLİDİS :
Mihailidis Savvidis'in teklifini teyit ederim.

BAY EZEKİAS PAPAYUANNU :
Meclis Reisi adayı olarak gösterilen şahsın, görevlerini sadakat ve hakkaniyetle yapacağı ve demokratik prensiplerin geliştirilmesi ve Kıbrıs halkının birliği için çalışacağı ümidiyle Akel Meclis Üyeleri, Bay Glafkos Kliridis'in adaylığını destekler ve bu suretle de halkın birliğinin geliştirilmesine yardım eder.

GEÇİCİ MECLİS REİSİ BAY H. HACIHAROS :
Başka aday olmadığından, Bay Glafkos Kliridis Meclis Reisliğine seçilmiştir. Bay Kliridis'i yerini almağa davet ederim.

GLAFKOS KLİRİDİS :
Sayın Üye Arkadaşlar,
Hür Kıbrıs'ın Birinci Meclisinin Reisliğini şahsıma emanet etmek suretiyle, bana vermiş olduğunuz şerefi kabul etmekle mütehassisim. Burada, hepimizin birlikte kabul ettiğimiz sorumluluğu tamamen müdrik olarak Kıbrıs Temsilciler Meclisini hür düşünce ve ifade ve insan hak ve hürriyetlerini muhafaza edecek örnek bir yer yapmamız için sizlerle çalışacağıma söz veririm.
Ümit ederim ki, işbirliğimiz, pek yakında hürriyetin nimetlerini elde etmeleri için dua ettiğimiz bütün esir insan topluluklarına bir örnek olacaktır. Anayasa hükümlerine dayanarak Bay Lellos Dimitriadis ile Bay Petros Stilyanu'yu Meclis Sekreteri; Bay Titos Fanos ile Bay Nikos Koşis'i de Meclis İdare Âmiri tâyin ederim.
""",
    ),
    4: (
        """GEÇİCİ MECLİS REİS VEKİLİ NİYAZİ MANYERA :
Başka aday olmadığından Türk Temsilcilerden Dr. Orhan Müderrisoğlu Meclis Reis Vekilliğine seçilmiştir.

DR. ORHAN MÜDERRİSOĞLU :
Anayasa hükümlerine dayanarak Meclis Türk Sekreterliğine Dr. Hasan Güvener'i ; Türk İdare Âmirliğine de Bay Necdet Hüseyin'i tâyin ederim.

MECLİS REİSİ GLAFKOS KLİRİDİS :
Meclis, Cumhurbaşkanı ve Cumhurbaşkan Muavinini kabul etmeğe hazır olup kendilerini davet eder. (Meclis huzurunda Cumhurbaşkanı Başpiskopos Makarios ve Cumhurbaşkan Muavini Ekselâns Dr. Fazıl Küçük Anayasanın 42'nci maddesi gereğince yemin ettiler: "Kıbrıs Cumhuriyetinin, Anayasasına ve buna uygun olarak yapılmış kanunlara, bağımsızlığının ve toprak bütünlüğünün korunmasına, iman ve riayet edeceğime söz veririm.") Anayasanın 76'ncı maddesi hükümleri gereğince bu toplantının sona erdiğini bildiririm. (Sona eriş saati : ö.e. 11.30.)
""",
        """GEÇİCİ MECLİS REİS VEKİLİ NİYAZİ MANYERA :
Başka aday olmadığından Türk Temsilcilerden Dr. Orhan Müderrisoğlu Meclis Reis Vekilliğine seçilmiştir.

DR. ORHAN MÜDERRİSOĞLU :
Anayasa hükümlerine dayanarak Meclis Türk Sekreterliğine Dr. Hasan Güvener'i ; Türk İdare Âmirliğine de Bay Necdet Hüseyin'i tâyin ederim.

MECLİS REİSİ GLAFKOS KLİRİDİS :
Meclis, Cumhurbaşkanı ve Cumhurbaşkan Muavinini kabul etmeğe hazır olup kendilerini davet eder. (Bunun üzerine Cumhurbaşkanı Başpiskopos Makarios ve Cumhurbaşkan Muavini Ekselâns Dr. Fazıl Küçük Meclise gelerek Anayasanın 42'nci maddesi gereğince söz verdiler: "Kıbrıs Cumhuriyetinin, Anayasasına ve buna uygun olarak yapılmış kanunlara, bağımsızlığının ve toprak bütünlüğünün korunmasına, iman ve riayet edeceğime söz veririm." Müteakiben Bakanlar refakatinde Meclis salonundan ayrıldılar.) Anayasanın 76'ncı maddesi hükümleri gereğince bu toplantının sona erdiğini bildiririm. (Sona eriş saati : ö.e. 11.30.)
""",
    ),
    5: (
        """ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ 29ης ΑΥΓΟΥΣΤΟΥ 1960
(Ὥρα Ἐνάρξεως 5 μ.μ.)
29 AĞUSTOS 1960 TARİHLİ TOPLANTI
(Başlangıç saati : ö.s. 5.00)

ΠΡΟΕΔΡΟΣ :
Συμφώνως τῶν προνοιῶν τοῦ ἄρθρου 76 (1) τοῦ Συντάγματος κηρύσσω τὴν ἔναρξιν τῆς συνεδριάσεως. Παρακαλῶ τοὺς ἐντίμους κ.κ. Γραμματεῖς νὰ σημειώσουν τὴν ὥραν τῆς ἐνάρξεως τῆς συνεδριάσεως καὶ νὰ διαπιστώσουν ἐὰν ὑπάρχῃ ἀπαρτία. (Οἱ Γραμματεῖς βεβαιοῦν ὅτι ὑπάρχει ἀπαρτία διότι παρόντες εἶναι ἅπαντες οἱ Βουλευταί).
Τὸ πρῶτον θέμα ἐπὶ τῆς ἡμερησίας διατάξεως εἶναι ἡ κατάρτισις Ἐπιτροπῆς Ἐπιλογῆς. Συμφώνως πρὸς τὰς προνοίας τοῦ ἄρθρου 73, παραγράφους 2 καὶ 3 τοῦ Συντάγματος, πρέπει νὰ ἐκλεγῇ ἐπιτροπὴ ἡ ὁποία θὰ καταρτίσῃ τὰς Κοινοβουλευτικὰς Ἐπιτροπάς. Ἡ Ἐπιτροπὴ Ἐπιλογῆς δέον νὰ ἀποτελῆται ἀπὸ 6 Ἕλληνας καὶ 2 Τούρκους. Πρόεδρος τῆς Ἐπιτροπῆς Ἐπιλογῆς εἶναι ὁ Πρόεδρος τῆς Βουλῆς καὶ Ἀντιπρόεδρος τῆς Ἐπιτροπῆς ὁ Ἀντιπρόεδρος τῆς Βουλῆς. Δύνασθε τώρα νὰ κάμετε εἰσηγήσεις ἐπιλογῆς προσώπων. Ζητεῖ τὸν λόγον τὸ ἔντιμον μέλος ἐξ Ἀμμοχώστου ὁ κ. Παῦλος Παύλου. Ἔχετε τὸν λόγον.

Π. ΠΑΥΛΟΥ :
Προτείνω τοὺς κ.κ. Αἰμίλιον Φράγκον, Γεώργιον Ἰωαννίδην, Γεώργιον Τζιρκώτην, Ἀνδρέαν Γιάγκου, Κώσταν Χριστοδουλίδην καὶ Γεώργιον Τομπάζον ὡς ἑλληνικὰ μέλη τῆς Ἐπιτροπῆς.

ΠΡΟΕΔΡΟΣ :
Ὡς μέλη τῆς Ἐπιτροπῆς Ἐπιλογῆς ὑπεδείχθησαν οἱ ἀκόλουθοι : Αἰμίλιος Φράγκος, Γεώργιος Ἰωαννίδης, Γεώργιος Τζιρκώτης, Ἀνδρέας Γιάγκου, Κώστας Χριστοδουλίδης καὶ Γεώργιος Τομπάζος.

Ε. ΠΑΠΑΪΩΑΝΝΟΥ :
Προτείνω τὸν κ. Γιάγκον Ποταμίτην.

Ü. SÜLEYMAN :
Avukat Halit Ali Rıza ile Dr. Burhan Nalbantoğlu'nu Seçme Komitesine üye teklif ediyorum.

ΠΡΟΕΔΡΟΣ :
Οἱ δύο προταθέντες ὑπὸ τῆς Τουρκικῆς Κοινοβουλευτικῆς ὁμάδος θεωροῦνται ὡς ἐκλεγέντες, ἐκτὸς ἐὰν ὑπάρχουν ἄλλαι προτάσεις. Κατὰ τὰς εἰσηγήσεις τῶν Ἑλλήνων Βουλευτῶν ὑπάρχουν ἑπτὰ ὑποψήφιοι. Ἐὰν οἱ προτείναντες τὸν κ. Ποταμίτην ἐπιμένουν εἰς τὴν πρότασίν των τότε θὰ τεθῇ τὸ ζήτημα εἰς ψηφοφορίαν.

Ε. ΠΑΠΑΪΩΑΝΝΟΥ :
Ἐπιμένω εἰς τὴν πρότασίν μου διότι νομίζω ὅτι αὐτὸ εἶναι τὸ ὀρθόν.

ΠΡΟΕΔΡΟΣ :
Θέλετε νὰ ἀντιληφθῶ μὲ αὐτό, ὅτι ἐπιθυμεῖτε νὰ θέσω τὸ ζήτημα εἰς ψηφοφορίαν;

Ε. ΠΑΠΑΪΩΑΝΝΟΥ :
Μάλιστα. Ἐκτὸς ἐὰν ὁρισθῇ ἄλλως.

ΠΡΟΕΔΡΟΣ :
Δεδομένου ὅτι ὑπάρχουν ἑπτὰ ὑποψήφιοι δι' ἓξ θέσεις, τὸ ζήτημα τίθεται εἰς ψηφοφορίαν. Ἐπὶ τοῦ θέματος αὐτοῦ θὰ ψηφίσουν μόνον οἱ Ἕλληνες Βουλευταί. Ἡ ψηφοφορία δὲν θὰ εἶναι μυστική. Καλῶ ἐκείνους οἱ ὁποῖοι ὑποστηρίζουν τὴν ὑποψηφιότητα τῶν προταθέντων ὑπὸ τοῦ κ. Παύλου Παυλάκη ἐξ Ἀμμοχώστου, νὰ ὑψώσουν τὴν δεξιὰν χεῖρα. Παρακαλῶ τοὺς Γραμματεῖς νὰ σημειώσουν τὸ ἀποτέλεσμα. Παρακαλῶ ἐκείνους, οἱ ὁποῖοι ὑποστηρίζουν τὴν ὑποψηφιότητα τοῦ κ. Ποταμίτη, νὰ ὑψώσουν τὴν δεξιὰν χεῖρα. Ποῖον εἶναι τὸ ἀποτέλεσμα τῆς ψηφοφορίας; Ἐξελέγησαν οἱ κ.κ. Αἰμίλιος Φράγκος, Γεώργιος Ἰωαννίδης, Γεώργιος Τζιρκώτης, Ἀνδρέας Γιάγκου, Κώστας Χριστοδουλίδης καὶ Γεώργιος Τομπάζος, ψηφισθέντες ὑπὸ 28 Βουλευτῶν. Ὁ κ. Ποταμίτης ἔλαβε μόνον 4 ψήφους.
Τὸ δεύτερον θέμα ἐπὶ τῆς ἡμερησίας διατάξεως εἶναι ὁ καθορισμὸς ἡμερομηνίας πρὸς πλήρωσιν τῶν βουλευτικῶν ἑδρῶν, αἱ ὁποῖαι ἐκενώθησαν λόγῳ τοῦ ὅτι εἷς Ἕλλην καὶ τρεῖς Τοῦρκοι βουλευταὶ ἔχουσι διορισθῇ Ὑπουργοί. Ὁ κ. Χαλὶτ Ἀλῆ Ριζᾶ ἔχει τὸν λόγον.

H. A. RIZA :
Sayın Meclis Reisi, Seçme Komitesi Elen Üyelerinin sadece Elen Üyeler tarafından seçileceği hakkında bir beyanat yapıldı. Halbuki Anayasanın 73'üncü maddesinin 2'nci fıkrası, Seçme Komitesine seçilecek Elen Üyelerin, Elen Üyeler arasından seçileceğini kaydediyor tarafından değil. Her ne kadar Türk Grubu bu hususta müstenkif kalmağı tercih ediyorsa da, bu hususun açıklanmasını rica ediyorum.
""",
        """29 AĞUSTOS 1960 TARİHLİ TOPLANTI
(Başlangıç saati : ö.s. 5.00)
GÜNDEM: 1. Seçme Komitesinin kuruluşu. 2. İnhilâl eden Temsilciliklerin doldurulması için yapılacak seçimlerin tarihinin tesbiti. 3. Meclis sözlü soruları için gün ve sürenin tesbiti.

BAŞKAN :
Anayasanın 76(1) maddesi hükümleri uyarınca oturumu açıyorum. Sayın Kâtiplerden oturumun başlangıç saatini kaydetmelerini ve toplantı yeter sayısı (nisap) bulunup bulunmadığını tespit etmelerini rica ederim. (Kâtipler bütün milletvekillerinin hazır bulunması nedeniyle yeter sayının mevcut olduğunu doğrularlar.)
Gündemin ilk maddesi Seçme Komitesinin kurulmasıdır. Anayasanın 73. maddesinin 2. ve 3. fıkraları uyarınca Meclis komitelerini oluşturacak bir komitenin seçilmesi gerekmektedir. Seçme Komitesi 6 Rum ve 2 Türk üyeden oluşmalıdır. Seçme Komitesinin Başkanı Meclis Başkanı, Başkan Yardımcısı ise Meclis Başkan Yardımcısıdır. Şimdi aday önerilerinizi sunabilirsiniz. Mağusa'nın sayın üyesi Bay Pavlos Pavlu söz istiyor. Buyurunuz.

P. PAVLU :
Komitenin Rum üyeleri olarak Sayın Aimilios Frangos, Georgios İoannidis, Georgios Tzirkotis, Andreas Yiangou, Kostas Hristodulidis ve Georgios Tombazos'u öneriyorum.

BAŞKAN :
Seçme Komitesi üyeliğine şu isimler önerilmiştir: Aimilios Frangos, Georgios İoannidis, Georgios Tzirkotis, Andreas Yiangou, Kostas Hristodulidis ve Georgios Tombazos.

E. PAPAYUANNU :
Sayın Yangos Potamitis'i öneriyorum.

Ü. SÜLEYMAN :
Avukat Halit Ali Rıza ile Dr. Burhan Nalbantoğlu'nu Seçme Komitesine üye teklif ediyorum.

BAŞKAN :
Türk Parlamento Grubu tarafından önerilen iki aday, başka bir öneri olmadığı takdirde seçilmiş sayılırlar. Rum milletvekillerinin önerilerine göre ise yedi aday bulunmaktadır. Bay Potamitis'i önerenler önerilerinde ısrar ederlerse konu oylamaya sunulacaktır.

E. PAPAYUANNU :
Önerimde ısrar ediyorum çünkü bunun doğru olduğuna inanıyorum.

BAŞKAN :
Bununla konuyu oylamaya sunmamı istediğinizi mi anlamalıyım?

E. PAPAYUANNU :
Evet. Aksi kararlaştırılmadıkça.

BAŞKAN :
Altı üyelik için yedi aday bulunduğundan konu oylamaya sunulmaktadır. Bu konuda yalnızca Rum milletvekilleri oy kullanacaktır. Oylama gizli olmayacaktır. Mağusa milletvekili Bay Pavlos Pavlakis tarafından önerilen adayları destekleyenlerin sağ ellerini kaldırmalarını rica ediyorum. Kâtiplerden sonucu kaydetmelerini rica ederim. Bay Potamitis'in adaylığını destekleyenlerin sağ ellerini kaldırmalarını rica ediyorum. Oylama sonucu nedir? 28 milletvekilinin oyuyla Sayın Aimilios Frangos, Georgios İoannidis, Georgios Tzirkotis, Andreas Yiangou, Kostas Hristodulidis ve Georgios Tombazos seçilmişlerdir. Bay Potamitis yalnızca 4 oy almıştır.
Gündemin ikinci maddesi, bir Rum ve üç Türk milletvekilinin Bakan olarak atanması nedeniyle boşalan milletvekilliği koltuklarının doldurulması için yapılacak ara seçimlerin tarihinin belirlenmesidir. Bay Halit Ali Rıza söz almıştır.

H. A. RIZA :
Sayın Meclis Reisi, Seçme Komitesi Elen Üyelerinin sadece Elen Üyeler tarafından seçileceği hakkında bir beyanat yapıldı. Halbuki Anayasanın 73'üncü maddesinin 2'nci fıkrası, Seçme Komitesine seçilecek Elen Üyelerin, Elen Üyeler arasından seçileceğini kaydediyor tarafından değil. Her ne kadar Türk Grubu bu hususta müstenkif kalmağı tercih ediyorsa da, bu hususun açıklanmasını rica ediyorum.
""",
    ),
    6: (
        """ΠΡΟΕΔΡΟΣ :
Θὰ ἤθελα νὰ ἀπαντήσω εἰς τὸν ἔντιμον Βουλευτὴν κ. Ἀλῆ Ριζᾶ ὅτι τὸ Ἑλληνικὸν κείμενον, παράγραφος 2, λέγει τὸ ἀντίθετον αὐτοῦ τὸ ὁποῖον ἰσχυρίζεται. «Ἐξ ὧν ἓξ ἐκ τῶν ἐκλεγέντων ὑπὸ τῆς Ἑλληνικῆς Κοινότητος καὶ δύο ἐκ τῆς Τουρκικῆς.»

H. A. RIZA :
Sayın Meclis Reisinin cevabından dolayı çok teşekkür ederim. Lâkin muhakkak ki, Sayın Meclis Reisi, Anayasanın Elence ve Türkçe metinleri arasında bir fark olduğunda, o hususta parafe edilen İngilizce metnin muteber olacağını biliyor ve İngilizce metnin 73'üncü maddesinin 2'nci fıkrasında ilgili kısım şöyle diyor :— "Six from amongst the Representatives elected by the Greek Community and two from amongst the Representatives elected by the Turkish Community." Buradaki "elected by the Turkish Community" ve "elected by the Greek Community" tabirleri, arasından seçim yapılacak Temsilcileri murad ediyor ve seçecek üyelere şamil değildir.

ΠΡΟΕΔΡΟΣ :
Εὐχαριστῶ τὸ ἔντιμον μέλος διὰ τὴν βοήθειαν τὴν ὁποίαν μοῦ παρέσχεν ἐπὶ τοῦ θέματος ὅτι, ἐν περιπτώσει διαφορᾶς μεταξὺ Ἑλληνικοῦ καὶ Τουρκικοῦ κειμένου, ἡ διαφορὰ λύεται βάσει τοῦ Ἀγγλικοῦ κειμένου. Ἀμφιβάλλω ὅμως ἐὰν ἡ ἐφαρμογὴ τῆς διατάξεως ταύτης ἐπαφίεται εἰς τὸν Πρόεδρον ἢ τὸν Ἀντιπρόεδρον τῆς Βουλῆς, καὶ δὲν περιορίζεται μόνον εἰς τὴν ἑρμηνείαν τὴν ὁποίαν θὰ δώσῃ τὸ Συνταγματικὸν Δικαστήριον. Ἐν πάσῃ περιπτώσει δὲν ἔχει ἀκόμη ἀποδειχθῇ ὅτι ὑπάρχει διαφορὰ μεταξὺ τοῦ Ἑλληνικοῦ καὶ τοῦ Τουρκικοῦ κειμένου. Μέχρι τῆς στιγμῆς μᾶς ὑπεδείχθη ὅτι ὑπάρχει διαφορὰ μεταξὺ τοῦ Ἑλληνικοῦ καὶ τοῦ Ἀγγλικοῦ κειμένου. Διὰ νὰ δυνηθῶμεν νὰ ἀναφερθῶμεν εἰς τὸ Ἀγγλικὸν κείμενον θὰ πρέπει πρῶτον νὰ ἀποδειχθῇ ὅτι ὑπάρχει διαφορὰ μεταξὺ Ἑλληνικοῦ καὶ Τουρκικοῦ κειμένου, καὶ οὐχὶ μεταξὺ Ἑλληνικοῦ καὶ Ἀγγλικοῦ κειμένου.

Χ. ΔΗΜΗΤΡΙΑΔΗΣ :
Νὰ μοῦ ἐπιτρέψετε νὰ συμφωνήσω μὲ τὴν ἄποψιν τοῦ ἐντίμου Μέλους τῆς Βουλῆς κ. Χαλὶτ Ἀλῆ Ριζᾶ, ὅτι τὸ ἄρθρον 73 (2) ὅπως εἶναι διατυπωμένον Ἑλληνιστὶ καὶ οὐχὶ Ἀγγλιστί, δὲν μᾶς ἐξαναγκάζει εἰς τὴν περίπτωσιν αὐτὴν νὰ ἀνατρέξωμεν εἰς τὸ Ἀγγλικὸν κείμενον. Τὸ κείμενον ὅπως εἶναι Ἑλληνιστὶ συμφωνεῖ μὲ τὴν ἄποψιν τὴν ὁποίαν ἐξέθεσε καὶ ὁ κ. Ἀλῆ Ριζᾶ.
Τὸ ἄρθρον 73 (2) λέγει ὅτι καταρτίζεται Ἐπιτροπὴ Ἐπιλογῆς, ἀποτελουμένη ἐκ τοῦ Προέδρου τῆς Βουλῆς τῶν Ἀντιπροσώπων ὡς Προέδρου, τοῦ Ἀντιπροέδρου αὐτῆς ὡς Ἀντιπροέδρου, καὶ ὀκτὼ ἑτέρων ἐκλεγομένων ὑπὸ τῆς Βουλῆς τῶν Ἀντιπροσώπων Βουλευτῶν, ἓξ ὧν ἓξ ἐκ τῶν ἐκλεγέντων ὑπὸ τῆς Ἑλληνικῆς κοινότητος καὶ 2 ἐκ τῶν ἐκλεγέντων ὑπὸ τῆς Τουρκικῆς κοινότητος—ἐννοεῖ τὸ σύνολον ἐδῶ, καὶ Ἑλληνικὴ κοινότης δὲν σημαίνει τὰ Ἑλληνικὰ μέλη τῆς Βουλῆς—ἐννοεῖ ὅτι οἱ ἓξ πρέπει νὰ εἶναι εἰς τὴν Βουλὴν παρόντες, ἐκλεγμένοι ὑπὸ τῆς Ἑλληνικῆς κοινότητος, καὶ δύο ἐξ ἐκείνων οἵτινες εἶναι εἰς τὴν Βουλὴν παρόντες, ἐκλεγμένοι ὑπὸ τῆς Τουρκικῆς κοινότητος. Μὲ ἄλλα λόγια 6 Ἕλληνες καὶ 2 Τοῦρκοι. Εὐσεβάστως εἰσηγοῦμαι ὅτι αὐτὴ εἶναι ἡ ὀρθὴ ἑρμηνεία καὶ νὰ μοῦ ἐπιτρέψητε νὰ διαφωνήσω μὲ τὴν ἄποψιν τοῦ ἐντίμου κ. Προέδρου.

Φ. ΠΑΡΑΣΚΕΥΑΪΔΗΣ :
Ἐὰν ὁ Ἔντιμος Τοῦρκος Βουλευτὴς εἶναι τῆς ἀπόψεως ὅτι πρέπει συνολικῶς ἅπαντα τὰ μέλη τῆς Ἐπιτροπῆς νὰ ἐκλεγοῦν συνολικῶς ἀπὸ ὅλους τοὺς Βουλευτάς, τότε ἡμεῖς δὲν ἔχομεν καμμίαν ἀντίρρησιν νὰ ἐκλεγοῦν τὰ μέλη τῆς Ἐπιτροπῆς ἀπὸ ὅλα τὰ μέλη τῆς Βουλῆς.

ΠΡΟΕΔΡΟΣ :
Ὁ κ. Μεταφραστὴς παρέλειψε νὰ μεταφράσῃ τὴν ὁμιλίαν τοῦ κ. Χρύση Δημητριάδη. Ὁ κ. Δημητριάδης, ἐν συντομίᾳ, συνεφώνησε μὲ τὴν ἄποψιν τοῦ κ. Χαλὶτ Ἀλῆ Ριζᾶ ὅτι τὰ μέλη τῆς Ἐπιτροπῆς ἐκλέγονται ὑπὸ τῶν Ἑλλήνων καὶ Τούρκων Βουλευτῶν ἀπὸ κοινοῦ, καὶ οὐχὶ κεχωρισμένως. Τὸ ἔντιμον μέλος ἐκ Πάφου κ. Σιβιτανίδης.

Π. ΣΙΒΙΤΑΝΙΔΗΣ :
Διαφωνῶ ὡς πρὸς τὴν ἑρμηνείαν τὴν ὁποίαν δίδει ὁ κ. Δημητριάδης εἰς τὸ ἄρθρον 73 παράγραφος 2. Οὐδεμία οὐσιώδης διαφορὰ ὑπάρχει εἰς τὰ κείμενα—ὅσον ἀφορᾷ τὸ θέμα τὸ ὁποῖον συζητοῦμεν—ἀλλὰ εἰς τὴν ἑρμηνείαν, νομίζω δὲ ὅτι ὀρθῶς ἡρμηνεύθη τὸ Ἑλληνικὸν κείμενον, δηλαδὴ ὅτι οἱ Ἕλληνες ἐκλέγονται ὑπὸ τῶν Ἑλλήνων Βουλευτῶν καὶ οἱ δύο Τοῦρκοι ὑπὸ τῶν Τούρκων Βουλευτῶν, καθότι ἡ φρασεολογία τῆς τελευταίας παραγράφου ἔχει ὡς ἑξῆς : «ἓξ ὧν ἓξ ἐκ τῶν ἐκλεγέντων ὑπὸ τῆς Ἑλληνικῆς κοινότητος», ἐνῷ ἐὰν ἦτο ἄλλως πως θὰ ἔλεγεν, «ἓξ ἐκ τῶν ἐκλεγέντων ἐκ τῆς Ἑλληνικῆς κοινότητος».

H. A. RIZA :
Sayın Meclis Reisinin benim maruzatıma verdiği cevapta bir yanlış anlayış olduğu için onu evvelâ tasrih etmek istiyorum. Ben, Türkçe metnin, bu gece Mecliste takip edilen usule istinaden farklı olduğunu söylemiştim. Sayın Meclis Reisi ise Elence metnin tatbik etmek istediği şekilde olduğunu söyleyince, otomatik olarak Türkçe ve Elence metinler arasında bir fark olduğu anlaşılıyor. Çünkü Türkçe metinde, sarahaten, Komite üyelerinin bütün Temsilciler tarafından seçileceğini görüyorum ve bir Elen Üyeden memnuniyetle öğreniyorum ki, Elence metinde de vaziyet aynidir.

ΠΡΟΕΔΡΟΣ :
Ὁ κ. Χαλὶτ βεβαιοῖ ὅτι τὸ Τουρκικὸν κείμενον εἶναι σαφές, καὶ ὅτι τὸ κείμενον αὐτὸ προβλέπει ὅτι οἱ Ἕλληνες ἐκλέγονται καὶ ὑπὸ τῶν Τούρκων καὶ οἱ Τοῦρκοι ἐκλέγονται καὶ ὑπὸ τῶν Ἑλλήνων.
""",
        """BAŞKAN :
Sayın milletvekili Bay Ali Rıza'ya, Yunanca metnin 2. fıkrasının onun iddia ettiğinin aksini söylediğini bildirmek isterim: "Bunlardan altısı Rum Cemaati tarafından seçilenlerden, ikisi Türk Cemaatinden."

H. A. RIZA :
Sayın Meclis Reisinin cevabından dolayı çok teşekkür ederim. Lâkin muhakkak ki, Sayın Meclis Reisi, Anayasanın Elence ve Türkçe metinleri arasında bir fark olduğunda, o hususta parafe edilen İngilizce metnin muteber olacağını biliyor ve İngilizce metnin 73'üncü maddesinin 2'nci fıkrasında ilgili kısım şöyle diyor :— "Six from amongst the Representatives elected by the Greek Community and two from amongst the Representatives elected by the Turkish Community." Buradaki "elected by the Turkish Community" ve "elected by the Greek Community" tabirleri, arasından seçim yapılacak Temsilcileri murad ediyor ve seçecek üyelere şamil değildir.

BAŞKAN :
Yunanca ve Türkçe metinler arasında fark olması hâlinde meselenin İngilizce metne göre çözüleceği hususunda bana yardımcı olduğu için sayın üyeye teşekkür ederim. Ancak bu hükmün uygulanmasının Meclis Başkanına veya Başkan Yardımcısına mı bırakıldığı, yoksa yalnızca Yüksek Anayasa Mahkemesinin vereceği yorumla mı sınırlı olduğu konusunda tereddütlüyüm. Her hâlükârda, Yunanca ile Türkçe metin arasında bir fark bulunduğu henüz kanıtlanmış değildir. Şu ana kadar bize yalnızca Yunanca metin ile İngilizce metin arasında bir fark olduğu gösterildi. İngilizce metne başvurabilmemiz için öncelikle Yunanca ve İngilizce metin arasında değil, Yunanca ile Türkçe metin arasında fark olduğunun ortaya konması gerekir.

H. DİMİTRİADİS :
Sayın milletvekili Bay Halit Ali Rıza'nın görüşüne katılmama müsaade ediniz; 73(2). maddenin İngilizce değil Yunanca yazılışı dahi bu durumda İngilizce metne başvurmamızı gerektirmiyor. Yunanca metin olduğu hâliyle Bay Ali Rıza'nın ortaya koyduğu görüşle uyuşmaktadır.
73(2). madde, Meclis Başkanının başkanlığında, Meclis Başkan Yardımcısının başkan yardımcılığında ve Temsilciler Meclisi tarafından seçilecek sekiz diğer milletvekilinden oluşan bir Seçme Komitesi kurulacağını söyler; bunlardan altısı Rum Cemaati tarafından seçilenler arasından, ikisi de Türk Cemaati tarafından seçilenler arasından olacaktır — burada bütün kast edilmektedir ve "Rum Cemaati" Meclisteki Rum üyeler anlamına gelmez; yani altısının Rum Cemaatince seçilmiş Meclis üyeleri, ikisinin de Türk Cemaatince seçilmiş Meclis üyeleri olması gerektiğini ifade eder. Başka bir deyişle 6 Rum ve 2 Türk. Saygıyla arz ederim ki doğru yorum budur ve Sayın Başkanın görüşüne katılmamama izin vermenizi rica ederim.

F. PARASKEVAİDİS :
Eğer Sayın Türk Milletvekili, Komitenin bütün üyelerinin topluca bütün milletvekilleri tarafından seçilmesi gerektiği görüşündeyse, o hâlde bizlerin de Komite üyelerinin tüm Meclis üyelerince seçilmesine hiçbir itirazımız yoktur.

BAŞKAN :
Sayın Tercüman, Bay Hrisis Dimitriadis'in konuşmasını tercüme etmeyi atladı. Bay Dimitriadis özetle Bay Halit Ali Rıza'nın görüşüne katılarak, Komite üyelerinin Rum ve Türk milletvekilleri tarafından ayrı ayrı değil, ortaklaşa seçileceğini söyledi. Baf'ın sayın üyesi Bay Sivitanidis buyurunuz.

P. SİVİTANİDİS :
Bay Dimitriadis'in 73. maddenin 2. fıkrasına getirdiği yoruma katılmıyorum. Tartıştığımız konu bakımından metinler arasında esaslı bir fark yoktur; mesele yorumdadır ve bence Yunanca metin doğru yorumlanmıştır, yani Rum üyeler Rum milletvekillerince, iki Türk üye de Türk milletvekillerince seçilir; zira son fıkranın ifadesi "Rum Cemaati tarafından seçilenlerden altısı" şeklindedir, aksi olsaydı "Rum Cemaatinden seçilenlerden altısı" denirdi.

H. A. RIZA :
Sayın Meclis Reisinin benim maruzatıma verdiği cevapta bir yanlış anlayış olduğu için onu evvelâ tasrih etmek istiyorum. Ben, Türkçe metnin, bu gece Mecliste takip edilen usule istinaden farklı olduğunu söylemiştim. Sayın Meclis Reisi ise Elence metnin tatbik etmek istediği şekilde olduğunu söyleyince, otomatik olarak Türkçe ve Elence metinler arasında bir fark olduğu anlaşılıyor. Çünkü Türkçe metinde, sarahaten, Komite üyelerinin bütün Temsilciler tarafından seçileceğini görüyorum ve bir Elen Üyeden memnuniyetle öğreniyorum ki, Elence metinde de vaziyet aynidir.

BAŞKAN :
Bay Halit, Türkçe metnin açık olduğunu ve bu metnin Rum üyelerin Türklerce de, Türk üyelerin de Rumlarca seçilmesini öngördüğünü teyit ediyor.
""",
    ),
    7: (
        """H. A. RIZA :
Şunu sarahaten arzetmek istiyorum ki, Seçme Komitesinin gerek Elen ve gerekse Türk üyeleri bütün Meclis tarafından seçilir.

ΠΡΟΕΔΡΟΣ :
Ὑπὸ ὁλοκλήρου τῆς Βουλῆς, αὐτὴ εἶναι ἡ σαφὴς διατύπωσις τοῦ Τουρκικοῦ κειμένου;

H. A. RIZA :
Benim anlayışım böyledir.

ΠΡΟΕΔΡΟΣ :
Θὰ ἤθελα μίαν διευκρίνισιν διὰ νὰ κάμωμεν τὸ ἑπόμενον βῆμα κατὰ πόσον θὰ ἀναφερθῶμεν εἰς τὸ Ἀγγλικὸν κείμενον ἢ ὄχι. Εἶναι ὅπως τὸ ἀντιλαμβάνεται ἢ εἶναι σαφὴς ἡ διατύπωσις; Δηλαδὴ θὰ ἤθελα νὰ ἐρωτήσω τὸν κ. Χαλίτ : Εἶναι δυνατὸν νὰ ἑρμηνευθῇ τὸ Τουρκικὸν κείμενον κατὰ δύο τρόπους, καὶ ὁ κ. Χαλὶτ ἀντιλαμβάνεται ὅτι πρέπει νὰ ἑρμηνευθῇ κατὰ τὸν ἕνα ἐκ τῶν δύο τρόπων ἢ εἶναι σαφές;

H. A. RIZA :
Memnuniyetle öğreniyorum ki burada, Meclisteki Türk Grubundaki bütün üye arkadaşlar da benim anladığım şekilde anlıyor ve bu suretle Türkçe metnin sarih olduğu kanaatine varıyoruz.

ΠΡΟΕΔΡΟΣ :
Ἐφ' ὅσον ὅλα τὰ μέλη τῆς Τουρκικῆς κοινοβουλευτικῆς ὁμάδος εἰς τὴν Βουλὴν δίδουν τὴν ἰδίαν ἑρμηνείαν εἰς τὸ Τουρκικὸν κείμενον, καὶ ἐφ' ὅσον προφανῶς ὑπάρχει διαφορὰ μεταξὺ τοῦ Ἑλληνικοῦ καὶ τοῦ Τουρκικοῦ κειμένου, πρὸς διασαφήνισιν τῆς διαφορᾶς αὐτῆς δυνάμεθα νὰ ἀναφερθῶμεν εἰς τὸ Ἀγγλικὸν κείμενον. Θὰ ἐπανέλθω εἰς αὐτὸ τὸ θέμα. Μέχρις ὅτου γίνουν οἱ κανονισμοὶ τῆς Βουλῆς θὰ ἀναφερόμεθα εἰς τὸ Ἀγγλικὸν κείμενον τοῦ Συντάγματος.

Β. ΛΥΣΣΑΡΙΔΗΣ :
Θὰ ἤθελα προτοῦ ἀναφερθῶ εἰς τὸ Ἀγγλικὸν κείμενον, νὰ ὁμιλήσω ἐπὶ τοῦ Ἑλληνικοῦ. Νομίζω ὅτι δὲν ὑπάρχει διαφορὰ μεταξὺ Ἑλληνικοῦ καὶ Τουρκικοῦ κειμένου. Ἑπομένως νομίζω ὅτι θὰ πρέπει νὰ ἀποφευχθῇ ἡ προσφυγὴ εἰς τὸ Ἀγγλικὸν κείμενον διὰ νὰ ἀποφευχθῇ μία ἴσως πρόωρος πρᾶξις τῆς Βουλῆς περὶ ἀναφορᾶς εἰς τὸ Ἀγγλικὸν κείμενον. Εἰς τὸ Σύνταγμα ἀναφέρεται ὅτι πρέπει νὰ ἐκλέγωνται ὑπὸ τῆς Βουλῆς τῶν Ἀντιπροσώπων ὡς συνόλου, μὲ τὸν μόνον περιορισμὸν ὅτι τὰ 6 μέλη πρέπει νὰ ἐκλέγωνται μεταξὺ ἐκείνων ἐκ τῶν μελῶν τὰ ὁποῖα παρακάθηνται εἰς τὴν Βουλήν, ὡς ἐκλεγέντα ὑπὸ τῆς Ἑλληνικῆς κοινότητος ὑπὸ τῶν Ἑλλήνων ψηφοφόρων, δηλαδὴ ἓξ Ἑλληνικὰ μέλη τῆς Βουλῆς.

ΠΡΟΕΔΡΟΣ :
Εἰς τὴν νομικὴν ὅμως ἑρμηνείαν θὰ ἦτο παράλογον νὰ ἰσχυρισθῇ κανεὶς ὅτι τὰ δύο Τουρκικὰ μέλη θὰ ἐκλέγωνται ὑπὸ τῶν Ἑλλήνων Βουλευτῶν, δεδομένου ὅτι τίθεται ὁ περιορισμὸς τὰ δύο μέλη νὰ εἶναι Τοῦρκοι διότι ἐν τοιαύτῃ περιπτώσει μὲ τὴν Ἑλληνικὴν πλειοψηφίαν ἡ ὁποία ὑπάρχει, ἐὰν αὐτὴ ἦτο ἡ πραγματικὴ ἔννοια τοῦ ἄρθρου, θὰ ἐψηφίζοντο ἐκ τῶν Τούρκων ἐκεῖνοι τοὺς ὁποίους ἤθελον οἱ Ἕλληνες καὶ οὐχὶ ἐκεῖνοι τοὺς ὁποίους ἤθελον οἱ Τοῦρκοι.

ΕΛΛΗΝ ΒΟΥΛΕΥΤΗΣ :
Νομίζω ὅτι δὲν ἔχετε τὸ δικαίωμα νὰ κάνετε διαχωρισμὸν μεταξὺ Ἑλλήνων καὶ Τούρκων, καὶ ἐφ' ὅσον τὸ Σύνταγμα μᾶς δίδει αὐτὸ τὸ δικαίωμα, ὁ μόνος περιορισμός... ἐξακολουθῶ νὰ πιστεύω ὅτι εἶναι κακὸς ὁ διαχωρισμὸς ὅπως γίνεται τώρα.

ΠΡΟΕΔΡΟΣ :
Δὲν ὁμιλῶ περὶ διαχωρισμοῦ, ὁμιλῶ περὶ νομικῆς ἑρμηνείας. Ὅταν ὑπάρχῃ μία διάταξις ἡ ὁποία ὁρίζει ὅτι δύο μέλη πρέπει νὰ εἶναι ἐκ τῆς Τουρκικῆς κοινότητος καὶ ἓξ ἐκ τῆς Ἑλληνικῆς κοινότητος, ἡ κανονικὴ συνέπεια μιᾶς τοιαύτης προνοίας εἶναι ὅτι τὰ μὲν Ἑλληνικὰ μέλη ἐκλέγονται ὑπὸ τῶν Ἑλλήνων, τὰ δὲ Τουρκικὰ μέλη ἐκλέγονται ὑπὸ τῶν Τούρκων, ἐκτὸς ἐὰν ὑπάρχῃ σαφὴς διάταξις ἡ ὁποία ὁρίζει ὅτι πρέπει νὰ ἐκλέγωνται ὑφ' ὁλοκλήρου τῆς Βουλῆς. Εἰς τὴν περίπτωσιν αὐτὴν κατὰ τὴν γνώμην μου τὸ Ἑλληνικὸν κείμενον ἔχει τὴν ἀσάφειαν ὅτι λέγει «ὑπὸ» καὶ ὄχι «ἐκ». Ἐν τοιαύτῃ περιπτώσει τὸ ζήτημα ἐκτίθεται σαφῶς ἐὰν ἀναφερθῶμεν εἰς τὸ Ἀγγλικὸν κείμενον· ἤδη ἐξεφράσθησαν ἀπόψεις ἑκατέρωθεν καὶ ὑπὸ τῆς Ἑλληνικῆς ὁμάδος ὑποστηρίζουσαι δύο ἑρμηνείας ἀντίκειται πρὸς τὸ Τουρκικὸν κείμενον. Ἐν τοιαύτῃ περιπτώσει ὑπάρχει ἡ διάταξις ἡ ὁποία μᾶς δίδει τὸ δικαίωμα νὰ ἀναφερθῶμεν εἰς τὸ Ἀγγλικὸν κείμενον, καὶ ἀναφερόμενοι εἰς τοῦτο νὰ διασαφηνίσωμεν τὸ ζήτημα.

Ü. SÜLEYMAN :
Sayın Başkanın müsaadeleriyle arzedeyim. Konuşulanların maalesef tercüme edilmediğini görüyorum. Biz konuşulanlardan birşey anlamadığımızdan, mümkünse daha yavaş konuşulsun ve tercümana fırsat verilsin ve biz de ne konuşulduğunu takip edip görüşlerimizi söyleyebilelim.

ΠΡΟΕΔΡΟΣ :
Ἐλήφθη ὑπὸ σημείωσιν ἡ παρατήρησις τοῦ κ. Οὐμὶτ Σουλεϊμάν. Παρακαλῶ τὰ ἔντιμα Μέλη νὰ ὁμιλοῦν βραδύτερον διὰ νὰ δύναται ὁ μεταφραστὴς νὰ ἀποδίδῃ τὸ περιεχόμενον τῶν ἀγορεύσεων.

B. NALBANTOĞLU :
Ben daha ileri giderek, tercüme edilmeyen konuşmaların zabıtlara girmemesini teklif edeceğim.

ΠΡΟΕΔΡΟΣ :
Ποῖα εἶναι τὰ μέρη τῶν ἀγορεύσεων τὰ ὁποῖα ἰσχυρίζεσθε ὅτι δὲν μετεφράσθησαν;

Ü. SÜLEYMAN :
Sayın Başkanın ve Dr. Lissaridis'in konuşmaları tercüme edilmedi. Maalesef bu konuşmaları hiç de takip edemedik.
""",
        """H. A. RIZA :
Şunu sarahaten arzetmek istiyorum ki, Seçme Komitesinin gerek Elen ve gerekse Türk üyeleri bütün Meclis tarafından seçilir.

BAŞKAN :
Bütün Meclis tarafından mı — Türkçe metnin açık ifadesi bu mudur?

H. A. RIZA :
Benim anlayışım böyledir.

BAŞKAN :
Bir sonraki adımı atabilmek ve İngilizce metne başvurup başvurmayacağımıza karar verebilmek için bir açıklığa ihtiyacım var. Bu onun kendi anlayışı mıdır, yoksa ifade gerçekten açık mıdır? Yani Bay Halit'e sormak isterim: Türkçe metin iki farklı şekilde yorumlanabilir mi ve Bay Halit bu iki yorumdan birini mi benimsiyor, yoksa metin tamamen açık mıdır?

H. A. RIZA :
Memnuniyetle öğreniyorum ki burada, Meclisteki Türk Grubundaki bütün üye arkadaşlar da benim anladığım şekilde anlıyor ve bu suretle Türkçe metnin sarih olduğu kanaatine varıyoruz.

BAŞKAN :
Meclisteki Türk Parlamento Grubunun bütün üyeleri Türkçe metne aynı yorumu verdiğine ve Yunanca ile Türkçe metin arasında açıkça bir fark bulunduğuna göre, bu farkı açıklığa kavuşturmak için İngilizce metne başvurabiliriz. Bu konuya döneceğim. Meclis İç Tüzüğü hazırlanana kadar Anayasanın İngilizce metnine başvuracağız.

V. LİSSARİDİS :
İngilizce metne başvurmadan önce Yunanca metin üzerine konuşmak isterim. Bence Yunanca ve Türkçe metinler arasında bir fark yoktur. Dolayısıyla, Meclisin belki de zamansız biçimde İngilizce metne başvurma eyleminden kaçınmak için İngilizce metne müracaat edilmemelidir. Anayasada üyelerin bir bütün olarak Temsilciler Meclisi tarafından seçileceği belirtilmektedir; tek sınırlama, 6 üyenin Rum seçmenlerce seçilip Mecliste bulunan Rum cemaati üyeleri arasından, yani 6 Rum milletvekilinden seçilmesidir.

BAŞKAN :
Ancak hukuki yorumda, iki Türk üyenin Rum milletvekillerince seçileceğini savunmak mantıksız olurdu; zira iki üyenin Türk olması sınırlaması konulmuştur. Çünkü maddenin gerçek anlamı bu olsaydı, mevcut Rum çoğunluğu ile Türkler arasından Türklerin istediği değil, Rumların istediği kişiler seçilmiş olurdu.

RUM MİLLETVEKİLİ :
Rumlar ve Türkler arasında ayrım yapmaya hakkınız olmadığını düşünüyorum; Anayasa bize bu hakkı verdiği sürece tek sınırlama budur... Şu an yapıldığı biçimiyle bu ayrımın kötü olduğuna inanmaya devam ediyorum.

BAŞKAN :
Ayrımdan söz etmiyorum, hukuki yorumdan söz ediyorum. İki üyenin Türk cemaatinden ve altı üyenin Rum cemaatinden olmasını öngören bir hüküm bulunduğunda, bu hükmün olağan sonucu — bütün Meclisçe seçilmelerini öngören açık bir hüküm olmadıkça — Rum üyelerin Rumlarca, Türk üyelerin de Türklerce seçilmesidir. Bu durumda benim görüşüme göre Yunanca metinde "arasından" yerine "tarafından" denmesi bir belirsizlik yaratmaktadır. Böyle bir durumda mesele İngilizce metne başvurularak açıklığa kavuşur; zaten Rum grubundan da Türkçe metinle çelişen iki farklı yorum dile getirildi. Bu hâlde bize İngilizce metne başvurma hakkı veren hüküm geçerlidir ve buna başvurarak meseleyi netleştirelim.

Ü. SÜLEYMAN :
Sayın Başkanın müsaadeleriyle arzedeyim. Konuşulanların maalesef tercüme edilmediğini görüyorum. Biz konuşulanlardan birşey anlamadığımızdan, mümkünse daha yavaş konuşulsun ve tercümana fırsat verilsin ve biz de ne konuşulduğunu takip edip görüşlerimizi söyleyebilelim.

BAŞKAN :
Bay Ümit Süleyman'ın uyarısı not edilmiştir. Tercümanın konuşmaların içeriğini aktarabilmesi için sayın üyelerin daha yavaş konuşmalarını rica ederim.

B. NALBANTOĞLU :
Ben daha ileri giderek, tercüme edilmeyen konuşmaların zabıtlara girmemesini teklif edeceğim.

BAŞKAN :
Konuşmaların tercüme edilmediğini ileri sürdüğünüz kısımları hangileridir?

Ü. SÜLEYMAN :
Sayın Başkanın ve Dr. Lissaridis'in konuşmaları tercüme edilmedi. Maalesef bu konuşmaları hiç de takip edemedik.
""",
    ),
    8: (
        """ΠΡΟΕΔΡΟΣ :
Θὰ παρακαλέσω τὸν κ. Λυσσαρίδην νὰ ἐπαναλάβῃ ἐν συντομίᾳ ὅ,τι εἶπε, μὲ βραδὺ ρυθμὸν διὰ νὰ μεταφρασθῇ.

Β. ΛΥΣΣΑΡΙΔΗΣ :
Τὸ πρῶτον μέρος τῆς ἀγορεύσεώς μου ἀφεώρα τὸ γεγονός, ὅτι δὲν θὰ ἤθελα ἀπὸ τώρα νὰ θεωρηθῇ ὅτι ἡ Βουλὴ εἶναι ὑποχρεωμένη νὰ καταφεύγῃ εἰς τὸ Ἀγγλικὸν κείμενον εἰς περίπτωσιν διαφορᾶς μεταξὺ Ἑλληνικοῦ καὶ Τουρκικοῦ κειμένου.
Τὸ δεύτερον μέρος τῆς ἀγορεύσεώς μου ἀφεώρα τὸ Ἑλληνικὸν κείμενον, καὶ ἰσχυρίσθην ὅτι τὸ Ἑλληνικὸν κείμενον συμφωνεῖ μὲ τὸ Τουρκικόν. Διότι τὸ κείμενον λέγει ὅτι ὅλοι θὰ πρέπει νὰ ἐκλέγωνται ὑπὸ τῆς Βουλῆς τῶν Ἀντιπροσώπων, καὶ ὁ μόνος περιορισμὸς τὸν ὁποῖον θέτει εἶναι ὅτι, ἓξ ἐξ αὐτῶν πρέπει νὰ εἶναι ἐξ ἐκείνων οἱ ὁποῖοι ἐξελέγησαν ὑπὸ τῆς Ἑλληνικῆς κοινότητος, δηλαδὴ πρέπει νὰ εἶναι Ἕλληνες, καὶ δύο ἐξ αὐτῶν πρέπει νὰ εἶναι ἐξ ἐκείνων οἱ ὁποῖοι ἐξελέγησαν ὑπὸ τῆς Τουρκικῆς κοινότητος. Πρὸς ἐνίσχυσιν τοῦ ἰσχυρισμοῦ μου λέγω ὅτι τὸ ἄρθρον 72 εἰς τὸ ὁποῖον τὸ Σύνταγμα θέλει νὰ καθορίσῃ πραγματικὰ μὲ ποῖον τρόπον πρέπει νὰ γίνεται ἡ ἐκλογή, λέγει ὅτι ὁ Πρόεδρος τῆς Βουλῆς τῶν Ἀντιπροσώπων εἶναι Ἕλλην καὶ ἐκλέγεται ὑπὸ τῶν παρὰ τῆς Ἑλληνικῆς κοινότητος ἐκλεγομένων Ἑλλήνων Βουλευτῶν. Εἰς περίπτωσιν δὲ κατὰ τὴν ὁποίαν οἱ Τοῦρκοι θὰ εἶχον πέραν τῶν δύο ὑποψηφίων, ἰσχυρίζομαι ὅτι εἶναι δικαίωμα τῆς Βουλῆς νὰ ἐκλέξῃ ἐν τῷ συνόλῳ της ἐκείνους τοὺς ὁποίους θὰ ἤθελε νὰ ἐκλέξῃ, καὶ αὐτὸ δὲν θεωρεῖται ἐπιβολὴ τῆς θελήσεως τῆς Ἑλληνικῆς κοινότητος ἐπὶ τῆς Τουρκικῆς, διότι διαχωρισμὸς εἰς αὐτὴν τὴν περίπτωσιν δὲν γίνεται ὑπὸ τοῦ Συντάγματος.

ΠΡΟΕΔΡΟΣ :
Θὰ ἤθελα νὰ διευκρινισθῇ κάτι. Ὁ κ. Λυσσαρίδης εἶπεν «εἰς περίπτωσιν κατὰ τὴν ὁποίαν θὰ ὑπῆρχον περισσότεροι τῶν δύο ὑποψηφίων». Θὰ ἠδύνατο νὰ διευκρινίσῃ τὸ θέμα τοῦτο;

Β. ΛΥΣΣΑΡΙΔΗΣ :
Ἂς ὑποθέσωμεν ὅτι ὑπάρχουν 4 ὑποψήφιοι διὰ τὰς δύο ἕδρας τὰς ὁποίας δικαιοῦνται οἱ Τοῦρκοι εἰς τὴν Ἐπιτροπήν· τότε καὶ τὰ 50 μέλη τῆς Βουλῆς θὰ ἐλάμβανον μέρος εἰς τὴν ψηφοφορίαν καὶ θὰ ἦσαν ὑποχρεωμένα ἐκ τῶν τεσσάρων νὰ ἐκλέξουν τὰ δύο. Δὲν θὰ ἠδύναντο νὰ ἐκλέξουν 8 Ἑλληνικὰ μέλη. Θὰ ἦσαν ὑποχρεωμένοι νὰ ἐκλέξουν 6 Ἕλληνας καὶ δύο Τούρκους ἀλλὰ οἱουσδήποτε δύο Τούρκους ἤθελον ἐκ τῶν τεσσάρων, καὶ δὲν θὰ περιωρίζετο τὸ δικαίωμα αὐτὸ εἰς τὸ Τουρκικὸν τμῆμα τῆς Βουλῆς ἀλλὰ εἰς ὁλόκληρον τὴν Βουλήν.

ΠΡΟΕΔΡΟΣ :
Εἰς περίπτωσιν κατὰ τὴν ὁποίαν θὰ ὑπῆρχον δύο Βουλευταὶ τοὺς ὁποίους θὰ εἰσηγεῖτο ἡ Τουρκικὴ Κοινοβουλευτικὴ ὁμάς, καὶ δύο τοὺς ὁποίους θὰ εἰσηγεῖτο ἡ Ἑλληνικὴ Κοινοβουλευτικὴ ὁμάς, ἡ ψηφοφορία πάντως θὰ διεξήγετο ὑφ' ὁλοκλήρου τῆς Βουλῆς.

Α. ΑΝΑΣΤΑΣΙΑΔΗΣ :
Ὅσοι εἶναι δικηγόροι εἶμαι βέβαιος ὅτι θὰ συμφωνήσουν ὅτι ἐπὶ ζητημάτων ἑρμηνείας μπορεῖ νὰ ὑποστηριχθῇ καὶ ἡ μία ἄποψις καὶ ἡ ἄλλη, καὶ εἰσηγοῦμαι ὅτι ἡ ἑρμηνεία τὴν ὁποίαν ὁ κ. Πρόεδρος τῆς Βουλῆς ἔδωσεν, εἶναι δεῖγμα τοῦ ἀνεπηρεάστου τρόπου κατὰ τὸν ὁποῖον ἀπεφάσισε νὰ ἐκτελῇ τὰ καθήκοντά του. Ἔδωσε φιλευλευθέραν ἑρμηνείαν εἰς τὸ ἄρθρον αὐτό, ἡ ὁποία κατὰ τὴν γνώμην μου ἐξυπηρετεῖ περισσότερον τὰ συμφέροντα τῆς Τουρκικῆς κοινότητος, καὶ θὰ ἐξηγηθῶ διατί. Διὰ τῆς ἑρμηνείας καὶ τοῦ τρόπου ποὺ ἐξελέγησαν τὰ μέλη τῆς περὶ ἧς ὁ λόγος Ἐπιτροπῆς, τὰ Ἑλληνικὰ μέλη τῆς Βουλῆς αὐτῆς δὲν ἔδωσαν ψῆφον οὔτε ἐξέφρασαν γνώμην ποῖα θὰ ἦσαν τὰ Τουρκικὰ μέλη τῆς Ἐπιτροπῆς. Μὲ ἄλλα λόγια ἐπαφίεται εἰς τοὺς ἰδίους τοὺς Τούρκους συμφώνως πρὸς τὴν ἑρμηνείαν αὐτὴν νὰ ἐκλέξουν τὰ ἰδικά των μέλη. Δι' αὐτὸν τὸν λόγον ἐπαναλαμβάνω ὅτι ἡ πλέον φιλελευθέρα ἑρμηνεία ἐδόθη ὑπὸ τοῦ Προεδρείου. Ὀφείλω ὅμως νὰ προσθέσω ὅτι ἡ εἰσήγησίς μου εἶναι ὅτι, ἐὰν τὸ ἔντιμον Τουρκικὸν μέλος τὸ ὁποῖον ὡμίλησε πρῶτον ἐπὶ τοῦ ζητήματος ἐπιμένῃ εἰς τὴν εἰσήγησίν του, τότε ἡ ἰδική μου εἰσήγησις εἶναι ὁλόκληρος ἡ Βουλὴ νὰ ψηφίζῃ ἐπὶ ἑνὸς ἑκάστου μέλους Τουρκικοῦ ἢ Ἑλληνικοῦ, καὶ θὰ ἦτο εὐχῆς ἔργον, προσθέτω, ἐὰν ἐπὶ ἑνὸς ἑκάστου ζητήματος ὁλόκληρος ἡ Βουλὴ ὡς ἓν σῶμα ἐψήφιζε. Δυστυχῶς τὸ Σύνταγμα τὸ ὁποῖον ἔχομεν ἐξαιρεῖ ὡρισμένα ζητήματα. Δὲν θέλω νὰ ἐπεκταθῶ ἐπὶ τῆς πλευρᾶς αὐτῆς τοῦ ζητήματος, καὶ ἐπαναλαμβάνω τὴν εἰσήγησίν μου νὰ γίνῃ ἐκλογὴ ὑπὸ ὁλοκλήρου τῆς Βουλῆς δι' ἓν ἕκαστον τῶν μελῶν τῆς Ἐπιτροπῆς Ἐπιλογῆς. Εἶναι λυπηρὸν διότι δι' ἓν τόσον ἁπλοῦν ζήτημα κατεσπαταλήθη τόσος χρόνος, καὶ ἐλπίζω ὅτι εἰς τὸ μέλλον, ζητήματα τοιαύτης φύσεως τὰ ὁποῖα κατὰ τὴν γνώμην μου δὲν εἶναι τόσον οὐσιαστικά, δὲν θὰ μᾶς ἀναγκάζουν νὰ σπαταλῶμεν τὸν χρόνον μας, καὶ ὅτι θὰ δυνηθῶμεν νὰ ἀσχοληθῶμεν μὲ τὰ οὐσιαστικώτερα ζητήματα τὰ ὁποῖα ἔχομεν νὰ ἀντιμετωπίσωμεν ὡς Κύπριοι. Καὶ ἐννοῶ νὰ ἔχωμεν πάντοτε ὑπ' ὄψιν μας τὰς τάξεις ἐκείνας τῶν Κυπρίων, αἱ ὁποῖαι μέχρι σήμερον ὑποφέρουν, συγκεκριμένως δὲ ἀναφέρομαι εἰς τὴν ἀγροτικὴν τάξιν καὶ εἰς τὴν ἐργατικήν, αἱ ὁποῖαι ἀναμένουν πολλὰ ἀπὸ τὴν νέαν Δημοκρατίαν καὶ ἀπὸ τὴν Βουλὴν ταύτην. Δὲν κατονομάζω ἄλλας τάξεις διότι ἐὰν αἱ δύο τάξεις αὐταὶ εὐημεροῦν, αὐτομάτως θὰ εὐημερήσουν ὅλαι αἱ ἄλλαι τάξεις τοῦ Κυπριακοῦ λαοῦ.
""",
        """BAŞKAN :
Bay Lissaridis'ten söylediklerini tercüme edilebilmesi için yavaş bir tempoyla kısaca tekrarlamasını rica edeceğim.

V. LİSSARİDİS :
Konuşmamın ilk bölümü, Yunanca ve Türkçe metinler arasında fark olması hâlinde Meclisin şimdiden İngilizce metne başvurmakla yükümlü sayılmasını istemediğime ilişkindi.
Konuşmamın ikinci bölümü ise Yunanca metne ilişkindi ve Yunanca metnin Türkçe metinle uyumlu olduğunu savundum. Zira metin, tüm üyelerin Temsilciler Meclisince seçilmesi gerektiğini belirtmekte ve koyduğu tek sınırlama, bunlardan altısının Rum Cemaati tarafından seçilenler arasından (yani Rum), ikisinin de Türk Cemaati tarafından seçilenler arasından (yani Türk) olmasıdır. İddiamı desteklemek için şunu ekliyorum: Anayasa seçimin nasıl yapılacağını gerçekten belirlemek istediğinde, 72. maddede olduğu gibi, Temsilciler Meclisi Başkanının Rum olduğunu ve Rum Cemaati tarafından seçilen Rum milletvekillerince seçileceğini açıkça yazar. Türklerin ikiden fazla aday göstermesi durumunda, Meclisin bir bütün olarak istediklerini seçme hakkına sahip olduğunu savunuyorum; bu durum Rum cemaatinin iradesini Türk cemaatine dayatması sayılmaz, çünkü Anayasa bu konuda bir ayrım yapmamaktadır.

BAŞKAN :
Bir hususun açıklığa kavuşmasını isterim. Bay Lissaridis "ikiden fazla aday olması durumunda" dedi. Bu konuyu biraz açabilir mi?

V. LİSSARİDİS :
Türklerin Komitede hak sahibi olduğu iki koltuk için 4 aday olduğunu varsayalım; bu durumda Meclisin 50 üyesinin tamamı oylamaya katılır ve bu dördü arasından ikisini seçmek zorunda olurdu. 8 Rum üye seçemezlerdi. 6 Rum ve 2 Türk seçmek zorundalar; ancak bu dördü arasından istedikleri herhangi iki Türk'ü seçerlerdi ve bu hak Meclisin yalnız Türk bölümüyle değil, tüm Meclisle sınırlı olurdu.

BAŞKAN :
Türk Parlamento Grubunun önereceği iki milletvekili ile Rum Parlamento Grubunun önereceği iki Türk milletvekili bulunması hâlinde de oylama her hâlükârda bütün Meclis tarafından yapılacaktı.

A. ANASTASİADİS :
Hukukçu olan herkesin, yorum meselelerinde hem bir görüşün hem de diğerinin savunulabileceği hususunda hemfikir olacağından eminim; Meclis Başkanının yaptığı yorumun, görevini ne kadar tarafsız bir şekilde yerine getirmeye kararlı olduğunun göstergesi olduğunu düşünüyorum. Bu maddeye bana göre Türk cemaatinin menfaatlerine daha fazla hizmet eden liberal bir yorum getirdi ve nedenini açıklayayım: Bu yorum ve Komite üyelerinin seçiliş biçimi sayesinde Meclisin Rum üyeleri, Komitenin Türk üyelerinin kimler olacağı konusunda ne oy kullandı ne de görüş bildirdi. Başka bir deyişle bu yoruma göre kendi üyelerini seçmek bizzat Türklere bırakılmıştır. Bu nedenle en liberal yorumun Başkanlıkça yapıldığını tekrarlıyorum. Ancak şunu da eklemeliyim: Bu konuda ilk söz alan Sayın Türk üye önerisinde ısrar ediyorsa, benim önerim de ister Türk ister Rum olsun her bir üye için tüm Meclisin oy kullanmasıdır; hatta temenni ederim ki her konuda tüm Meclis tek bir vücut olarak oy kullansın. Ne yazık ki sahip olduğumuz Anayasa bazı konuları bundan istisna tutmaktadır. Meselenin bu yönüne girmek istemiyorum ve Seçme Komitesinin her bir üyesi için bütün Meclisçe seçim yapılması önerimi yineliyorum. Böylesine basit bir meselede bu kadar zaman harcanmış olması üzücüdür; umarım gelecekte bence o kadar da esaslı olmayan bu tür meseleler vaktimizi almaz ve Kıbrıslılar olarak önümüzdeki daha esaslı meselelerle ilgilenebiliriz. Kastettiğim, bugüne dek sıkıntı çeken Kıbrıslı sınıfları, özellikle de yeni Cumhuriyetten ve bu Meclisten çok şey bekleyen çiftçi ve işçi sınıflarını daima göz önünde bulundurmamızdır. Diğer sınıfları saymıyorum çünkü bu iki sınıf refaha kavuşursa Kıbrıs halkının diğer tüm sınıfları da kendiliğinden refaha kavuşacaktır.
""",
    ),
    9: (
        """ΠΡΟΕΔΡΟΣ :
Ὁ κ. Ραματὰν Τζεμήλ.

R. CEMİL :
Sayın Meclis Reisine arzetmek isterim ki, meb'us arkadaşımız Halit Ali Rıza Beyin beyan ettiği gibi, Türkçe metin sarihtir ve bizce böyle anlaşılmıştır. Bizim anlayışımızı takviye eder mahiyette iki Elen arkadaşımız bu hususta konuştu ve arkadaşım Bay Anastasiadis'in de ileri sürdüğü gibi, Meclisin vaktini harcamamamız doğru olduğu cihetle, Sayın Meclis Reisinden ricam, sual Rum Üyelere de tevcih edilsin. Eğer ekseriyeti Elence metinde olduğu gibi anlıyorlarsa bir sonuca varmış oluruz.

ΠΡΟΕΔΡΟΣ :
Δὲν εἶναι εὔκολον νὰ θέσω τὸ ζήτημα εἰς τὰ Ἑλληνικὰ μέλη διὰ νὰ συμφωνήσουν περὶ τοῦ Ἑλληνικοῦ κειμένου, διότι ἤδη διεπιστώθη ὅτι ὑπάρχουν ἀντίθετοι ἀπόψεις περὶ τῆς ἑρμηνείας τοῦ κειμένου. Ἐπειδὴ δὲ πρόκειται περὶ νομικῆς ἑρμηνείας, δὲν εἶναι θέμα εἰς τὸ ὁποῖον δυνάμεθα νὰ ζητήσωμεν ψῆφον κατὰ πόσον συμφωνοῦν ὅλοι ὁμοφώνως μὲ τὴν μίαν ἐκ τῶν δύο ἀπόψεων. Ἐφ' ὅσον ὅμως διεπιστώθη ὅτι τὸ Τουρκικὸν κείμενον εἶναι σαφὲς ἐπὶ τοῦ θέματος αὐτοῦ, καὶ ἐφ' ὅσον ὑπάρχει τουλάχιστον ἀμφιβολία ἐπὶ τῆς ἑρμηνείας τοῦ Ἑλληνικοῦ κειμένου, καὶ ἐφ' ὅσον ὑπάρχει διάταξις εἰς τὸ Σύνταγμα, ἡ ὁποία ὁρίζει ὅτι ἐὰν ὑπάρξῃ διαφορὰ ἢ ἀντίφασις μεταξὺ τοῦ Ἑλληνικοῦ καὶ τοῦ Τουρκικοῦ κειμένου τότε ἀναφερόμεθα εἰς τὸ Ἀγγλικὸν κείμενον, ἡ ἀπόφασις τοῦ Προέδρου εἶναι ὅπως γίνῃ προσφυγὴ εἰς τὸ Ἀγγλικὸν κείμενον καὶ ἐξετασθῇ τὸ ζήτημα, λαμβανομένου ὑπ' ὄψιν τοῦ ἄρθρου 73 (2) τοῦ Ἀγγλικοῦ κειμένου μόνον διὰ σκοποὺς ἑρμηνείας. Προτοῦ προχωρήσω, ἐζήτησε τὸν λόγον ὁ ἔντιμος Ἀντιπρόεδρος τῆς Βουλῆς καὶ δίδεται εἰς αὐτὸν ὁ λόγος.

O. MÜDERRİSOĞLU :
Muhterem arkadaşlar, arkadaşımız Halit Ali Rıza Beyin, Reisi ve bizi ikaz etmesi, emin olmalısınız ki, hüsnüniyetle yapılmıştır. Arkadaşımız Anayasanın hazırlanmasında, başından sonuna kadar uzun müddet emek sarfetmiştir. Binaenaleyh bu günkü oturumumuzda bizi ikaz etmekle, bize çok büyük fayda sağladığı kanaatindeyim. Biz, Meclis olarak Anayasayı tamamıyle tatbik etmekle mükellefiz ve hiç bir suretle, hiç bir maddenin haricine çıkmamıza salâhiyetimiz yoktur ve çıkamayız. Burada son konuşan arkadaşımızın konuşmasının tercümesi yanlış yapılmamışsa, ki "Anayasada maalesef tatbik etmeğe mecbur olduğumuz bazı maddeler" diye bir cümle sarfetmiştir, bizlere düşen vazife Anayasayı tatbik etmektir ve bunda teessüf edilecek bir şey yoktur. Anayasayı tatbik etmezsek teessüf ederiz. Bu mevzu, bizim aramızda bir fikir ihtilâfı değil, fakat bundan sonra alınacak kararların, yapılacak konuşma ve görüşmelerin Anayasa çerçevesi dahilinde olmasını hepimize göstermesi bakımından önemlidir. Türkçe, Elence ve İngilizce 73'üncü maddenin 2'nci fıkrası ileride tekrar tetkik edilir ve buna göre kat'i bir netice alınabilir. Biz burada ne kadar uzun boylu tetkik etsek bir netice alamayız.

ΠΡΟΕΔΡΟΣ :
Εἶναι καθαρὸν ἀπὸ τὸ ἄρθρον 73 (2) τοῦ Ἀγγλικοῦ κειμένου τοῦ ὁποίου ἡ διατύπωσις ἔχει ὡς ἀκολούθως :
"There shall be a committee to be known as the Committee of Selection consisting of the President of the House as Chairman, the Vice-President of the House as Vice-Chairman and eight other members elected by the House of Representatives at its meeting after the election of the President and the Vice-President of the House, six from amongst the Representatives elected by the Greek Community and two from amongst the Representatives elected by the Turkish Community."
Ἡ ὀρθὴ ἑρμηνεία ἔχει ὡς ἀκολούθως :
Πρῶτον : Τὰ μέλη τῆς Ἐπιτροπῆς ἐκλέγονται "by the House of Representatives" ὑπὸ τῆς Βουλῆς τῶν Ἀντιπροσώπων.
Δεύτερον : Ὅτι ἓξ ἐξ αὐτῶν ἐκλέγονται «ἀπὸ» τὴν Ἑλληνικὴν κοινότητα καὶ ὄχι «ὑπὸ» ὅπως εἶναι διατυπωμένον εἰς τὸ Ἑλληνικόν, ἀλλὰ «ἀπὸ» τὴν Ἑλληνικὴν κοινότητα καὶ δύο ἐκ τῆς Τουρκικῆς κοινότητος. Ἐὰν συγκρίνῃ τὴν παράγραφον 2 ὁ παρατηρητής, μὲ τὰ ἄρθρα τὰ ὁποῖα προβλέπουν περὶ χωριστῆς πλειοψηφίας καὶ τὰ ὁποῖα εἶναι περιοριστικά, δηλαδὴ περιορίζουν τὸ θέμα χωριστῆς πλειοψηφίας εἰς ὡρισμένα θέματα σαφῶς ἀναφερόμενα εἰς τὸ Σύνταγμα, πρέπει νὰ καταλήξῃ εἰς τὸ συμπέρασμα ὅτι τὰ μέλη τῆς Ἐπιτροπῆς Ἐπιλογῆς ἐκλέγονται ἀπὸ κοινοῦ ὑπὸ τῶν Τούρκων καὶ Ἑλλήνων μὲ περιορισμὸν ὅτι δύο ἐξ αὐτῶν πρέπει νὰ εἶναι Τοῦρκοι Βουλευταὶ καὶ ἓξ ἐξ αὐτῶν Ἕλληνες. Αὐτὴ εἶναι ἡ ἀπόφασις τοῦ Προέδρου ἐπὶ τοῦ θέματος τούτου. Κατηναλώθη χρόνος ἀλλὰ διεσάφηνίσθη τὸ ἄρθρον τοῦ Συντάγματος. Οὐδεμίαν ἀμφιβολίαν περὶ τῆς καλῆς προθέσεως τοῦ κ. Χαλὶτ εἶχον, ἢ οὐδεὶς ἐξ ὑμῶν εἶχε καμμίαν ἀμφιβολίαν περὶ τῆς καλῆς του προθέσεως, καὶ τὸν εὐχαριστοῦμεν διότι ἤγειρε τὸ θέμα τοῦτο. Ἐν ὄψει τῆς ἀποφάσεως αὐτῆς θὰ ἀκυρωθῇ ἡ προηγουμένη ψηφοφορία καὶ θὰ γίνῃ νέα ψηφοφορία διὰ τὴν ἐκλογὴν τῶν μελῶν τῆς Ἐπιτροπῆς Ἐπιλογῆς.

H. A. RIZA :
Sayın Reis ve Reis Vekilinin hakkımda buyurdukları iyi ifadelerden dolayı çok teşekkür ederim. Şahsen konuşuyorum, lâkin tahmin ediyorum ki, bütün Türk arkadaşlar da fikrime iştirak edecektir. Bütün gayemiz Anayasanın tamamen tatbik edilmesidir. Elen arkadaşların kendi hatalarını dahi istismar etmek istemiyoruz. Bu iyi niyetli hareketlerimize karşı kendilerinin de hüsnüniyet göstermelerini ve son konuşan Elen Üye gibi bir meseleyi fırsat bilerek itham yoluna gidilmemesini temenni ederiz. Anayasa Komisyonunda bu husus uzun boylu müzakere edilmiştir. Bu hususun mevsuf ekseriyete tabi olmasını istemiştik. Lâkin Sayın Meclis Reisinin bizzat kendisi, Zürih anlaşmasında böyle bir ekseriyet yoktur diye Anayasaya konmasına itiraz etmişti. Kısaca şunu arzetmek istiyorum ki, Anayasanın tatbikinde hiç bir mesele küçük mesele değildir. Cumhuriyete başlarken ta başlangıçtan daima doğru hareket etmemizi temenni ederim.
""",
        """BAŞKAN :
Buyurunuz Bay Ramadan Cemil.

R. CEMİL :
Sayın Meclis Reisine arzetmek isterim ki, meb'us arkadaşımız Halit Ali Rıza Beyin beyan ettiği gibi, Türkçe metin sarihtir ve bizce böyle anlaşılmıştır. Bizim anlayışımızı takviye eder mahiyette iki Elen arkadaşımız bu hususta konuştu ve arkadaşım Bay Anastasiadis'in de ileri sürdüğü gibi, Meclisin vaktini harcamamamız doğru olduğu cihetle, Sayın Meclis Reisinden ricam, sual Rum Üyelere de tevcih edilsin. Eğer ekseriyeti Elence metinde olduğu gibi anlıyorlarsa bir sonuca varmış oluruz.

BAŞKAN :
Rum üyelerin Yunanca metin üzerinde uzlaşmaları için konuyu onlara sormak kolay değildir, çünkü metnin yorumu hakkında karşıt görüşler olduğu zaten ortaya çıktı. Konu hukuki bir yorum meselesi olduğundan, iki görüşten birine herkesin oybirliğiyle katılıp katılmadığını oylamaya sunamayız. Ancak Türkçe metnin bu konuda açık olduğu tespit edildiğine, Yunanca metnin yorumunda en azından tereddüt bulunduğuna ve Anayasada Yunanca ile Türkçe metinler arasında fark veya çelişki olması hâlinde İngilizce metne başvurulacağını öngören hüküm yer aldığına göre, Başkanın kararı, yalnızca yorum amacıyla İngilizce metnin 73(2). maddesi esas alınarak konunun incelenmesidir. Devam etmeden önce Sayın Meclis Başkan Yardımcısı söz istedi; söz kendisindedir.

O. MÜDERRİSOĞLU :
Muhterem arkadaşlar, arkadaşımız Halit Ali Rıza Beyin, Reisi ve bizi ikaz etmesi, emin olmalısınız ki, hüsnüniyetle yapılmıştır. Arkadaşımız Anayasanın hazırlanmasında, başından sonuna kadar uzun müddet emek sarfetmiştir. Binaenaleyh bu günkü oturumumuzda bizi ikaz etmekle, bize çok büyük fayda sağladığı kanaatindeyim. Biz, Meclis olarak Anayasayı tamamıyle tatbik etmekle mükellefiz ve hiç bir suretle, hiç bir maddenin haricine çıkmamıza salâhiyetimiz yoktur ve çıkamayız. Burada son konuşan arkadaşımızın konuşmasının tercümesi yanlış yapılmamışsa, ki "Anayasada maalesef tatbik etmeğe mecbur olduğumuz bazı maddeler" diye bir cümle sarfetmiştir, bizlere düşen vazife Anayasayı tatbik etmektir ve bunda teessüf edilecek bir şey yoktur. Anayasayı tatbik etmezsek teessüf ederiz. Bu mevzu, bizim aramızda bir fikir ihtilâfı değil, fakat bundan sonra alınacak kararların, yapılacak konuşma ve görüşmelerin Anayasa çerçevesi dahilinde olmasını hepimize göstermesi bakımından önemlidir. Türkçe, Elence ve İngilizce 73'üncü maddenin 2'nci fıkrası ileride tekrar tetkik edilir ve buna göre kat'i bir netice alınabilir. Biz burada ne kadar uzun boylu tetkik etsek bir netice alamayız.

BAŞKAN :
İngilizce metnin 73(2). maddesinden mesele açıkça anlaşılmaktadır:
"Meclis Başkanı başkanlığında, Meclis Başkan Yardımcısı başkan yardımcılığında ve Temsilciler Meclisi tarafından Başkan ve Başkan Yardımcısının seçiminin ardından yapılacak toplantıda — altısı Rum Cemaatince seçilen Temsilciler arasından ve ikisi Türk Cemaatince seçilen Temsilciler arasından olmak üzere — seçilecek sekiz diğer üyeden oluşan, Seçme Komitesi adıyla anılacak bir komite bulunur."
Doğru yorum şöyledir:
Birincisi: Komite üyeleri Temsilciler Meclisi ("by the House of Representatives") tarafından seçilir.
İkincisi: Bunlardan altısı Yunanca metinde yazıldığı gibi Rum cemaati "tarafından" değil, Rum cemaati "arasından" ve ikisi de Türk cemaati "arasından" seçilir. 2. fıkra, Anayasada ayrı çoğunluğu öngören ve bunu yalnızca açıkça sayılan konularla sınırlayan maddelerle karşılaştırıldığında, Seçme Komitesi üyelerinin — ikisinin Türk, altısının Rum milletvekili olması kaydıyla — Türkler ve Rumlarca ortaklaşa seçildiği sonucuna varılmalıdır. Başkanın bu konudaki kararı budur. Zaman harcandı ancak Anayasa maddesi açıklığa kavuşturuldu. Bay Halit'in iyi niyetinden ne benim ne de içinizden herhangi birinin en ufak şüphesi vardı; bu konuyu gündeme getirdiği için kendisine teşekkür ederiz. Bu karar doğrultusunda önceki oylama iptal edilecek ve Seçme Komitesi üyelerinin seçimi için yeni bir oylama yapılacaktır.

H. A. RIZA :
Sayın Reis ve Reis Vekilinin hakkımda buyurdukları iyi ifadelerden dolayı çok teşekkür ederim. Şahsen konuşuyorum, lâkin tahmin ediyorum ki, bütün Türk arkadaşlar da fikrime iştirak edecektir. Bütün gayemiz Anayasanın tamamen tatbik edilmesidir. Elen arkadaşların kendi hatalarını dahi istismar etmek istemiyoruz. Bu iyi niyetli hareketlerimize karşı kendilerinin de hüsnüniyet göstermelerini ve son konuşan Elen Üye gibi bir meseleyi fırsat bilerek itham yoluna gidilmemesini temenni ederiz. Anayasa Komisyonunda bu husus uzun boylu müzakere edilmiştir. Bu hususun mevsuf ekseriyete tabi olmasını istemiştik. Lâkin Sayın Meclis Reisinin bizzat kendisi, Zürih anlaşmasında böyle bir ekseriyet yoktur diye Anayasaya konmasına itiraz etmişti. Kısaca şunu arzetmek istiyorum ki, Anayasanın tatbikinde hiç bir mesele küçük mesele değildir. Cumhuriyete başlarken ta başlangıçtan daima doğru hareket etmemizi temenni ederim.
""",
    ),
    10: (
        """ΠΡΟΕΔΡΟΣ :
Ἡ συζήτησις ἐπὶ τοῦ θέματος αὐτοῦ ἔκλεισε, καὶ θὰ προβῶμεν τώρα εἰς τὴν ὑποβολὴν προτάσεων ὑποψηφίων διὰ τὴν Ἐπιτροπὴν Ἐπιλογῆς.

ΑΙΜ. ΦΡΑΓΚΟΣ :
Ἐν ὄψει τῆς ἑρμηνείας τὴν ὁποίαν ἔδωσεν ὁ κ. Πρόεδρος, καὶ ἐφ' ὅσον θὰ προχωρήσωμεν εἰς νέαν ψηφοφορίαν, θὰ ἤθελα νὰ ἀποσαφηνισθῇ τὸ ἑξῆς : Αἱ προτάσεις δι' ὑποψηφίους θὰ προέρχωνται ἐξ ἑκατέρας τῶν πλευρῶν ἄνευ περιορισμῶν;

H. A. RIZA :
Sayın Meclis Reisi, tabiî biraz evvel konuşan Elen Üyenin söylediği doğrudur. Yalnız biz, şimdi, Türk Grubu olarak prensibimizi açıklıyoruz ve takip edilecek usulün bir an'ane haline gelmesini temenni ederim. Biz Seçme Komitesine Elen aday göstermiyeceğiz ve onların seçiminde müstenkif kalacağız ve biraz evvel Ümit Bey arkadaşımızın gösterdiği namzedleri aynen teklif ediyoruz.

Β. ΛΥΣΣΑΡΙΔΗΣ :
Παρ' ὅλον ὅτι εἶναι φυσικὸν πολλὰς φορὰς νὰ γίνεται αὐτὸ τὸ ὁποῖον τὸ ἔντιμον Μέλος προέτεινε, δὲν νομίζω ὅτι δυνάμεθα νὰ δεχθῶμεν κανένα προηγούμενον εἴτε ὑπὸ μορφὴν παραδόσεως εἴτε ὑπὸ μορφὴν κανονισμοῦ. Ἐλπίζομεν νὰ μὴ χρειασθῇ βεβαίως νὰ ὑπεισέρχεται ἡ μία πλευρὰ εἰς τὴν ἄλλην, ἀλλὰ νομίζω ὅτι πρέπει νὰ παραμένῃ δικαίωμα τῆς Βουλῆς ὅταν καὶ ἐφ' ὅσον ἡ Βουλὴ θὰ ἐπεθύμει.

ΠΡΟΕΔΡΟΣ :
Εἶναι ἀδύνατον εἴτε ὑπὸ τύπον παραδόσεως εἴτε ὑπὸ τύπον συμπράξεως ἢ συμφωνίας νὰ ἐλαττώσωμεν τὰ δικαιώματα, ὅπως καὶ νὰ αὐξήσωμεν τὰ δικαιώματα τὰ ὁποῖα δίδονται ρητῶς ὑπὸ τοῦ Συντάγματος. Ἡ εἰσήγησις τοῦ ἐντίμου κ. Χαλὶτ δὲν νομίζω ὅτι ἐγένετο μὲ σκοπὸν νὰ φθάσῃ μέχρι τοῦ σημείου νὰ εἰσηγηθῇ τροποποίησιν ἢ ἐλάττωσιν τῶν δικαιωμάτων τὰ ὁποῖα δίδονται ὑπὸ τοῦ Συντάγματος. Ἴσως ὁ κ. Χαλὶτ ἐκεῖνο τὸ ὁποῖον ἤθελε νὰ εἰσηγηθῇ εἶναι ὅτι θὰ ἠδύνατο νὰ ἀποτελέσῃ θέμα συμφωνίας εἰς ἑκάστην περίπτωσιν, ἄνευ ἐπηρεασμοῦ τῶν δικαιωμάτων οἱασδήποτε παρατάξεως ἢ οἱουδήποτε μέλους, νὰ δέχεται τὰς προτάσεις διὰ τὰ μέλη τῆς Ἐπιτροπῆς αὐτῆς, αἱ ὁποῖαι γίνονται ὑφ' ἑκάστης τῶν δύο κοινοτήτων χωρὶς ἡ μία ἐκ τῶν δύο κοινοτήτων νὰ λαμβάνῃ θέσιν, οὐχὶ ὅμως ὡς κανόνα ἀπαράβατον, ἀλλὰ εἰς ἑκάστην συγκεκριμένην περίπτωσιν κατόπιν συμφωνίας μεταξὺ τῶν μελῶν. Νομίζω ὅτι ὀρθῶς ἀπέδωσα τὸ πνεῦμα τῆς εἰσηγήσεως τοῦ ἐντίμου Βουλευτοῦ.

H. A. RIZA :
Daha evvel tercüme yapılmadığından, tercüme edilmesini rica ederiz.

ΠΡΟΕΔΡΟΣ :
Ἐκεῖνο τὸ ὁποῖον ἀντελήφθην νὰ εἰσηγῆται ὁ κ. Χαλὶτ εἶναι ὅτι θὰ ἠδύνατο εἰς ἑκάστην περίπτωσιν νὰ ἐγένετο εἰδικὴ συμφωνία ἐπὶ τοῦ θέματος αὐτοῦ χωρὶς ὅμως μία τοιαύτη συμφωνία νὰ ἐλαττώνῃ τὰ δικαιώματα τὰ ἀπορρέοντα ἐκ τοῦ Συντάγματος.

H. A. RIZA :
Sayın Meclis Reisi anlayışında gayet haklıdır. Benim izah ettiğim şekil, hukukî hükmü olmıyan bir usül durumunda olması noktai nazarıdır.

ΠΡΟΕΔΡΟΣ :
Παρακαλῶ ὅπως γίνουν προτάσεις περὶ μελῶν Ἐπιτροπῆς Ἐπιλογῆς. Ὁ κ. Παῦλος Παυλάκης τὸ ἔντιμον μέλος ἐξ Ἀμμοχώστου ζητεῖ τὸν λόγον.

Π. ΠΑΥΛΟΥ :
Ἐπαναλαμβάνω τὴν πρότασιν περὶ τῶν προσώπων περὶ τῶν ὁποίων ἐγένετο πρότασις καὶ προηγουμένως.

Ü. SÜLEYMAN :
Daha evvel de teklif ettiğim gibi, Dr. Burhan Nalbantoğlu'nu ve Avukat Halit Ali Rıza Beyi, Seçme Komitesine üye teklif ederim. Biz, Meclisteki Türk Hey'eti olarak, ikiden fazla namzet göstermiyeceğiz ve Elen arkadaşların göstereceği üyeler hakkında reyimizi kullanmıyacağız.

Ε. ΠΑΠΑΪΩΑΝΝΟΥ :
Ἐπαναλαμβάνω τὴν πρότασιν διὰ τὸ ἔντιμον Μέλος ἐκ Λεμεσοῦ κ. Γιάγκον Ποταμίτην, καὶ θέλω νὰ συνοδεύσω αὐτὴν τὴν πρότασίν μου μὲ μίαν ἔκκλησιν, ὅπως ὑποστηριχθῇ ἡ ὑποψηφιότης αὐτοῦ διότι ἔχω τὴν γνώμην ὅτι εἶναι ὀρθὸν εἰς τὴν Ἐπιτροπὴν Ἐπιλογῆς, ἡ ὁποία θὰ καταρτίζῃ ὅλας τὰς ἄλλας ἐπιτροπάς, νὰ ἀντιπροσωπεύωνται ὅλαι αἱ παρατάξεις, καὶ συνεπῶς νὰ ἀκούωνται ὅλαι αἱ ἀπόψεις.

ΠΡΟΕΔΡΟΣ :
Θὰ ἤθελα νὰ ἀπαντήσω εἰς τὸν κ. Παπαϊωάννου ὅτι ὅσον ἀφορᾷ τὴν Ἐπιτροπὴν Ἐπιλογῆς, οὐδεμία νομικὴ ὑποχρέωσις ὑπάρχει ὅπως ἀντιπροσωπεύωνται ὅλαι αἱ παρατάξεις. Τὸ καθῆκον τῆς Ἐπιτροπῆς Ἐπιλογῆς εἶναι ἁπλῶς νὰ ὀνομάσῃ ποῖαι θὰ εἶναι αἱ ἄλλαι ἐπιτροπαὶ καὶ ποῖοι θὰ τὰς ἀποτελέσουν. Ὅταν ἔλθῃ εἰς τὴν ἐπάνδρωσιν τῶν ἐπιτροπῶν αὐτῶν ὑποχρεοῦται νὰ λάβῃ ὑπ' ὄψιν της ὅλας τὰς παρατάξεις. Ἐν πάσῃ περιπτώσει εἰς τὴν περίπτωσιν αὐτὴν δὲν εἶναι μόνον θέμα νομικῆς ἑρμηνείας, ἀλλὰ εἶναι θέμα ἐκφρασθείσης ἐπιθυμίας ἢ εἰσηγήσεως ὅπως ὁ κ. Γιάγκος Ποταμίτης, τὸ ἔντιμον Μέλος ἐκ Λεμεσοῦ, συμπεριληφθῇ εἰς τὴν Ἐπιτροπὴν Ἐπιλογῆς. Ὑπάρχουν ἑπομένως ἑπτὰ Ἕλληνες ὑποψήφιοι δι' ἓξ ἕδρας. Ἑπομένως εἶναι ἀνάγκη ὅπως διεξαχθῇ ψηφοφορία. Ὅσον ἀφορᾷ τὰ δύο Τουρκικὰ μέλη ἐφ' ὅσον δὲν ὑπάρχουν ἀνθυποψήφιοι θεωροῦνται ὡς ἐκλεγέντα.
""",
        """BAŞKAN :
Bu konudaki tartışma kapanmıştır; şimdi Seçme Komitesi için aday önerilerine geçeceğiz.

AİM. FRANGOS :
Sayın Başkanın yaptığı yorum ışığında ve yeni bir oylamaya geçeceğimize göre şu hususun açıklığa kavuşturulmasını isterim: Aday önerileri her iki taraftan da herhangi bir kısıtlama olmaksızın mı gelecektir?

H. A. RIZA :
Sayın Meclis Reisi, tabiî biraz evvel konuşan Elen Üyenin söylediği doğrudur. Yalnız biz, şimdi, Türk Grubu olarak prensibimizi açıklıyoruz ve takip edilecek usulün bir an'ane haline gelmesini temenni ederim. Biz Seçme Komitesine Elen aday göstermiyeceğiz ve onların seçiminde müstenkif kalacağız ve biraz evvel Ümit Bey arkadaşımızın gösterdiği namzedleri aynen teklif ediyoruz.

V. LİSSARİDİS :
Sayın üyenin önerdiği uygulamanın çoğu zaman kendiliğinden gerçekleşmesi doğal olsa da, bunu ne bir gelenek ne de bir iç tüzük kuralı olarak emsal kabul edebileceğimizi düşünüyorum. Elbette bir tarafın diğerine karışmasına gerek kalmamasını umuyoruz; ancak Meclis arzu ettiği takdirde bu hakkın Mecliste saklı kalması gerektiğine inanıyorum.

BAŞKAN :
Anayasa tarafından açıkça tanınan hakları ne gelenek ne de anlaşma yoluyla azaltmamız ya da artırmamız mümkün değildir. Sayın Halit'in önerisinin Anayasadan doğan hakları değiştirecek veya azaltacak bir noktaya varmayı amaçladığını sanmıyorum. Bay Halit'in önermek istediği şey muhtemelen, herhangi bir grubun veya üyenin haklarına halel gelmeksizin, her somut olayda iki cemaatten her birinin bu Komite için sunduğu adayların diğer cemaatçe taraf tutulmaksızın kabul edilmesinin, değişmez bir kural değil üyeler arası bir mutabakat konusu olabileceğidir. Sayın Milletvekilinin önerisinin ruhunu doğru aktardığımı sanıyorum.

H. A. RIZA :
Daha evvel tercüme yapılmadığından, tercüme edilmesini rica ederiz.

BAŞKAN :
Bay Halit'in önerisinden anladığım şudur: Her somut olayda bu konuda özel bir mutabakat sağlanabilir, ancak böyle bir mutabakat Anayasadan kaynaklanan hakları azaltmaz.

H. A. RIZA :
Sayın Meclis Reisi anlayışında gayet haklıdır. Benim izah ettiğim şekil, hukukî hükmü olmıyan bir usül durumunda olması noktai nazarıdır.

BAŞKAN :
Seçme Komitesi üyeleri için önerilerin sunulmasını rica ederim. Mağusa'nın sayın üyesi Bay Pavlos Pavlakis söz istiyor.

P. PAVLU :
Daha önce önerilmiş olan isimlere ilişkin önerimi yineliyorum.

Ü. SÜLEYMAN :
Daha evvel de teklif ettiğim gibi, Dr. Burhan Nalbantoğlu'nu ve Avukat Halit Ali Rıza Beyi, Seçme Komitesine üye teklif ederim. Biz, Meclisteki Türk Hey'eti olarak, ikiden fazla namzet göstermiyeceğiz ve Elen arkadaşların göstereceği üyeler hakkında reyimizi kullanmıyacağız.

E. PAPAYUANNU :
Limasol'un sayın üyesi Bay Yangos Potamitis için yaptığım öneriyi yineliyor ve adaylığının desteklenmesi çağrısında bulunuyorum; zira tüm diğer komiteleri oluşturacak Seçme Komitesinde bütün grupların temsil edilmesinin ve böylece tüm görüşlerin duyulmasının doğru olduğuna inanıyorum.

BAŞKAN :
Bay Papayuannu'ya şunu belirtmek isterim ki Seçme Komitesinde tüm grupların temsil edilmesine ilişkin hukuki bir zorunluluk yoktur. Seçme Komitesinin görevi yalnızca diğer komiteleri belirlemek ve kimlerin bu komitelerde yer alacağını saptamaktır; o komiteleri oluştururken tüm grupları gözetmekle yükümlüdür. Her hâlükârda burada söz konusu olan, Limasol'un sayın üyesi Bay Yangos Potamitis'in Seçme Komitesine alınması yönündeki bir dilek ve öneridir. Dolayısıyla altı koltuk için yedi Rum aday bulunmaktadır ve oylama yapılması gerekmektedir. İki Türk üye bakımından ise başka aday bulunmadığından seçilmiş sayılırlar.
""",
    ),
    11: (
        """Π. ΠΑΥΛΟΥ :
Εἰς περίπτωσιν καθ' ἣν οἱ Ἕλληνες Βουλευταὶ δὲν θὰ ἐνέκριναν τοὺς δύο αὐτοὺς ὑποψηφίους τοὺς προερχομένους ἐκ τῆς Τουρκικῆς πλευρᾶς, οὗτοι δὲν θὰ συνεκέντρωναν τὴν ὑποστήριξιν τῆς πλειοψηφίας τῆς Βουλῆς ὡς συνόλου· τότε τί θὰ ἐγένετο; Θὰ ἔπρεπε συνεπῶς τὰ δύο Τουρκικὰ μέλη νὰ ἐκλεγοῦν καὶ ἀπὸ τοὺς Ἕλληνας.

ΠΡΟΕΔΡΟΣ :
Κανονικῶς θὰ ἔπρεπε νὰ ἐκλεγοῦν ἐὰν ὑπῆρχον ἀνθυποψήφιοι. Αὐτὴν τὴν στιγμὴν δὲν ὑπάρχουν ἀνθυποψήφιοι· δικαιοῦνται τὰ Ἑλληνικὰ μέλη νὰ εἰσηγηθοῦν ἀνθυποψηφίους, ἐφ' ὅσον δὲν εἰσηγήθησαν ἀνθυποψηφίους σημαίνει ὅτι δέχονται τὰ δύο αὐτὰ πρόσωπα. (Ὁ κ. Σιβιτανίδης ζητεῖ ὅπως μεταφρασθῇ ἡ ὁμιλία τοῦ κ. Παυλάκη.)
Ὁ κ. Παύλου ἐν συντομίᾳ εἶπε τὰ ἑξῆς : Ἡ ἐρώτησις τὴν ὁποίαν ἔθεσεν εἶναι κατὰ πόσον οἱ δύο Τοῦρκοι ὑποψήφιοι θὰ ἔπρεπε νὰ ψηφισθοῦν τώρα ὑφ' ὁλοκλήρου τῆς Βουλῆς. Ἡ ἀπάντησις, ἡ ὁποία ἐδόθη ἦτο ὅτι αὐτὴ εἶναι ἡ ὀρθὴ ἄποψις τοῦ ζητήματος ἐὰν προετείνοντο ἀνθυποψήφιοι. Ἐφ' ὅσον δὲν ὑπάρχει πρότασις περὶ ἀνθυποψηφίων δὲν ὑπάρχει λόγος ψηφοφορίας ἐπὶ τοῦ θέματος αὐτοῦ. Ὅσον ἀφορᾷ τὰ προταθέντα Ἑλληνικὰ μέλη λόγῳ τοῦ ὅτι ὑπάρχουν ἑπτὰ ὑποψήφιοι δι' ἓξ θέσεις τίθεται τὸ ζήτημα εἰς ψηφοφορίαν. Παρακαλοῦνται οἱ ὑποστηρίζοντες τὴν πρότασιν τοῦ ἐντίμου Βουλευτοῦ κ. Παύλου ἐξ Ἀμμοχώστου, ὅπως ὑψώσουν τὴν δεξιὰν χεῖρα. Παρακαλοῦνται οἱ κ.κ. γραμματεῖς νὰ κρατήσουν σημείωσιν περὶ τῶν ψηφισάντων ὑπὲρ τῆς προτάσεως. Ἐψήφισαν ὑπὲρ τῆς προτάσεως τοῦ κ. Παύλου 28 Βουλευταί. Παρακαλοῦνται οἱ ὑποστηρίζοντες τὴν πρότασιν τοῦ ἐντίμου Μέλους κ. Παπαϊωάννου ὅπως ὑψώσουν τὴν δεξιάν. Ἐψήφισαν ὑπὲρ τῆς προτάσεως τοῦ κ. Παπαϊωάννου τέσσαρα μέλη. Θεωροῦνται ὡς ἐγκύρως ἐκλεγέντες οἱ κ.κ. Αἰμίλιος Φράγκος, Γεώργιος Ἰωαννίδης, Γεώργιος Τζιρκώτης, Ἀνδρέας Γιάγκου, Κώστας Χριστοδουλίδης καὶ Γεώργιος Τομπάζος.
Τὸ δεύτερον θέμα τῆς ἡμερησίας διατάξεως εἶναι «Καθορισμὸς ἡμερομηνίας ἐκλογῶν πρὸς πλήρωσιν τῶν κενωθεισῶν θέσεων, τριῶν Τούρκων Βουλευτῶν καὶ ἑνὸς Ἕλληνος». Τὸ ἄρθρον 66 (2) τοῦ Συντάγματος παρέχει τὴν ἐξουσίαν εἰς τὴν Βουλὴν ὅπως ὁρίσῃ τὴν ἡμέραν τῆς ἀναπληρωματικῆς ἐκλογῆς. Παρακαλῶ ὅπως ὑποβληθοῦν εἰσηγήσεις ἐπὶ τοῦ θέματος.

Λ. ΡΟΔΟΣΘΕΝΟΥΣ :
Κύριε Πρόεδρε προτείνω ὅπως ἡ 25η Σεπτεμβρίου ὁρισθῇ ὡς ἡμέρα ἀναπληρωματικῶν ἐκλογῶν.

A. M. BERBEROĞLU :
Sayın Meclis Başkanı, Temsilciler Meclisinde üç Türk ve bir Elen Âzanın seçimi için 25 Eylül 1960 tarihine müsadif Pazar gününü teklif eder ve Elen arkadaşımın teklif ettiği ayni tarihin münasip olduğunu teyit ederim.

ΠΡΟΕΔΡΟΣ :
Ὑπάρχουν ἄλλαι προτάσεις; Τότε δι' ὁμοφώνου ἀποφάσεως ὁρίζεται ἡ 25η Σεπτεμβρίου ὡς ἡμέρα ἐκλογῶν.
Τὸ τελευταῖον θέμα ἐπὶ τῆς ἡμερησίας διατάξεως εἶναι «Καθορισμὸς ἡμερομηνίας καὶ χρόνου δι' ἐρωτήσεις εἰς τὴν Βουλήν». Ὁ λόγος διὰ τὸν ὁποῖον ἐγείρεται αὐτὸ τὸ θέμα εἶναι διότι δὲν ὑπάρχουν ἀκόμη οἱ κανονισμοὶ τῆς Βουλῆς. Καὶ ἐλλείψει κανονισμῶν θὰ πρέπει νὰ ληφθῇ ἀπόφασις περὶ τοῦ ποῖαι ἐκ τῶν ἡμερῶν ἐργασίας τῆς Βουλῆς θὰ ἀφιερωθοῦν ἐν ὅλῳ ἢ ἐν μέρει, δι' ἐρωτήσεις τῶν ἐντίμων Μελῶν. Εἰσηγοῦμαι ὅτι, ὡς προσωρινὸν μέτρον, θὰ ἦτο ὀρθὸν νὰ υἱοθετηθῇ ἡ τακτικὴ ὅπως ὁρίζηται εἰς ἑκάστην συνεδρίασιν ὁ χρόνος ὁ ὁποῖος θὰ ἀφιεροῦται δι' ἐρωτήσεις εἰς τὴν ἑπομένην συνεδρίασιν. Εἰσηγοῦμαι ὅπως διὰ τὴν ἑπομένην συνεδρίασιν τῆς Βουλῆς ὁρίσωμεν μίαν ὥραν δι' ἐρωτήσεις.

B. NALBANTOĞLU :
Muhterem Meclis Reisi, Türk Grubu adına size bir sual tevcih etmek isterim. Bunun evvel emirde bir tercüme hatası olduğunu tahmin ediyorum. Bize gönderilen gündemde sözlü sorudan bahsediliyor. Halbuki şimdiki tercümede gensorudan bahsediliyor. Bunun tasrih edilmesini hassaten rica edeceğim. İkinci olarak soracağım, sizin teklifinizden her toplantıda her günlük toplantıdan önce bu maksat için bir saat tahsis edilip edilmiyeceğidir.

ΠΡΟΕΔΡΟΣ :
Ὅσον ἀφορᾷ τὸ πρῶτον θέμα, ἡ ἡμερησία διάταξις εἰς τὸ Ἑλληνικὸν κείμενον ἔχει ὡς ἀκολούθως : «Καθορισμὸς ἡμερομηνίας καὶ χρόνου δι' ἐρωτήσεις ἐν τῇ Βουλῇ». Λυποῦμαι ἐὰν ἡ μετάφρασις δὲν εἶναι ὀρθή, ἀλλὰ θὰ ἤθελα νὰ παρακαλέσω τὰ ἔντιμα Μέλη νὰ λάβουν ὑπ' ὄψιν των ὅτι ἡ Βουλὴ πρὸς τὸ παρὸν δὲν διαθέτει μεταφραστὰς μέχρις ὅτου ψηφισθῇ ὁ νόμος περὶ διαρθρώσεως τοῦ προσωπικοῦ τῆς Βουλῆς. Εἶχον ὅμως τὴν εὐγενῆ καλωσύνην ὡρισμένα ἄλλα Κυβερνητικὰ Τμήματα νὰ μᾶς δανείσουν διὰ τὴν σημερινὴν συνεδρίασιν τοὺς διερμηνεῖς τοὺς ὁποίους ἔχομεν. Εἰς τὸ μέλλον ἐλπίζω νὰ διαθέτωμεν τουλάχιστον ἓξ διερμηνεῖς διὰ νὰ δύνανται νὰ μεταφράζουν ὄχι μόνον τὴν ἡμερησίαν διάταξιν ἀλλὰ καὶ τὰ διάφορα νομοσχέδια τὰ ὁποῖα θὰ εἶναι ἀνάγκη νὰ ψηφίζῃ ἡ Βουλή.
""",
        """P. PAVLU :
Rum milletvekilleri Türk tarafından gelen bu iki adayı onaylamamış olsalardı, bu adaylar Meclisin bütününün çoğunluğunu kazanamamış olurlardı; o zaman ne olurdu? Dolayısıyla iki Türk üyenin Rumlarca da seçilmesi gerekirdi.

BAŞKAN :
Başka adaylar olsaydı normal olarak oylama gerekirdi. Şu anda başka aday yoktur; Rum üyelerin karşı aday önerme hakkı vardır, önermediklerine göre bu iki ismi kabul ediyorlar demektir. (Bay Sivitanidis, Bay Pavlakis'in konuşmasının tercüme edilmesini ister.)
Bay Pavlu özetle şunu söyledi: İki Türk adayın şimdi tüm Meclisçe oylanmasının gerekip gerekmediğini sordu. Verilen yanıt, karşı aday önerilmesi hâlinde bunun doğru olacağı, ancak başka aday bulunmadığından oylamaya gerek olmadığıdır. Rum adaylar bakımından ise altı koltuk için yedi aday bulunduğundan konu oylamaya sunulmaktadır. Mağusa milletvekili Bay Pavlu'nun önerisini destekleyenler sağ ellerini kaldırsınlar. Bay Pavlu'nun önerisi lehine 28 milletvekili oy kullandı. Bay Papayuannu'nun önerisini destekleyenler sağ ellerini kaldırsınlar. Bay Papayuannu'nun önerisi lehine 4 üye oy kullandı. Sayın Aimilios Frangos, Georgios İoannidis, Georgios Tzirkotis, Andreas Yiangou, Kostas Hristodulidis ve Georgios Tombazos geçerli olarak seçilmiş sayılırlar.
Gündemin ikinci maddesi "Üç Türk ve bir Rum milletvekilinin boşalan koltuklarının doldurulması için yapılacak ara seçimlerin tarihinin belirlenmesi"dir. Anayasanın 66(2). maddesi ara seçim gününü belirleme yetkisini Meclise vermektedir. Bu konuda önerilerinizi rica ederim.

L. RODOSTHENUS :
Sayın Başkan, 25 Eylül gününün ara seçim günü olarak belirlenmesini öneriyorum.

A. M. BERBEROĞLU :
Sayın Meclis Başkanı, Temsilciler Meclisinde üç Türk ve bir Elen Âzanın seçimi için 25 Eylül 1960 tarihine müsadif Pazar gününü teklif eder ve Elen arkadaşımın teklif ettiği ayni tarihin münasip olduğunu teyit ederim.

BAŞKAN :
Başka öneri var mı? O hâlde oybirliğiyle 25 Eylül seçim günü olarak belirlenmiştir.
Gündemin son maddesi "Mecliste sorular için gün ve sürenin belirlenmesi"dir. Bu konunun gündeme gelmesinin nedeni Meclis İç Tüzüğünün henüz hazırlanmamış olmasıdır. İç tüzük yokluğunda, Meclisin çalışma günlerinden hangilerinin tamamen veya kısmen sayın üyelerin sorularına ayrılacağına karar verilmesi gerekir. Geçici bir tedbir olarak, her oturumda bir sonraki oturumda sorulara ayrılacak sürenin belirlenmesi yöntemini öneriyorum. Meclisin bir sonraki oturumu için sorulara bir saat ayırmamızı öneririm.

B. NALBANTOĞLU :
Muhterem Meclis Reisi, Türk Grubu adına size bir sual tevcih etmek isterim. Bunun evvel emirde bir tercüme hatası olduğunu tahmin ediyorum. Bize gönderilen gündemde sözlü sorudan bahsediliyor. Halbuki şimdiki tercümede gensorudan bahsediliyor. Bunun tasrih edilmesini hassaten rica edeceğim. İkinci olarak soracağım, sizin teklifinizden her toplantıda her günlük toplantıdan önce bu maksat için bir saat tahsis edilip edilmiyeceğidir.

BAŞKAN :
İlk konuya gelince, gündemin Yunanca metni şöyledir: "Mecliste sorular için gün ve sürenin belirlenmesi." Tercüme hatalıysa üzgünüm; ancak sayın üyelerin, Meclis personelinin kadro yasası kabul edilinceye dek Meclisin şimdilik kendi tercümanlarına sahip olmadığını dikkate almalarını rica ederim. Bugünkü oturum için bazı diğer devlet daireleri elimizdeki tercümanları bize ödünç verme nezaketini gösterdiler. Gelecekte yalnızca gündemi değil, Meclisin oylamak zorunda olduğu çeşitli yasa tasarılarını da çevirebilecek en az altı tercümana sahip olacağımızı umuyorum.
""",
    ),
    12: (
        """ΠΡΟΕΔΡΟΣ :
Ὅσον ἀφορᾷ τὸ δεύτερον θέμα θὰ ἤθελα διευκρίνισιν ἀπὸ τὸ ἔντιμον Μέλος, κατὰ πόσον εἰσηγεῖται νὰ διαθέτωμεν μίαν ὥραν εἰς ἑκάστην συνεδρίασιν ἢ κατὰ πόσον ἐρωτᾷ ἐὰν θὰ ἦτο δυνατόν, ἐὰν θὰ ἦτο δηλαδὴ εὔκολον, νὰ διαθέτωμεν μίαν ὥραν.

B. NALBANTOĞLU :
Biz her toplantıda sorular için ne kadar müddet ayrılacağını Sayın Meclis Başkanından öğrenemedik. Bunun tasrihini istiyoruz.

ΠΡΟΕΔΡΟΣ :
Ὑπάρχουν τρεῖς ἢ τέσσαρες τρόποι κατὰ τοὺς ὁποίους θὰ ἠδύνατο νὰ διευθετηθῇ τὸ ζήτημα τῶν ἐρωτήσεων, μέχρις ὅτου ρυθμισθῇ ὑπὸ τῶν κανονισμῶν τὸ ζήτημα τοῦτο. Ὁ ἕνας τρόπος εἶναι νὰ ὁρίζεται μία συνεδρίασις ἀποκλειστικῶς διὰ τὸ θέμα τῶν ἐρωτήσεων. Αὐτὸς ὅμως ὁ τρόπος δὲν εἶναι πρακτικὸς διότι μέχρις ὅτου συγκεντρωθῇ ἀρκετὸς ἀριθμὸς ἐρωτήσεων, πολλὰ θέματα ἐπὶ τῶν ὁποίων μέλη ἤθελον ὑποβάλει ἐρωτήσεις θὰ καθυστεροῦν. Ἡ εἰσήγησις τὴν ὁποίαν εἶχα κάμει εἶναι ὅτι εἰς ἑκάστην συνεδρίασιν θὰ ἦτο δυνατὸν νὰ ὁρίζεται χρονικὸν διάστημα μιᾶς ὥρας διὰ σκοποὺς ἐρωτήσεων, αἱ ὁποῖαι θὰ ἀπαντῶνται εἴτε ὑπὸ τοῦ Προεδρείου εἴτε ὑπὸ μελῶν τῆς Βουλῆς. Ἐὰν ὅμως εἶναι ἐρωτήσεις αἱ ὁποῖαι χρήζουν ἀπαντήσεως ὑπὸ Ὑπουργοῦ, ὡς ἀναφερόμεναι εἰς θέματα τὰ ὁποῖα τὰ Μέλη τῆς Βουλῆς δὲν κατέχουν, θὰ πρέπει αἱ ἐρωτήσεις αὐταὶ νὰ ὑποβάλλωνται γραπτῶς πρὸς τὸ Προεδρεῖον, οὕτως ὥστε νὰ ἀποστέλλωνται εἰς τὸ ἁρμόδιον Ὑπουργεῖον διὰ νὰ εἶναι δυνατόν, ἐὰν ἀποφασίσῃ ὁ Ὑπουργὸς νὰ ἀπαντήσῃ εἰς τὴν ἐρώτησιν, νὰ δίδεται προειδοποίησις ποίαν ἡμέραν καὶ ὥραν θὰ δοθῇ ἡ ἀπάντησις εἰς τὴν ἐρώτησιν. Ὑπάρχουν ἄλλαι εἰσηγήσεις;

B. NALBANTOĞLU :
Temsilciler Meclisi Türk Grubu olarak Sayın Meclis Başkanının teklifini vâfi ve kâfi buluyoruz ve Sayın Meclis Reisine Grubun teşekkürlerini arzederiz.

ΠΡΟΕΔΡΟΣ :
Ὑπάρχουν ἄλλαι προτάσεις; Ὥστε ἀποφασίζεται ὅτι εἰς κάθε συνεδρίασιν θὰ διαθέτωμεν χρονικὴν περίοδον μιᾶς ὥρας δι' ἀπάντησιν εἰς ἐρωτήσεις, ἐὰν ὅμως αἱ ἐρωτήσεις ἀφοροῦν θέματα τῆς Ἐκτελεστικῆς Ἐξουσίας θὰ κατατίθενται γραπτῶς διὰ νὰ διαβιβάζωνται εἰς τὸ ἁρμόδιον Ὑπουργεῖον πρὸς μελέτην καὶ ἀπάντησιν.

ΧΡ. ΜΙΧΑΗΛΙΔΗΣ :
Νὰ καθορισθῇ τὸ χρονικὸν διάστημα ἐντὸς τοῦ ὁποίου πρέπει νὰ ὑποβάλλωνται αἱ ἐρωτήσεις αἵτινες χρήζουν ἀπαντήσεως ἐκ μέρους τῶν Ὑπουργῶν, διὰ νὰ γνωρίζουν τὰ ἔντιμα μέλη τῆς Βουλῆς πρὸ πόσων ἡμερῶν πρέπει νὰ ὑποβάλλωσι ταύτας.

ΠΡΟΕΔΡΟΣ :
Θὰ εἰσηγούμην ὅτι θὰ ἦτο ὀρθὸν ὅπως αἱ ἐρωτήσεις ὑποβάλλωνται τουλάχιστον πέντε ἡμέρας πρὸ τῆς συνεδριάσεως.

ΧΡ. ΔΗΜΗΤΡΙΑΔΗΣ :
Κατόπιν τῆς πολὺ ὀρθῆς ἀποφάσεως τῆς Βουλῆς, ἡ ὁποία ἐλήφθη κατόπιν τῆς προτάσεως ἐπὶ τοῦ θέματος τῶν ἐρωτήσεων, καὶ μέχρις ὅτου γίνουν γραπτοὶ κανονισμοὶ οἱ ὁποῖοι νὰ διέπουν αὐτὰς λεπτομερῶς, εἰσηγοῦμαι τουλάχιστον αὐτὴν τὴν γενικὴν ἀρχὴν ἡ ὁποία ὑπάρχει παντοῦ ὅπου τίθενται ἐρωτήσεις εἰς τὴν Βουλήν, ὅπως, ὅταν δίδεται ἡ ἀπάντησις μέσῳ ἑνὸς Ὑπουργοῦ ἢ μέσῳ τοῦ Προέδρου τῆς Βουλῆς, ὁ ὑποβαλὼν τὴν ἐρώτησιν δύναται νὰ ὁμιλήσῃ ἐπὶ πεντάλεπτον ἐπὶ τοῦ θέματος τῆς ἐρωτήσεως καὶ τῆς δοθείσης ἀπαντήσεως, ἐὰν δὲν εὑρίσκῃ ἱκανοποιητικὴν τὴν ἀπάντησιν, διὰ νὰ κάμῃ τὰς παρατηρήσεις του. Αὐτὸ ἀντιλαμβάνομαι εἶναι μία συνήθης μορφὴ τῆς κοινοβουλευτικῆς διαδικασίας εἰς τὰς περιπτώσεις ἐρωτήσεων καὶ ἐπερωτήσεων, καὶ εἰσηγοῦμαι ὅπως μέχρις ὅτου γίνουν οἱ λεπτομερεῖς κανονισμοὶ ἰσχύσῃ μόνον αὐτὴ ἡ γενικὴ ἀρχή.

ΠΡΟΕΔΡΟΣ :
Τὸ ἔντιμον Μέλος ἐκ Πάφου ἀνεφέρθη εἰς τὸ τὶ συνήθως γίνεται εἰς κοινοβουλευτικὰ πολιτεύματα. Θὰ ἤθελα νὰ τονίσω ὅτι εἰς τὰ κοινοβουλευτικὰ πολιτεύματα, ὁ Ὑπουργὸς ὁ ὁποῖος δίδει τὴν ἀπάντησιν εἶναι κατὰ κανόνα μέλος τῆς Βουλῆς καὶ δύναται νὰ ἀπαντήσῃ ὁ ἴδιος εἰς τὸν Βουλευτὴν ὅστις ἐγείρει τὴν ἐρώτησιν, ἐὰν ὁ Βουλευτὴς ζητήσῃ νὰ ὁμιλήσῃ καὶ εἴπῃ ὅτι δὲν εἶναι ἱκανοποιημένος ἐκ τῆς δοθείσης ἀπαντήσεως. Εἰς τὸ Προεδρικὸν σύστημα τὰ μέλη τοῦ Ὑπουργικοῦ Συμβουλίου δὲν εἶναι μέλη τῆς Βουλῆς, καὶ ἑπομένως γεννᾶται τὸ ζήτημα κατὰ πόσον θὰ ἦτο ὀρθόν, ἐκτὸς ἐὰν πρόκειται περὶ συζητήσεως ἐφ' ὁλοκλήρου τοῦ θέματος καὶ ὄχι ἐπὶ ἐρωτήσεως, νὰ δοθῇ τὸ δικαίωμα εἰς ἕνα Βουλευτὴν νὰ ὑποβάλλῃ οἱανδήποτε ἐρώτησιν ἐπιθυμεῖ καὶ νὰ λέγῃ ὅτι δὲν εἶναι ἱκανοποιημένος ἐκ τῆς ἀπαντήσεως, χωρὶς νὰ ὑπάρχῃ τὸ ἀντίστοιχον δικαίωμα καὶ εἰς τὸ μέλος τῆς Ἐκτελεστικῆς Ἐξουσίας τὸ ὁποῖον ὀφείλει νὰ δώσῃ τὴν ἀπάντησιν. Εἶναι ἕνα θέμα λεπτοτάτης φύσεως τὸ ὁποῖον δὲν ἀμφιβάλλω ὅτι οἱ κανονισμοὶ θὰ ρυθμίσουν, δὲν θὰ ἦτο ὅμως ὀρθόν, προτοῦ οἱ κανονισμοὶ ρυθμίσουν τὸ θέμα, νὰ δώσωμεν τὴν εὐκαιρίαν εἰς τὸν Βουλευτὴν ὁ ὁποῖος ὑποβάλλει τὴν ἐρώτησιν ὑπὸ τύπον αἰτήσεως πρὸς παροχὴν πληροφοριῶν—διότι ἡ ἐρώτησις ὑποβάλλεται οὐχὶ ὡς ἔκφρασις μομφῆς, ἀλλὰ ὡς αἴτησις πρὸς παροχὴν πληροφοριῶν—νὰ κάμνῃ κατάχρησιν τοῦ δικαιώματός του πρὸς λῆψιν ὡρισμένων πληροφοριῶν μὲ τὸ νὰ λέγῃ ὅτι δὲν εἶναι ἱκανοποιημένος. Νομίζω ὅτι ἡ ὀρθὴ γραμμὴ εἰς τὸ στάδιον αὐτὸ θὰ ἦτο ἁπλῶς νὰ ἔχῃ τὸ δικαίωμα νὰ ὑποβάλλῃ ἐρωτήσεις δι' οἱανδήποτε πληροφορίαν ἐπιθυμεῖ, καὶ νὰ μένῃ μέχρι τοῦ σημείου αὐτοῦ. Ἐὰν ἀπὸ τὰς ἀπαντήσεις τὰς ὁποίας θὰ λαμβάνῃ δὲν θὰ εἶναι ἱκανοποιημένος τότε νὰ ἔχῃ τὸ δικαίωμα νὰ ζητήσῃ ὅπως τὸ θέμα ἐγγραφῇ εἰς τὴν ἡμερησίαν διάταξιν διὰ νὰ διεξαχθῇ συζήτησις ἐφ' ὁλοκλήρου τοῦ θέματος.

B. NALBANTOĞLU :
Bu söylediklerinizi bize kim tercüme edecek ?
""",
        """BAŞKAN :
İkinci konuya gelince, sayın üyeden şunu netleştirmesini rica ederim: Her oturumda bir saat ayrılmasını mı öneriyor, yoksa bir saat ayırmanın mümkün ve kolay olup olmayacağını mı soruyor?

B. NALBANTOĞLU :
Biz her toplantıda sorular için ne kadar müddet ayrılacağını Sayın Meclis Başkanından öğrenemedik. Bunun tasrihini istiyoruz.

BAŞKAN :
İç tüzük bu konuyu düzenleyinceye dek sorular meselesinin çözülebileceği üç veya dört yol vardır. Birinci yol, yalnızca sorulara ayrılmış özel bir oturum belirlemektir; ancak yeterli soru birikene kadar üyelerin sormak istediği birçok konu gecikeceğinden bu pratik değildir. Benim önerim, her oturumda Başkanlık veya Meclis üyelerince yanıtlanacak sorular için bir saatlik bir süre ayrılmasıdır. Ancak Meclis üyelerinin yetki alanında olmayan ve bir Bakanın yanıtlamasını gerektiren sorular söz konusuysa, bu sorular Başkanlığa yazılı olarak sunulmalı, ilgili Bakanlığa gönderilmeli ve Bakan yanıtlamaya karar verirse yanıtın hangi gün ve saatte verileceği önceden bildirilmelidir. Başka öneri var mı?

B. NALBANTOĞLU :
Temsilciler Meclisi Türk Grubu olarak Sayın Meclis Başkanının teklifini vâfi ve kâfi buluyoruz ve Sayın Meclis Reisine Grubun teşekkürlerini arzederiz.

BAŞKAN :
Başka öneri var mı? O hâlde her oturumda soruların yanıtlanması için bir saatlik süre ayrılmasına, ancak Yürütme Organını ilgilendiren soruların incelenmek ve yanıtlanmak üzere ilgili Bakanlığa iletilmesi için yazılı olarak sunulmasına karar verilmiştir.

HR. MİHAİLİDİS :
Sayın Meclis üyelerinin kaç gün önceden vermeleri gerektiğini bilmeleri için, Bakanlarca yanıtlanması gereken soruların sunulma süresi belirlensin.

BAŞKAN :
Soruların oturumdan en az beş gün önce sunulmasının doğru olacağını öneririm.

HR. DİMİTRİADİS :
Sorular konusundaki çok yerinde kararın ardından, bunları ayrıntılı olarak düzenleyecek yazılı iç tüzük hazırlanana dek, meclislerde sorular sorulan her yerde geçerli olan şu genel ilkeyi öneriyorum: Bir Bakan veya Meclis Başkanı aracılığıyla yanıt verildiğinde, soruyu soran milletvekili yanıtı tatmin edici bulmazsa, görüşlerini belirtmek üzere soru ve verilen yanıt hakkında beş dakika konuşabilmelidir. Anladığım kadarıyla bu, soru ve gensoru durumlarında olağan bir parlamento usulüdür; ayrıntılı iç tüzük yapılana kadar bu genel ilkenin uygulanmasını öneririm.

BAŞKAN :
Baf'ın sayın üyesi parlamenter sistemlerde genellikle yapılanlara değindi. Vurgulamak isterim ki parlamenter sistemlerde yanıtı veren Bakan kural olarak Meclis üyesidir ve soruyu soran milletvekili yanıttan tatmin olmadığını söylerse Bakan bizzat cevap verebilir. Başkanlık sisteminde ise Bakanlar Kurulu üyeleri Meclis üyesi değildir; dolayısıyla konunun bütünü üzerine bir görüşme yapılmadan, yalnızca bir soru üzerine milletvekiline dilediği soruyu sorup yanıttan tatmin olmadığını söyleme hakkı tanınırken yanıt vermekle yükümlü Yürütme Organı üyesine aynı hakkın tanınmaması doğru olur mu? Bu son derece hassas bir konudur ve iç tüzüğün bunu düzenleyeceğinden şüphem yoktur; ancak iç tüzük düzenlemeden önce, bilgi edinme talebi niteliğindeki soruyu soran milletvekilinin — çünkü soru bir kınama değil, bilgi alma talebidir — tatmin olmadığını söyleyerek bu hakkı suistimal etmesine fırsat vermemek gerekir. Bu aşamada doğru yol, milletvekilinin dilediği her bilgi için soru sorma hakkına sahip olması ve bununla yetinmesidir. Aldığı yanıttan tatmin olmazsa konunun bütünüyle tartışılmak üzere gündeme alınmasını talep etme hakkına sahip olmalıdır.

B. NALBANTOĞLU :
Bu söylediklerinizi bize kim tercüme edecek ?
""",
    ),
    13: (
        """ΠΡΟΕΔΡΟΣ :
Ἡ ἀπάντησις τὴν ὁποίαν ἔχω δώσει ἔχει ἐν ὀλίγοις ὡς ἑξῆς : Ἐπειδὴ τὸ σύστημά μας εἶναι Προεδρικὸν καὶ ὄχι Κοινοβουλευτικόν, καὶ ἐπειδὴ οἱ Ὑπουργοὶ δὲν εἶναι μέλη τῆς Βουλῆς, δὲν θὰ ἦτο ὀρθὸν νὰ δώσωμεν εἰς ἕνα Βουλευτὴν τὸ δικαίωμα νὰ ὑποβάλλῃ μίαν ἐρώτησιν διὰ πληροφοριακοὺς σκοποὺς καὶ νὰ ἐκφράζῃ μομφὴν κατὰ τῆς Κυβερνήσεως λέγων ὅτι δὲν εἶναι ἱκανοποιημένος ἐκ τῆς ἀπαντήσεως, χωρὶς νὰ ἔχῃ τὴν εὐχέρειαν ὁ Ὑπουργὸς εἰς τὸν ὁποῖον ὑπεβλήθη ἡ ἐρώτησις νὰ δώσῃ ἀπάντησιν. Εἰς τὸ μέλλον, ὅταν οἱ κανονισμοὶ τῆς Βουλῆς θὰ ἐξετάσουν τὸ θέμα αὐτό, πιθανὸν νὰ ἀποφασίσουν νὰ δώσουν αὐτὸ τὸ δικαίωμα εἰς τοὺς Βουλευτάς. Μέχρις ὅτου ὅμως θεσπισθοῦν οἱ κανονισμοὶ τῆς Βουλῆς θὰ πρέπει νὰ περιορισθῶμεν εἰς τὸ ζήτημα τῆς ὑποβολῆς ἐρωτήσεων διὰ σκοποὺς πληροφοριακούς, καὶ ἐὰν τὸ ἔντιμον Μέλος τὸ ὁποῖον ὑποβάλλει τὴν ἐρώτησιν δὲν εἶναι ἱκανοποιημένον ἐκ τῆς ἀπαντήσεως, νὰ δύναται τότε νὰ ζητήσῃ, ὅπως τὸ θέμα ἐγγραφῇ εἰς τὴν ἡμερησίαν διάταξιν πρὸς συζήτησιν εἰς τὴν Βουλήν. Ἁπλῶς ὅμως τὸ νὰ ὑποβάλλῃ μίαν ἐρώτησιν, νὰ λαμβάνῃ μίαν ἀπάντησιν καὶ νὰ λέγῃ «δὲν εἶμαι ἱκανοποιημένος», χωρὶς νὰ ὑπάρχῃ τρόπος διὰ τὴν Κυβέρνησιν ὅπως ἀπαντήσῃ εἰς τὴν τελευταίαν παρατήρησιν τοῦ ἐντίμου Μέλους ὅτι δὲν εἶναι ἱκανοποιημένον, νομίζω ὅτι ἡ ἀρχὴ αὕτη δὲν θὰ ἦτο ὀρθὸν νὰ υἱοθετηθῇ ἀπὸ τώρα.

H. A. RIZA :
Son konuşan Sayın Elen Üyenin ileri sürdüğü fikri teyit etmek isterim. Biz, Meclis Üyelerinin sual sormak hakkını sadece "İlgili İcra Organından bilgi almak" olarak saymıyoruz. Meclis Üyesi tenkid yaparken, tenkidini ilgili organın verdiği bilgi üzerine istinad ettirmesini istiyoruz. Bu suretle gelişi güzel tenkidi önlemiş oluruz. Başkanlık rejimine müstenit bir idarede İcra Organı tenkitten muaf değildir. Tenkitleri zabıtlardan dahi takip edebilirler ve ona göre cevap vermek hakları da vardır. Eğer suale verilen cevap üzerine tenkid yapılmıyacaksa, sual sormanın manası yoktur. Sayın Meclis Reisi bunun İç Tüzükte sağlanabileceğini söylemişti. Mademki İç Tüzük yapılmadan sual mevzuunda bir usül takip ediyoruz, cevap alan Üyenin konuşmak hakkını da tanımalıyız. Aksi takdirde kötü bir emsal yaratmaktan korkuyorum.

ΠΡΟΕΔΡΟΣ :
Ὁ κ. Χαλὶτ δὲν νομίζω ὅτι ἀντελήφθη καλῶς ὅ,τι ἔχω πεῖ. Ἐρωτήσεις ὑποβάλλονται ἐκ μέρους ἑνὸς Βουλευτοῦ πρὸς τὴν Ἐκτελεστικὴν Ἐξουσίαν διὰ πληροφοριακὸν σκοπόν, κατὰ πρῶτον. Ἐὰν ἡ ἀπάντησις τὴν ὁποίαν θὰ λάβῃ ἕνας Βουλευτὴς δὲν εἶναι ἱκανοποιητική, δὲν εἶναι ὀρθὸν διὰ τὸν Βουλευτήν, χωρὶς νὰ δώσῃ προειδοποίησιν εἰς τὴν ἡμερησίαν διάταξιν τῆς ἑπομένης συνεδριάσεως ὅτι θὰ ἐγείρῃ αὐτὸ τὸ θέμα πρὸς συζήτησιν, νὰ εἴπῃ ἁπλῶς ὅτι δὲν εἶναι ἱκανοποιημένος ἐκ τῆς ἀπαντήσεως. Ἐὰν δὲν εἶναι ἱκανοποιημένος ἐκ τῆς ἀπαντήσεως θὰ ἦτο ὀρθὸν νὰ θέσῃ τὸ ὅλον θέμα τῆς ἐρωτήσεως ἐπὶ τῆς ἡμερησίας διατάξεως καὶ νὰ ζητήσῃ νὰ εἶναι ὁμιλητὴς ἢ εἰσηγητὴς διὰ νὰ ἐκφράσῃ τὰς ἀπόψεις του, καὶ ἡ Βουλὴ νὰ λάβῃ θέσιν ἐπὶ τοῦ ὅλου ζητήματος. Αἱ ἐρωτήσεις τίθενται κατὰ πρῶτον λόγον διὰ σκοποὺς πληροφοριακούς. Ἐὰν ἡ ἀπάντησις δὲν ἱκανοποιῇ τὸν Βουλευτὴν δὲν εἶναι ὀρθὸν ἁπλῶς καὶ μόνον νὰ ἔχῃ τὸ δικαίωμα νὰ εἴπῃ ὅτι δὲν εἶναι ἱκανοποιημένος, ἀλλὰ νὰ ζητήσῃ ὅπως τὸ θέμα τῆς ἐρωτήσεως καὶ τῆς ἀπαντήσεως συζητηθῇ εἰς συνεδρίασιν τῆς Βουλῆς. Ἐν τοιαύτῃ περιπτώσει τὸ θέμα θὰ ἐγγραφῇ εἰς τὴν ἡμερησίαν διάταξιν καὶ θὰ ὁρισθῇ ἡμερομηνία πρὸς συζήτησιν. Ὁπότε, ὄχι μόνον ὁ Βουλευτὴς ὁ ὁποῖος ἤγειρε τὴν ἐρώτησιν θὰ ἔχῃ τὸ δικαίωμα νὰ ἐκφράσῃ τὴν ἄποψίν του, ἀλλὰ καὶ οἱονδήποτε ἄλλον μέλος τῆς Βουλῆς ἐπιθυμεῖ, θὰ δύναται νὰ ἐκφράσῃ ἄποψιν ἢ νὰ λάβῃ μέρος εἰς τὴν συζήτησιν. Δὲν εἰσηγήθην ὅπως αἱ πράξεις τῆς Ἐκτελεστικῆς Ἐξουσίας εἰς ἕνα Προεδρικὸν σύστημα χαίρουν ἀσυδοσίας ἔναντι τῆς Βουλῆς. Τουναντίον εἰσηγήθην ὅτι κριτικὴ δύναται νὰ γίνῃ ἀλλ' ἀφοῦ ἀκολουθήσωμεν ὡρισμένην διαδικασίαν.

H. A. RIZA :
Sayın Meclis Reisinin söylediklerini pek iyi anladım ve tehlikeli gördüğüm için bilhassa Meclisi ikaz etmek istiyorum. Eğer tenkid mevzuu gündeme alınarak müzakere edilecekse, Meclisteki şahsî hürriyeti öldürmüş olur. Çünkü, eğer bunu Meclis Reisi kendisi koymazsa, gündeme alınması için Meclis ekseriyetinin reyi lâzımdır. Bu da, tabiîdir ki, demokrasinin tamamen imhası demektir.

ΠΡΟΕΔΡΟΣ :
Δὲν εἰσηγήθην ὅτι διὰ νὰ συμπεριληφθῇ εἰς τὴν ἡμερησίαν διάταξιν, διαρκούσης τῆς περιόδου κατὰ τὴν ὁποίαν δὲν θὰ ὑπάρχουν κανονισμοί, θὰ χρειάζεται πλειοψηφία ἢ ὅ,τιδήποτε ἄλλο. Ἁπλῶς εἰσηγήθην ὅτι ὡς Βουλὴ εἰς τὸ παρὸν στάδιον δὲν ἔχομεν διάταξιν περὶ τῆς μεθόδου κατὰ τὴν ὁποίαν θὰ ὑποβάλλωνται ἐρωτήσεις πρὸς τὴν Ἐκτελεστικὴν Ἐξουσίαν. Ἐν τῇ ἐπιθυμίᾳ πάντων καὶ τῆς ἰδικῆς μου ἐπιθυμίας ὅπως μὴ βραδύνωμεν νὰ θέσωμεν εἰς ἐφαρμογὴν τὸ σύστημα αὐτό, εἰσηγήθην ὅπως ἀποφασίσωμεν νὰ διαθέτωμεν μίαν ὥραν εἰς κάθε συνεδρίασιν διὰ τὸν σκοπὸν τῶν ἐρωτήσεων. Καὶ εἰσηγήθην περαιτέρω ὅτι ὁ Βουλευτὴς ὁ ὁποῖος θὰ λάβῃ ἀπάντησιν, ἀντὶ νὰ ἔχῃ ἁπλῶς τὸ δικαίωμα νὰ λέγῃ ὅτι διαφωνεῖ ἢ δὲν εἶναι ἱκανοποιημένος ἐκ τῆς ἀπαντήσεως, νὰ ἔχῃ τὸ δικαίωμα νὰ ἐγείρῃ τὸ θέμα αὐτὸ πρὸς συζήτησιν διὰ τὴν ἑπομένην συνεδρίασιν, καὶ τοῦτο πάλιν ὑπὸ μορφὴν προσωρινῆς λύσεως μέχρις ὅτου οἱ κανονισμοὶ ἐπιληφθοῦν τοῦ ὅλου ζητήματος.

ΧΡ. ΔΗΜΗΤΡΙΑΔΗΣ :
Ἡ διαδικασία τὴν ὁποίαν προτείνετε ὡς προσωρινὴν λύσιν βεβαίως θὰ ἦτο πολὺ ὀρθή, ἐὰν δυστυχῶς, κατὰ τὴν γνώμην μου, δὲν ἀντέκειτο πρὸς ρητὴν διάταξιν τοῦ Συντάγματος.
""",
        """BAŞKAN :
Verdiğim yanıt özetle şöyledir: Sistemimiz Parlamenter değil Başkanlık sistemi olduğundan ve Bakanlar Meclis üyesi olmadığından, bir milletvekiline bilgi edinme amaçlı bir soru sorup ardından ilgili Bakanın yanıt verme olanağı olmaksızın "yanıttan tatmin olmadım" diyerek Hükümete kınama yöneltme hakkı tanımak doğru olmaz. Gelecekte Meclis İç Tüzüğü bu konuyu ele aldığında belki bu hakkı milletvekillerine vermeye karar verebilir. Ancak İç Tüzük yasalaşıncaya kadar yalnızca bilgi amaçlı soru sormakla yetinmeliyiz; soruyu soran sayın üye yanıttan tatmin olmazsa konunun Mecliste tartışılmak üzere gündeme alınmasını isteyebilir. Fakat Hükümetin cevap verme imkânı olmaksızın yalnızca "tatmin olmadım" deme ilkesinin şimdiden benimsenmesinin doğru olmadığı kanısındayım.

H. A. RIZA :
Son konuşan Sayın Elen Üyenin ileri sürdüğü fikri teyit etmek isterim. Biz, Meclis Üyelerinin sual sormak hakkını sadece "İlgili İcra Organından bilgi almak" olarak saymıyoruz. Meclis Üyesi tenkid yaparken, tenkidini ilgili organın verdiği bilgi üzerine istinad ettirmesini istiyoruz. Bu suretle gelişi güzel tenkidi önlemiş oluruz. Başkanlık rejimine müstenit bir idarede İcra Organı tenkitten muaf değildir. Tenkitleri zabıtlardan dahi takip edebilirler ve ona göre cevap vermek hakları da vardır. Eğer suale verilen cevap üzerine tenkid yapılmıyacaksa, sual sormanın manası yoktur. Sayın Meclis Reisi bunun İç Tüzükte sağlanabileceğini söylemişti. Mademki İç Tüzük yapılmadan sual mevzuunda bir usül takip ediyoruz, cevap alan Üyenin konuşmak hakkını da tanımalıyız. Aksi takdirde kötü bir emsal yaratmaktan korkuyorum.

BAŞKAN :
Bay Halit'in söylediklerimi tam olarak anladığını sanmıyorum. Bir milletvekilince Yürütme Organına sorular öncelikle bilgi edinme amacıyla sorulur. Milletvekilinin aldığı yanıt tatmin edici değilse, bir sonraki oturumun gündeminde bu konuyu tartışmaya açacağına dair bildirimde bulunmaksızın yalnızca tatmin olmadığını söylemesi doğru değildir. Yanıttan tatmin olmadıysa, sorunun bütününü gündeme aldırarak görüşlerini açıklamak üzere konuşmacı olmayı talep etmesi ve Meclisin de tüm mesele hakkında tutum alması doğru olur. Bu durumda yalnız soruyu soran milletvekili değil, dileyen herhangi bir Meclis üyesi de görüşünü açıklayabilir ve tartışmaya katılabilir. Başkanlık sisteminde Yürütme Organının eylemlerinin Meclis karşısında dokunulmaz olmasını önermedim; aksine eleştirinin yapılabileceğini, ancak belirli bir usul izlenerek yapılması gerektiğini önerdim.

H. A. RIZA :
Sayın Meclis Reisinin söylediklerini pek iyi anladım ve tehlikeli gördüğüm için bilhassa Meclisi ikaz etmek istiyorum. Eğer tenkid mevzuu gündeme alınarak müzakere edilecekse, Meclisteki şahsî hürriyeti öldürmüş olur. Çünkü, eğer bunu Meclis Reisi kendisi koymazsa, gündeme alınması için Meclis ekseriyetinin reyi lâzımdır. Bu da, tabiîdir ki, demokrasinin tamamen imhası demektir.

BAŞKAN :
İç tüzük bulunmayan bu dönemde bir konunun gündeme alınması için çoğunluk ya da başka bir şart gerekeceğini önermedim. Sadece Meclis olarak şu aşamada Yürütme Organına soru sorma usulüne dair bir hükmümüz olmadığını belirttim. Bu sistemi gecikmeden uygulamaya koymak adına her oturumda sorulara bir saat ayırmamızı ve yanıt alan milletvekilinin, sadece tatmin olmadığını söylemek yerine geçici çözüm olarak bir sonraki oturumda bu konuyu tartışmaya açma hakkına sahip olmasını önerdim.

HR. DİMİTRİADİS :
Geçici çözüm olarak önerdiğiniz usul elbette çok doğru olurdu; ancak ne yazık ki benim görüşüme göre Anayasanın açık bir hükmüne aykırıdır.
""",
    ),
    14: (
        """ΠΡΟΕΔΡΟΣ :
Κύριε Χρ. Δημητριάδη, διὰ νὰ μὴ κωλυσιεργοῦμεν περισσότερον, ὁ Πρόεδρος καταρτίζει τὴν ἡμερησίαν διάταξιν. Ὁ Πρόεδρος ἀναλαμβάνει δέσμευσιν ἔναντι τῆς Βουλῆς αὐτῆς ὅτι οἱαδήποτε ἐρώτησις τεθῇ ὑπὸ Βουλευτοῦ, ὅταν ὁ Βουλευτής του εἴπῃ ὅτι δὲν εἶναι ἱκανοποιημένος ἐκ τῆς ἀπαντήσεως, θὰ τὴν συμπεριλάβῃ εἰς τὴν ἡμερησίαν διάταξιν τῆς ἑπομένης συνεδριάσεως. Αὐτὸ εἶναι. Μέχρις ὅτου γίνουν οἱ κανονισμοὶ τῆς Βουλῆς. Εἶχα ὑπ' ὄψιν μου ὅτι χρειάζεται πλειοψηφία, ἀλλ' ἁπλῶς ὁ Πρόεδρος δεσμεύεται ἔναντι τῆς Βουλῆς ὡς πρὸς τὸ παρὸν μέχρις ὅτου γίνουν κανονισμοί.
Ὑπάρχουν ἄλλαι εἰσηγήσεις ἐπὶ τοῦ θέματος αὐτοῦ; Προτοῦ κηρύξω τὴν λῆξιν τῆς συνεδριάσεως αὐτῆς εἶναι ἀνάγκη συμφώνως τοῦ ἄρθρου 76 (2) τοῦ Συντάγματος ὅπως ὁρίσωμεν τὴν ἡμέραν καὶ ὥραν τῆς ἑπομένης συνεδριάσεως. Εἰσηγοῦμαι τὴν 16ην Σεπτεμβρίου.
Εἰς τὴν ἑπομένην συνεδρίασιν τῆς Βουλῆς θὰ εἶναι ἀνάγκη ὅπως ἐπιληφθῶμεν ὡρισμένων νομοσχεδίων δι' ἐπείγοντα θέματα, ὡς τὸ θέμα τοῦ προσωπικοῦ τῆς Βουλῆς διὰ νὰ καθορισθῇ διὰ νόμου ποῖαι θὰ εἶναι αἱ θέσεις καὶ ἡ μισθοδοσία, διὰ νὰ δυνηθῶμεν νὰ προχωρήσωμεν μὲ τὴν ἐργασίαν. Ἐπίσης ὑπάρχουν ὡρισμένα ἄλλα νομοσχέδια ἐκ τῶν ὁποίων εἶναι καὶ ἓν διὰ ποσὸν £300,000 τὸ ὁποῖον θὰ διατεθῇ δι' ἀνακουφιστικὰ ἔργα σχετικὰ μὲ τὸ ἀνεργιακὸν πρόβλημα. Εἶναι ἀνάγκη ὅπως τὰ νομοσχέδια αὐτὰ σταλοῦν εἰς τὰς Ἐπιτροπὰς προτοῦ ἔλθουν ἐνώπιον τῆς Βουλῆς. Εἶναι ἐπίσης ἀνάγκη ὅπως ταῦτα συνταχθοῦν Ἑλληνιστὶ καὶ Τουρκιστί. Εἶναι ἐπίσης ἀνάγκη ὅπως μετὰ τὰς Ἐπιτροπὰς ἀποσταλοῦν εἰς ἅπαντα τὰ μέλη τῆς Βουλῆς μετὰ τῆς ἐκθέσεως τῆς Ἐπιτροπῆς, τουλάχιστον 48 ὥρας πρὸ τῆς ἐνάρξεως τῆς συνεδριάσεως.
Ὁμοφώνως ἀποφασίζεται ὅπως ἡ ἑπομένη συνεδρίασις τῆς Βουλῆς ὁρισθῇ διὰ τὴν 16ην Σεπτεμβρίου, καὶ εἰσηγοῦμαι τὴν 5ην ἀπογευματινὴν ὥραν. Τὰ δύο θέματα τὰ ὁποῖα εἶναι βέβαιον ὅτι θὰ εἶναι ἕτοιμα εἶναι πρῶτον «Συζήτησις νομοσχεδίου περὶ τῆς συνθέσεως τοῦ προσωπικοῦ τῆς Βουλῆς τῶν Ἀντιπροσώπων». Δεύτερον θέμα «Συζήτησις νομοσχεδίου περὶ ἀποζημιώσεως τῶν μελῶν τῆς Βουλῆς τῶν Ἀντιπροσώπων». Τὸ τρίτον θέμα τὸ ὁποῖον ἔχω ἤδη ἀναφέρει εἶναι νομοσχέδιον διὰ τὴν διάθεσιν ποσοῦ £300,000 περίπου διὰ τὸ ἀνεργιακὸν πρόβλημα. Συμφώνως τοῦ ἄρθρου 76 τοῦ Συντάγματος κηρύττω τὴν λῆξιν τῆς συνεδριάσεως αὐτῆς, καὶ παρακαλῶ τοὺς κ.κ. γραμματεῖς ὅπως σημειώσουν τὸν χρόνον τῆς λήξεως τῶν ἐργασιῶν τῆς συνεδριάσεως. (Ὥρα λήξεως 7.15 μ.μ. / Sona eriş saati : ö.s. 7.15.)
""",
        """BAŞKAN :
Sayın Hr. Dimitriadis, daha fazla vakit kaybetmemek adına: Gündemi Başkan hazırlar. Başkan bu Meclis önünde şu taahhüdü üstlenir: Bir milletvekilince sorulan herhangi bir soruda milletvekili verilen yanıttan tatmin olmadığını belirttiğinde, Başkan bu konuyu bir sonraki oturumun gündemine mutlaka alacaktır. İşte bu kadar — Meclis İç Tüzüğü hazırlanıncaya dek Başkan Meclise karşı şimdilik bu taahhüdü vermektedir.
Bu konuda başka öneri var mı? Oturumu kapatmadan önce Anayasanın 76(2). maddesi uyarınca bir sonraki oturumun gün ve saatini belirlememiz gerekmektedir. 16 Eylül gününü öneriyorum.
Bir sonraki oturumda acil konulara ilişkin bazı yasa tasarılarını ele almamız gerekecektir: İşlerimizi yürütebilmemiz için kadroları ve maaşları yasayla belirleyecek olan Meclis personeli yasası gibi. Ayrıca, işsizlik sorununa yönelik rahatlatıcı projeler için ayrılacak 300.000 sterlin tutarındaki ödenek yasası dâhil başka tasarılar da vardır. Bu tasarıların Meclis önüne gelmeden önce komitelere gönderilmesi, hem Yunanca hem Türkçe hazırlanması ve komite raporuyla birlikte oturumdan en az 48 saat önce tüm Meclis üyelerine ulaştırılması gerekmektedir.
Meclisin bir sonraki oturumunun 16 Eylül günü saat 17.00'de yapılması oybirliğiyle kararlaştırılmıştır. Hazır olacağı kesin olan konular şunlardır: Birincisi, "Temsilciler Meclisi personelinin yapısına ilişkin yasa tasarısı"; ikincisi, "Temsilciler Meclisi üyelerinin ödeneklerine ilişkin yasa tasarısı"; üçüncüsü ise işsizlik sorunu için yaklaşık 300.000 sterlin tahsisine ilişkin yasa tasarısıdır. Anayasanın 76. maddesi uyarınca oturumu kapatıyorum; sayın kâtiplerden kapanış saatini kaydetmelerini rica ederim. (Sona eriş saati : ö.s. 7.15.)
""",
    ),
    15: (
        """ΣΥΝΕΔΡΙΑΣΙΣ ΤΗΣ 16ης ΣΕΠΤΕΜΒΡΙΟΥ 1960
(Ὥρα ἐνάρξεως 5.05 μ.μ.)
16 EYLÜL 1960 TARİHLİ TOPLANTI
(Başlangıç saati : ö.s. 5.05)

ΠΡΟΕΔΡΟΣ :
Συμφώνως τοῦ ἄρθρου 76 (1) τοῦ Συντάγματος κηρύσσω τὴν ἔναρξιν τῆς Συνεδριάσεως αὐτῆς. Τὸ πρῶτον θέμα ἐπὶ τῆς ἡμερησίας διατάξεως εἶναι αἱ ἐρωτήσεις αἱ ὑποβληθεῖσαι ὑπὸ ἐντίμων Βουλευτῶν, καὶ αἱ ἀπαντήσεις αἱ ὁποῖαι ἐλήφθησαν ἀπὸ τὰ ἐνδιαφερόμενα Ὑπουργεῖα. Προτοῦ προβῶμεν εἰς τὴν ἀνάγνωσιν τῶν ἐρωτήσεων καὶ ἀπαντήσεων, καλῶ τοὺς Γραμματεῖς τῆς Βουλῆς τῶν Ἀντιπροσώπων ὅπως διαπιστώσουν ἐὰν ὑπάρχῃ ἢ ὄχι ἀπαρτία.
Πληροφοροῦμαι ἀπὸ τὴν Γραμματείαν ὅτι ὑπάρχει ἀπαρτία. Καλῶ τὸν ἔντιμον Γραμματέα κ. Λέλλον Δημητριάδην καὶ τὸν Τοῦρκον Γραμματέα ὅπως ἀναγνώσουν τὰς ὑποβληθείσας ἐρωτήσεις, παρακολουθοῦντες αὐστηρῶς τὴν σειρὰν κατὰ τὴν ὁποίαν αὗται ὑπεβλήθησαν εἰς τὴν Βουλήν. Ἐρωτήσεις ὑποβληθεῖσαι ὑπὸ Ἑλλήνων Βουλευτῶν καὶ ἀπαντηθεῖσαι ὑπὸ Ἑλλήνων Ὑπουργῶν θὰ ἀναγνωσθοῦν πρῶτον εἰς τὴν Ἑλληνικὴν γλῶσσαν, καὶ ἀκολούθως θὰ ἀναγνωσθῇ μετάφρασίς των εἰς τὴν Τουρκικὴν τοιαύτην. Τὸ ἴδιον ἰσχύει δι' ἐρωτήσεις αἵτινες ὑπεβλήθησαν ὑπὸ Τούρκων Βουλευτῶν. Καλοῦνται οἱ Γραμματεῖς νὰ σημειώσουν ὅτι ἡ ὥρα εἶναι 5.10 μ.μ. διότι τὸ ὅλον χρονικὸν διάστημα τὸ ὁποῖον θὰ διατεθῇ διὰ τὸν σκοπὸν ἐρωτήσεων καὶ ἀπαντήσεων εἶναι μία ὥρα συμφώνως προηγουμένης ἀποφάσεως τῆς Βουλῆς.

ΓΡΑΜΜΑΤΕΥΣ :
Ὑπεβλήθησαν ὑπὸ τῶν κ.κ. Βουλευτῶν (35) ἐν ὅλῳ ἐρωτήσεις. Ἐκ τούτων ἐδόθη ἀπάντησις ὑπὸ τῶν Ἁρμοδίων εἰς ἓξ περιπτώσεις. Αἱ ἐρωτήσεις ἔχουν ὡς ἀκολούθως :
Ἐρώτησις ὑποβληθεῖσα τὴν 1ην Σεπτεμβρίου 1960, ὑπὸ τῶν ἐντίμων Βουλευτῶν κ. Γ. Ποταμίτη (Λεμεσοῦ) καὶ κ. Χρύση Δημητριάδη (Πάφου) : «Ποῖοι λόγοι ὤθησαν τοὺς Ὑπουργοὺς Ἐμπορίου καὶ Βιομηχανίας, Οἰκονομικῶν καὶ Γεωργίας νὰ ὁρίσουν καὶ ἀργότερον παρ' ὅλας τὰς παραστάσεις τῶν ἀμπελουργῶν νὰ μὴν ἀναθεωρήσουν τὰς ὁρισθείσας τιμὰς ἀμπελουργικῶν προϊόντων, δεδομένου ὅτι ὡς εἶναι γενικῶς δεκτὸν ὄχι μόνον ὑπὸ τῶν ἀμπελουργῶν ἀλλὰ καὶ ὑπὸ τῶν ἁρμοδίων Συνεργατικῶν Ὀργανισμῶν ἡ ὁρισθεῖσα τιμὴ 22½ μὶλς κατ' ὀκὰν σταφυλῶν δὲν καλύπτει τὸν μέσον ὅρον τοῦ κόστους παραγωγῆς τῶν σταφυλῶν, διὰ δὲ τὰς ὀρεινὰς περιοχὰς εἶναι πολὺ χαμηλοτέρα τοῦ κόστους παραγωγῆς».

KÂTİP :
Leymosun Temsilcisi Sayın G. Potamitis ile Baf Temsilcisi Sayın Hrisis Demetriades'in 1 Eylül 1960 tarihli müşterek soruları :—
"Üzüm fiatının okka başına 22½ mil olarak tesbit edilmesinin ortalama istihsal masrafını karşılamadığının ve dağlık bölgeler için istihsal masrafından çok daha düşük olduğunun yalnız üzüm müstahsilleri tarafından değil fakat ayni zamanda yetkili Kooperatif Organizasyonları tarafından da genel olarak kabul edildiği cihetle, Ticaret ve Sanayi Bakanı ile Ziraat ve Tabii Kaynaklar Bakanını, mezkûr fiatları tesbit etmeğe ve daha sonra müstahsillerinin teşebbüslerine rağmen tesbit edilen fiatı yeniden gözden geçirmeğe sevkeden sebepler nelerdir ?"

ΓΡΑΜΜΑΤΕΥΣ :
Ἐρώτησις ὑποβληθεῖσα τὴν 1ην Σεπτεμβρίου 1960, ὑπὸ τοῦ ἐντίμου Βουλευτοῦ κ. Χρύση Δημητριάδη (Πάφου) : «Ἐν ὄψει τῶν εἰς τὸν ἐγχώριον καὶ ἐξωτερικὸν τύπον δημοσιευθεισῶν πληροφοριῶν σχετικῶς μὲ τὸ ναζιστικὸν παρελθὸν τοῦ διορισθέντος Προέδρου τοῦ Ἀνωτάτου Συνταγματικοῦ Δικαστηρίου κ. Ἔρνστ Φόρστχοφ, καὶ ἐν ὄψει τοῦ γεγονότος ὅτι εἶναι παραδεκτὸν καὶ ὑπὸ τοῦ ἰδίου ὅτι εἶναι συγγραφεὺς βιβλίου ὑποστηρίζοντος τὸ ὁλοκληρωτικὸν κράτος, καὶ ἐν ὄψει τοῦ γεγονότος ὅτι αἱ γνώσεις του τῆς Ἀγγλικῆς εἶναι πτωχαί, πρᾶγμα τὸ ὁποῖον καθιστᾷ ἀδύνατον τὴν ὑπ' αὐτοῦ ἑρμηνείαν τοῦ Κυπριακοῦ Συντάγματος, ὅπερ θὰ εἶναι καὶ τὸ κυριώτερον ἔργον του, καὶ ἐν ὄψει τοῦ γεγονότος ὅτι προτίθεται νὰ διατηρήσῃ τὴν ἕδραν τοῦ Καθηγητοῦ τοῦ Πανεπιστημίου τῆς Χαϊδελβέργης, πρᾶγμα τὸ ὁποῖον σοβαρῶς θὰ ἐπηρεάζῃ τὴν ὁμαλὴν λειτουργίαν τοῦ Ἀνωτάτου Συνταγματικοῦ Δικαστηρίου. Ἐρωτᾶται : Διατὶ οὗτος διωρίσθη εἰς τὴν τόσον ὑπεύθυνον αὐτὴν θέσιν, ὑπὸ ποίους ὅρους ἐγένετο ὁ διορισμός του, καὶ ἐὰν κατόπιν τῶν μὴ ἱκανοποιητικῶν ἐξηγήσεων αἵτινες ἐδόθησαν ὑπ' αὐτοῦ ὑπάρχει πρόθεσις παύσεως αὐτοῦ».

KÂTİP :
Baf Temsilcisi Sayın Hrisis Demetriades'in 1 Eylül 1960 tarihli sorusu :—
"Yüksek Anayasa Mahkemesi Reisliğine tâyin edilen Bay Earnst Forsthoff'un geçmişte bir Nazi olduğuna dair yerli ve yabancı basında yayınlanan haberler muvacehesinde ve Bay Forsthoff'un totaliter devlet sistemini destekliyen bir kitabın yazarı olduğunu bizzat kabul etmesi karşısında ve Mr. Forsthoff'un İngilizcesinin zayıf olduğu ve bu yüzden Kıbrıs Anayasasını tefsir edemiyeceği, halbuki Anayasanın tefsirinin onun başlıca vazifesi olduğu ve ayrıca Bay Forsthoff'un Heidelberg Üniversitesinde öğretmenlik vazifesine devam edeceğini ve bunun, Yüksek Anayasa Mahkemesinin düzenli bir şekilde işlemesine tesir edeceğini göz önünde tutarak, Bu zatın, bu kadar mes'uliyetli bir mevkie niçin tâyin edildiğini, tâyininin hangi şartlar altında kabul olunduğunu ve kendisinin verdiği, fakat tatminkâr olmıyan izahattan sonra vazifesine son verilmesinin düşünülüp düşünülmediğini sorabilir miyiz ?"
""",
        """16 EYLÜL 1960 TARİHLİ TOPLANTI
(Başlangıç saati : ö.s. 5.05)

BAŞKAN :
Anayasanın 76(1). maddesi uyarınca bu oturumu açıyorum. Gündemin ilk maddesi sayın milletvekillerince sunulan sorular ve ilgili Bakanlıklardan alınan yanıtlardır. Soru ve yanıtların okunmasına geçmeden önce Temsilciler Meclisi Kâtiplerini toplantı yeter sayısı (nisap) bulunup bulunmadığını tespit etmeye davet ediyorum.
Sekreterlikten yeter sayının mevcut olduğu bildirildi. Sayın Kâtip Bay Lellos Dimitriadis ile Türk Kâtibi, sunulan soruları Meclise veriliş sırasına sıkı sıkıya uyarak okumaya davet ediyorum. Rum milletvekillerince sorulan ve Rum Bakanlarca yanıtlanan sorular önce Yunanca okunacak, ardından Türkçe tercümeleri okunacaktır; Türk milletvekillerince sorulan sorular için de aynı usul geçerlidir. Kâtiplerden saatin 17.10 olduğunu kaydetmelerini rica ediyorum; zira Meclisin önceki kararı uyarınca soru ve yanıtlara ayrılan toplam süre bir saattir.

ΓΡΑΜΜΑΤΕΥΣ :
Sayın milletvekilleri tarafından toplam 35 soru sunulmuştur. Bunlardan altısına yetkili makamlarca yanıt verilmiştir. Limasol milletvekili Bay G. Potamitis ile Baf milletvekili Bay Hrisis Dimitriadis'in 1 Eylül 1960 tarihli sorusu: "Üzüm fiyatının okka başına 22,5 mil olarak belirlenmesinin ortalama üretim maliyetini karşılamadığı ve dağlık bölgelerde üretim maliyetinin çok altında kaldığı yalnız bağcılarca değil yetkili Kooperatif Örgütlerince de genel kabul gördüğü hâlde, Ticaret ve Sanayi, Maliye ve Tarım Bakanlarını bu fiyatları belirlemeye ve üreticilerin tüm girişimlerine rağmen gözden geçirmemeye iten sebepler nelerdir?"

KÂTİP :
Leymosun Temsilcisi Sayın G. Potamitis ile Baf Temsilcisi Sayın Hrisis Demetriades'in 1 Eylül 1960 tarihli müşterek soruları :—
"Üzüm fiatının okka başına 22½ mil olarak tesbit edilmesinin ortalama istihsal masrafını karşılamadığının ve dağlık bölgeler için istihsal masrafından çok daha düşük olduğunun yalnız üzüm müstahsilleri tarafından değil fakat ayni zamanda yetkili Kooperatif Organizasyonları tarafından da genel olarak kabul edildiği cihetle, Ticaret ve Sanayi Bakanı ile Ziraat ve Tabii Kaynaklar Bakanını, mezkûr fiatları tesbit etmeğe ve daha sonra müstahsillerinin teşebbüslerine rağmen tesbit edilen fiatı yeniden gözden geçirmeğe sevkeden sebepler nelerdir ?"

ΓΡΑΜΜΑΤΕΥΣ :
Baf milletvekili Bay Hrisis Dimitriadis'in 1 Eylül 1960 tarihli sorusu: "Yüksek Anayasa Mahkemesi Başkanlığına atanan Bay Ernst Forsthoff'un Nazi geçmişine ilişkin yerli ve yabancı basında çıkan haberler, kendisinin de totaliter devleti savunan bir kitabın yazarı olduğunu kabul etmesi, İngilizce bilgisinin yetersizliğinin başlıca görevi olan Kıbrıs Anayasasını yorumlamasını imkânsız kılması ve Heidelberg Üniversitesindeki profesörlük kürsüsünü koruyarak Yüksek Anayasa Mahkemesinin düzenli işleyişini ciddi biçimde etkileyecek olması karşısında: Bu kişi bu denli sorumlu bir makama neden atanmıştır, atanma şartları nelerdir ve verdiği tatmin edici olmayan açıklamaların ardından görevden alınması düşünülmekte midir?"

KÂTİP :
Baf Temsilcisi Sayın Hrisis Demetriades'in 1 Eylül 1960 tarihli sorusu :—
"Yüksek Anayasa Mahkemesi Reisliğine tâyin edilen Bay Earnst Forsthoff'un geçmişte bir Nazi olduğuna dair yerli ve yabancı basında yayınlanan haberler muvacehesinde ve Bay Forsthoff'un totaliter devlet sistemini destekliyen bir kitabın yazarı olduğunu bizzat kabul etmesi karşısında ve Mr. Forsthoff'un İngilizcesinin zayıf olduğu ve bu yüzden Kıbrıs Anayasasını tefsir edemiyeceği, halbuki Anayasanın tefsirinin onun başlıca vazifesi olduğu ve ayrıca Bay Forsthoff'un Heidelberg Üniversitesinde öğretmenlik vazifesine devam edeceğini ve bunun, Yüksek Anayasa Mahkemesinin düzenli bir şekilde işlemesine tesir edeceğini göz önünde tutarak, Bu zatın, bu kadar mes'uliyetli bir mevkie niçin tâyin edildiğini, tâyininin hangi şartlar altında kabul olunduğunu ve kendisinin verdiği, fakat tatminkâr olmıyan izahattan sonra vazifesine son verilmesinin düşünülüp düşünülmediğini sorabilir miyiz ?"
""",
    ),
    16: (
        """ΓΡΑΜΜΑΤΕΥΣ :
Ἐρώτησις ὑποβληθεῖσα τὴν 1ην Σεπτεμβρίου 1960, ὑπὸ τοῦ ἐντίμου Βουλευτοῦ Λεμεσοῦ κ. Γ. Ποταμίτη : «Ἐν ὄψει τοῦ γεγονότος ὅτι ἔχει συνταχθῆ ἀπὸ καιροῦ Σχέδιον Κανονισμῶν προνοούντων περὶ πληρωμῆς συντάξεων εἰς ἀποχωροῦντας τῆς ἐργασίας δικηγόρους, ἐρωτᾶται ἐὰν ὁ ἁρμόδιος Ὑπουργὸς προτίθεται καὶ πότε νὰ ὑποβάλῃ εἰς τὴν Βουλὴν τὸ ρηθὲν σχέδιον κανονισμῶν καὶ ἐὰν ἡ Κυβέρνησις προτίθεται νὰ ὑποβοηθήσῃ οἰκονομικῶς καὶ κατὰ ποῖον τρόπον τὴν λειτουργίαν τοῦ Ταμείου Συντάξεως Νομικῶν».
Ἀπάντησις Ὑπουργοῦ Δικαιοσύνης : «Συμφώνως πρὸς τὸ ἄρθρον 22 τοῦ περὶ Δικηγόρων Νόμου (Κεφ. 2) ἡ σύνταξις Κανονισμῶν περὶ Ἱδρύσεως Ταμείου Συντάξεως Δικηγόρων ἐμπίπτει εἰς τὴν ἁρμοδιότητα τοῦ Συμβουλίου τοῦ Δικηγορικοῦ Σώματος. Τὰ μέλη τοῦ Συμβουλίου τούτου ὑπέβαλον παραίτησιν κατὰ τὴν διάρκειαν τῆς ἐκτάκτου ἀνάγκης, καὶ ἤδη διευθετήσεις πρὸς ἐπανασύστασιν τοῦ Συμβουλίου γίνονται. Οἱ ἀνωτέρω κανονισμοί, συμφώνως τοῦ ρηθέντος Νόμου, θὰ δημοσιευθοῦν εἰς τὴν ἐπίσημον ἐφημερίδα τῆς Δημοκρατίας».

KÂTİP :
Leymosun Temsilcisi Sayın G. Potamitis'in 1 Eylül 1960 tarihli sorusu :—
"Bundan bir müddet evvel işten ayrılan avukatlara tekaüdiye ödenmesini derpiş eden bir Kanun Tasarısı yapıldığı ve yaşlı hukukçuları sıkıntıdan kurtarmak için tatbikat sahasına konmasının müstacel ve zaruri bir mesele olduğu göz önünde tutularak, Salâhiyettar Bakanın, mezkûr Kanun Tasarısını Meclise sunmak niyetinde olup olmadığını ve eğer sunacaksa ne zaman sunacağını ve Hükûmetin mezkûr Kanunda zikredilen Hukukçular Tekaüdiye Sandığının işlemesine, Yunanistan'da ve sair memleketlerde olduğu gibi, iktisaden yardım etmek niyetinde olup olmadığını ve bu yardımın ne şekilde yapılmasının düşünüldüğünü sormak isteriz."
Leymosun Temsilcisi Sayın G. Potamitis'in 1 Eylül 1960 tarihli sorusuna Adalet Bakanının cevabı :—
"Avukatlar Kanununun 22'nci Maddesi (Bölüm 2) tahtinde, Avukatlar Tekaüdiye Sandığı Kurulmasına dair Nizamnameleri hazırlama işi Avukatlar Cemiyeti Konseyinin Salâhiyeti çerçevesine girer. Sayın Temsilcinin bildiği gibi, bu Konseyin üyeleri olağanüstü durum sırasında istifa etmişlerdir ve şimdi Konseyin yeniden kurulması için tertibat alınmaktadır. Şüphe yoktur ki yeni kurulacak Konseyi meşgul edecek meselelerden biri de mezkûr Nizamnameleri hazırlamak olacaktır. Yukarıda zikredilen Kanun tahtinde hazırlanan nizamnameler, Cumhuriyetin Resmî Gazetesinde yayınlanacaktır."

ΓΡΑΜΜΑΤΕΥΣ :
Ἐρώτησις ὑποβληθεῖσα τὴν 1ην Σεπτεμβρίου 1960, ὑπὸ τοῦ ἐντίμου Βουλευτοῦ Λεμεσοῦ κ. Γ. Ποταμίτη : «Δεδομένου ὅτι ὁ Νόμος 44 τοῦ 1958, θεσπισθεὶς ὑπὸ τῆς Ἀποικιακῆς Κυβερνήσεως, ηὔξησε σημαντικῶς τὰ δικαιώματα τὰ πληρωτέα εἰς τὸ Κτηματολόγιον διὰ μεταβιβάσεις ἀκινήτου περιουσίας, δὲν σκέπτεται ἡ Κυβέρνησις τώρα ποὺ κατελύθη ἡ θεσπίσασα τὸν νόμον τοῦτον Ἀποικιακὴ Κυβέρνησις νὰ τὸν καταργήσῃ πρὸς ἀνακούφισιν τοῦ λαοῦ εἰς τὸν ὁποῖον προκαλεῖ τόσα βάρη καὶ δυσκολίας;»

KÂTİP :
Leymosun Temsilcisi Sayın G. Potamitis'in 1 Eylül 1960 tarihli sorusu :—
"Müstemleke Hükûmeti tarafından kabul edilen 44/1958 sayılı kanunun gayrimenkul mal satışlarında Tapu Dairesine ödenen vergiyi büyük ölçüde artırdığı ve bunun halk için ağır ve adaletsiz bir yük teşkil ettiği göz önünde tutularak, bu kanunu çıkaran Müstemleke Hükûmeti ortadan kalktığına göre Hükûmetin halkı rahatlatmak amacıyla mezkûr kanunu yürürlükten kaldırmayı düşünüp düşünmediğini sorarız."
""",
        """ΓΡΑΜΜΑΤΕΥΣ :
Limasol milletvekili Bay G. Potamitis'in 1 Eylül 1960 tarihli sorusu: "Meslekten ayrılan avukatlara emekli aylığı ödenmesini öngören tüzük taslağı bir süredir hazırlanmış olduğundan, yetkili Bakanın bu taslağı Meclise sunup sunmayacağı, sunacaksa ne zaman sunacağı ve Hükümetin Yunanistan ve diğer ülkelerde olduğu gibi Hukukçular Emeklilik Sandığına mali destek sağlayıp sağlamayacağı sorulmaktadır."
Adalet Bakanının yanıtı: "Avukatlar Yasasının 22. maddesi (Bölüm 2) uyarınca Avukatlar Emeklilik Sandığı Tüzüğünü hazırlama yetkisi Baro Konseyine aittir. Konsey üyeleri olağanüstü hâl döneminde istifa etmiş olup Konseyin yeniden oluşturulması için düzenlemeler yapılmaktadır; hazırlanacak tüzükler Cumhuriyet Resmî Gazetesinde yayımlanacaktır."

KÂTİP :
Leymosun Temsilcisi Sayın G. Potamitis'in 1 Eylül 1960 tarihli sorusu :—
"Bundan bir müddet evvel işten ayrılan avukatlara tekaüdiye ödenmesini derpiş eden bir Kanun Tasarısı yapıldığı ve yaşlı hukukçuları sıkıntıdan kurtarmak için tatbikat sahasına konmasının müstacel ve zaruri bir mesele olduğu göz önünde tutularak, Salâhiyettar Bakanın, mezkûr Kanun Tasarısını Meclise sunmak niyetinde olup olmadığını ve eğer sunacaksa ne zaman sunacağını ve Hükûmetin mezkûr Kanunda zikredilen Hukukçular Tekaüdiye Sandığının işlemesine, Yunanistan'da ve sair memleketlerde olduğu gibi, iktisaden yardım etmek niyetinde olup olmadığını ve bu yardımın ne şekilde yapılmasının düşünüldüğünü sormak isteriz."
Leymosun Temsilcisi Sayın G. Potamitis'in 1 Eylül 1960 tarihli sorusuna Adalet Bakanının cevabı :—
"Avukatlar Kanununun 22'nci Maddesi (Bölüm 2) tahtinde, Avukatlar Tekaüdiye Sandığı Kurulmasına dair Nizamnameleri hazırlama işi Avukatlar Cemiyeti Konseyinin Salâhiyeti çerçevesine girer. Sayın Temsilcinin bildiği gibi, bu Konseyin üyeleri olağanüstü durum sırasında istifa etmişlerdir ve şimdi Konseyin yeniden kurulması için tertibat alınmaktadır. Şüphe yoktur ki yeni kurulacak Konseyi meşgul edecek meselelerden biri de mezkûr Nizamnameleri hazırlamak olacaktır. Yukarıda zikredilen Kanun tahtinde hazırlanan nizamnameler, Cumhuriyetin Resmî Gazetesinde yayınlanacaktır."

ΓΡΑΜΜΑΤΕΥΣ :
Limasol milletvekili Bay G. Potamitis'in 1 Eylül 1960 tarihli sorusu: "Sömürge Hükümetince çıkarılan 44/1958 sayılı Yasa taşınmaz mal devirlerinde Tapu Dairesine ödenen harçları büyük ölçüde artırdığından, bu yasayı çıkaran Sömürge Hükümeti artık sona erdiğine göre Hükümetin halkın üzerindeki bu ağır ve adaletsiz yükü kaldırmak için söz konusu yasayı yürürlükten kaldırmayı düşünüp düşünmediği sorulmaktadır."

KÂTİP :
Leymosun Temsilcisi Sayın G. Potamitis'in 1 Eylül 1960 tarihli sorusu :—
"Müstemleke Hükûmeti tarafından kabul edilen 44/1958 sayılı kanunun gayrimenkul mal satışlarında Tapu Dairesine ödenen vergiyi büyük ölçüde artırdığı ve bunun halk için ağır ve adaletsiz bir yük teşkil ettiği göz önünde tutularak, bu kanunu çıkaran Müstemleke Hükûmeti ortadan kalktığına göre Hükûmetin halkı rahatlatmak amacıyla mezkûr kanunu yürürlükten kaldırmayı düşünüp düşünmediğini sorarız."
""",
    ),
}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for pno, (orig, tr) in PAGES.items():
        (OUT_DIR / f"p{pno:04d}.txt").write_text(orig.strip() + "\n", encoding="utf-8")
        (OUT_DIR / f"p{pno:04d}.tr.txt").write_text(tr.strip() + "\n", encoding="utf-8")
    print(f"Seeded {len(PAGES)} verified bilingual pages (p0003..p0016) -> {OUT_DIR}/")


if __name__ == "__main__":
    main()
