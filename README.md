# 🏗 ANÁLISE DO ANDAMENTO DE OBRAS PÚBLICAS UTILIZANDO DADOS DE PORTAIS DE TRANSPARÊNCIA

Trabalho desenvolvido para disciplina de Ciência de Dados. 

Disponível para acesso em: 

[![Abrir no Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://obras-publicas.streamlit.app/)

## Resumo

Após um longo processo em torno da construção do direito à informação no país, foi sancionada a Lei de Acesso à Informação (Nº 12.527 de 18 de novembro de 2011). Esta tem como diretriz o princípio de publicidade máxima da administração pública, definindo que os dados públicos devem ser acessíveis à população, permitindo a consulta e o acompanhamento da gestão financeira do Estado. Em seu artigo 3º, a lei prevê a utilização de ferramentas de comunicação viabilizadas pela tecnologia da informação, uma prática já comum nas administrações municipais brasileiras - inclusive no município objeto do presente estudo: a cidade de Cascavel, estado do Paraná. 

Os chamados Portais da Transparência, são as principais aplicações Web onde os municípios conseguem aglomerar e distribuir conteúdos de diversas fontes. Em Cascavel, os principais grupos de informação disponibilizados no portal são: Licitações, Contratos, Patrimônio, Receitas, Despesas, Contas e Obras Públicas, Programas, Pessoal, Saúde e Educação. Dada a grande variedade e volume de dados, optou-se por delimitar o estudo apenas à base de dados de Obras Públicas, disponibilizada no portal em formato padrão CSV (Comma Separated Values), este amplamente utilizado para divulgação e publicação deste tipo de conteúdo. 

Para o pré-processamento e a transformação dos dados, foram utilizadas as bibliotecas da linguagem de programação Python:  Pandas e NumPy, que oferecem estruturas e operações para manipular tabelas numéricas e séries temporais. Já para a visualização dos dados, as bibliotecas utilizadas foram: Matplotlib e Seaborn para apresentação de tabelas e gráficos e WordCloud para exibição das palavras mais frequentes, com objetivo de destacar os termos mais importantes nas descrições das obras. Por fim, com a interpretação dos dados agrupados foi possível a visualização de informações importantes relacionadas a situação, duração, empresas e valores das obras durante o período de 2014 a 2024.


## Como executar o app na sua máquina

1. Instale os requisitos

   ```
   $ pip install -r requirements.txt
   ```

2. Executar o aplicativo

   ```
   $ streamlit run streamlit_app.py
   ```
