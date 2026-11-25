# -*- coding: utf-8 -*-
"""
Fonte única dos posts da Fundação Net do Bem (Instagram e Facebook).

Fluxo: estrategista define fase/pauta/CTA -> copywriter escreve slides e legendas
-> designer escolhe o tipo de slide -> técnico roda render.py e build.py.

Regras do Briefing V2 aplicadas a cada post:
- 1 ideia e 1 CTA por post (CTA da lista da seção 11)
- gancho do slide 1 com até 6 palavras
- sem criança identificável, sem endereço, sem rotina de casa parceira
- nada de Imposto de Renda antes da Fase 5
- sem travessão em nenhum texto
Se faltar informação real (foto, entrevista, confirmação), status = "pendencia".
"""

HASHTAGS_BASE = "#FundacaoNetDoBem #Sorocaba #Acolhimento #QuemCuidaDeQuemCuida"

POSTS = [
    # ════════════════════════════ NOVEMBRO · FASE 0 · INAUGURAÇÃO ════════════════════════════
    {
        "id": "01", "mes": "novembro-dezembro", "data_ordem": "2026-11-26", "data": "26/11", "dia_semana": "Quinta-feira",
        "horario": "17h, antes do evento",
        "fase": 0, "fase_nome": "Fase 0 · Inauguração", "pauta": "P0.1 · Inauguramos hoje",
        "formato": "Arte limpa (versão com foto opcional)", "formato_slug": "foto-faixa",
        "titulo": "Hoje é dia de inaugurar",
        "objetivo": "Existir. Avisar que a fundação foi inaugurada e que o perfil começa hoje.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": [
            "Sugestão do plano de crescimento: publicar em collab com o perfil pessoal do André (e de parceiros de Sorocaba, se houver), pedir para seguir o perfil na fala de abertura e deixar o QR code do Instagram (gerado no próprio app) visível no evento.",
            "Opcional: se a equipe tirar uma foto antes das 17h, trocar a arte pela versão com foto e faixa verde (slide 2 desta peça mostra o layout).",
        ],
        "prova": "Sem foto real no momento: arte limpa, como pede o briefing.",
        "slides": [
            {"tipo": "capa", "img": "inauguracao-b.jpg", "kicker": "26 . 11 . 2026  ·  Sorocaba", "titulo": "Hoje é dia de inaugurar"},
            {"tipo": "foto", "img": None, "faixa": "Hoje é dia de inaugurar",
             "placeholder": "Versão opcional: foto da equipe (só adultos) antes do evento"},
        ],
        "legenda_ig": (
            "Hoje é dia de inaugurar.\n\n"
            "Um ano depois de nascer, a Fundação Net do Bem é inaugurada hoje, em Sorocaba, num encontro com convidados. Nosso trabalho é apoiar as casas de acolhimento "
            "e as pessoas que cuidam nelas: educadores, equipes técnicas, gestores e voluntários. "
            "A partir de agora, você acompanha esse trabalho por aqui.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Hoje é dia de inaugurar.\n\n"
            "Um ano depois de nascer, a Fundação Net do Bem é inaugurada hoje, em Sorocaba, num encontro com convidados. Nosso trabalho é apoiar as casas de acolhimento "
            "de crianças e adolescentes e as pessoas que cuidam nelas: educadores, equipes técnicas, gestores e voluntários.\n\n"
            "Esta página vai mostrar esse trabalho de perto, sem expor nenhuma criança.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Arte em fundo creme com o logo da Fundação Net do Bem, um coração desenhado com linhas e pontos, e a frase "
               "Hoje é dia de inaugurar. Abaixo, a data 26 de novembro de 2026 e a cidade, Sorocaba.",
        "stories": [
            {"quando": "Manhã", "titulo": "Hoje é o dia", "corpo": "Inauguração da Fundação Net do Bem", "tema": "verde"},
            {"quando": "Durante", "titulo": "Começou", "corpo": "Repost de quem marcar o perfil, só com adultos na imagem", "tema": "creme"},
            {"quando": "Depois", "titulo": "Obrigado", "corpo": "Amanhã a gente conta como foi", "tema": "verde"},
        ],
    },
    {
        "id": "02", "mes": "novembro-dezembro", "data_ordem": "2026-11-27", "data": "27/11", "dia_semana": "Sexta-feira",
        "horario": "18h",
        "fase": 0, "fase_nome": "Fase 0 · Inauguração", "pauta": "P0.2 · Frase-mãe",
        "formato": "Card de posicionamento", "formato_slug": "card",
        "titulo": "Fortalecer quem cuida também é proteger a infância",
        "objetivo": "Fixar a frase-mãe no primeiro dia depois da inauguração.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": [],
        "prova": "Card de posicionamento, sem foto.",
        "slides": [
            {"tipo": "card", "frase": "Fortalecer quem cuida também é proteger a infância."},
        ],
        "legenda_ig": (
            "Fortalecer quem cuida também é proteger a infância.\n\n"
            "Escolhemos essa frase para explicar a Net do Bem. Uma casa de acolhimento funciona porque tem gente cuidando "
            "todos os dias. Quando essa equipe tem formação, estrutura e apoio, crianças e adolescentes recebem um cuidado melhor.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Fortalecer quem cuida também é proteger a infância.\n\n"
            "Escolhemos essa frase para explicar a Fundação Net do Bem. Uma casa de acolhimento funciona porque tem gente cuidando "
            "todos os dias: educadores, equipe técnica, coordenação e voluntários. Quando essa equipe tem formação, estrutura e apoio, "
            "crianças e adolescentes recebem um cuidado melhor.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Card verde profundo com a frase em branco: Fortalecer quem cuida também é proteger a infância. Logo pequeno da Fundação Net do Bem abaixo.",
    },
    {
        "id": "03", "mes": "novembro-dezembro", "data_ordem": "2026-11-28", "data": "28/11", "dia_semana": "Sábado",
        "horario": "11h",
        "fase": 0, "fase_nome": "Fase 0 · Inauguração", "pauta": "P0.3 · Bastidor",
        "formato": "Carrossel de fotos reais com faixa", "formato_slug": "foto-faixa",
        "titulo": "Os bastidores da inauguração",
        "objetivo": "Mostrar pessoas reais e a preparação, com foto de verdade.",
        "publico": "Convidados e comunidade",
        "cta": "Siga e compartilhe",
        "status": "pendencia",
        "pendencias": [
            "Fotos do evento: equipe montando, convidados adultos, fala da Patrícia e da Agda. Nenhuma criança, nenhuma placa ou fachada do local.",
            "Confirmar autorização de imagem dos adultos que aparecem de rosto.",
        ],
        "prova": "Capa em massinha; fotos reais do evento entram nos slides 2 a 5.",
        "slides": [
            {"tipo": "capa", "img": "bastidores-a.jpg", "kicker": "Antes da quinta-feira", "titulo": "Os bastidores da inauguração"},
            {"tipo": "foto", "img": None, "faixa": "Preparando o espaço", "placeholder": "Foto da equipe preparando o espaço"},
            {"tipo": "foto", "img": "banner-verde.jpg", "faixa": "O banner que recebeu os convidados", "fit": "contain"},
            {"tipo": "foto", "img": None, "faixa": "Quem esteve com a gente", "placeholder": "Foto de convidados adultos, com autorização"},
            {"tipo": "foto", "img": None, "faixa": "A apresentação da fundação", "placeholder": "Foto da Patrícia ou da Agda falando"},
            {"tipo": "cta", "texto": "Siga e compartilhe", "apoio": "Em dezembro, a gente explica o nosso trabalho post a post."},
        ],
        "legenda_ig": (
            "Os bastidores da inauguração.\n\n"
            "Antes de quinta-feira teve banner chegando da gráfica, apresentação sendo ajustada e muita conversa sobre como contar o que a Net do Bem faz. "
            "Nesta galeria estão alguns desses momentos e as pessoas que estiveram com a gente.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Os bastidores da inauguração.\n\n"
            "Antes de quinta-feira teve banner chegando da gráfica, apresentação sendo ajustada e muita conversa sobre como contar o que a Fundação Net do Bem faz. "
            "Nesta galeria estão alguns desses momentos e as pessoas que estiveram com a gente. Obrigado a cada um.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Carrossel de fotos da inauguração com faixa verde na parte de baixo. Mostra o banner verde com o logo e a frase Sejam bem-vindos, "
               "a equipe e convidados adultos. Não aparecem crianças.",
    },
    {
        "id": "04", "mes": "novembro-dezembro", "data_ordem": "2026-11-29", "data": "29/11", "dia_semana": "Domingo",
        "horario": "18h",
        "fase": 0, "fase_nome": "Fase 0 · Inauguração", "pauta": "P0.4 · Quem está por trás",
        "formato": "Carrossel de retratos + Reels do fundador", "formato_slug": "carrossel",
        "titulo": "Quem faz a Net do Bem",
        "objetivo": "Dar rosto e função às três pessoas que apresentaram a fundação.",
        "publico": "Todos os públicos",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": [
            "Reels do André (30 a 45 s) gravado na inauguração: se existir, publicar o Reels neste dia e guardar o carrossel para 06/12.",
            "Confirmar com Patrícia e Agda os cargos como devem aparecer.",
        ],
        "prova": "Retratos oficiais em massinha do site e trajetória confirmada nos textos da inauguração.",
        "slides": [
            {"tipo": "capa", "img": "trio-b.jpg", "kicker": "Quem está por trás", "titulo": "Quem faz a Net do Bem", "sub": "Três pessoas, três trajetórias"},
            {"tipo": "retrato", "img": "founder-net-do-bem.webp", "nome": "André Facciolli", "papel": "Fundador",
             "corpo": "Empresário há mais de 30 anos na tecnologia. Criou a fundação para colocar gestão e rede a serviço da infância."},
            {"tipo": "retrato", "img": "patricia-operacoes-netdobem.webp", "nome": "Patrícia Galheigo", "papel": "Diretora administrativa",
             "corpo": "Psicóloga. Passou 18 anos formando lideranças e equipes em empresas."},
            {"tipo": "retrato", "img": "agda-estrategia-net-do-bem.webp", "nome": "Agda Ximenes", "papel": "Assessoramento técnico",
             "corpo": "Assistente social. Trabalhou 12 anos no SUAS, perto das casas de acolhimento."},
            {"tipo": "cta", "texto": "Siga e compartilhe", "apoio": "Nos próximos posts, cada um conta por que está aqui."},
        ],
        "roteiro": [
            "0 a 3 s, olhando para a câmera: \"Eu sou o André e criei a Fundação Net do Bem.\"",
            "Por que existimos: \"As casas de acolhimento fazem um trabalho enorme e quase sempre sem apoio de gestão. A gente quer mudar isso.\"",
            "O que pedimos hoje: \"Siga o perfil e compartilhe com quem trabalha com acolhimento.\"",
        ],
        "legenda_ig": (
            "Quem faz a Net do Bem.\n\n"
            "O André Facciolli fundou a Net do Bem para colocar a experiência de gestão dele a serviço da infância. "
            "A Patrícia Galheigo é psicóloga e passou 18 anos formando lideranças e equipes. "
            "A Agda Ximenes é assistente social e trabalhou 12 anos no SUAS, perto das casas de acolhimento.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Quem faz a Fundação Net do Bem.\n\n"
            "André Facciolli, fundador, é empresário há mais de 30 anos na área de tecnologia e criou a fundação para colocar essa experiência de gestão a serviço da infância.\n"
            "Patrícia Galheigo, diretora administrativa, é psicóloga e passou 18 anos formando lideranças e equipes.\n"
            "Agda Ximenes, do assessoramento técnico, é assistente social e trabalhou 12 anos no SUAS, perto das casas de acolhimento.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Carrossel com retratos em massinha das três pessoas da fundação: André Facciolli, fundador, de camiseta azul com o logo; "
               "Patrícia Galheigo, diretora administrativa; e Agda Ximenes, do assessoramento técnico. Cada slide traz nome, função e uma frase sobre a trajetória.",
    },
    {
        "id": "05", "mes": "novembro-dezembro", "data_ordem": "2026-11-30", "data": "30/11", "dia_semana": "Segunda-feira",
        "horario": "18h",
        "fase": 0, "fase_nome": "Fase 0 · Inauguração", "pauta": "P0.5 · Obrigado",
        "formato": "Arte limpa (versão com foto opcional)", "formato_slug": "foto-faixa",
        "titulo": "Obrigado por estar aqui",
        "objetivo": "Agradecer e anunciar o que vem em dezembro.",
        "publico": "Convidados e novos seguidores",
        "cta": "Siga e compartilhe",
        "status": "pronto",
        "pendencias": [
            "Opcional: trocar pela foto da equipe no evento, com a mesma faixa (slide 2).",
        ],
        "prova": "Arte limpa; foto da equipe se disponível.",
        "slides": [
            {"tipo": "capa", "img": "maos-coracao-a.jpg", "kicker": "Depois da inauguração", "titulo": "Obrigado por estar aqui"},
            {"tipo": "foto", "img": None, "faixa": "Obrigado por estar aqui", "placeholder": "Versão opcional: foto da equipe na inauguração"},
        ],
        "legenda_ig": (
            "Obrigado por estar aqui.\n\n"
            "Na quinta-feira recebemos convidados na nossa inauguração, em Sorocaba, e muita gente acompanhou por aqui. "
            "Em dezembro vamos explicar, post a post, como a Net do Bem apoia as casas de acolhimento e quem cuida nelas.\n\n"
            "Siga e compartilhe."
        ),
        "legenda_fb": (
            "Obrigado por estar aqui.\n\n"
            "Na quinta-feira recebemos convidados na inauguração da Fundação Net do Bem, em Sorocaba. "
            "Em dezembro vamos explicar, post a post, como a fundação apoia as casas de acolhimento e as pessoas que cuidam nelas.\n\n"
            "Siga a página e compartilhe."
        ),
        "alt": "Arte em fundo creme com o coração de linhas e pontos da Fundação Net do Bem e a frase Obrigado por estar aqui.",
    },

    # ════════════════════════════ DEZEMBRO · FASE 1 · QUEM SOMOS ════════════════════════════
    {
        "id": "06", "mes": "novembro-dezembro", "data_ordem": "2026-12-01", "data": "01/12", "dia_semana": "Terça-feira",
        "horario": "18h",
        "fase": 1, "fase_nome": "Fase 1 · Quem somos", "pauta": "Pauta-mãe 1 · Quem somos",
        "formato": "Carrossel educativo", "formato_slug": "carrossel",
        "titulo": "A Net do Bem em 5 slides",
        "objetivo": "A pessoa entender em 10 segundos o que a fundação faz. Post para fixar no perfil.",
        "publico": "Todos os públicos",
        "cta": "Salva e compartilha",
        "status": "pronto",
        "pendencias": [],
        "prova": "Frentes de atuação publicadas no site netdobem.org.br e pesquisa aberta no portal.",
        "slides": [
            {"tipo": "capa", "img": "equipe-a.jpg", "kicker": "Para fixar no perfil", "titulo": "A Net do Bem em 5 slides"},
            {"tipo": "texto", "num": "1", "titulo": "Somos uma fundação de Sorocaba.", "corpo": "Apoiamos casas de acolhimento de crianças e adolescentes."},
            {"tipo": "texto", "num": "2", "titulo": "Cuidamos de quem cuida.", "corpo": "Educadores, técnicos, gestores e voluntários seguram o dia a dia de uma casa. O nosso foco está neles."},
            {"tipo": "lista", "num": "3", "titulo": "Quatro frentes de trabalho", "itens": ["Pesquisa e conhecimento", "Capacitação e gestão", "Aceleração de organizações", "Articulação com parceiros"]},
            {"tipo": "texto", "num": "4", "titulo": "Começamos ouvindo.", "corpo": "Um mapeamento das casas de acolhimento já está no ar para entender o que cada uma precisa."},
            {"tipo": "cta", "texto": "Salva e compartilha", "apoio": "Assim fica fácil explicar a Net do Bem para alguém."},
        ],
        "legenda_ig": (
            "A Net do Bem em 5 slides.\n\n"
            "Se você chegou agora, este é o resumo. Apoiamos casas de acolhimento e as equipes que trabalham nelas, com pesquisa, formação, "
            "apoio de gestão e conexão com parceiros. O primeiro passo é ouvir as casas, com um mapeamento que já está no ar.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "A Fundação Net do Bem em 5 slides.\n\n"
            "Se você chegou agora, este é o resumo. Apoiamos casas de acolhimento e as equipes que trabalham nelas, com pesquisa, formação, "
            "apoio de gestão e conexão com parceiros. O primeiro passo é ouvir as casas, com um mapeamento que já está no ar.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Carrossel em fundo creme com títulos em verde. Slides: somos uma fundação de Sorocaba; cuidamos de quem cuida; quatro frentes de trabalho "
               "(pesquisa, capacitação, aceleração e articulação); começamos ouvindo; e o convite para salvar e compartilhar.",
    },
    {
        "id": "07", "mes": "novembro-dezembro", "data_ordem": "2026-12-03", "data": "03/12", "dia_semana": "Quinta-feira",
        "horario": "18h",
        "fase": 1, "fase_nome": "Fase 1 · Quem somos", "pauta": "Pauta-mãe 2 · O que não fazemos",
        "formato": "Carrossel educativo", "formato_slug": "carrossel",
        "titulo": "O que não fazemos",
        "objetivo": "Evitar a confusão com abrigo e adoção logo no começo.",
        "publico": "Sociedade e potenciais apoiadores",
        "cta": "Salva e compartilha",
        "status": "pronto",
        "pendencias": [],
        "prova": "Posicionamento do Briefing V2 e fala da Agda na inauguração.",
        "slides": [
            {"tipo": "capa", "img": "escuta-a.jpg", "kicker": "Para entender o nosso papel", "titulo": "O que não fazemos"},
            {"tipo": "texto", "num": "1", "titulo": "Não acolhemos crianças.", "corpo": "Apoiamos as casas de acolhimento que fazem esse trabalho."},
            {"tipo": "texto", "num": "2", "titulo": "Não trabalhamos com adoção.", "corpo": "Adoção tem caminho próprio, pela Justiça da Infância e da Juventude."},
            {"tipo": "texto", "num": "3", "titulo": "Não chegamos para fiscalizar.", "corpo": "Chegamos para ouvir cada casa e construir o apoio junto com a equipe."},
            {"tipo": "texto", "num": "4", "titulo": "O que fazemos", "corpo": "Formação, apoio de gestão, pesquisa e conexão com parceiros para quem cuida."},
            {"tipo": "cta", "texto": "Salva e compartilha", "apoio": "Ajuda quem ainda confunde fundação com abrigo."},
        ],
        "legenda_ig": (
            "O que não fazemos.\n\n"
            "A Net do Bem não acolhe crianças e não trabalha com adoção. Apoiamos as casas de acolhimento que já fazem esse trabalho, "
            "com formação, gestão e conexão com parceiros. E chegamos para ouvir, sem fiscalizar ninguém.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "O que a Fundação Net do Bem não faz.\n\n"
            "Não acolhemos crianças e não trabalhamos com adoção. Apoiamos as casas de acolhimento que já fazem esse trabalho, "
            "com formação, gestão e conexão com parceiros. Chegamos para ouvir cada casa, sem papel de fiscalização.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Carrossel em fundo creme: não acolhemos crianças; não trabalhamos com adoção; não chegamos para fiscalizar; e o que fazemos, "
               "formação, apoio de gestão, pesquisa e conexão com parceiros.",
    },
    {
        "id": "08", "mes": "novembro-dezembro", "data_ordem": "2026-12-05", "data": "05/12", "dia_semana": "Sábado",
        "horario": "11h",
        "fase": 1, "fase_nome": "Fase 1 · Quem somos", "pauta": "Fase 1 · Por que Sorocaba?",
        "formato": "Carrossel educativo", "formato_slug": "carrossel",
        "titulo": "Por que Sorocaba?",
        "objetivo": "Dar raiz local à fundação.",
        "publico": "Comunidade de Sorocaba",
        "cta": "Salva e compartilha",
        "status": "pendencia",
        "pendencias": [
            "Confirmar com o André o motivo pessoal da escolha de Sorocaba para o slide 2. O texto atual só usa o que está no CNPJ e no site.",
            "Confirmar se a pesquisa do portal já recebe casas de fora de Sorocaba (o portal fala em diagnóstico nacional).",
        ],
        "prova": "Sede registrada em Sorocaba e portal da pesquisa no ar.",
        "slides": [
            {"tipo": "capa", "img": "rede-casas-b.jpg", "kicker": "Raiz local", "titulo": "Por que Sorocaba?"},
            {"tipo": "texto", "num": "1", "titulo": "Foi aqui que a fundação nasceu.", "corpo": "A Net do Bem nasceu em Sorocaba em 26 de novembro de 2025. [Motivo pessoal do André a confirmar]"},
            {"tipo": "texto", "num": "2", "titulo": "Perto das casas.", "corpo": "Estar na mesma cidade permite visitar, ouvir e acompanhar cada organização de perto."},
            {"tipo": "texto", "num": "3", "titulo": "A escuta vai além.", "corpo": "O mapeamento no portal recebe casas de acolhimento de todo o Brasil."},
            {"tipo": "cta", "texto": "Salva e compartilha", "apoio": "Marca quem é de Sorocaba e trabalha com acolhimento."},
        ],
        "legenda_ig": (
            "Por que Sorocaba?\n\n"
            "A Net do Bem nasceu aqui em novembro de 2025, e começar perto das casas de acolhimento permite visitar, ouvir e acompanhar cada uma. "
            "[Frase do André sobre a escolha da cidade, a confirmar]\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "Por que a Fundação Net do Bem nasceu em Sorocaba?\n\n"
            "Começar perto das casas de acolhimento permite visitar, ouvir e acompanhar cada uma. "
            "[Frase do André sobre a escolha da cidade, a confirmar]\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Carrossel em fundo creme sobre a escolha de Sorocaba: a fundação nasceu na cidade, trabalha perto das casas e recebe casas de todo o Brasil no mapeamento.",
    },
    {
        "id": "09", "mes": "novembro-dezembro", "data_ordem": "2026-12-08", "data": "08/12", "dia_semana": "Terça-feira",
        "horario": "18h",
        "fase": 1, "fase_nome": "Fase 1 · Quem somos", "pauta": "Fase 1 · Reels do fundador",
        "formato": "Reels 30 a 45 s + capa", "formato_slug": "reels",
        "titulo": "Por que criei a Net do Bem",
        "objetivo": "Rosto real e motivação do fundador, em vídeo.",
        "publico": "Todos os públicos",
        "cta": "Salva e compartilha",
        "status": "pendencia",
        "pendencias": [
            "Reels de 30 a 60 s; publicar em collab com o perfil pessoal do André.",
            "Gravar o André olhando para a câmera, fundo real, sem estúdio, até 04/12.",
            "Se o Reels já tiver sido publicado em 29/11, trocar esta data pelo carrossel de retratos.",
        ],
        "prova": "Vídeo do fundador com consentimento.",
        "slides": [
            {"tipo": "reels", "img": "founder-net-do-bem.webp", "titulo": "Por que criei a Net do Bem", "sub": "André Facciolli, fundador"},
        ],
        "roteiro": [
            "0 a 3 s: \"Depois de 30 anos construindo empresa, eu quis devolver uma parte disso.\"",
            "Meio: \"Conheci casas de acolhimento com equipes incríveis e sem apoio de gestão, de captação, de planejamento. A Net do Bem existe para levar esse apoio.\"",
            "Fecho: \"Salva este vídeo e compartilha com quem trabalha com acolhimento.\"",
        ],
        "legenda_ig": (
            "Por que criei a Net do Bem.\n\n"
            "O André passou mais de 30 anos construindo empresa na tecnologia. Neste vídeo, ele conta por que decidiu colocar essa experiência "
            "de gestão a serviço das casas de acolhimento.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "Por que criei a Fundação Net do Bem.\n\n"
            "O André Facciolli passou mais de 30 anos construindo empresa na tecnologia. Neste vídeo, ele conta por que decidiu colocar essa experiência "
            "de gestão a serviço das casas de acolhimento.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Capa de Reels com retrato em massinha do André Facciolli e o título Por que criei a Net do Bem.",
    },
    {
        "id": "10", "mes": "novembro-dezembro", "data_ordem": "2026-12-10", "data": "10/12", "dia_semana": "Quinta-feira",
        "horario": "18h",
        "fase": 1, "fase_nome": "Fase 1 · Quem somos", "pauta": "Pauta-mãe 9 · Perguntas que mais recebemos",
        "formato": "Carrossel educativo", "formato_slug": "carrossel",
        "titulo": "3 perguntas da inauguração",
        "objetivo": "Responder as dúvidas reais que surgiram no evento.",
        "publico": "Convidados, casas e apoiadores",
        "cta": "Salva e compartilha",
        "status": "pendencia",
        "pendencias": [
            "Trocar pelas 3 perguntas que a equipe mais ouviu na inauguração (pedir à Patrícia e à Agda até 05/12).",
            "Definir a resposta oficial para \"como posso ajudar?\" antes de publicar.",
        ],
        "prova": "Perguntas reais registradas pela equipe.",
        "slides": [
            {"tipo": "capa", "img": "perguntas-a.jpg", "kicker": "Respostas curtas", "titulo": "3 perguntas da inauguração"},
            {"tipo": "pergunta", "num": "1", "pergunta": "Vocês acolhem crianças?", "resposta": "Não. Apoiamos as casas de acolhimento e as equipes que trabalham nelas."},
            {"tipo": "pergunta", "num": "2", "pergunta": "Como uma casa participa?", "resposta": "O primeiro passo é responder ao mapeamento em portal.netdobem.org.br."},
            {"tipo": "pergunta", "num": "3", "pergunta": "Como eu posso ajudar?", "resposta": "[Resposta oficial a confirmar com a diretoria]"},
            {"tipo": "cta", "texto": "Salva e compartilha", "apoio": "Tem outra pergunta? Responderemos nos próximos posts."},
        ],
        "legenda_ig": (
            "3 perguntas da inauguração.\n\n"
            "Separamos as dúvidas que mais ouvimos na quinta-feira, 26/11. A primeira é a mais comum: a Net do Bem não acolhe crianças. "
            "Apoiamos as casas e as equipes que fazem esse trabalho.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "3 perguntas que ouvimos na inauguração.\n\n"
            "Separamos as dúvidas que mais apareceram no dia 26/11. A primeira é a mais comum: a Fundação Net do Bem não acolhe crianças. "
            "Apoiamos as casas e as equipes que fazem esse trabalho.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Carrossel de perguntas e respostas em fundo creme: vocês acolhem crianças; como uma casa participa; como eu posso ajudar.",
    },
    {
        "id": "11", "mes": "novembro-dezembro", "data_ordem": "2026-12-12", "data": "12/12", "dia_semana": "Sábado",
        "horario": "11h",
        "fase": 1, "fase_nome": "Fase 1 · Quem somos", "pauta": "Card de posicionamento da semana",
        "formato": "Card de posicionamento", "formato_slug": "card",
        "titulo": "Quem fortalece uma organização alcança muitas histórias",
        "objetivo": "Reforçar o modelo: apoiar a organização em vez de atender direto.",
        "publico": "Empresas e potenciais parceiros",
        "cta": "Salva e compartilha",
        "status": "pronto",
        "pendencias": [],
        "prova": "Frase de apoio do documento de identidade.",
        "slides": [
            {"tipo": "card", "frase": "Quem fortalece uma organização alcança muitas histórias."},
        ],
        "legenda_ig": (
            "Quem fortalece uma organização alcança muitas histórias.\n\n"
            "Uma casa de acolhimento bem organizada atende crianças e adolescentes por anos, com a mesma equipe ganhando experiência. "
            "Por isso a Net do Bem investe na organização e em quem trabalha nela.\n\n"
            "Salva e compartilha."
        ),
        "legenda_fb": (
            "Quem fortalece uma organização alcança muitas histórias.\n\n"
            "Uma casa de acolhimento bem organizada atende crianças e adolescentes por anos, com a mesma equipe ganhando experiência. "
            "Por isso a Fundação Net do Bem investe na organização e em quem trabalha nela.\n\n"
            "Salve e compartilhe."
        ),
        "alt": "Card verde profundo com a frase em branco: Quem fortalece uma organização alcança muitas histórias.",
    },

    # ════════════════════════════ DEZEMBRO · FASE 2 · QUEM CUIDA ════════════════════════════
    {
        "id": "12", "mes": "novembro-dezembro", "data_ordem": "2026-12-15", "data": "15/12", "dia_semana": "Terça-feira",
        "horario": "18h",
        "fase": 2, "fase_nome": "Fase 2 · Quem cuida", "pauta": "Pauta-mãe 3 · Quem cuida de quem cuida",
        "formato": "Carrossel educativo", "formato_slug": "carrossel",
        "titulo": "Quem cuida de quem cuida?",
        "objetivo": "Abrir o território próprio da marca.",
        "publico": "Equipes de acolhimento e sociedade",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pronto",
        "pendencias": [],
        "prova": "Funcionamento contínuo do serviço de acolhimento institucional (Tipificação Nacional dos Serviços Socioassistenciais).",
        "slides": [
            {"tipo": "capa", "img": "equipe-b.jpg", "kicker": "O nosso território", "titulo": "Quem cuida de quem cuida?"},
            {"tipo": "texto", "num": "1", "titulo": "Uma casa não fecha.", "corpo": "O acolhimento funciona 24 horas por dia, todos os dias. Sempre tem alguém de plantão."},
            {"tipo": "texto", "num": "2", "titulo": "Essa equipe também precisa de apoio.", "corpo": "Formação, supervisão, troca com outras casas e uma gestão que funcione."},
            {"tipo": "texto", "num": "3", "titulo": "A Net do Bem existe para isso.", "corpo": "Levar formação, apoio de gestão e parceiros para quem está na ponta."},
            {"tipo": "cta", "texto": "Compartilha com quem cuida de alguém", "apoio": "Manda por direct para quem trabalha numa casa de acolhimento."},
        ],
        "legenda_ig": (
            "Quem cuida de quem cuida?\n\n"
            "Uma casa de acolhimento funciona 24 horas por dia, e sempre tem um educador, uma técnica ou uma coordenadora de plantão. "
            "Essas pessoas também precisam de formação, supervisão e uma gestão que funcione. A Net do Bem existe para levar esse apoio.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Quem cuida de quem cuida?\n\n"
            "Uma casa de acolhimento funciona 24 horas por dia, e sempre tem um educador, uma técnica ou uma coordenadora de plantão. "
            "Essas pessoas também precisam de formação, supervisão e uma gestão que funcione. A Fundação Net do Bem existe para levar esse apoio.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Carrossel em fundo creme: uma casa não fecha; essa equipe também precisa de apoio; a Net do Bem existe para isso; compartilha com quem cuida de alguém.",
    },
    {
        "id": "13", "mes": "novembro-dezembro", "data_ordem": "2026-12-17", "data": "17/12", "dia_semana": "Quinta-feira",
        "horario": "18h",
        "fase": 2, "fase_nome": "Fase 2 · Quem cuida", "pauta": "Pauta-mãe 4 · 3 coisas que uma casa precisa",
        "formato": "Carrossel lista", "formato_slug": "carrossel",
        "titulo": "3 necessidades que ninguém vê",
        "objetivo": "Mostrar o trabalho invisível que sustenta o cuidado.",
        "publico": "Empresas e sociedade",
        "cta": "Marca uma empresa que poderia ajudar",
        "status": "pronto",
        "pendencias": [],
        "prova": "Frentes de atuação da fundação e falas da equipe técnica na inauguração.",
        "slides": [
            {"tipo": "capa", "img": "planejamento-b.jpg", "escala": 84, "kicker": "Lista rápida", "titulo": "3 necessidades que ninguém vê"},
            {"tipo": "texto", "num": "1", "titulo": "Gestão e planejamento", "corpo": "Orçamento, prestação de contas e editais. Sem isso, o cuidado fica sem continuidade."},
            {"tipo": "texto", "num": "2", "titulo": "Formação da equipe", "corpo": "Quem cuida lida com histórias difíceis todos os dias. Formação e supervisão ajudam na rotina."},
            {"tipo": "texto", "num": "3", "titulo": "Rede de apoio", "corpo": "Escola, saúde, conselhos, empresas e voluntários. Uma casa não dá conta sozinha."},
            {"tipo": "cta", "texto": "Marca uma empresa que poderia ajudar", "apoio": "Gestão, formação e rede também se apoiam."},
        ],
        "legenda_ig": (
            "3 necessidades que ninguém vê.\n\n"
            "Quando se fala de casa de acolhimento, quase sempre a conversa é sobre doação de itens. "
            "O dia a dia também depende de gestão, de uma equipe com formação e de uma rede de apoio por perto.\n\n"
            "Marca uma empresa que poderia ajudar."
        ),
        "legenda_fb": (
            "3 necessidades que ninguém vê numa casa de acolhimento.\n\n"
            "Quando se fala de casa de acolhimento, quase sempre a conversa é sobre doação de itens. "
            "O dia a dia também depende de gestão, de uma equipe com formação e de uma rede de apoio por perto.\n\n"
            "Marque uma empresa que poderia ajudar."
        ),
        "alt": "Carrossel em fundo creme com três itens numerados: gestão e planejamento, formação da equipe e rede de apoio.",
    },
    {
        "id": "14", "mes": "novembro-dezembro", "data_ordem": "2026-12-19", "data": "19/12", "dia_semana": "Sábado",
        "horario": "11h",
        "fase": 2, "fase_nome": "Fase 2 · Quem cuida", "pauta": "Card de posicionamento da semana",
        "formato": "Card de posicionamento", "formato_slug": "card",
        "titulo": "Por trás de cada casa, tem gente",
        "objetivo": "Fixar o território quem cuida.",
        "publico": "Todos os públicos",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pronto",
        "pendencias": [],
        "prova": "Frase do Briefing V2.",
        "slides": [
            {"tipo": "card", "frase": "Por trás de cada casa, tem gente que precisa de apoio também."},
        ],
        "legenda_ig": (
            "Por trás de cada casa, tem gente que precisa de apoio também.\n\n"
            "Educadores, cozinheiras, psicólogas, assistentes sociais e coordenadores fazem o acolhimento acontecer. "
            "É para essas pessoas que a Net do Bem trabalha.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Por trás de cada casa, tem gente que precisa de apoio também.\n\n"
            "Educadores, cozinheiras, psicólogas, assistentes sociais e coordenadores fazem o acolhimento acontecer. "
            "É para essas pessoas que a Fundação Net do Bem trabalha.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Card verde profundo com a frase em branco: Por trás de cada casa, tem gente que precisa de apoio também.",
    },
    {
        "id": "15", "mes": "novembro-dezembro", "data_ordem": "2026-12-22", "data": "22/12", "dia_semana": "Terça-feira",
        "horario": "18h",
        "fase": 2, "fase_nome": "Fase 2 · Quem cuida", "pauta": "Fase 2 · Cuidar sem se anular",
        "formato": "Carrossel educativo", "formato_slug": "carrossel",
        "titulo": "Dá para cuidar sem se anular?",
        "objetivo": "Conteúdo útil para cuidadores no fim de ano.",
        "publico": "Equipes de acolhimento e cuidadores em geral",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pendencia",
        "pendencias": [
            "Revisão técnica da Patrícia (psicóloga) antes de publicar.",
        ],
        "prova": "Conteúdo educativo com revisão de profissional habilitada.",
        "slides": [
            {"tipo": "capa", "img": "pausa-a.jpg", "kicker": "Para quem cuida", "titulo": "Dá para cuidar sem se anular?"},
            {"tipo": "texto", "num": "1", "titulo": "Cansaço também é sinal.", "corpo": "Quem cuida de outras pessoas o dia todo costuma deixar o próprio cansaço para depois."},
            {"tipo": "texto", "num": "2", "titulo": "Pausa faz parte do trabalho.", "corpo": "Escala organizada, folga respeitada e espaço para falar do que pesa."},
            {"tipo": "texto", "num": "3", "titulo": "Ninguém cuida bem sozinho.", "corpo": "Supervisão e conversa com colegas ajudam a dividir as situações difíceis."},
            {"tipo": "cta", "texto": "Compartilha com quem cuida de alguém", "apoio": "Revisado pela psicóloga Patrícia Galheigo."},
        ],
        "legenda_ig": (
            "Dá para cuidar sem se anular?\n\n"
            "Quem trabalha numa casa de acolhimento passa o dia atento às necessidades dos outros. "
            "Escala organizada, folga respeitada e supervisão ajudam essa pessoa a continuar cuidando bem, inclusive de si.\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "Dá para cuidar sem se anular?\n\n"
            "Quem trabalha numa casa de acolhimento passa o dia atento às necessidades dos outros. "
            "Escala organizada, folga respeitada e supervisão ajudam essa pessoa a continuar cuidando bem, inclusive de si.\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Carrossel em fundo creme: cansaço também é sinal; pausa faz parte do trabalho; ninguém cuida bem sozinho.",
    },
    {
        "id": "16", "mes": "novembro-dezembro", "data_ordem": "2026-12-29", "data": "29/12", "dia_semana": "Terça-feira",
        "horario": "18h",
        "fase": 2, "fase_nome": "Fase 2 · Quem cuida", "pauta": "Pauta-mãe 8 · Depoimento de cuidador",
        "formato": "Foto real com faixa ou Reels", "formato_slug": "foto-faixa",
        "titulo": "O que eu queria que soubessem",
        "objetivo": "Primeira voz de quem cuida no perfil.",
        "publico": "Sociedade e empresas",
        "cta": "Compartilha com quem cuida de alguém",
        "status": "pendencia",
        "pendencias": [
            "Entrevista com um cuidador ou educador adulto de casa parceira, com termo de uso de imagem assinado.",
            "Foto só do adulto, sem crianças, sem fachada, placa ou ambiente que identifique a casa.",
            "A frase do slide e da legenda deve ser fala real da pessoa, sem edição de sentido.",
        ],
        "prova": "Depoimento autorizado de adulto.",
        "slides": [
            {"tipo": "foto", "img": None, "faixa": "O que eu queria que soubessem", "placeholder": "Retrato do cuidador (adulto, com autorização)"},
            {"tipo": "texto", "num": "", "titulo": "\"[Fala real do cuidador]\"", "corpo": "[Nome], educador(a) em casa de acolhimento"},
            {"tipo": "cta", "texto": "Compartilha com quem cuida de alguém", "apoio": "Depoimento publicado com autorização."},
        ],
        "roteiro": [
            "Pergunta 1: O que você queria que mais pessoas soubessem sobre o seu trabalho?",
            "Pergunta 2: Que tipo de apoio faria diferença na sua rotina?",
            "Pergunta 3: O que te faz continuar?",
        ],
        "legenda_ig": (
            "O que eu queria que soubessem.\n\n"
            "[Nome] trabalha numa casa de acolhimento e topou contar como é a rotina de quem cuida. "
            "[Trecho real do depoimento, até 3 linhas]\n\n"
            "Compartilha com quem cuida de alguém."
        ),
        "legenda_fb": (
            "O que eu queria que soubessem.\n\n"
            "[Nome] trabalha numa casa de acolhimento e topou contar como é a rotina de quem cuida. "
            "[Trecho real do depoimento, até 3 linhas]\n\n"
            "Compartilhe com quem cuida de alguém."
        ),
        "alt": "Retrato de um adulto que trabalha em casa de acolhimento, com faixa verde e a frase O que eu queria que soubessem. Não aparecem crianças.",
    },
]

RESERVA = [
    {"titulo": "Bastidor de formação de quem cuida", "fase": "Fase 2", "quando": "Assim que a primeira formação acontecer",
     "motivo": "Depende de uma formação real com registro e autorização."},
    {"titulo": "Casa de acolhimento? Responda ao mapeamento", "fase": "Fase 1 ou 2", "quando": "Quando a diretoria aprovar",
     "motivo": "Precisa de um CTA novo (\"Acesse o portal na bio\"), que não está na lista da seção 11 do briefing."},
]
