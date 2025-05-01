import streamlit as st
import webbrowser

# Page configuration
st.set_page_config(
    page_title="REPP - Avaliação de Visitação",
    page_icon="💊",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stRadio > div {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f2f6;
    }
    .stButton > button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border: none;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #FF6B6B;
    }
    .result-box {
        padding: 2rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 1rem 0;
    }
    h1 {
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("Perguntas REPP 💊")
st.markdown("---")

# Progress bar
progress = st.progress(0)

# Function to update progress


def update_progress(question_number):
    # Calculate progress as a percentage of total questions (14 questions total)
    progress_value = min(int((question_number / 14) * 100), 100)
    progress.progress(progress_value)


# Main content
with st.container():
    Pergunta1 = st.radio(
        'Você já possui visitador de consultório?',
        ['Sim', 'Não'],
        index=None,
        horizontal=True
    )
    update_progress(1)

    if Pergunta1 == 'Não':
        Pergunta2 = st.radio(
            'Pretende contratar visitador nos próximos 2 meses?',
            ['Sim', 'Não'],
            index=None,
            horizontal=True
        )
        update_progress(2)

        if Pergunta2 == 'Sim':
            st.markdown("""
                <div class='result-box'>
                    <h3>Nota: 2</h3>
                    <p>Você está no caminho certo para alavancar as vendas de sua farmácia!</p>
                    <p>A REPP te ajuda a:</p>
                    <ul>
                        <li>Contratar esse visitador</li>
                        <li>Fornecer cadastro médico com endereço e horário de visita</li>
                        <li>Aplicativo para seu representante visitar mais e melhor</li>
                        <li>Co gerenciamento para ele atingir as metas!</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("---")
            btn = st.button("Acesse nosso site")
            if btn:
                webbrowser.open_new_tab("https://www.reppmobile.com")

        if Pergunta2 == 'Não':
            st.markdown("""
                <div class='result-box'>
                    <h3>Nota: 5</h3>
                    <p>Infelizmente sem o visitador, seu resultado vai depender muito da sorte do paciente deste médico encontrar sua farmácia.</p>
                    <p>O peso do médico indicar sua farmácia, ainda faz muita diferença e você sabe disso.</p>
                    <p>Com a REPP, você terá:</p>
                    <ul>
                        <li>Aplicação para seu visitador executar melhor as visitas e acompanhar performance</li>
                        <li>Relatório de retorno financeiro sobre as visitas</li>
                        <li>Co gerenciamento do seu propagandista</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("---")
            btn = st.button("Acesse nosso site")
            if btn:
                webbrowser.open_new_tab("https://www.reppmobile.com")

    if Pergunta1 == 'Sim':
        Pergunta3 = st.radio(
            'Seu(s) visitador(es) precisa(m) ir semanalmente/mensalmente na farmácia reportar quantas e como foram as visitas?',
            ['Sim', 'Não'],
            index=None,
            horizontal=True
        )
        update_progress(3)

        if Pergunta3 == 'Sim' or 'Não':
            Pergunta4 = st.radio(
                'Você sabe quantas visitas seu(s) visitador(es) fazem em média, por dia?',
                ['Sei', 'Não sei'],
                index=None,
                horizontal=True
            )
            update_progress(4)

            if Pergunta4 == 'Não sei':
                Pergunta5 = st.radio(
                    'Você mede o retorno financeiro das visitas realizadas?',
                    ['Sim', 'Não'],
                    index=None,
                    horizontal=True
                )
                update_progress(5)

                if Pergunta5 == 'Sim':
                    Pergunta6 = st.radio(
                        'Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                        ['Sim', 'Não'],
                        index=None,
                        horizontal=True
                    )
                    update_progress(6)

                    if Pergunta6 == 'Sim':
                        st.markdown("""
                            <div class='result-box'>
                                <h3>Resultado: 40%</h3>
                                <p>Sua farmácia precisa entender a média diária de visitas do seu visitador, para entender quantos médicos ele terá no cadastro e seja efetivo mês a mês.</p>
                                <p>Sem isso fica muito difícil entender o retorno de cada uma das visitas.</p>
                                <p>Mas não precisa ser assim, a REPP pode te ajudar a gerir e entender a performance do seu visitador!</p>
                                <ul>
                                    <li>Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade</li>
                                    <li>Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele</li>
                                    <li>Fornecendo dados para decisões estratégicas</li>
                                    <li>Liberando tempo para você focar em outras áreas e ajudar seu propagandista a vender mais!</li>
                                </ul>
                            </div>
                        """, unsafe_allow_html=True)

                        st.markdown("---")
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab(
                                "https://www.reppmobile.com")

                    if Pergunta6 == 'Não':
                        st.markdown("""
                            <div class='result-box'>
                                <h3>Resultado: 35%</h3>
                                <p>Tempo.... o grande ativo da humanidade.</p>
                                <p>Entendemos o quanto é desgastante gerenciar este profissional no dia a dia, já que ele não está no ambiente onde você pode observar sua performance. E mais você não tem o controle de quantas visitas e quem ele está visitando dia a dia.</p>
                                <p>A REPP vai te ajudar:</p>
                                <ul>
                                    <li>Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade</li>
                                    <li>Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele</li>
                                    <li>Fornecendo dados consolidados para você tomar decisões estratégicas</li>
                                </ul>
                            </div>
                        """, unsafe_allow_html=True)

                        st.markdown("---")
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab(
                                "https://www.reppmobile.com")

                if Pergunta5 == 'Não':
                    Pergunta7 = st.radio(
                        'Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                        ['Sim', 'Não'],
                        index=None,
                        horizontal=True
                    )
                    update_progress(7)

                    if Pergunta7 == 'Sim':
                        st.markdown("""
                            <div class='result-box'>
                                <h3>Resultado: 15%</h3>
                                <p>Não adianta ter tempo para gerir seu propagandista se você não possui os dados consolidados para medir o retorno financeiro destas visitas e tomar decisões. Uma coisa é fato, seu visitador poderia visitar mais prescritores.</p>
                                <p>Saia do achismo.</p>
                                <p>Com a REPP, além de fornecer um aplicativo para seu visitador visitar mais em menos tempo, você terá:</p>
                                <ul>
                                    <li>Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque</li>
                                    <li>Co gerenciamento do seu propagandista para atingir as metas estabelecidas</li>
                                </ul>
                                <p>Venha ser REPP.</p>
                            </div>
                        """, unsafe_allow_html=True)

                        st.markdown("---")
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab(
                                "https://www.reppmobile.com")

                    if Pergunta7 == 'Não':
                        st.markdown("""
                            <div class='result-box'>
                                <h3>Resultado: 10%</h3>
                                <p>Será que seu visitador está sendo efetivo? Você não está conseguindo medir o resultado das visitas, e não tem tempo para gerenciar. Você está trabalhando 100% com a intuição, e isso não é bom.</p>
                                <p>Tenha uma visitação profissional com a REPP!</p>
                                <ul>
                                    <li>Aplicativo para seu visitador executar melhor as visitas e acompanhar performance</li>
                                    <li>Relatório de retorno financeiro sobre as visitas</li>
                                    <li>Co gerenciamento do seu propagandista</li>
                                </ul>
                                <p>A REPP será seu parceiro de resultado!</p>
                            </div>
                        """, unsafe_allow_html=True)

                        st.markdown("---")
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab(
                                "https://www.reppmobile.com")

            if Pergunta4 == 'Sei':
                Pergunta8 = st.slider(
                    'Quantas visitas, em média, cada um de seu(s) visitadores faz por dia?',
                    0, 10, None
                )
                update_progress(8)

                if Pergunta8 >= 5:
                    Pergunta9 = st.radio(
                        'Você mede o retorno financeiro das visitas realizadas?',
                        ['Sim', 'Não'],
                        index=None,
                        horizontal=True
                    )
                    update_progress(9)

                    if Pergunta9 == 'Sim':
                        Pergunta10 = st.radio(
                            'Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'],
                            index=None,
                            horizontal=True
                        )
                        update_progress(10)

                        if Pergunta10 == 'Sim':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 75%</h3>
                                    <p>Você possui faca e o queijo na mão!</p>
                                    <p>Conhece os números do seu propagandista, consegue medir seu impacto no negócio e possui tempo para gerir ele no dia a dia.</p>
                                    <p>A REPP pode te ajudar a otimizar seu tempo e do seu visitador!</p>
                                    <ul>
                                        <li>Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade</li>
                                        <li>Co gerenciamento do seu visitador no dia a dia</li>
                                        <li>Fornecendo dados para decisões estratégicas</li>
                                        <li>Liberando tempo para você focar em outras áreas</li>
                                    </ul>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                        if Pergunta10 == 'Não':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 50%</h3>
                                    <p>Tempo.... o grande ativo da humanidade.</p>
                                    <p>Entendemos o quanto é desgastante gerenciar este profissional no dia a dia, já que ele não está no ambiente onde você pode observar sua performance.</p>
                                    <p>A REPP vai te ajudar:</p>
                                    <ul>
                                        <li>Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade</li>
                                        <li>Co gerenciamento do seu visitador no dia a dia</li>
                                        <li>Fornecendo dados consolidados para você tomar decisões estratégicas</li>
                                    </ul>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                    if Pergunta9 == 'Não':
                        Pergunta11 = st.radio(
                            'Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'],
                            index=None,
                            horizontal=True
                        )
                        update_progress(11)

                        if Pergunta11 == 'Sim':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 40%</h3>
                                    <p>Não adianta ter tempo para gerir seu propagandista se você não possui os dados consolidados para medir o retorno financeiro destas visitas e tomar decisões.</p>
                                    <p>Saia do achismo.</p>
                                    <p>Com a REPP, além de fornecer um aplicativo para seu visitador visitar mais em menos tempo, você terá:</p>
                                    <ul>
                                        <li>Relatório de retorno financeiro sobre as visitas</li>
                                        <li>Co gerenciamento do seu propagandista</li>
                                    </ul>
                                    <p>Venha ser REPP.</p>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                        if Pergunta11 == 'Não':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 30%</h3>
                                    <p>Será que seu visitador está sendo efetivo? Você não está conseguindo medir o resultado das visitas, e não tem tempo para gerenciar. Será que ele faz mais de 5 visitas?</p>
                                    <p>Tenha uma visitação profissional com a REPP!</p>
                                    <ul>
                                        <li>Aplicativo para seu visitador executar melhor as visitas</li>
                                        <li>Relatório de retorno financeiro sobre as visitas</li>
                                        <li>Co gerenciamento do seu propagandista</li>
                                    </ul>
                                    <p>A REPP será seu parceiro de resultado!</p>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                if Pergunta8 < 5:
                    Pergunta12 = st.radio(
                        'Você mede o retorno financeiro das visitas realizadas?',
                        ['Sim', 'Não'],
                        index=None,
                        horizontal=True
                    )
                    update_progress(12)

                    if Pergunta12 == 'Sim':
                        Pergunta13 = st.radio(
                            'Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'],
                            index=None,
                            horizontal=True
                        )
                        update_progress(13)

                        if Pergunta13 == 'Sim':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 65%</h3>
                                    <p>Sua farmácia está no caminho!</p>
                                    <p>Conhece os números do seu visitador, consegue medir seu impacto no negócio e possui tempo para gerir ele no dia a dia. Mas pode ter certeza que seu visitador pode visitar mais, e com a qualidade.</p>
                                    <p>A REPP pode te ajudar a otimizar seu tempo e do seu visitador!</p>
                                    <ul>
                                        <li>Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade</li>
                                        <li>Co gerenciamento do seu visitador no dia a dia</li>
                                        <li>Fornecendo dados para decisões estratégicas</li>
                                        <li>Liberando tempo para você focar em outras áreas</li>
                                    </ul>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                        if Pergunta13 == 'Não':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 35%</h3>
                                    <p>Tempo.... o grande ativo da humanidade.</p>
                                    <p>Entendemos o quanto é desgastante gerenciar este profissional no dia a dia, já que ele não está no ambiente onde você pode observar sua performance. E ele pode ter uma meta maior de visitação para aumentar as vendas.</p>
                                    <p>A REPP vai te ajudar:</p>
                                    <ul>
                                        <li>Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade</li>
                                        <li>Co gerenciamento do seu visitador no dia a dia</li>
                                        <li>Fornecendo dados consolidados para você tomar decisões estratégicas</li>
                                    </ul>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                    if Pergunta12 == 'Não':
                        Pergunta14 = st.radio(
                            'Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'],
                            index=None,
                            horizontal=True
                        )
                        update_progress(14)

                        if Pergunta14 == 'Sim':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 20%</h3>
                                    <p>Não adianta ter tempo para gerir seu propagandista se você não possui os dados consolidados para medir o retorno financeiro destas visitas e tomar decisões. Uma coisa é fato, seu visitador poderia visitar mais prescritores.</p>
                                    <p>Saia do achismo.</p>
                                    <p>Com a REPP, além de fornecer um aplicativo para seu visitador visitar mais em menos tempo, você terá:</p>
                                    <ul>
                                        <li>Relatório de retorno financeiro sobre as visitas</li>
                                        <li>Co gerenciamento do seu propagandista</li>
                                    </ul>
                                    <p>Venha ser REPP.</p>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")

                        if Pergunta14 == 'Não':
                            st.markdown("""
                                <div class='result-box'>
                                    <h3>Resultado: 15%</h3>
                                    <p>Será que seu visitador está sendo efetivo? Você não está conseguindo medir o resultado das visitas, e não tem tempo para gerenciar. Porque ele não está conseguindo fazer acima de 5 visitas/dia?</p>
                                    <p>Tenha uma visitação profissional com a REPP!</p>
                                    <ul>
                                        <li>Aplicativo para seu visitador executar melhor as visitas</li>
                                        <li>Relatório de retorno financeiro sobre as visitas</li>
                                        <li>Co gerenciamento do seu propagandista</li>
                                    </ul>
                                    <p>A REPP será seu parceiro de resultado!</p>
                                </div>
                            """, unsafe_allow_html=True)

                            st.markdown("---")
                            btn = st.button("Acesse nosso site")
                            if btn:
                                webbrowser.open_new_tab(
                                    "https://www.reppmobile.com")
