# -*- coding: utf-8 -*-
"""
Fonte única dos posts da Fundação Net do Bem (Instagram e Facebook) · V.1 (25/11/2026).

Ordem do fluxo: pesquisador (estrategia/06) -> estrategista (estrategia/07) -> copywriter (este arquivo)
-> designer (render.py) -> técnico (build.py + push).

Regras aplicadas a cada post:
- 1 ideia e 1 CTA; carrossel com no máximo 3 cards (pré-briefing)
- gancho do slide 1 com até 6 palavras
- sem criança identificável, sem endereço, sem rotina de casa parceira
- post de doação: para que, para quem, quanto, como, prazo
- FIA aponta para o fundo municipal, nunca para a fundação, e só sai com revisão de contador
- sem travessão
Se faltar informação real, status = "pendencia" (RASCUNHO COM PENDÊNCIA).
"""

HASHTAGS_BASE = "#FundacaoNetDoBem #Sorocaba #Acolhimento #QuemCuidaDeQuemCuida"
WHATS = "(15) 99100-3425"
M = "novembro-dezembro"

POSTS = [
    # ═════════════════════════ INAUGURAÇÃO ═════════════════════════
    {
        "id": "01", "mes": M, "data_ordem": "2026-11-25", "data": "25/11", "dia_semana": "Quarta-feira", "horario": "18h",
        "fase": 0, "fase_nome": "Etapa 1 · Inauguração", "pauta": "Expectativa · Conhecer para fortalecer",
        "formato": "Post único", "formato_slug": "post",
        "titulo": "Amanhã: conhecer para fortalecer",
        "objetivo": "Avisar que a inauguração é amanhã, deixar claro que o evento é fechado e abrir contato para quem quer conhecer.",
        "publico": "Comunidade e potenciais apoiadores",
        "cta": "Chama no WhatsApp",
        "status": "pronto",
        "pendencias": ["Publicar hoje, se o post de expectativa ainda não saiu no perfil."],
        "prova": "Ilustração em massinha; data e cidade confirmadas.",
        "slides": [
            {"tipo": "capa", "img": "bastidores-b.jpg", "kicker": "26 . 11 . 2026  ·  Sorocaba", "mao": "amanhã", "titulo": "Conhecer para fortalecer"},
        ],
        "legenda_ig": (
            "Amanhã, conhecer para fortalecer.\n\n"
            "Nesta quinta-feira, 26/11, a Fundação Net do Bem completa um ano e faz sua inauguração em Sorocaba, num encontro fechado com convidados. "
            "A proposta é ouvir as casas de acolhimento e começar a construir uma rede de apoio junto com elas.\n\n"
            f"Quer conhecer a fundação? Chama no WhatsApp: {WHATS}."
        ),
        "legenda_fb": (
            "Amanhã, conhecer para fortalecer.\n\n"
            "Nesta quinta-feira, 26/11, a Fundação Net do Bem completa um ano e faz sua inauguração em Sorocaba, num encontro fechado com convidados. "
            "A proposta é ouvir as casas de acolhimento e começar a construir uma rede de apoio junto com elas.\n\n"
            f"Quer conhecer a fundação? Chame no WhatsApp: {WHATS}."
        ),
        "alt": "Ilustração em massinha de três adultos preparando um evento: uma estende um tapete verde com um coração, outro carrega uma planta, outro arruma cadeiras. "
               "Texto: amanhã, conhecer para fortalecer. 26 de novembro de 2026, Sorocaba.",
    },
    {
        "id": "02", "mes": M, "data_ordem": "2026-11-26", "data": "26/11", "dia_semana": "Quinta-feira", "horario": "17h, antes do evento",
        "fase": 0, "fase_nome": "Etapa 1 · Inauguração", "pauta": "Inauguração",
        "formato": "Post único + stories em tempo real", "formato_slug": "post",
        "titulo": "Hoje é dia de inaugurar",
        "objetivo": "Marcar a inauguração e trazer os convidados para o perfil.",
        "publico": "Convidados e comunidade",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": [
            "Publicar em collab com o perfil pessoal do André.",
            "Deixar o QR code do perfil visível no evento e pedir para seguir na fala de abertura.",
            "Stories em tempo real da abertura, só com adultos; priorizar o depoimento da Dra. Cristina.",
        ],
        "prova": "Ilustração em massinha; foto real da equipe pode substituir.",
        "slides": [
            {"tipo": "capa", "img": "inauguracao-b.jpg", "kicker": "26 . 11 . 2026  ·  Sorocaba", "mao": "um ano depois", "titulo": "Hoje é dia de inaugurar"},
        ],
        "legenda_ig": (
            "Hoje é dia de inaugurar.\n\n"
            "Um ano depois de nascer, a Fundação Net do Bem é inaugurada hoje, em Sorocaba, num encontro com convidados. "
            "Nosso trabalho é apoiar as casas de acolhimento e as pessoas que cuidam nelas. A partir de agora, você acompanha esse trabalho por aqui.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Hoje é dia de inaugurar.\n\n"
            "Um ano depois de nascer, a Fundação Net do Bem é inaugurada hoje, em Sorocaba, num encontro com convidados. "
            "Nosso trabalho é apoiar as casas de acolhimento de crianças e adolescentes e as pessoas que cuidam nelas.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Ilustração em massinha de quatro adultos cortando uma fita verde diante de um grande coração feito de hastes e pontos. Texto: um ano depois, hoje é dia de inaugurar.",
        "stories": [
            {"quando": "Manhã", "titulo": "Hoje é o dia", "corpo": "Inauguração da Fundação Net do Bem", "tema": "verde"},
            {"quando": "Durante", "titulo": "Começou", "corpo": "Repost de quem marcar o perfil, só com adultos na imagem", "tema": "creme"},
            {"quando": "Depois", "titulo": "Obrigado", "corpo": "Amanhã a gente conta como foi", "tema": "verde"},
        ],
    },
    {
        "id": "03", "mes": M, "data_ordem": "2026-11-27", "data": "27/11", "dia_semana": "Sexta-feira", "horario": "18h",
        "fase": 0, "fase_nome": "Etapa 1 · Inauguração", "pauta": "Triangulação no coração",
        "formato": "Carrossel 3 cards (infográfico)", "formato_slug": "carrossel",
        "titulo": "Uma rede, quatro papéis",
        "objetivo": "Explicar em um olhar o que é a casa de acolhimento, o papel do poder público, dos apoiadores e da fundação.",
        "publico": "Sociedade, empresas e convidados da inauguração",
        "cta": "Salva e compartilha",
        "status": "pronto",
        "pendencias": ["Revisão técnica da Agda (assistente social) sobre o papel do poder público."],
        "prova": "Modelo de atuação do site e da fala da equipe na inauguração.",
        "slides": [
            {"tipo": "triangulo", "mao": "em um olhar", "titulo": "Uma rede, quatro papéis"},
            {"tipo": "papeis", "titulo": "Quem faz o quê", "itens": [
                ["Casa de acolhimento", "Acolhe e cuida de crianças e adolescentes afastados da família por medida de proteção."],
                ["Poder público", "Justiça, Conselho Tutelar e assistência social decidem o acolhimento, financiam e acompanham o serviço."],
                ["Apoiadores e empresas", "Doam recursos, tempo e conhecimento para o cuidado continuar."],
                ["Net do Bem", "Conecta as três pontas e fortalece as casas com gestão, formação e pesquisa."],
            ]},
            {"tipo": "cta", "titulo": "Uma rede só funciona junta", "texto": "Salva e compartilha", "apoio": "Para explicar o acolhimento a alguém em um olhar."},
        ],
        "legenda_ig": (
            "Uma rede, quatro papéis.\n\n"
            "O acolhimento de crianças e adolescentes depende de quatro pontas trabalhando juntas. A casa acolhe e cuida. "
            "O poder público decide, financia e acompanha. Apoiadores e empresas trazem recursos e conhecimento. "
            "A Net do Bem conecta essas pontas e fortalece as casas.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "Uma rede, quatro papéis.\n\n"
            "O acolhimento de crianças e adolescentes depende de quatro pontas trabalhando juntas. A casa de acolhimento acolhe e cuida. "
            "O poder público (Justiça, Conselho Tutelar e assistência social) decide, financia e acompanha. Apoiadores e empresas trazem recursos e conhecimento. "
            "A Fundação Net do Bem conecta essas pontas e fortalece as casas com gestão, formação e pesquisa.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Infográfico com o coração de linhas e pontos da Net do Bem. Nos vértices: casa de acolhimento, poder público e apoiadores e empresas; no centro, a Net do Bem conectando as três pontas. "
               "Segundo card explica o papel de cada um.",
    },
    {
        "id": "04", "mes": M, "data_ordem": "2026-11-28", "data": "28/11", "dia_semana": "Sábado", "horario": "11h",
        "fase": 0, "fase_nome": "Etapa 1 · Inauguração", "pauta": "Pós-evento",
        "formato": "Carrossel 3 fotos oficiais (ou Reels)", "formato_slug": "foto-faixa",
        "titulo": "O que ouvimos na inauguração",
        "objetivo": "Registrar o evento com fotos reais e a mensagem de escuta e construção conjunta.",
        "publico": "Convidados, casas e parceiros",
        "cta": "Siga e compartilhe",
        "status": "pendencia",
        "pendencias": [
            "Fotos oficiais da fotógrafa: 3 melhores momentos, só adultos, sem placa ou fachada.",
            "Uma frase real sobre o que foi ouvido no evento, definida pela equipe.",
            "Se houver depoimento da Dra. Cristina em vídeo, publicar como Reels com autorização dela.",
            "Confirmar se representantes de casas de acolhimento estiveram presentes antes de citar.",
        ],
        "prova": "Fotos oficiais do evento.",
        "slides": [
            {"tipo": "foto", "img": None, "faixa": "O que ouvimos na inauguração", "placeholder": "Foto oficial: abertura do evento"},
            {"tipo": "foto", "img": None, "faixa": "Construir junto com as casas", "placeholder": "Foto oficial: conversa entre convidados adultos"},
            {"tipo": "foto", "img": None, "faixa": "Obrigado a quem esteve com a gente", "placeholder": "Foto oficial: equipe da fundação"},
        ],
        "legenda_ig": (
            "O que ouvimos na inauguração.\n\n"
            "Na quinta-feira, recebemos convidados, parceiros e representantes de casas de acolhimento em Sorocaba. "
            "[Uma frase sobre o que foi ouvido, definida pela equipe.] Foi o primeiro passo de um trabalho que vamos construir junto com as instituições.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "O que ouvimos na inauguração.\n\n"
            "Na quinta-feira, a Fundação Net do Bem recebeu convidados, parceiros e representantes de casas de acolhimento em Sorocaba. "
            "[Uma frase sobre o que foi ouvido, definida pela equipe.] Foi o primeiro passo de um trabalho que vamos construir junto com as instituições.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Carrossel com três fotos oficiais da inauguração e faixa verde: abertura do evento, convidados adultos conversando e a equipe da fundação. Não aparecem crianças.",
    },
    {
        "id": "05", "mes": M, "data_ordem": "2026-11-30", "data": "30/11", "dia_semana": "Segunda-feira", "horario": "18h",
        "fase": 0, "fase_nome": "Etapa 1 · Inauguração", "pauta": "Equipe · André (padrão do post da Patrícia)",
        "formato": "Foto + notas manuscritas", "formato_slug": "post",
        "titulo": "Um pouco mais sobre o André",
        "objetivo": "Humanizar: mostrar quem é o fundador e o que ele faz na prática.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pendencia",
        "pendencias": [
            "Trocar o retrato em massinha por uma foto real do André, como no post da Patrícia.",
            "O André revisa as notas \"Sobre mim\" e \"O que faço\".",
        ],
        "prova": "Biografia publicada no site da fundação.",
        "slides": [
            {"tipo": "nota", "img": "founder-net-do-bem.webp", "nome": "André Facciolli", "papel": "Fundador",
             "sobre": ["30 anos de tecnologia e gestão", "Ciência da Computação", "Mestre em Administração"],
             "faz": ["Aproximo empresas e poder público das casas", "Mobilizo recursos para a rede", "Penso a fundação no longo prazo"]},
        ],
        "legenda_ig": (
            "Um pouco mais sobre o André.\n\n"
            "Fundador da Net do Bem, o André passou mais de 30 anos construindo empresa na área de tecnologia e decidiu colocar essa experiência de gestão a serviço da infância. "
            "Na fundação, ele aproxima empresas, profissionais e poder público das casas de acolhimento.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Um pouco mais sobre o André Facciolli, fundador da Fundação Net do Bem.\n\n"
            "Ele passou mais de 30 anos construindo empresa na área de tecnologia e decidiu colocar essa experiência de gestão a serviço da infância. "
            "Na fundação, aproxima empresas, profissionais e poder público das casas de acolhimento.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Card com retrato do André Facciolli, fundador, e notas escritas à mão: sobre mim, 30 anos de tecnologia e gestão; o que faço, aproximo empresas e poder público das casas.",
    },

    # ═════════════════════════ PESQUISA DE MAPEAMENTO · DEZEMBRO ═════════════════════════
    {
        "id": "06", "mes": M, "data_ordem": "2026-12-01", "data": "01/12", "dia_semana": "Terça-feira", "horario": "10h",
        "fase": 1, "fase_nome": "Etapa 2 · Pesquisa e doação", "pauta": "Dia de Doar",
        "formato": "Carrossel 2 cards", "formato_slug": "carrossel",
        "titulo": "Hoje é Dia de Doar",
        "objetivo": "Primeiro pedido de doação, concreto, com as cinco informações do briefing.",
        "publico": "Pessoas físicas e empresas",
        "cta": "Chama no WhatsApp",
        "status": "pendencia",
        "pendencias": [
            "Definir o valor de referência (\"quanto ajuda\"), por exemplo o que R$ 50 ou R$ 100 viabilizam.",
            "Confirmar o canal de doação: formulário do site, WhatsApp ou PIX.",
        ],
        "prova": "Destino da doação descrito em netdobem.org.br/contato; data oficial em diadedoar.org.br.",
        "slides": [
            {"tipo": "capa", "img": "doar-a.jpg", "kicker": "01 . 12 . 2026", "mao": "hoje é", "titulo": "Dia de Doar"},
            {"tipo": "doacao", "titulo": "Sua doação, em cinco linhas", "itens": [
                ["Para que", "Capacitação, gestão e apoio estrutural"],
                ["Para quem", "Casas de acolhimento e suas equipes"],
                ["Quanto", "[Valor de referência a definir]"],
                ["Como", f"netdobem.org.br/contato ou WhatsApp {WHATS}"],
                ["Prazo", "Hoje é o Dia de Doar. A doação fica aberta o ano todo."],
            ]},
        ],
        "legenda_ig": (
            "Hoje é Dia de Doar.\n\n"
            "No Dia de Doar, organizações do Brasil inteiro recebem apoio. A doação para a Net do Bem vai para capacitação, gestão e apoio estrutural "
            "de casas de acolhimento de crianças e adolescentes. [Valor de referência: R$ X ajuda em ...] Você doa pelo site netdobem.org.br/contato ou pelo WhatsApp.\n\n"
            f"Chama no WhatsApp: {WHATS}."
        ),
        "legenda_fb": (
            "Hoje é Dia de Doar.\n\n"
            "No Dia de Doar, organizações do Brasil inteiro recebem apoio. A doação para a Fundação Net do Bem vai para capacitação, gestão e apoio estrutural "
            "de casas de acolhimento de crianças e adolescentes. [Valor de referência: R$ X ajuda em ...] Você doa pelo site netdobem.org.br/contato ou pelo WhatsApp.\n\n"
            f"Chame no WhatsApp: {WHATS}."
        ),
        "alt": "Ilustração em massinha de adultos entregando um coração de rede a uma pequena casa. Texto: hoje é Dia de Doar. Segundo card: para que, para quem, quanto, como e prazo da doação.",
    },
    {
        "id": "07", "mes": M, "data_ordem": "2026-12-02", "data": "02/12", "dia_semana": "Quarta-feira", "horario": "18h",
        "fase": 1, "fase_nome": "Etapa 2 · Pesquisa e doação", "pauta": "Equipe · Sandra (padrão do post da Patrícia)",
        "formato": "Foto + notas manuscritas", "formato_slug": "post",
        "titulo": "Um pouco mais sobre a Sandra",
        "objetivo": "Humanizar: apresentar mais uma pessoa da equipe e o que ela faz na prática.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pendencia",
        "pendencias": [
            "Nome completo, cargo e foto real da Sandra.",
            "Três notas \"Sobre mim\" e três \"O que faço\", escritas ou aprovadas por ela.",
        ],
        "prova": "Foto real e texto aprovado pela Sandra.",
        "slides": [
            {"tipo": "nota", "img": None, "nome": "Sandra [sobrenome]", "papel": "[Cargo a confirmar]",
             "sobre": ["[Formação]", "[Trajetória]", "[Um detalhe pessoal]"],
             "faz": ["[O que faz na fundação]", "[Com quem trabalha]", "[Por que está aqui]"]},
        ],
        "legenda_ig": (
            "Um pouco mais sobre a Sandra.\n\n"
            "[Duas frases sobre a trajetória da Sandra e o que ela faz na Net do Bem, aprovadas por ela.]\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Um pouco mais sobre a Sandra, da Fundação Net do Bem.\n\n"
            "[Duas frases sobre a trajetória da Sandra e o que ela faz na fundação, aprovadas por ela.]\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Card com foto da Sandra e notas escritas à mão sobre quem ela é e o que faz na Fundação Net do Bem.",
    },
    {
        "id": "08", "mes": M, "data_ordem": "2026-12-03", "data": "03/12", "dia_semana": "Quinta-feira", "horario": "18h",
        "fase": 1, "fase_nome": "Etapa 2 · Pesquisa e doação", "pauta": "Lançamento da pesquisa de mapeamento",
        "formato": "Carrossel 3 cards", "formato_slug": "carrossel",
        "titulo": "A pesquisa de mapeamento começou",
        "objetivo": "Explicar que a pesquisa é o primeiro passo prático, ética, confidencial e sem punição, e levar gestores ao portal.",
        "publico": "Gestores e equipes de casas de acolhimento",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pendencia",
        "pendencias": ["Confirmar a data de lançamento e se o portal já recebe casas de todo o Brasil."],
        "prova": "Portal portal.netdobem.org.br no ar, com termo de participação.",
        "slides": [
            {"tipo": "capa", "img": "escuta-a.jpg", "kicker": "Primeiro passo", "mao": "começou", "titulo": "A pesquisa de mapeamento"},
            {"tipo": "lista", "titulo": "Ética, confidencial e sem punição", "itens": [
                "Nenhuma casa é avaliada ou exposta",
                "Só dados da instituição, nenhuma criança identificada",
                "As respostas orientam apoios reais",
            ]},
            {"tipo": "cta", "titulo": "Como participar", "texto": "Compartilha com quem cuida de alguém", "apoio": "portal.netdobem.org.br · etapas curtas, salvas automaticamente"},
        ],
        "legenda_ig": (
            "A pesquisa de mapeamento começou.\n\n"
            "Antes de propor qualquer apoio, a Net do Bem quer conhecer as casas de acolhimento. A pesquisa é ética e confidencial, nenhuma casa é avaliada "
            "ou exposta e nenhuma criança é identificada. Gestores respondem em portal.netdobem.org.br, em etapas curtas.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "A pesquisa de mapeamento das casas de acolhimento começou.\n\n"
            "Antes de propor qualquer apoio, a Fundação Net do Bem quer conhecer as casas. A pesquisa é ética e confidencial, nenhuma casa é avaliada "
            "ou exposta e nenhuma criança é identificada. Gestores respondem em portal.netdobem.org.br, em etapas curtas.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Ilustração em massinha de duas adultas conversando sentadas, uma anota e a outra explica. Texto: começou, a pesquisa de mapeamento. "
               "Cards seguintes: ética, confidencial e sem punição; como participar pelo portal.",
    },
    {
        "id": "09", "mes": M, "data_ordem": "2026-12-05", "data": "05/12", "dia_semana": "Sábado", "horario": "11h",
        "fase": 1, "fase_nome": "Etapa 2 · Pesquisa e doação", "pauta": "Dia Internacional do Voluntário",
        "formato": "Post único", "formato_slug": "post",
        "titulo": "Obrigado a quem doa tempo",
        "objetivo": "Reconhecer voluntários das casas de acolhimento numa data especial.",
        "publico": "Voluntários e comunidade",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pronto",
        "pendencias": [],
        "prova": "Data da ONU (Resolução 40/212).",
        "slides": [
            {"tipo": "capa", "img": "voluntario-b.jpg", "kicker": "05/12 · Dia Internacional do Voluntário", "mao": "obrigado", "titulo": "A quem doa tempo"},
        ],
        "legenda_ig": (
            "Obrigado a quem doa tempo.\n\n"
            "Hoje é o Dia Internacional do Voluntário. Nas casas de acolhimento, voluntários ajudam na manutenção, na organização, em eventos e em projetos. "
            "Esse tempo faz diferença na rotina de quem cuida.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Obrigado a quem doa tempo.\n\n"
            "Hoje é o Dia Internacional do Voluntário. Nas casas de acolhimento, voluntários ajudam na manutenção, na organização, em eventos e em projetos. "
            "Esse tempo faz diferença na rotina de quem cuida.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Ilustração em massinha de adultos voluntários pintando e consertando uma pequena casa. Texto: obrigado a quem doa tempo.",
    },
    {
        "id": "10", "mes": M, "data_ordem": "2026-12-08", "data": "08/12", "dia_semana": "Terça-feira", "horario": "18h",
        "fase": 1, "fase_nome": "Etapa 2 · Pesquisa e doação", "pauta": "Reels da Agda sobre a pesquisa",
        "formato": "Reels 30 a 60 s + capa", "formato_slug": "reels",
        "titulo": "Por que a pesquisa é confidencial",
        "objetivo": "Dar rosto e voz técnica à pesquisa e tirar o medo de avaliação.",
        "publico": "Gestores de casas de acolhimento",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pendencia",
        "pendencias": ["Gravar a Agda até 05/12, celular na vertical, fundo real, legenda no vídeo.", "Trocar a capa pelo frame do vídeo, se preferirem."],
        "prova": "Vídeo da Agda, assistente social com 12 anos de SUAS.",
        "slides": [
            {"tipo": "reels", "img": "agda-estrategia-net-do-bem.webp", "titulo": "Por que a pesquisa é confidencial", "sub": "Agda Ximenes, assessoramento técnico"},
        ],
        "roteiro": [
            "0 a 3 s, olhando para a câmera: \"Ninguém vai avaliar a sua casa nessa pesquisa.\"",
            "Meio: \"Eu trabalhei 12 anos no SUAS e sei como é responder questionário com medo de punição. Aqui é diferente: as respostas são confidenciais e servem para a gente entender do que cada casa precisa.\"",
            "Fecho: \"Se você trabalha numa casa de acolhimento, responde em portal.netdobem.org.br e compartilha com quem também cuida.\"",
        ],
        "legenda_ig": (
            "Por que a pesquisa é confidencial.\n\n"
            "A Agda trabalhou 12 anos no SUAS, perto das casas de acolhimento. Neste vídeo ela explica por que as respostas da pesquisa de mapeamento "
            "são confidenciais e para que elas servem.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Por que a pesquisa de mapeamento é confidencial.\n\n"
            "A Agda Ximenes trabalhou 12 anos no SUAS, perto das casas de acolhimento. Neste vídeo ela explica por que as respostas são confidenciais "
            "e para que elas servem.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Capa de Reels com retrato em massinha da Agda Ximenes e o título Por que a pesquisa é confidencial.",
    },
    {
        "id": "11", "mes": M, "data_ordem": "2026-12-10", "data": "10/12", "dia_semana": "Quinta-feira", "horario": "18h",
        "fase": 1, "fase_nome": "Etapa 2 · Pesquisa e doação", "pauta": "Dia Internacional dos Direitos Humanos",
        "formato": "Card de posicionamento", "formato_slug": "card",
        "titulo": "Construir com as instituições",
        "objetivo": "Posicionamento do mês, no tom da carta-convite.",
        "publico": "Todos os públicos",
        "cta": "Salva e compartilha",
        "status": "pronto",
        "pendencias": [],
        "prova": "Frase da carta-convite da inauguração.",
        "slides": [
            {"tipo": "card", "mao": "10/12 · Direitos Humanos", "frase": "Construir com as instituições, e não apenas para elas."},
        ],
        "legenda_ig": (
            "Construir com as instituições, e não apenas para elas.\n\n"
            "Hoje é o Dia Internacional dos Direitos Humanos. Proteger a infância passa por fortalecer quem cuida dela todos os dias. "
            "Por isso cada passo da Net do Bem começa ouvindo as casas de acolhimento.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "Construir com as instituições, e não apenas para elas.\n\n"
            "Hoje é o Dia Internacional dos Direitos Humanos. Proteger a infância passa por fortalecer quem cuida dela todos os dias. "
            "Por isso cada passo da Fundação Net do Bem começa ouvindo as casas de acolhimento.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Card verde profundo com a frase em branco: Construir com as instituições, e não apenas para elas. Acima, escrito à mão: 10/12, Direitos Humanos.",
    },

    # ═════════════════════════ NATAL E CONTINUIDADE ═════════════════════════
    {
        "id": "12", "mes": M, "data_ordem": "2026-12-15", "data": "15/12", "dia_semana": "Terça-feira", "horario": "18h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "Campanha de Natal e continuidade",
        "formato": "Carrossel 3 cards", "formato_slug": "carrossel",
        "titulo": "Natal que dura o ano inteiro",
        "objetivo": "Transformar a vontade de ajudar no Natal em apoio contínuo para 2027.",
        "publico": "Pessoas físicas e empresas",
        "cta": "Chama no WhatsApp",
        "status": "pendencia",
        "pendencias": ["Definir como funciona a doação mensal (valor, canal) antes de publicar."],
        "prova": "Canal de doação do site e WhatsApp.",
        "slides": [
            {"tipo": "capa", "img": "natal-a2.jpg", "kicker": "Campanha de Natal", "mao": "um natal", "titulo": "que dura o ano inteiro"},
            {"tipo": "texto", "num": "", "titulo": "Dezembro mobiliza. Março também precisa.", "corpo": "As contas, a equipe e a formação de uma casa de acolhimento continuam o ano todo."},
            {"tipo": "cta", "titulo": "Apoio que continua", "texto": "Chama no WhatsApp", "apoio": "Doação mensal ou parceria da sua empresa. A gente explica como."},
        ],
        "legenda_ig": (
            "Natal que dura o ano inteiro.\n\n"
            "Em dezembro, muita gente se mobiliza para ajudar casas de acolhimento. Em março, as contas, a equipe e a formação continuam. "
            "Uma doação mensal ou uma parceria com a sua empresa mantém esse apoio de pé em 2027.\n\n"
            f"Chama no WhatsApp: {WHATS}."
        ),
        "legenda_fb": (
            "Natal que dura o ano inteiro.\n\n"
            "Em dezembro, muita gente se mobiliza para ajudar casas de acolhimento. Em março, as contas, a equipe e a formação continuam. "
            "Uma doação mensal ou uma parceria com a sua empresa mantém esse apoio de pé em 2027.\n\n"
            f"Chame no WhatsApp: {WHATS}."
        ),
        "alt": "Ilustração em massinha de adultos enfeitando uma pequena casa com luzes de Natal, ao lado do coração de rede. Texto: um Natal que dura o ano inteiro.",
    },
    {
        "id": "13", "mes": M, "data_ordem": "2026-12-17", "data": "17/12", "dia_semana": "Quinta-feira", "horario": "18h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "Empresas na rede",
        "formato": "Post único", "formato_slug": "post",
        "titulo": "Sua empresa na rede",
        "objetivo": "Convidar empresas a conhecer a rede por contato direto.",
        "publico": "Empresas e gestores de RH",
        "cta": "Marca uma empresa que poderia ajudar",
        "status": "pronto",
        "pendencias": [],
        "prova": "Modelo de articulação do site.",
        "slides": [
            {"tipo": "capa", "img": "empresa-b.jpg", "kicker": "Para empresas", "mao": "sua empresa", "titulo": "pode fazer parte da rede"},
        ],
        "legenda_ig": (
            "Sua empresa na rede.\n\n"
            "Empresas podem apoiar casas de acolhimento com recursos, conhecimento e voluntariado das equipes. "
            "A Net do Bem aproxima empresas das casas e acompanha esse apoio de perto, o ano inteiro.\n\n"
            "Marca uma empresa que poderia ajudar."
        ),
        "legenda_fb": (
            "Sua empresa na rede.\n\n"
            "Empresas podem apoiar casas de acolhimento com recursos, conhecimento e voluntariado das equipes. "
            "A Fundação Net do Bem aproxima empresas das casas e acompanha esse apoio de perto, o ano inteiro.\n\n"
            "Marque uma empresa que poderia ajudar."
        ),
        "alt": "Ilustração em massinha de profissionais adultos ligando fios coloridos de um pequeno prédio de escritório até uma casa. Texto: sua empresa pode fazer parte da rede.",
    },
    {
        "id": "14", "mes": M, "data_ordem": "2026-12-19", "data": "19/12", "dia_semana": "Sábado", "horario": "11h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "Destinação ao FIA (educativo)",
        "formato": "Carrossel 3 cards", "formato_slug": "carrossel",
        "titulo": "Seu imposto pode ficar na cidade",
        "objetivo": "Educar sobre a doação ao Fundo da Infância e Adolescência até 31/12, sem prometer destinação à fundação.",
        "publico": "Pessoas físicas que declaram IR completo",
        "cta": "Salva e compartilha",
        "status": "pendencia",
        "pendencias": [
            "Checklist 9.2 do briefing: revisão do contador da fundação antes de publicar.",
            "Confirmar o nome e o canal oficial do Fundo Municipal dos Direitos da Criança e do Adolescente de Sorocaba.",
        ],
        "prova": "ECA, arts. 260 e 260-A; orientação do gov.br sobre doações aos fundos.",
        "slides": [
            {"tipo": "capa", "img": "fia-a.jpg", "kicker": "Imposto de Renda", "mao": "até 31/12", "titulo": "Seu imposto pode ficar na cidade"},
            {"tipo": "texto", "num": "", "titulo": "Fundo da Infância e da Adolescência", "corpo": "Quem declara pelo modelo completo pode doar ao fundo municipal até 31/12 e deduzir até 6% do imposto devido."},
            {"tipo": "cta", "titulo": "Fale antes com seu contador", "texto": "Salva e compartilha", "apoio": "O recibo vem do conselho municipal. O valor vai para o fundo, não para a Net do Bem."},
        ],
        "legenda_ig": (
            "Seu imposto pode ficar na cidade.\n\n"
            "Até 31 de dezembro, quem declara o Imposto de Renda pelo modelo completo pode doar ao Fundo Municipal dos Direitos da Criança e do Adolescente "
            "e deduzir até 6% do imposto devido. O valor financia projetos da infância aprovados pelo conselho do seu município. Converse com seu contador antes de doar.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "Seu imposto pode ficar na cidade.\n\n"
            "Até 31 de dezembro, quem declara o Imposto de Renda pelo modelo completo pode doar ao Fundo Municipal dos Direitos da Criança e do Adolescente "
            "e deduzir até 6% do imposto devido (ECA, art. 260). O valor financia projetos da infância aprovados pelo conselho do seu município. Converse com seu contador antes de doar.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Ilustração em massinha de um adulto com documentos e calculadora, ligado por fios a um prédio público e a uma casa. Texto: até 31/12, seu imposto pode ficar na cidade.",
    },
    {
        "id": "15", "mes": M, "data_ordem": "2026-12-22", "data": "22/12", "dia_semana": "Terça-feira", "horario": "18h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "Cuidar sem se anular",
        "formato": "Carrossel 3 cards", "formato_slug": "carrossel",
        "titulo": "Dá para cuidar sem se anular?",
        "objetivo": "Conteúdo útil para quem trabalha nas casas no fim de ano.",
        "publico": "Equipes de acolhimento e cuidadores",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pendencia",
        "pendencias": ["Revisão técnica da Patrícia (psicóloga) antes de publicar."],
        "prova": "Conteúdo educativo com revisão de profissional habilitada.",
        "slides": [
            {"tipo": "capa", "img": "pausa-a.jpg", "kicker": "Para quem cuida", "mao": "no fim de ano", "titulo": "Dá para cuidar sem se anular?"},
            {"tipo": "lista", "titulo": "Três cuidados para dezembro", "itens": [
                "Respeitar a folga e a escala",
                "Falar do que pesa com colegas e supervisão",
                "Pedir ajuda antes do limite",
            ]},
            {"tipo": "cta", "texto": "Compartilha com quem cuida de alguém", "apoio": "Revisado pela psicóloga Patrícia Galheigo."},
        ],
        "legenda_ig": (
            "Dá para cuidar sem se anular?\n\n"
            "Quem trabalha numa casa de acolhimento passa o fim de ano atento às necessidades dos outros. "
            "Folga respeitada, conversa com colegas e supervisão ajudam essa pessoa a continuar cuidando bem, inclusive de si.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Dá para cuidar sem se anular?\n\n"
            "Quem trabalha numa casa de acolhimento passa o fim de ano atento às necessidades dos outros. "
            "Folga respeitada, conversa com colegas e supervisão ajudam essa pessoa a continuar cuidando bem, inclusive de si.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Ilustração em massinha de uma cuidadora descansando numa poltrona com uma xícara, e uma colega com a mão em seu ombro. Card seguinte lista três cuidados para dezembro.",
    },
    {
        "id": "16", "mes": M, "data_ordem": "2026-12-25", "data": "25/12", "dia_semana": "Sexta-feira", "horario": "10h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "Natal",
        "formato": "Post único", "formato_slug": "post",
        "titulo": "Feliz Natal a quem cuida",
        "objetivo": "Mensagem de Natal centrada em quem trabalha nas casas.",
        "publico": "Todos os públicos",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pronto",
        "pendencias": [],
        "prova": "Funcionamento contínuo do serviço de acolhimento.",
        "slides": [
            {"tipo": "capa", "img": "natal-b2.jpg", "kicker": "25 . 12", "mao": "feliz natal", "titulo": "a quem cuida"},
        ],
        "legenda_ig": (
            "Feliz Natal a quem cuida.\n\n"
            "Hoje tem educador, cozinheira, técnica e coordenadora de plantão nas casas de acolhimento. "
            "A cada uma dessas pessoas e a todas as equipes, nosso obrigado neste Natal.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Feliz Natal a quem cuida.\n\n"
            "Hoje tem educador, cozinheira, técnica e coordenadora de plantão nas casas de acolhimento. "
            "A cada uma dessas pessoas e a todas as equipes, o obrigado da Fundação Net do Bem neste Natal.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Ilustração em massinha de adultos de uma equipe reunidos em volta de uma pequena árvore de Natal com o coração de rede. Texto: feliz Natal a quem cuida.",
    },
    {
        "id": "17", "mes": M, "data_ordem": "2026-12-29", "data": "29/12", "dia_semana": "Terça-feira", "horario": "18h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "O que vem em 2027",
        "formato": "Carrossel 3 cards", "formato_slug": "carrossel",
        "titulo": "O que vem em 2027",
        "objetivo": "Fechar o ano mostrando os próximos passos e a continuidade.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": ["Barros, Patrícia e Agda confirmam os três passos."],
        "prova": "Plano da fundação; passos descritos como intenção.",
        "slides": [
            {"tipo": "capa", "img": "ano2027-a.jpg", "kicker": "Próximos passos", "mao": "em 2027", "titulo": "O que vem por aí"},
            {"tipo": "lista", "titulo": "Três passos", "itens": [
                "Concluir o mapeamento das casas",
                "Construir os apoios junto com elas",
                "Ampliar a rede de apoiadores e empresas",
            ]},
            {"tipo": "cta", "texto": "Siga e compartilhe", "apoio": "A gente conta cada passo por aqui."},
        ],
        "legenda_ig": (
            "O que vem em 2027.\n\n"
            "O primeiro ano da Net do Bem termina com a inauguração e a pesquisa de mapeamento no ar. "
            "Em 2027, o plano é concluir esse retrato das casas de acolhimento, construir os apoios junto com elas e ampliar a rede de apoiadores.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "O que vem em 2027.\n\n"
            "O primeiro ano da Fundação Net do Bem termina com a inauguração e a pesquisa de mapeamento no ar. "
            "Em 2027, o plano é concluir esse retrato das casas de acolhimento, construir os apoios junto com elas e ampliar a rede de apoiadores.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Ilustração em massinha de adultos plantando uma muda ao lado do coração de rede. Texto: em 2027, o que vem por aí. Card seguinte lista três passos.",
    },
    {
        "id": "18", "mes": M, "data_ordem": "2026-12-31", "data": "31/12", "dia_semana": "Quinta-feira", "horario": "11h",
        "fase": 2, "fase_nome": "Etapa 3 · Natal e continuidade", "pauta": "Ano Novo",
        "formato": "Card", "formato_slug": "card",
        "titulo": "Em 2027, seguimos juntos",
        "objetivo": "Fechar o ano com agradecimento.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": [],
        "prova": "Card de posicionamento.",
        "slides": [
            {"tipo": "card", "mao": "2027", "frase": "Seguimos juntos."},
        ],
        "legenda_ig": (
            "Em 2027, seguimos juntos.\n\n"
            "Obrigado a quem acompanhou o primeiro ano da Fundação Net do Bem. A gente se vê em janeiro.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Em 2027, seguimos juntos.\n\n"
            "Obrigado a quem acompanhou o primeiro ano da Fundação Net do Bem. A gente se vê em janeiro.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Card verde profundo com 2027 escrito à mão e a frase em branco: Seguimos juntos.",
    },
]

RESERVA = [
    {"titulo": "Depoimento de cuidador ou de uma casa", "fase": "2027", "quando": "Depois da pesquisa",
     "motivo": "O pré-briefing pede adiar para não dar foco a uma única casa."},
    {"titulo": "Como funciona o apoio, passo a passo", "fase": "2027", "quando": "Depois da pesquisa",
     "motivo": "Adiado pelo pré-briefing: o primeiro passo agora é a pesquisa."},
    {"titulo": "Perguntas da inauguração", "fase": "Stories", "quando": "Semana de 30/11",
     "motivo": "Vai para stories de caixinha de perguntas, com as respostas provisórias de roteiros/04."},
]
