# Kıbrıs Cumhuriyeti Temsilciler Meclisi Tutanak Arşivi — Türkçe (Konuşmacı Bazlı Arama)

Kıbrıs Cumhuriyeti Temsilciler Meclisi (`parliament.cy`) resmî tutanaklarının, **Kıbrıs Türk okuyucuların tamamını Türkçe okuyup arayabilmesi** için [`kktcmeclisarsivi.org`](https://kktcmeclisarsivi.org/) (`RYucel/kktc-meclis-tutanak`) ile **birebir aynı mimari ve arayüz formatında** hazırlanmış konuşmacı bazlı (speaker-turn) veri seti ve sunucusuz DuckDB-WASM web uygulaması.

## Öne Çıkan Özellikler

* **Tamamı Türkçe Okuma & Arama:**
  * 1960–1963 iki toplumlu dönemdeki Türk milletvekillerinin konuşmaları (Halit Ali Rıza, Dr. Orhan Müderrisoğlu, Ümit Süleyman Onan, Dr. Burhan Nalbantoğlu, Ahmet Mithat Berberoğlu, Ramadan Cemil, Dr. Niyazi Manyera vb.) zabıtlardaki **orijinal Türkçe** hâliyle kelimesi kelimesine korunur.
  * Yunanca (politonik Katharevousa ve modern Yunanca) konuşmalar **sadık Türkçe çevirisiyle** (`text`) indekslenir ve aranır; her konuşmada tek tıkla **Orijinal Yunanca** zabıt metni (`text_original`) açılıp doğrulanabilir.
* **Çapraz Alfabe Konuşmacı Birleştirme (`src/speaker_resolution.py`):** Aynı konuşmacının Türkçe ve Yunanca tutanaklardaki tüm yazımlarını (`H. A. RIZA` + `ΧΑΛΙΤ ΑΛΗ ΡΙΖΑ` → `Halit Ali Rıza`, `Ü. SÜLEYMAN` + `ΟΥΜΙΤ ΣΟΥΛΕΫΜΑΝ` → `Ümit Süleyman Onan`, `ΠΡΟΕΔΡΟΣ` → `Glafkos Kleridis`) tek kanonik kimlikte birleştirir.
* **`kktcmeclisarsivi.org` ile Birebir Aynı Arayüz (`space_static/index.html`):**
  * Sunucusuz **DuckDB-WASM + HTTP Range Parquet** sorgulama
  * 0 ms yerel otomatik tamamlama (Türkçe + Yunanca takma ad desteği)
  * **Konuşmacı Dosyası:** İstatistikler, biyografi, yıllık konuşma yoğunluğu, konu ağırlıkları ve öne çıkan kavramlar
  * **Dönemlere Göre Vekiller:** Parti/grup, seçim bölgesi ve toplum rozetli vekil dizini
  * **Gündem & Konular:** Vektörel DuckDB RE2 konu analizi ve dönemler arası trend grafiği
  * **Tam Konuşma & Oturum Okuyucu:** Kaynak gösterimi (Alıntıla), kalıcı bağlantı, Orijinal Yunanca karşılaştırması, resmî PDF sayfa bağlantısı ve CSV dışa aktarma.

## Boru Hattı (Pipeline)

1. **Kaynak Kataloğu (`src/crawl_manifest.py`):**
   ```bash
   python3 src/crawl_manifest.py
   # Yeni PDF linki eklemek için:
   python3 src/crawl_manifest.py --add-url "https://www.parliament.cy/images/media/redirectfile/..."
   # Tarayıcıdan kaydedilen parliament.cy tutanaklar sayfası HTML'inden toplu aktarım:
   python3 src/crawl_manifest.py --from-html parliament_minutes.html
   ```
   *(Not: `parliament.cy` HTML sayfaları Cloudflare doğrulaması arkasında olduğundan yeni dönemlerin toplu linkleri tarayıcıdan kaydedilen HTML veya URL listesi üzerinden aktarılır; doğrudan PDF bağlantıları kesintisiz indirilir.)*

2. **PDF İndirme (`src/download_files.py`):**
   ```bash
   python3 src/download_files.py --checksum
   ```

3. **İki Sütunlu İki Dilli OCR & Türkçe Çeviri (`src/reocr_vlm.py` / `src/translate_to_tr.py`):**
   1960–1961 PDF'inin (1.050 sayfa) ilk 684 sayfasında metin katmanı yoktur; son 365 sayfasındaki eski Adobe Acrobat OCR katmanı ise İngilizce OCR ile Yunancayı bozmuştur (`extract_text.py` bunu otomatik tespit edip `pdf_needs_ocr` olarak işaretler).
   ```bash
   # Gemini Vision API ile sayfa bazlı (kaldığı yerden devam eden) OCR + Türkçe çeviri:
   export GEMINI_API_KEY=...
   python3 src/reocr_vlm.py --from-page 17 --to-page 1050 --engine gemini --model gemini-2.5-flash --with-turkish --workers 6

   # Alternatif: yerel OpenAI-uyumlu VLM sunucusu (vLLM / Ollama / llama-server):
   python3 src/reocr_vlm.py --from-page 17 --to-page 1050 --engine openai --base-url http://localhost:8000/v1 --model qwen2.5-vl --with-turkish

   # Alternatif: yerel iki sütunlu Tesseract (ell+tur) ardından konuşma bazlı çeviri:
   python3 src/reocr_vlm.py --from-page 17 --to-page 1050 --engine tesseract
   ```

4. **Metin Çıkarımı, Oturum & Konuşmacı Ayrıştırma, Parquet & WASM İndeksleri:**
   ```bash
   python3 src/extract_text.py --only-cached
   python3 src/parse_speakers.py
   python3 src/translate_to_tr.py      # Çevrilmemiş Yunanca konuşmalar varsa tamamlar
   python3 src/build_dataset.py        # data/hf_dataset/data/*.parquet + data/search.db
   python3 src/optimize_for_wasm.py --local-copy
   python3 src/analyze_topics.py
   ```

5. **Yerel Arama & Önizleme:**
   ```bash
   # Komut satırından anlık FTS5 arama:
   python3 src/search_cli.py --speaker "Halit Ali Rıza" --query "anayasa"
   python3 src/search_cli.py --query "Forsthoff" --show-original

   # Web arayüzünü yerelde başlatma:
   python3 -m http.server 8080 --directory space_static
   ```

6. **Hugging Face Hub & Static Space Yayını:**
   ```bash
   python3 src/upload_hf.py --repo-id <kullanici>/KC_Meclis_Tutanak
   # space_static/index.html içinde HF_DATASET_REPO = '<kullanici>/KC_Meclis_Tutanak' ayarlayın:
   python3 src/deploy_space.py --repo-id <kullanici>/KC-Meclis-Tutanak-Arama --with-indices
   ```

## Testler

```bash
pytest -v tests/
```

## Lisans ve Atıf

Orijinal tutanakların hakları **Kıbrıs Cumhuriyeti Temsilciler Meclisi**'ne (`parliament.cy`) aittir. Ayrıştırma, çeviri ve açık veri katmanı **CC BY 4.0** lisansı ile paylaşılmaktadır.
