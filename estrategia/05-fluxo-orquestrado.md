# Fluxo orquestrado · 5 papéis

Cada mês passa pelos cinco papéis nesta ordem. Os papéis existem como agentes do Claude Code em `.claude/agents/`, então o próximo mês pode ser gerado abrindo esta pasta e pedindo "rode o fluxo de janeiro".

```
Estrategista ──> Pesquisador ──> Copywriter ──> Designer ──> Técnico ──> Revisão do time ──> Publicação
  fase, pautas     tendências,     slides e       artes        git, página     aprovação no
  CTA, datas       riscos          legendas       1080x1350    do mês          WhatsApp
```

| Papel | Recebe | Entrega | Onde fica |
|---|---|---|---|
| Estrategista | Briefing V2, dados do mês anterior | Fase, pautas, datas, CTA e público de cada post | `estrategia/01-estrategia.md` e campos de `ferramentas/conteudo.py` |
| Pesquisador | Benchmark, perfis do terceiro setor | Tendências, oportunidades, riscos, datas da causa | `estrategia/02-pesquisa-tendencias.md` |
| Copywriter | Pautas aprovadas | Slides, legenda Instagram, legenda Facebook, alt text, revisão no-ai-slop | `ferramentas/conteudo.py`, `estrategia/04-guia-copy.md` |
| Designer | Copy pronta | Tipo de slide, artes renderizadas | `ferramentas/render.py`, `estrategia/03-sistema-visual.md` |
| Técnico | Artes e legendas | Pastas por post, página do mês, commit e push, link do GitHub Pages | `novembro/`, `dezembro/`, `index.html` |

## Comandos do técnico

```powershell
python ferramentas/render.py
```

```powershell
python ferramentas/build.py
```

```powershell
git add -A; git commit -m "Dezembro: ajustes da revisão"; git push
```

## Revisão e aprovação

1. O técnico publica a página do mês no GitHub Pages (`substratodigital.github.io/fundacao/<mes>/`).
2. Cada post tem botão "Aprovar no WhatsApp" e campo de ajustes que gera a mensagem pronta.
3. Ajustes voltam para o copywriter ou o designer, que editam `conteudo.py`; o técnico roda de novo os dois scripts.
4. Post com status "Rascunho com pendência" não é publicado até a pendência sair da ficha.

## Pasta de cada post

```
dezembro/12-quem-cuida-de-quem-cuida/
  1.jpg ... 5.jpg     artes do feed, na ordem
  story-1.jpg ...     stories, quando houver
  instagram.txt       legenda com hashtags
  facebook.txt        legenda da página
  alt-text.txt        texto alternativo
  ficha.md            fase, CTA, pendências, roteiro e checklist de segurança
```
