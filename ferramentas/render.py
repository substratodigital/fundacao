# -*- coding: utf-8 -*-
"""
Designer + técnico: transforma conteudo.py em artes 1080x1350 (feed) e 1080x1920 (stories/Reels)
e grava, em cada pasta de post, as legendas de Instagram e Facebook, o texto alternativo e a ficha.

Uso:  python ferramentas/render.py            (todos os posts)
      python ferramentas/render.py 03 07      (só alguns ids)
"""
import sys, re, html, unicodedata, shutil
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent))
from conteudo import POSTS, HASHTAGS_BASE

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "ferramentas"
TMP = TOOLS / "_tmp"

C = dict(verde="#2F6F4C", marca="#66AA83", menta="#5BDEA8", creme="#FAF6EF", tinta="#1F2330",
         coral="#DE6F5B", muted="#5B6B63", linha="#E4DED1")


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


def post_dir(p):
    return ROOT / p["mes"] / f'{p["id"]}-{slug(p["titulo"])}'


def u(path):  # caminho relativo ao HTML temporário
    return "../" + path


def esc(s):
    return html.escape(s or "")


CSS = f"""
@font-face{{font-family:Manrope;font-weight:700;src:url(../fonts/manrope-latin-700-normal.woff2)}}
@font-face{{font-family:Manrope;font-weight:800;src:url(../fonts/manrope-latin-800-normal.woff2)}}
@font-face{{font-family:Montserrat;font-weight:400;src:url(../fonts/montserrat-latin-400-normal.woff2)}}
@font-face{{font-family:Montserrat;font-weight:600;src:url(../fonts/montserrat-latin-600-normal.woff2)}}
@font-face{{font-family:Montserrat;font-style:italic;font-weight:400;src:url(../fonts/montserrat-latin-400-italic.woff2)}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:var(--h);overflow:hidden}}
body{{font-family:Montserrat,sans-serif;color:{C['tinta']};-webkit-font-smoothing:antialiased}}
.s{{position:relative;width:1080px;height:var(--h);overflow:hidden;padding:96px 92px}}
.creme{{background:{C['creme']}}}
.verde{{background:{C['verde']};color:#fff}}
.h{{font-family:Manrope,sans-serif;font-weight:800;letter-spacing:-.025em;line-height:1.02}}
.top{{position:absolute;top:72px;left:92px;right:92px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:58px}}
.count{{font-weight:600;font-size:26px;color:{C['muted']};letter-spacing:.08em}}
.verde .count{{color:rgba(255,255,255,.7)}}
.foot{{position:absolute;bottom:64px;left:92px;right:92px;display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:26px;color:{C['muted']}}}
.verde .foot{{color:rgba(255,255,255,.75)}}
.dots{{display:flex;gap:10px}}.dots i{{width:12px;height:12px;border-radius:50%;background:{C['linha']}}}.dots i.on{{background:{C['verde']};width:34px;border-radius:8px}}
.verde .dots i{{background:rgba(255,255,255,.25)}}.verde .dots i.on{{background:{C['menta']}}}
.heart{{position:absolute;opacity:.10;pointer-events:none}}
.kicker{{display:inline-block;font-weight:600;font-size:28px;letter-spacing:.14em;text-transform:uppercase;color:{C['verde']};
  border-bottom:5px solid {C['menta']};padding-bottom:10px;margin-bottom:44px}}
.mid{{position:absolute;left:92px;right:92px;top:50%;transform:translateY(-50%)}}
.capa .t{{font-size:118px;color:{C['verde']}}}
.capa .sub{{margin-top:40px;font-size:38px;color:{C['muted']};font-weight:400}}
.num{{font-family:Manrope;font-weight:800;font-size:150px;line-height:1;color:{C['marca']};margin-bottom:24px}}
.texto .t{{font-size:84px;color:{C['verde']}}}
.texto .b{{margin-top:44px;font-size:42px;line-height:1.42;max-width:860px}}
.lista .t{{font-size:76px;color:{C['verde']};margin-bottom:46px}}
.lista ul{{list-style:none}}.lista li{{font-size:42px;font-weight:600;padding:26px 0;border-top:3px solid {C['linha']};display:flex;gap:26px;align-items:center}}
.lista li b{{width:22px;height:22px;border-radius:50%;background:{C['menta']};flex:none}}
.q{{font-family:Manrope;font-weight:800;font-size:80px;color:{C['verde']};line-height:1.05}}
.a{{margin-top:48px;font-size:44px;line-height:1.42;padding-left:34px;border-left:8px solid {C['menta']}}}
.card .t{{font-size:96px;line-height:1.08;color:#fff}}
.card .mark{{width:120px;height:8px;background:{C['menta']};border-radius:4px;margin-bottom:56px}}
.cta .t{{font-size:64px;color:{C['verde']};margin-bottom:56px}}
.pill{{display:inline-block;background:{C['coral']};color:#fff;font-family:Manrope;font-weight:800;font-size:54px;padding:34px 56px;border-radius:999px;line-height:1.1}}
.cta .b{{margin-top:56px;font-size:38px;line-height:1.45;color:{C['muted']};max-width:820px}}
.foto{{padding:0;background:#E9E3D6}}
.foto .img{{position:absolute;inset:0 0 300px 0;background-size:cover;background-position:center}}
.foto .img.contain{{background-size:contain;background-repeat:no-repeat;background-color:#EDE8DC}}
.foto .ph{{position:absolute;inset:0 0 300px 0;display:flex;align-items:center;justify-content:center;padding:120px;text-align:center;
  background:repeating-linear-gradient(135deg,#ECE6D9 0 26px,#E5DECF 26px 52px)}}
.foto .ph div{{border:5px dashed {C['muted']};border-radius:28px;padding:56px;font-size:40px;font-weight:600;color:{C['muted']};line-height:1.35;background:rgba(250,246,239,.85)}}
.faixa{{position:absolute;left:0;right:0;bottom:0;height:300px;background:{C['verde']};display:flex;align-items:center;justify-content:space-between;padding:0 80px;gap:40px}}
.faixa .t{{font-size:66px;color:#fff;line-height:1.05}}
.faixa img{{height:120px;flex:none}}
.retrato{{text-align:left}}
.retrato .av{{width:470px;height:470px;border-radius:50%;background:{C['marca']};overflow:hidden;margin-bottom:56px;border:10px solid #fff;box-shadow:0 20px 50px rgba(47,111,76,.18)}}
.retrato .av img{{width:100%;height:100%;object-fit:cover;object-position:center 18%}}
.retrato .n{{font-size:82px;color:{C['verde']}}}
.retrato .p{{margin-top:18px;font-weight:600;font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:{C['verde']}}}
.retrato .b{{margin-top:34px;font-size:40px;line-height:1.42;max-width:880px}}
.logo .lg{{width:640px;margin-bottom:80px}}
.logo .t{{font-size:112px;color:{C['verde']}}}
.logo .sub{{margin-top:46px;font-size:40px;font-weight:600;letter-spacing:.08em;color:{C['muted']}}}
.story .t{{font-size:150px}}
.story .b{{margin-top:44px;font-size:52px;line-height:1.35}}
.reels .av{{position:absolute;left:50%;top:330px;transform:translateX(-50%);width:760px;height:760px;border-radius:50%;overflow:hidden;background:{C['marca']}}}
.reels .av img{{width:100%;height:100%;object-fit:cover;object-position:center 15%}}
.reels .tt{{position:absolute;left:92px;right:92px;top:1180px;text-align:center}}
.reels .t{{font-size:104px;color:#fff}}
.reels .sub{{margin-top:30px;font-size:40px;color:rgba(255,255,255,.85)}}
.tag{{position:absolute;top:150px;left:50%;transform:translateX(-50%);background:{C['coral']};color:#fff;font-weight:600;font-size:30px;letter-spacing:.12em;padding:14px 30px;border-radius:999px;text-transform:uppercase}}
"""


