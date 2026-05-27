# 📊 Tech Jobs Analytics

> Dashboard analítico de vagas de tecnologia — transformando dados brutos em insights sobre o mercado tech.

---

## 🧩 Sobre o Projeto

O **Tech Jobs Analytics** é um dashboard interativo construído com Python que analisa vagas de emprego na área de tecnologia. A partir de um dataset do LinkedIn, o projeto aplica técnicas de ETL, limpeza de dados, NLP básico e visualização para revelar tendências do mercado tech — como tecnologias mais demandadas, distribuição por senioridade e evolução temporal das vagas.

---

## 🚀 Funcionalidades

- 📍 **Vagas por localização** — onde estão concentradas as oportunidades
- 💼 **Top cargos** — os títulos mais recorrentes no mercado
- 📅 **Evolução temporal** — como as vagas se distribuem ao longo do tempo
- 🛠️ **Tecnologias mais requisitadas** — extração automática via NLP das descrições
- 🎓 **Distribuição de senioridade** — classificação automática (Junior / Pleno / Sênior)
- 🔎 **Filtros interativos** — por localização, senioridade e tecnologia

---

## 🗂️ Estrutura do Projeto

```
tech-jobs/
│
├── data/               # Dataset de vagas (.csv)
├── src/
│   ├── app.py          # Dashboard principal (Streamlit)
│   ├── analytics.py    # Criação dos gráficos (Plotly)
│   ├── transform.py    # Limpeza e transformação dos dados
│   └── data_loader.py  # Carregamento do CSV com Pandas
├── venv/               # Ambiente virtual
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca   | Finalidade                        |
|--------------|-----------------------------------|
| `pandas`     | Manipulação e análise de dados    |
| `streamlit`  | Dashboard web interativo          |
| `plotly`     | Gráficos interativos              |
| `re` (regex) | Classificação de senioridade      |

---

## ⚙️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/tech-jobs-analytics.git
cd tech-jobs-analytics
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install pandas streamlit plotly
```

### 4. Adicione o dataset

Coloque o arquivo `.csv` com as vagas na pasta `data/`.

O dataset deve conter as colunas: `title`, `location`, `date`, `description`, `link`.

### 5. Execute o dashboard

```bash
streamlit run src/app.py
```

Acesse em: [http://localhost:8501](http://localhost:8501)

---

## 🔬 Como Funciona

### Pipeline de Dados (ETL)

```
CSV (LinkedIn)
    ↓
data_loader.py  →  leitura com pd.read_csv()
    ↓
transform.py    →  limpeza, deduplicação, padronização
    ↓
analytics.py    →  NLP + classificação de senioridade + gráficos
    ↓
app.py          →  dashboard com filtros interativos
```

### Extração de Tecnologias (NLP Básico)

O projeto detecta automaticamente tecnologias nas descrições das vagas:

```python
TECNOLOGIAS = ["Python", "SQL", "AWS", "Docker", ...]

def extrair_tecnologias(descricao):
    return [tech for tech in TECNOLOGIAS if tech.lower() in descricao.lower()]
```

### Classificação de Senioridade (Regex)

```python
import re

def classificar_senioridade(titulo):
    titulo = titulo.lower()
    if re.search(r'senior|sr\.', titulo):
        return 'Senior'
    elif re.search(r'junior|jr\.', titulo):
        return 'Junior'
    else:
        return 'Pleno'
```

---

## 📚 Conceitos Aplicados

- ✅ ETL básico
- ✅ Limpeza e tratamento de dados
- ✅ NLP básico (extração de entidades)
- ✅ Regex e classificação textual
- ✅ Feature Engineering
- ✅ Visualização de dados com Plotly
- ✅ Dashboards interativos com Streamlit
- ✅ Modularização e arquitetura de projetos
- ✅ Manipulação de DataFrames com Pandas
- ✅ Boas práticas com ambientes virtuais

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

> Desenvolvido com 🐍 Python como projeto de aprendizado em Análise e Engenharia de Dados.
