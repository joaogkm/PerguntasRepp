import streamlit as st
import webbrowser

st.title("Perguntas Repp 💊")

Pergunta1 = st.radio('Você já possui visitador de consultório?',
                     ['Sim', 'Não'], index=None, horizontal=True)

if Pergunta1 == 'Não':
    Pergunta2 = st.radio('Pretende contratar visitador nos próximos 2 meses?',
                         ['Sim', 'Não'], index=None, horizontal=True)
    if Pergunta2 == 'Sim':
        'Nota: 2'
        'Você está no caminho certo para alavancar as vendas de sua farmácia!'
        'A REPP te ajuda a contratar esse visitador, fornecer cadastro médico com endereço e horário de visita, aplicativo para seu representante visitar mais e melhor e co gerenciamento para ele atingir as metas!'
        st.divider()
        btn = st.button("Acesse nosso site")
        if btn:
            webbrowser.open_new_tab("https://www.reppmobile.com")

    if Pergunta2 == 'Não':
        'Nota: 5'
        'Infelizmente sem o visitador, seu resultado vai depender muito da sorte do paciente deste médico encontrar sua farmácia.'
        'O peso do médico indicar sua farmácia, ainda faz muita diferença e você sabe disso.'
        'Com a REPP, você terá, além da indicação do propagandista para contratar:'
        'Aplicativo para seu visitador executar melhor as visitas, e acompanhar performance.'
        'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
        'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
        'Abre o olho e venha conversar com a REPP:'
        st.divider()
        btn = st.button("Acesse nosso site")
        if btn:
            webbrowser.open_new_tab("https://www.reppmobile.com")

