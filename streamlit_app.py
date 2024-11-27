import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from wordcloud import WordCloud
import PIL.Image as Image
from collections import Counter
import re

st.set_page_config(page_title="Obras Publicas")

#st.markdown("### 🏗️ ANÁLISE DO ANDAMENTO DE OBRAS PÚBLICAS UTILIZANDO DADOS DE PORTAIS DE TRANSPARÊNCIA")
st.markdown("<h3 style='color: #20201E; text-align: center;'> 🏗️ ANÁLISE DO ANDAMENTO DE OBRAS PÚBLICAS UTILIZANDO DADOS DE PORTAIS DE TRANSPARÊNCIA</h3>", unsafe_allow_html=True)

################################### SEÇÃO DE GUIAS

tab1, tab2 = st.tabs(["🏠 Página Inicial - Conceitos, Tabelas e Gráficos", "🎯 Tutorial - Obtendo dados no Portal da Transparência de Cascavel "])

with tab1:
    #st.markdown("#### O que caracteriza uma Obra Pública?")
    st.markdown("<h3 style='color: #20201E; text-align: center;'> O que caracteriza uma Obra Pública?</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(">**Definição de Obra Pública:**")
        st.markdown("De acordo com o Conselho Nacional do Ministério Público, obra pública é considerada “toda construção, reforma, fabricação, recuperação ou ampliação de bem público” (CNMP, 2017).")
        st.image("https://egob.com/wp-content/uploads/2021/01/egob_obra_publica-1024x671.png", width=220)
        st.markdown("Ressalte-se que a qualidade de uma obra depende do adequado gerenciamento de suas diversas etapas intermediárias e da participação de profissionais capacitados (CNMP, 2017).")
    with col2:
        st.markdown(">**Lei de Acesso à Informação:**")
        st.markdown(" A Lei de Acesso à Informação Nº 12.527, foi sancionada em 18 de novembro de 2011. Esta tem como diretriz o princípio de publicidade máxima da administração pública. ")
        st.image("https://goias.gov.br/educacao/wp-content/uploads/sites/40/2024/03/lei.png", width=400)
        st.markdown("O artigo 3º da lei prevê a utilização de ferramentas de comunicação viabilizadas pela tecnologia da informação. Uma das principais manifestações da utilização da T.I. na publicidade dos dados públicos está no chamados Portais da Transparência.")
    st.divider()
    st.markdown("##### Definição de Portal da Transparência:")
    st.markdown(">\"é um site de acesso livre, no qual o cidadão pode encontrar informações sobre como o dinheiro público é utilizado, além de se informar sobre assuntos relacionados à gestão pública\" (Controladoria Geral da União).")
    st.markdown("Dados geralmente disponibilizadas nos portais estão relacionados as áreas de: Licitações, Contratos, Compras, Recursos Humanos, Despesas, Receitas, Tributos, etc.")
with tab2:
    st.markdown("#### Portal da Transparência de Cascavel ")
    st.markdown("Tutorial: Acessando e Obtendo Dados em Formato .CSV no Portal da Transparência de Cascavel")
    st.markdown("Este tutorial tem como objetivo ajudar você a navegar pelo Portal da Transparência do Município de Cascavel e obter os dados de seu interesse em formato .CSV. Esse formato é ideal para análise na ferramenta que vamos utilizar, permitindo que você explore os dados de forma mais detalhada.")
    st.markdown("")
    st.markdown("##### Passo a Passo:")
    st.markdown("##### 1. **Acesse o Portal:**")
    st.markdown("* Abra seu navegador de internet (Google Chrome, Mozilla Firefox, etc.) e digite a seguinte URL na barra de endereço: https://cascavel.atende.net/transparencia/")
    st.markdown("##### 2. **Navegue pelo Site:**")
    st.markdown("* Explore as diferentes seções do portal. Geralmente, você encontrará menus ou categorias que dividem os dados por temas, encontre a seção destinada a \"OBRAS PUBLICAS\".")
    st.markdown("##### 3. **Consultar obras públicas:**")
    st.markdown("* Você será redirecionado para uma página dedicada e irá clicar no campo onde consta: \"CONSULTAR OBRAS PUBLICAS\".")
    st.markdown("* Feito isto, você irá clicar no botão: \"PORTAL DA TRANSPARÊNCIA MUNICIPAL\".")
    st.markdown("##### 4. **Aplique ou remova filtros antes do download:**")
    st.markdown("* A nova guia que será aberta apresentará uma ferramenta de pesquisa das obras, e antes de baixar a base de dados, recomendamos que remova o filtro de \"ANO\" clicando no ano que aparecerá automaticamente e selecionando a opção \"S...\".")
    st.markdown("##### 5. **Baixando a base de dados:**")
    st.markdown("* Feita a etapa de remoção ou seleção de filtros você estará pronto para salvar a base de dados em seu dispositivo, basta clicar na opção \"DADOS ABERTOS\", e depois, clicando em \"CONFIRMAR\".")

####################### ESCOLHA DA BASE E APRESENTAÇÃO DO MUNICIPIO/CASCAVEL ################

st.divider()
#plot = prettymaps.plot('Região do Lago, Cascavel, Brasil', radius = False,)
#st.pyplot(plot)
st.markdown("""
<div style='justify-content: center; text-align:center'>
    <h4 style='color: #20201E;'> 🏙️ Escolha da base de dados: município de Cascavel/PR</h4>
    <figure>
    <img src="https://github.com/pauloalfeu/obras-publicas/blob/main/base/cac_reg_lago.png?raw=true" width="700">
    <figcaption>Região do Lago, Cascavel - Paraná, Brasil. (Figura gerada com a biblioteca Prettymap).</figcaption>
  </figure>
</div>
""", unsafe_allow_html=True)

################################### SEÇÃO DE UPLOAD DE DATAFRAME

st.divider()
st.markdown("#### Carregue a base de dados para gerar as tabelas e gráficos:")
st.markdown("Busque um arquivo **_.csv_** clicando em **\"_Browse files_\"** no campo abaixo:")
st.warning(":bulb: **Importante:** siga as etapas apresentadas na guia **\"_Tutorial - Obtendo dados no Portal da Transparência de Cascavel_\"** para fazer o download do arquivo correto.")
uploaded_file = st.file_uploader("", help="Arraste e solte seu arquivo aqui")
if uploaded_file is not None:
    # Recebendo arquivo.csv:
    dataframe = pd.read_csv(uploaded_file, sep=';', encoding='latin1')
    Obras_CAC = dataframe
    st.info("Base de dados carregada com sucesso!")



########################## TRATAMENTO DO ARQUIVO P/ DATAFRAME ##############################

    # Convertendo a coluna 'Data de Início' para datetime
    Obras_CAC[['Data de Cadastro', 'Data de Início', 'Previsão Conclusão']] = Obras_CAC[['Data de Cadastro', 'Data de Início', 'Previsão Conclusão']].apply(pd.to_datetime, dayfirst=True)

    #Criando uma nova coluna com o ano
    Obras_CAC['Ano'] = Obras_CAC['Data de Início'].dt.year

    # Criando uma nova coluna com tempo da obra em dias
    Obras_CAC['Tempo Obra (Dias)'] = (Obras_CAC['Previsão Conclusão'] - Obras_CAC['Data de Início']).dt.days

    #Renovendo colunas
    Obras_CAC = Obras_CAC.drop('Entidade', axis=1)
    Obras_CAC = Obras_CAC.drop('Número/Ano Intervenção', axis=1)
    Obras_CAC = Obras_CAC.drop('Número/Ano Obra', axis=1)

    # Convertendo os valores da coluna 'Valor Total'
    def limpar_e_converter(valor):
        valor_str = str(valor)
        valor_str = valor_str.rstrip('.')  # Remove pontos no final
        # Substitui a vírgula por ponto
        valor_str = valor_str.replace(',', '.')
        # Remove todos os pontos, exceto o último
        valor_str = valor_str.replace('.', '', valor_str.count('.') - 1)
        # Remove espaços em branco
        valor_str = valor_str.strip()
        try:
            return float(valor_str)
        except ValueError:
            print(f"Erro ao converter {valor} para float.")
            return np.nan

    Obras_CAC['Valor Total'] = Obras_CAC['Valor Total'].apply(limpar_e_converter)




    ################## APRESENTANDO O DATAFRAME // FILTROS DO USUARIO ##################

    st.divider()
    st.markdown("#### 🔎 Aplicando filtros:")
    st.markdown("Agora que a base de dados foi carregada, você será capaz de filtrar o conteúdo para encontrar dados específicos que podem auxiliar na obtenção de novas informações.")
    st.markdown("> É possível selecionar um ou mais anos de cadastro de obra, sua situação e o percentual de conclusão (para este último, basta arrastar as extermidades da barra para atingir a porcentagem desejada.)")
    years_sorted = Obras_CAC["Ano"].unique()
    years_sorted= pd.DataFrame(years_sorted)
    years_sorted = years_sorted.sort_values(by=0, ascending=False)
    
    anos = st.multiselect("**Escolha o ano:**", years_sorted)
    situacao = st.multiselect("**Escolha a situação da obra:**", Obras_CAC["Situação"].unique())
    menor_p = Obras_CAC['Percentual Conclusão (%)'].min()
    maior_p = Obras_CAC['Percentual Conclusão (%)'].max()
    percent = st.slider("**Percentual de conclusão (%):**", menor_p, maior_p, (menor_p, maior_p))

   #Utilizando st.empty(), preenche o espaço com o widget quando necessário.
    placeholder = st.empty()
    
    if anos:
        placeholder.empty()
        select = Obras_CAC[Obras_CAC['Ano'].isin(anos)]
        placeholder.data_editor(select)
        
    if situacao:
        placeholder.empty()
        sit = Obras_CAC[Obras_CAC['Situação'].isin(situacao)]
        placeholder.data_editor(sit)
    
    if percent:
        placeholder.empty()
        pct = Obras_CAC[(Obras_CAC['Percentual Conclusão (%)']>= percent[0]) & (Obras_CAC['Percentual Conclusão (%)']<=percent[1])]
        placeholder.data_editor(pct)
    
    if anos and situacao:
        placeholder.empty()
        and_sit = select[select['Situação'].isin(situacao)]
        placeholder.data_editor(and_sit, key='and_sit')
    
    if anos and percent:
        placeholder.empty()
        and_pct = select[(select['Percentual Conclusão (%)']>= percent[0]) & (select['Percentual Conclusão (%)']<=percent[1])]
        placeholder.data_editor(and_pct, key='and_pct')
    
    if situacao and percent:
        placeholder.empty()
        sit_pct = sit[(sit['Percentual Conclusão (%)']>= percent[0]) & (sit['Percentual Conclusão (%)']<=percent[1])]
        placeholder.data_editor(sit_pct, key='sit_pct')
        
    if anos and situacao and percent:
        placeholder.empty()
        sit_and_pct = and_sit[(and_sit['Percentual Conclusão (%)']>= percent[0]) & (and_sit['Percentual Conclusão (%)']<=percent[1])]
        placeholder.data_editor(sit_and_pct, key='sit_and_pct')

    ################################### Adicionando o gráfico de distribuição das obras por ‘data de inicio’
    

    
    ################################### 
    #from collections import Counter
    #import re

    # Função para pré-processar o texto
    def preprocessar_texto(texto):
        texto = texto.lower()
        texto = re.sub(r'[^\w\s]', '', texto)
        palavras = texto.split()
        return palavras


    # Aplicar o pré-processamento em toda a coluna
    OBRS_Desc = pd.DataFrame()
    OBRS_Desc['Descrição']= Obras_CAC['Descrição'].apply(preprocessar_texto)

    # Contar a frequência das palavras
    todas_as_palavras = [palavra for lista in OBRS_Desc['Descrição'] for palavra in lista if len(palavra) >= 4]
    contagem_palavras = Counter(todas_as_palavras)

    #Criar um dataframe para receber as palavras-chave
    OBRAS_KeyWords = pd.DataFrame(columns=['Palavra', 'Contagem'])

    # Obter as palavras mais comuns - resultado geral
    i=0
    palavras_mais_frequentes = contagem_palavras.most_common()
    for palavra, contagem in palavras_mais_frequentes:
        if contagem >= 5:
            OBRAS_KeyWords.at[i, 'Palavra'] = palavra
            OBRAS_KeyWords.at[i, 'Contagem'] = contagem
            i += 1

    st.divider()
    tab3, tab4 = st.tabs(["Nuvem de palavras", "Base de dados"])
    
    with tab3:
        st.markdown("#### Nuvem de Palavras-Chave: Descrições das Obras Públicas")
        word_freq = dict(zip(OBRAS_KeyWords['Palavra'], OBRAS_KeyWords['Contagem']))
        #word_freq
        word_freq.pop('lote') #126
        word_freq.pop('municipal') #108
        word_freq.pop('pública') #64
        word_freq.pop('92021') #22
        word_freq.pop('72019') #15
        word_freq.pop('12020') # 13
        word_freq.pop('102020') # 12
        
        python_mask = np.array(Image.open('./base/CAC_logo.png')) 
        #para arquivos locais mudar o final do trecho de código acima
        wordcloud = WordCloud(width=900, height=400, background_color='#f2f3f5', colormap='Set2', mask= python_mask, contour_color="gray", contour_width=1, min_font_size=3).generate_from_frequencies(word_freq)

        # Define a cor da borda (por exemplo, preto)
        border_color = '#f2f3f5'
        # Adicionando título
        plt.figure(figsize=(10, 7), facecolor=border_color)  # Define a cor de fundo (borda)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.max_font_size = 150
        plt.axis('off')
        st.pyplot(plt)
        st.markdown("A imagem acima representa uma visualização das palavras mais frequentes encontradas nas descrições das obras públicas. Após um processo de limpeza e contagem, as palavras mais comuns, como ""lote"", ""municipal"" e ""pública"", foram removidas para destacar os termos mais relevantes e específicos. Essa nuvem de palavras oferece uma visão geral dos temas e características mais comuns presentes nas obras analisadas.")

    with tab4:
        st.data_editor(OBRAS_KeyWords)

st.divider()