# LangChain, Agent, RAG, LangGraph ve ReAct Öğrenme Projesi

LangChain ekosistemini adım adım öğrenmek için hazırladığım bir çalışma deposu. Her klasör tek bir konuya odaklanan, bağımsız ve küçük bir alt projedir: basit bir LLM çağrısından başlayıp hafızalı sohbet botuna, vektör veritabanına, RAG'e, LangGraph ile agent'lara ve ReAct agent'ına kadar ilerler.

## Depo yapısı

```
.
├── LangChainIntro/              # LangChain temelleri: mesaj, prompt şablonu, parser, LangServe
├── SimpleChatBotWithMemory/     # Oturum bazlı hafızası olan sohbet botu
├── VectorStoreIntro/            # Chroma vektör veritabanı ve basit RAG zinciri
├── RAGIntro/                    # Web'den makale çekip soru cevaplayan RAG uygulaması
├── AgentsIntro/                 # Tavily araçlı agent'lar ve LangGraph ile hafızalı agent
├── ReAct/                       # ReAct agent'ı (Thought / Action / Observation döngüsü)
├── PackageMenager/              # Python paket ve modül yapısı alıştırması
└── PythonQuizLLMOrchestration/  # Python alıştırma soruları (Q1 - Q8)
```

Her klasörün kendi `requirements.txt` dosyası vardır ve birbirinden bağımsız çalışır.

## Alt projeler

### 1. LangChainIntro: LangChain temelleri
LangChain'in en küçük yapı taşlarını sırayla gösterir.

| Dosya | Ne öğretiyor? |
|---|---|
| `simplemessage.py` | `SystemMessage` ve `HumanMessage` ile modeli doğrudan çağırma (İngilizceden İspanyolcaya çeviri) |
| `simplemessagewithoutputparser.py` | `StrOutputParser` ile model çıktısını düz metne çevirme ve `model \| parser` zinciri |
| `simplemessagewithtemplates.py` | `ChatPromptTemplate` ile `{language}` ve `{text}` değişkenli prompt şablonu |
| `serve.py` | Aynı çeviri zincirini **LangServe** ve **FastAPI** ile `/chain` adresinde API olarak yayınlama |
| `main.py` | PyCharm'ın örnek başlangıç dosyası, projeyle ilgili değil |

### 2. SimpleChatBotWithMemory: hafızalı sohbet botu
`RunnableWithMessageHistory` ve `InMemoryChatMessageHistory` ile her `session_id` için ayrı konuşma geçmişi tutan bir terminal sohbet botu. Model cevabı parça parça (`stream`) yazdırır, bu yüzden önceki mesajları hatırlar.

### 3. VectorStoreIntro: vektör veritabanı
- `vectorStoreIntro.py`: Evcil hayvanlarla ilgili 5 kısa belgeyi `OpenAIEmbeddings` ile vektörleştirip **Chroma**'ya yükler. `similarity_search`, `similarity_search_with_score` ve vektör ile arama yöntemlerini dener.
- `main.py`: Aynı veritabanının üstüne bir `retriever` ve prompt koyarak "yalnızca verilen bağlamı kullanarak cevapla" mantığıyla çalışan ilk RAG zincirini kurar.

### 4. RAGIntro: web tabanlı RAG
Lilian Weng'in agent makalesini `WebBaseLoader` ile indirir, BeautifulSoup ile yalnızca makale içeriğini ayıklar, `RecursiveCharacterTextSplitter` ile 1000 karakterlik (200 örtüşmeli) parçalara böler, Chroma'ya kaydeder ve `rlm/rag-prompt` ile cevap üretir. Örnek soru: *"What is Task Decomposition?"*. Cevap akış halinde yazdırılır.

### 5. AgentsIntro: araç kullanan agent'lar
| Dosya | Ne öğretiyor? |
|---|---|
| `introducingllmwithtavily..py` | `bind_tools` ile modele **Tavily** web arama aracını bağlama ve modelin hangi aracı çağırmak istediğini (`tool_calls`) görme |
| `withagent.py` | LangGraph'ın `create_react_agent` fonksiyonuyla araçları kendi başına kullanan agent |
| `agentwithmemory.py` | Aynı agent'a `SqliteSaver` checkpointer ekleyip `thread_id` ile konuşma hafızası kazandırma |