def chrome(theme, i, n, logo=True):
    lg = "brand/NET-DO-BEM-WHITE-HORIZONTAL.svg" if theme == "verde" else "brand/NET-DO-BEM-VERDE-HORIZONTAL.svg"
    count = f'<span class="count">{i}/{n}</span>' if n > 1 else "<span></span>"
    dots = "".join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(1, n + 1)) if n > 1 else ""
    top = f'<div class="top">{"<img src=" + chr(34) + u(lg) + chr(34) + ">" if logo else "<span></span>"}{count}</div>'
    foot = f'<div class="foot"><span>@fundacao.netdobem</span><span class="dots">{dots}</span></div>'
    return top, foot


def heart(theme, size=820, right=-220, bottom=-200):
    ic = "brand/icon_white.svg" if theme == "verde" else "brand/icon_green.svg"
    return f'<img class="heart" src="{u(ic)}" style="width:{size}px;right:{right}px;bottom:{bottom}px">'


def slide_html(s, i, n):
    t = s["tipo"]
    if t == "capa":
        top, foot = chrome("creme", i, n)
        sub = f'<div class="sub">{esc(s.get("sub"))}</div>' if s.get("sub") else ""
        body = f'<div class="mid"><div class="kicker">{esc(s.get("kicker",""))}</div><div class="h t">{esc(s["titulo"])}</div>{sub}</div>'
        return "creme capa", top + heart("creme") + body + foot
    if t == "texto":
        top, foot = chrome("creme", i, n)
        num = f'<div class="num">{esc(s["num"])}</div>' if s.get("num") else ""
        body = f'<div class="mid">{num}<div class="h t">{esc(s["titulo"])}</div><div class="b">{esc(s["corpo"])}</div></div>'
        return "creme texto", top + body + foot
    if t == "lista":
        top, foot = chrome("creme", i, n)
        num = f'<div class="num">{esc(s["num"])}</div>' if s.get("num") else ""
        li = "".join(f"<li><b></b>{esc(x)}</li>" for x in s["itens"])
        return "creme lista", top + f'<div class="mid">{num}<div class="h t">{esc(s["titulo"])}</div><ul>{li}</ul></div>' + foot
    if t == "pergunta":
        top, foot = chrome("creme", i, n)
        return "creme", top + f'<div class="mid"><div class="num">{esc(s["num"])}</div><div class="q">{esc(s["pergunta"])}</div><div class="a">{esc(s["resposta"])}</div></div>' + foot
    if t == "card":
        top, foot = chrome("verde", i, n, logo=False)
        logo = f'<img src="{u("brand/NET-DO-BEM-WHITE-HORIZONTAL.svg")}" style="position:absolute;left:92px;bottom:92px;height:70px">'
        return "verde card", heart("verde", 900, -260, -160) + f'<div class="mid"><div class="mark"></div><div class="h t">{esc(s["frase"])}</div></div>' + logo
    if t == "cta":
        top, foot = chrome("creme", i, n)
        return "creme cta", top + heart("creme", 700, -200, -180) + f'<div class="mid"><div class="h t">O próximo passo é seu</div><div class="pill">{esc(s["texto"])}</div><div class="b">{esc(s.get("apoio",""))}</div></div>' + foot
    if t == "foto":
        if s.get("img"):
            cls = "img contain" if s.get("fit") == "contain" else "img"
            media = f'<div class="{cls}" style="background-image:url({u("fotos/" + s["img"])})"></div>'
        else:
            media = f'<div class="ph"><div>FOTO REAL<br>{esc(s.get("placeholder",""))}</div></div>'
        faixa = f'<div class="faixa"><div class="h t">{esc(s["faixa"])}</div><img src="{u("brand/icon_white.svg")}"></div>'
        return "foto", media + faixa
    if t == "retrato":
        top, foot = chrome("creme", i, n)
        return "creme retrato", top + f'<div class="mid"><div class="av"><img src="{u("fotos/" + s["img"])}"></div><div class="h n">{esc(s["nome"])}</div><div class="p">{esc(s["papel"])}</div><div class="b">{esc(s["corpo"])}</div></div>' + foot
    if t == "logo":
        return "creme logo", heart("creme", 760, -240, -230) + f'<div class="mid"><img class="lg" src="{u("brand/NET-DO-BEM-VERDE-HORIZONTAL.svg")}"><div class="h t">{esc(s["titulo"])}</div><div class="sub">{esc(s["sub"])}</div></div>'
    if t == "obrigado":
        return "creme logo", f'<img class="heart" src="{u("brand/icon_green.svg")}" style="opacity:1;width:300px;left:92px;top:150px">' + \
            f'<div class="mid" style="top:58%"><div class="h t" style="font-size:120px">{esc(s["titulo"])}</div><div class="sub" style="letter-spacing:0;font-weight:400;line-height:1.4">{esc(s["sub"])}</div></div>' + \
            f'<img src="{u("brand/NET-DO-BEM-VERDE-HORIZONTAL.svg")}" style="position:absolute;left:92px;bottom:92px;height:62px">'
    if t == "reels":
        return "verde reels", '<div class="tag">Reels</div>' + f'<div class="av"><img src="{u("fotos/" + s["img"])}"></div><div class="tt"><div class="h t">{esc(s["titulo"])}</div><div class="sub">{esc(s["sub"])}</div></div>' + \
            f'<img src="{u("brand/NET-DO-BEM-WHITE-HORIZONTAL.svg")}" style="position:absolute;left:50%;transform:translateX(-50%);bottom:110px;height:64px">'
    if t == "story":
        th = s.get("tema", "verde")
        col = "#fff" if th == "verde" else C["verde"]
        lg = "brand/NET-DO-BEM-WHITE-HORIZONTAL.svg" if th == "verde" else "brand/NET-DO-BEM-VERDE-HORIZONTAL.svg"
        return f"{th} story", heart(th, 1000, -300, -160) + f'<img src="{u(lg)}" style="position:absolute;left:92px;top:180px;height:70px">' + \
            f'<div class="mid"><div class="kicker" style="color:{col}">{esc(s["quando"])}</div><div class="h t" style="color:{col}">{esc(s["titulo"])}</div><div class="b">{esc(s["corpo"])}</div></div>'
    raise ValueError(t)


