# Tech Jobs Analytics — Dashboard de Vagas de Tecnologia

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Plotly-Visualização-3F4F75?style=flat-square&logo=plotly&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Nível-Júnior-orange?style=flat-square"/>
</p>

> Projeto de análise de vagas de tecnologia desenvolvido com **Python, Pandas, Plotly e Streamlit**.  
> Transformando dados brutos do LinkedIn em insights sobre o mercado tech — da limpeza de dados até o dashboard interativo.

---

## Contexto

O mercado de tecnologia cresce rapidamente, mas entender **onde estão as oportunidades**, **quais habilidades são mais exigidas** e **como a demanda evolui ao longo do tempo** não é simples com dados brutos.

O projeto simula o trabalho de uma analista de dados com a seguinte missão:

> *"Precisamos entender quais tecnologias o mercado mais exige, como as vagas se distribuem por senioridade e localização, e como essa demanda muda ao longo do tempo."*

---

## Dataset

- **Fonte:** Dataset de vagas do LinkedIn  
- **Ferramenta:** VSCode + Python  
- **Colunas principais:** `title`, `location`, `date`, `description`, `link`

---

## Estrutura do Projeto

```
tech-jobs/
│
├── README.md
├── data/
│   └── vagas.csv                ← Dataset de vagas do LinkedIn
└── src/
    ├── app.py                   ← Dashboard principal (Streamlit)
    ├── analytics.py             ← Gráficos e visualizações (Plotly)
    ├── transform.py             ← Limpeza e transformação dos dados
    └── data_loader.py           ← Carregamento do CSV com Pandas
```

---

## Pipeline de Dados (ETL)

```
vagas.csv (LinkedIn)
      ↓
data_loader.py   ←  leitura com pd.read_csv()
      ↓
transform.py     ←  NLP + classificação + limpeza
      ↓
analytics.py     ←  gráficos e análises
      ↓
app.py           ←  dashboard com filtros interativos
```

---

## Técnicas Utilizadas

| Técnica | Onde foi aplicada |
|---|---|
| `pd.read_csv()`, `dropna()`, `drop_duplicates()` | Carregamento e limpeza dos dados |
| Remoção de nulos e duplicatas | Tratamento e padronização |
| NLP básico com listas e loops | Extração de tecnologias das descrições |
| `Regex` (`re`) | Classificação automática de senioridade |
| Feature Engineering | Criação das colunas `tecnologias` e `senioridade` |
| `Plotly` | Gráficos interativos de barras, linhas e pizza |
| `Streamlit` (sidebar, selectbox, multiselect) | Filtros dinâmicos e layout do dashboard |
| Modularização em arquivos `.py` | Separação de responsabilidades |

---

## Funcionalidades do Dashboard

- 📍 **Vagas por localização** — onde estão concentradas as oportunidades
- 💼 **Top cargos** — os títulos mais recorrentes no mercado
- 📅 **Evolução temporal** — como as vagas se distribuem ao longo do tempo
- 🛠️ **Tecnologias mais requisitadas** — extração automática via NLP
- 🎓 **Distribuição de senioridade** — classificação automática (Junior / Pleno / Sênior)
- 🔎 **Filtros interativos** — por localização, senioridade e tecnologia

---

## Principais Insights

- 🛠️ **Tecnologias mais exigidas:** Python e SQL lideram com ampla vantagem
- 📍 **Concentração geográfica:** a maioria das vagas está em São Paulo e remote
- 🎓 **Senioridade:** vagas para Pleno e Sênior superam as de Júnior na maior parte das áreas

---

## Como Rodar o Projeto

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/tech-jobs-analytics.git
cd tech-jobs-analytics
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install pandas streamlit plotly
```

**4. Execute o dashboard**
```bash
streamlit run src/app.py
```

Acesse em: [http://localhost:8501](http://localhost:8501)

---

## Sobre este Projeto

Este projeto foi desenvolvido para praticar habilidades reais de análise de dados com Python — desde a estruturação do projeto e limpeza dos dados até a criação de um dashboard interativo com filtros dinâmicos e insights de negócio.

---

## Autora

**Giovanna Borges de Freitas**  
Estudante de Análise e Desenvolvimento de Sistemas | Python · Dados em desenvolvimento

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Giovanna%20Freitas-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/giovanna-freitas-9b1b3a255)
[![GitHub](https://img.shields.io/badge/GitHub-giovanna--borges1-181717?style=flat-square&logo=github)](https://github.com/giovanna-borges1)