if Pergunta1 == 'Sim':
    Pergunta3 = st.radio('Seu(s) visitador(es) precisa(m) ir semanalmente/mensalmente na farmácia reportar quantas e como foram as visitas?',
                         ['Sim', 'Não'], index=None, horizontal=True)
    # COLOCAR UM BREAK
    if Pergunta3 == 'Sim' or 'Não':
        Pergunta4 = st.radio('Você sabe quantas visitas seu(s) visitador(es) fazem em média, por dia?',
                            ['Sei', 'Não sei'], index=None, horizontal=True)
        if Pergunta4 == 'Não sei':
            Pergunta5 = st.radio('Você mede o retorno financeiro das visitas realizadas?',
                            ['Sim', 'Não'], index=None, horizontal=True)
            if Pergunta5 == 'Sim':
                Pergunta6 = st.radio('Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                if Pergunta6 == 'Sim':
                    'Resultado: 40%'
                    'Sua farmácia precisa entender a média diária de visitas do seu visitador, para entender quantos médicos ele terá no cadastro e seja efetivo mês a mês.'
                    'Sem isso fica muito difícil entender o retorno de cada uma das visitas.'
                    'Mas não precisa ser assim, a REPP pode te ajudar a gerir e entender a performance do seu visitador!'
                    'Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade.'
                    'Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele.'
                    'Fornecendo dados para decisões estratégicas'
                    'Liberando tempo para você focar em outras áreas e ajudar seu propagandista a vender mais!'
                    st.divider()
                    btn = st.button("Acesse nosso site")
                    if btn:
                        webbrowser.open_new_tab("https://www.reppmobile.com")
                if Pergunta6 == 'Não':
                    'Resultado: 35%'
                    'Tempo.... o grande ativo da humanidade.'
                    'Entendemos o quanto é desgastante gerenciar este profissional no dia a dia, já que ele não está no ambiente onde você pode observar sua performance. E mais você não tem o controle de quantas visitas e quem ele está visitando dia a dia.'
                    'A REPP vai te ajudar:'
                    'Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade.'
                    'Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele.'
                    'Fornecendo dados consolidados para você tomar decisões estratégicas.'
                    st.divider()
                    btn = st.button("Acesse nosso site")
                    if btn:
                        webbrowser.open_new_tab("https://www.reppmobile.com")

            if Pergunta5 == 'Não':
                Pergunta7 = st.radio('Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                if Pergunta7 == 'Sim':
                    'Resultado: 15%'
                    'Não adianta ter tempo para gerir seu propagandista se você não possui os dados consolidados para medir o retorno financeiro destas visitas e tomar decisões. Uma coisa é fato, seu visitador poderia visitar mais prescritores.'
                    'Saia do achismo.'
                    'Com a REPP, além de fornecer um aplicativo para seu visitador visitar mais em menos tempo, você terá:'
                    'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
                    'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
                    'Venha ser REPP.'
                    st.divider()
                    btn = st.button("Acesse nosso site")
                    if btn:
                        webbrowser.open_new_tab("https://www.reppmobile.com")

                if Pergunta7 == 'Não':
                    'Resultado: 10%'
                    'Será que seu visitador está sendo efetivo? Você não está conseguindo medir o resultado das visitas, e não tem tempo para gerenciar. Você está trabalhando 100% com a intuição, e isso não é bom.'
                    'Tenha uma visitação profissional com a REPP!'
                    'Aplicativo para seu visitador executar melhor as visitas, e acompanhar performance'
                    'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
                    'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
                    'A REPP será seu parceiro de resultado!'
                    st.divider()
                    btn = st.button("Acesse nosso site")
                    if btn:
                        webbrowser.open_new_tab("https://www.reppmobile.com")

        if Pergunta4 == 'Sei':
            Pergunta8 = st.slider('Quantas visitas, em média, cada um de seu(s) visitadores faz por dia?', 0, 10, None)
            if Pergunta8 >=5:
                Pergunta9= st.radio('Você mede o retorno financeiro das visitas realizadas?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                if Pergunta9 =='Sim':
                    Pergunta10 = st.radio('Considera que possui tempo para gerir o visitador no dia a dia e tomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                    if Pergunta10 == 'Sim':
                        'Resultado: 75%'
                        'Você possui faca e o queijo na mão!'
                        'Conhece os números do seu propagandista, consegue medir seu impacto no negócio e possui tempo para gerir ele no dia a dia.'
                        'A REPP pode te ajudar a otimizar seu tempo e do seu visitador!' 
                        'Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade.'
                        'Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele.' 
                        'Fornecendo dados para decisões estratégicas' 
                        'Liberando tempo para você focar em outras áreas e ajudar seu propagandista a vender mais!'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

                    if Pergunta10 == 'Não':
                        'Resultado: 50%'
                        'Tempo.... o grande ativo da humanidade.'
                        'Entendemos o quanto é desgastante gerenciar este profissional no dia a dia, já que ele não está no ambiente onde você pode observar sua performance.'
                        'A REPP vai te ajudar:'
                        'Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade.'
                        'Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele.'
                        'Fornecendo dados consolidados para você tomar decisões estratégicas'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

                if Pergunta9 =='Não':
                    Pergunta11 = st.radio('Considera que possui tempo para gerir o visitador no dia a dia e ttomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                    if Pergunta11 == 'Sim':
                        'Resultado: 40%'
                        'Não adianta ter tempo para gerir seu propagandista se você não possui os dados consolidados para medir o retorno financeiro destas visitas e tomar decisões.'
                        'Saia do achismo.'
                        'Com a REPP, além de fornecer um aplicativo para seu visitador visitar mais em menos tempo, você terá:'
                        'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
                        'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
                        'Venha ser REPP.'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

                    if Pergunta11 == 'Não':
                        'Resultado: 30%'
                        'Será que seu visitador está sendo efetivo? Você não está conseguindo medir o resultado das visitas, e não tem tempo para gerenciar. Será que ele faz mais de 5 visitas?'
                        'Tenha uma visitação profissional com a REPP!'
                        'Aplicativo para seu visitador executar melhor as visitas.'
                        'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
                        'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
                        'A REPP será seu parceiro de resultado!'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

            if Pergunta8 <5:
                Pergunta12= st.radio('Você mede o retorno financeiro das visitas realizadas?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                if Pergunta12 =='Sim':
                    Pergunta13 = st.radio('Considera que possui tempo para gerir o visitador no dia a dia e ttomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                    if Pergunta13 == 'Sim':
                        'Resultado: 65%'
                        'Sua farmácia está no caminho!' 
                        'Conhece os números do seu visitador, consegue medir seu impacto no negócio e possui tempo para gerir ele no dia a dia. Mas pode ter certeza que seu visitador pode visitar mais, e com a qualidade.'
                        'A REPP pode te ajudar a otimizar seu tempo e do seu visitador!' 
                        'Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade.'
                        'Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele.'
                        'Fornecendo dados para decisões estratégicas' 
                        'Liberando tempo para você focar em outras áreas e ajudar seu propagandista a vender mais!'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

                    if Pergunta13 == 'Não':
                        'Resultado: 35%'
                        'Tempo.... o grande ativo da humanidade.'
                        'Entendemos o quanto é desgastante gerenciar este profissional no dia a dia, já que ele não está no ambiente onde você pode observar sua performance. E ele pode ter uma meta maior de visitação para aumentar as vendas.' 
                        'A REPP vai te ajudar:'
                        'Aplicativo para ele visitar mais prescritores em menos tempo e com mais qualidade.'
                        'Co gerenciando seu visitador no dia a dia, e sim cobramos resultado dele.' 
                        'Fornecendo dados consolidados para você tomar decisões estratégicas'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

                if Pergunta12 =='Não':
                    Pergunta14 = st.radio('Considera que possui tempo para gerir o visitador no dia a dia e ttomar decisões estratégicas de visitas, baseado em dados das visitas/faturamento?',
                            ['Sim', 'Não'], index=None, horizontal=True)
                    if Pergunta14 == 'Sim':
                        'Resultado: 20%'
                        'Não adianta ter tempo para gerir seu propagandista se você não possui os dados consolidados para medir o retorno financeiro destas visitas e tomar decisões. Uma coisa é fato, seu visitador poderia visitar mais prescritores.'
                        'Saia do achismo.'
                        'Com a REPP, além de fornecer um aplicativo para seu visitador visitar mais em menos tempo, você terá:'
                        'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
                        'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
                        'Venha ser REPP.'
                        'Venha ser REPP.'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")

                    if Pergunta14 == 'Não':
                        'Resultado: 15%'
                        'Será que seu visitador está sendo efetivo? Você não está conseguindo medir o resultado das visitas, e não tem tempo para gerenciar. Porque ele não está conseguindo fazer acima de 5 visitas/dia?'
                        'Tenha uma visitação profissional com a REPP!'
                        'Aplicativo para seu visitador executar melhor as visitas.'
                        'Relatório de retorno financeiro sobre as visitas: entenda os médicos que dão retorno ou não, e o porque. Com isso tome as melhores decisões.'
                        'Além disso, cogerenciamos seu propagandista, para ele atingir as metas estabelecidas e ganhe tempo.'
                        'A REPP será seu parceiro de resultado!'
                        st.divider()
                        btn = st.button("Acesse nosso site")
                        if btn:
                            webbrowser.open_new_tab("https://www.reppmobile.com")


  