def page(cls, inner, h):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body style="--h:{h}px"><div class="s {cls}">{inner}</div></body></html>'


def legenda_txt(p, rede):
    txt = p["legenda_ig"] if rede == "ig" else p["legenda_fb"]
    if rede == "ig":
        txt += "\n\n" + HASHTAGS_BASE
    return txt + "\n"


def ficha(p):
    L = [f'# {p["id"]} · {p["data"]} ({p["dia_semana"]}) · {p["titulo"]}', "",
         f'- Fase: {p["fase_nome"]}', f'- Pauta: {p["pauta"]}', f'- Formato: {p["formato"]}',
         f'- Horário sugerido: {p["horario"]}', f'- Público: {p["publico"]}', f'- Objetivo: {p["objetivo"]}',
         f'- CTA único: {p["cta"]}', f'- Prova: {p["prova"]}',
         f'- Status: {"PRONTO" if p["status"] == "pronto" else "RASCUNHO COM PENDÊNCIA"}', ""]
    if p.get("pendencias"):
        L += ["## Pendências", *[f"- [ ] {x}" for x in p["pendencias"]], ""]
    if p.get("roteiro"):
        L += ["## Roteiro", *[f"{k}. {x}" for k, x in enumerate(p["roteiro"], 1)], ""]
    if p.get("stories"):
        L += ["## Stories do dia", *[f'- {s["quando"]}: {s["titulo"]}. {s["corpo"]}' for s in p["stories"]], ""]
    L += ["## Checklist de segurança (Briefing V2, seção 12)",
          "- [x] 1 ideia central", "- [x] 1 CTA", "- [x] Gancho com até 6 palavras no slide 1 (card de frase-mãe é exceção prevista no briefing)",
          "- [x] Sem criança identificável", "- [x] Sem endereço, rotina ou detalhe de segurança",
          "- [x] Sem cópia de perfil de referência", "- [x] Sem conteúdo de Imposto de Renda",
          "- [ ] Foto ou vídeo com consentimento de adulto (se houver rosto)", "- [ ] Legenda revisada por 1 pessoa da fundação", ""]
    return "\n".join(L)


