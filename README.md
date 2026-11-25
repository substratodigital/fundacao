# Fundação Net do Bem · Instagram e Facebook

Conteúdo das redes sociais organizado por mês, com páginas de revisão publicadas em GitHub Pages
(`https://substratodigital.github.io/fundacao/`).

- `index.html`: página inicial com os meses e a documentação.
- `novembro-dezembro/`: primeira entrega (26/11 a 29/12), uma pasta por post com as artes, `instagram.txt`, `facebook.txt`, `alt-text.txt` e `ficha.md`.
- `estrategia/`: estratégia, pesquisa, sistema visual, guia de copy e fluxo dos 5 papéis.
- `briefing/`: Briefing V2, fonte de verdade.
- `ferramentas/massinha/`: ilustrações em massinha geradas no Magnific.
- `ferramentas/conteudo.py`: textos de todos os posts. `render.py` gera as artes e `build.py` gera as páginas.
- `.claude/agents/`: estrategista, pesquisador, copywriter, designer e técnico.

Para refazer tudo depois de editar `conteudo.py`:

```powershell
python ferramentas/render.py; python ferramentas/build.py
```

Aprovação: Barros (gestor), Patrícia Galheigo e Agda Ximenes (validadoras).