### 6. ReAct: ReAct agent'ı
`hwchase17/react-chat` prompt'u ve `create_react_agent` ile **Reason + Act** döngüsünü çalıştıran bir sohbet agent'ı. Agent, Tavily ile web araması yapabilir. `AgentExecutor` `verbose=True` ile çalıştığı için modelin düşünce, eylem ve gözlem adımları terminalde görülür. Konuşma geçmişi `chat_history` listesinde tutulup her turda prompt'a eklenir.



## Kullanılan teknolojiler

- **LangChain:** model, prompt, parser, retriever ve zincir yapısı (LCEL `|` operatörü)
- **LangGraph:** `create_react_agent` ve `SqliteSaver` ile agent ve hafıza
- **LangServe + FastAPI:** zinciri API olarak yayınlama
- **OpenAI:** `gpt-4`, `gpt-4o-mini`, `gpt-3.5-turbo` ve `OpenAIEmbeddings`
- **Chroma:** vektör veritabanı
- **Tavily:** web arama aracı
- **BeautifulSoup:** web sayfası ayrıştırma

## Kurulum ve çalıştırma

İstediğiniz alt projeye girip kendi sanal ortamını kurun. Örnek olarak `RAGIntro`:

```bash
git clone https://github.com/mnevveryild/LangChain-Agent-RAG-LangGraph-ReAct.git
cd LangChain-Agent-RAG-LangGraph-ReAct/RAGIntro

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

İlgili klasörde bir `.env` dosyası oluşturup anahtarlarınızı ekleyin (`.env` dosyaları `.gitignore` ile dışarıda tutulur):

```env
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...      # AgentsIntro ve ReAct için gerekli
```

Sonra çalıştırın:

```bash
python main.py
```

Diğer klasörlerde çalıştırılacak dosyalar:

| Klasör | Komut |
|---|---|
| `LangChainIntro` | `python simplemessagewithtemplates.py` veya API için `python serve.py` (port 8000) |
| `SimpleChatBotWithMemory` | `python main.py` |
| `VectorStoreIntro` | `python main.py` veya `python vectorStoreIntro.py` |
| `RAGIntro` | `python main.py` |
| `AgentsIntro` | `python withagent.py` veya `python agentwithmemory.py` |
| `ReAct` | `python main.py` |


> Not: Alt projelerin `requirements.txt` dosyalarındaki paket sürümleri birbirinden farklıdır (ör. `langchain` 0.2.7 ve 0.2.10), bu yüzden her klasör için ayrı sanal ortam kullanmanız gerekir.

## Bu projede neler öğrendim?

- **LCEL ile zincir kurmak:** `prompt | model | parser` yapısıyla küçük parçaları birleştirmeyi öğrendim.
- **Prompt şablonları ve çıktı ayrıştırma:** Sabit mesajdan değişkenli şablona, ham model çıktısından düz metne geçişi gördüm.
- **Modeli API olarak yayınlamak:** LangServe ve FastAPI ile bir zinciri birkaç satırda web servisine çevirdim.
- **Konuşma hafızası:** `RunnableWithMessageHistory` ile oturum bazlı geçmiş, LangGraph'ta ise `checkpointer` ve `thread_id` ile hafıza yönetimini öğrendim.
- **Embedding ve vektör veritabanı:** Metinlerin vektöre çevrilmesini, Chroma'ya kaydedilmesini ve benzerlik aramasını uyguladım.
- **RAG'in tüm adımları:** Belge yükleme, bölme (chunking), vektörleştirme, getirme, prompt ile birleştirme ve cevap üretme akışını uçtan uca kurdum.
- **Araç kullanımı (tool calling):** Modele araç bağlamayı, modelin araç çağırma kararını ve bunu agent'a dönüştürmeyi öğrendim.
- **ReAct yaklaşımı:** Modelin düşünüp, araç kullanıp, sonucu gözlemleyip tekrar düşündüğü döngüyü çalıştırdım ve adımlarını `verbose` çıktısında izledim.
- **Python temelleri:** Paket ve modül yapısı, `__init__.py` ve temel veri yapıları üzerine alıştırmalar yaptım.