def main(ids):
    TMP.mkdir(exist_ok=True)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        ctx = br.new_context(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        pg = ctx.new_page()
        for p in POSTS:
            if ids and p["id"] not in ids:
                continue
            d = post_dir(p)
            if d.exists():
                shutil.rmtree(d)
            d.mkdir(parents=True)
            frames = [(s, 1350) if s["tipo"] != "reels" else (s, 1920) for s in p["slides"]]
            frames += [(dict(s, tipo="story"), 1920) for s in p.get("stories", [])]
            n = len(p["slides"])
            for k, (s, h) in enumerate(frames, 1):
                cls, inner = slide_html(s, min(k, n), n)
                f = TMP / "slide.html"
                f.write_text(page(cls, inner, h), encoding="utf-8")
                pg.set_viewport_size({"width": 1080, "height": h})
                pg.goto(f.as_uri())
                pg.wait_for_timeout(120)
                png = TMP / "shot.png"
                pg.screenshot(path=str(png))
                name = f"{k}.jpg" if k <= n else f"story-{k - n}.jpg"
                Image.open(png).convert("RGB").save(d / name, quality=92)
            (d / "instagram.txt").write_text(legenda_txt(p, "ig"), encoding="utf-8")
            (d / "facebook.txt").write_text(legenda_txt(p, "fb"), encoding="utf-8")
            (d / "alt-text.txt").write_text(p["alt"] + "\n", encoding="utf-8")
            (d / "ficha.md").write_text(ficha(p), encoding="utf-8")
            print("ok", d.relative_to(ROOT))
        br.close()
    shutil.rmtree(TMP, ignore_errors=True)


if __name__ == "__main__":
    main(set(sys.argv[1:]))
