# -*- coding: utf-8 -*-
"""
Técnico: gera as páginas de revisão (modelo das páginas mensais da Gaia) a partir de conteudo.py.
Saída: index.html (hub), <mes>/index.html e doc.html (leitor dos documentos de estratégia).
Rode depois de render.py.
"""
import sys, json, html, urllib.parse
from pathlib import Path
from datetime import date, timedelta

sys.path.insert(0, str(Path(__file__).parent))
from conteudo import POSTS, RESERVA, HASHTAGS_BASE
from render import post_dir, ROOT

MESES = {"novembro-dezembro": ("Novembro e Dezembro", 12)}
INTRO = {
    "novembro-dezembro": "V.1, revisada em 25/11. A trilha do pré-briefing em 18 posts: inauguração (25 a 30/11), pesquisa de mapeamento e Dia de Doar (dezembro), Natal e continuidade para 2027. Carrosséis com no máximo 3 cards e nada que repita o que o perfil já publicou.",
}
e = html.escape
WA = "https://api.whatsapp.com/send?text="


def wa(t):
    return WA + urllib.parse.quote(t)


CSS = """
@font-face{font-family:Manrope;font-weight:800;src:url(../ferramentas/fonts/manrope-latin-800-normal.woff2)}
@font-face{font-family:Manrope;font-weight:700;src:url(../ferramentas/fonts/manrope-latin-700-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:400;src:url(../ferramentas/fonts/montserrat-latin-400-normal.woff2)}
@font-face{font-family:Montserrat;font-weight:600;src:url(../ferramentas/fonts/montserrat-latin-600-normal.woff2)}
:root{--verde:#2F6F4C;--marca:#66AA83;--menta:#5BDEA8;--creme:#FAF6EF;--tinta:#1F2330;--muted:#5B6B63;--coral:#DE6F5B;--borda:#E6E0D3;--card:#fff;--wpp:#25D366;--wppd:#128C7E;--alerta:#9A4A12;--alerta-bg:#FFF4E5;--r:18px}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Montserrat,system-ui,sans-serif;background:var(--creme);color:var(--tinta);line-height:1.6;padding-bottom:80px}
h1,h2,h3,.h{font-family:Manrope,Montserrat,sans-serif;font-weight:800;letter-spacing:-.02em;line-height:1.15}
a{color:var(--verde)}
.hero{background:linear-gradient(135deg,#21533A 0%,var(--verde) 60%,#3E8A62 100%);color:#fff;padding:44px 20px 38px;text-align:center;position:relative;overflow:hidden}
.hero:after{content:"";position:absolute;right:-90px;bottom:-120px;width:380px;height:380px;background:url(../ferramentas/brand/icon_white.svg) no-repeat center/contain;opacity:.08}
.hero .in{max-width:820px;margin:0 auto;position:relative;z-index:1}
.hero img.lg{height:54px;margin-bottom:18px}
.tag{display:inline-flex;gap:8px;align-items:center;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);padding:6px 16px;border-radius:30px;font-size:12px;font-weight:600;letter-spacing:1.4px;text-transform:uppercase;margin-bottom:14px}
.tag i{width:8px;height:8px;border-radius:50%;background:var(--menta)}
.hero h1{font-size:clamp(28px,5.5vw,42px);margin-bottom:12px}
.hero p{font-size:clamp(15px,3.6vw,18px);opacity:.92;max-width:680px;margin:0 auto}
.badges{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:18px}
.badge{background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);padding:7px 14px;border-radius:20px;font-size:13px;font-weight:600}
.nav{position:sticky;top:0;z-index:20;background:rgba(250,246,239,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--borda);display:flex;gap:8px;justify-content:center;flex-wrap:wrap;padding:10px}
.nav a{text-decoration:none;font-weight:600;font-size:14px;padding:8px 14px;border-radius:30px;background:#fff;border:1px solid var(--borda);color:var(--tinta)}
.nav a.wa{background:var(--wpp);border-color:var(--wpp);color:#fff}
.wrap{max-width:860px;margin:0 auto;padding:0 16px}
section{margin-top:36px}
.sec-t{font-size:24px;color:var(--verde);margin-bottom:6px}
.sec-p{color:var(--muted);font-size:15px;margin-bottom:18px}
.box{background:#fff;border:1px solid var(--borda);border-radius:var(--r);padding:18px;margin-bottom:16px}
.semana{font-weight:700;font-size:13px;letter-spacing:1px;text-transform:uppercase;color:var(--muted);margin:22px 0 10px;display:flex;justify-content:space-between}
.tl{display:flex;gap:12px;align-items:center;background:#fff;border:1px solid var(--borda);border-radius:14px;padding:10px;margin-bottom:10px;text-decoration:none;color:inherit;transition:.2s}
.tl:hover{box-shadow:0 10px 30px rgba(47,111,76,.12);transform:translateY(-1px)}
.dbox{width:56px;flex:none;text-align:center;background:var(--creme);border-radius:10px;padding:6px 0}
.dbox b{display:block;font-family:Manrope;font-size:22px;color:var(--verde);line-height:1.1}.dbox span{font-size:11px;text-transform:uppercase;color:var(--muted);font-weight:600}
.tl img{width:52px;height:65px;object-fit:cover;border-radius:6px;flex:none}
.tl .inf{flex:1;min-width:0}.tl .tt{font-weight:700;font-size:15px;line-height:1.3}.tl .mt{font-size:12px;color:var(--muted)}
.pill{display:inline-block;font-size:11px;font-weight:700;padding:3px 9px;border-radius:20px;letter-spacing:.3px;margin-right:4px}
.f0{background:#E3F4EA;color:#21533A}.f1{background:#E2EEF8;color:#1F4E70}.f2{background:#F6EFD3;color:#6B5A10}
.ok{background:#E3F4EA;color:#21533A}.pend{background:var(--alerta-bg);color:var(--alerta)}
.filtros{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}
.filtros button{font:600 13px Montserrat;padding:8px 14px;border-radius:30px;border:1px solid var(--borda);background:#fff;cursor:pointer}
.filtros button.on{background:var(--verde);color:#fff;border-color:var(--verde)}
.post{background:#fff;border:1px solid var(--borda);border-radius:22px;margin-bottom:28px;overflow:hidden;box-shadow:0 8px 30px rgba(47,111,76,.06);scroll-margin-top:70px}
.ph{padding:18px 18px 12px}.ph .n{font-size:12px;font-weight:700;color:var(--muted);letter-spacing:1px;text-transform:uppercase}
.ph h3{font-size:22px;color:var(--verde);margin:6px 0 8px}
.ph .sub{font-size:13px;color:var(--muted)}
.slider{position:relative;background:#EFEAE0}
.track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none}.track::-webkit-scrollbar{display:none}
.track img{flex:none;width:100%;scroll-snap-align:center;display:block;aspect-ratio:4/5;object-fit:contain;background:#EFEAE0}
.track img.v{aspect-ratio:9/16;max-height:80vh}
.arr{position:absolute;top:50%;transform:translateY(-50%);width:40px;height:40px;border-radius:50%;border:0;background:rgba(255,255,255,.92);font-size:20px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.15)}
.arr.l{left:10px}.arr.r{right:10px}
.cnt{position:absolute;top:12px;right:12px;background:rgba(31,35,48,.7);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px}
.thumbs{display:flex;gap:6px;overflow-x:auto;padding:10px 12px;background:#F6F2EA}
.thumbs img{width:46px;height:58px;object-fit:cover;border-radius:6px;cursor:pointer;opacity:.6;border:2px solid transparent;flex:none}
.thumbs img.on{opacity:1;border-color:var(--verde)}
.pb{padding:16px 18px 20px}
.alert{background:var(--alerta-bg);border-left:4px solid #E08A2E;border-radius:10px;padding:12px 14px;font-size:14px;margin-bottom:14px}
.alert b{color:var(--alerta)}.alert ul{margin:6px 0 0 18px}
.info{background:#F1F7F3;border-left:4px solid var(--marca);border-radius:10px;padding:12px 14px;font-size:14px;margin-bottom:14px}
.info ol,.info ul{margin:6px 0 0 18px}
.meta{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;font-size:13px;margin-bottom:14px}.meta div span{display:block;color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.6px;font-weight:600}
.tabs{display:flex;gap:6px;margin-bottom:8px}
.tabs button{font:600 13px Montserrat;padding:7px 14px;border-radius:30px;border:1px solid var(--borda);background:#fff;cursor:pointer}
.tabs button.on{background:var(--tinta);color:#fff;border-color:var(--tinta)}
.leg{white-space:pre-wrap;background:var(--creme);border-radius:12px;padding:14px;font-size:14.5px;border:1px solid var(--borda)}
.row{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.btn{font:700 14px Montserrat;padding:11px 16px;border-radius:12px;border:0;cursor:pointer;text-decoration:none;display:inline-flex;gap:6px;align-items:center}
.b-copy{background:#fff;border:1px solid var(--borda);color:var(--tinta)}
.b-ok{background:var(--wpp);color:#fff}.b-adj{background:#fff;border:1px solid var(--borda);color:var(--tinta)}
details{margin-top:12px;font-size:14px}summary{cursor:pointer;font-weight:600;color:var(--verde)}
.adj{display:none;margin-top:10px}.adj.on{display:block}
textarea{width:100%;min-height:90px;border:1px solid var(--borda);border-radius:12px;padding:10px;font:14px Montserrat}
.foot{text-align:center;color:var(--muted);font-size:13px;margin-top:40px}
.res li{margin:6px 0 0 18px}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--tinta);color:#fff;padding:10px 18px;border-radius:30px;font-size:14px;opacity:0;transition:.3s;pointer-events:none}.toast.on{opacity:1}
"""

JS = """
document.querySelectorAll('.slider').forEach(s=>{const t=s.querySelector('.track'),im=[...t.children],th=[...s.parentElement.querySelectorAll('.thumbs img')],c=s.querySelector('.cnt');
const go=i=>{i=Math.max(0,Math.min(im.length-1,i));t.scrollTo({left:im[i].offsetLeft,behavior:'smooth'})};
const cur=()=>Math.round(t.scrollLeft/t.clientWidth);
t.addEventListener('scroll',()=>{const i=cur();c.textContent=(i+1)+'/'+im.length;th.forEach((x,k)=>x.classList.toggle('on',k==i))});
s.querySelector('.l').onclick=()=>go(cur()-1);s.querySelector('.r').onclick=()=>go(cur()+1);th.forEach((x,k)=>x.onclick=()=>go(k));});
document.querySelectorAll('.tabs').forEach(tb=>{const bs=tb.querySelectorAll('button');bs.forEach(b=>b.onclick=()=>{bs.forEach(x=>x.classList.remove('on'));b.classList.add('on');
const p=tb.parentElement;p.querySelectorAll('.leg').forEach(l=>l.hidden=l.dataset.r!=b.dataset.r)})});
function toast(m){const t=document.querySelector('.toast');t.textContent=m;t.classList.add('on');setTimeout(()=>t.classList.remove('on'),1600)}
document.querySelectorAll('.b-copy').forEach(b=>b.onclick=()=>{const l=b.closest('.pb').querySelector('.leg:not([hidden])');navigator.clipboard.writeText(l.textContent).then(()=>toast('Legenda copiada'))});
document.querySelectorAll('.b-adj').forEach(b=>b.onclick=()=>b.closest('.pb').querySelector('.adj').classList.toggle('on'));
document.querySelectorAll('.b-send').forEach(b=>b.onclick=()=>{const p=b.closest('.pb'),t=p.querySelector('textarea').value.trim();if(!t){toast('Escreva o ajuste');return}
window.open('https://api.whatsapp.com/send?text='+encodeURIComponent(b.dataset.pre+t),'_blank')});
document.querySelectorAll('.filtros button').forEach(b=>b.onclick=()=>{const g=b.dataset.g;document.querySelectorAll('.filtros button[data-g="'+g+'"]').forEach(x=>x.classList.remove('on'));b.classList.add('on');
const f={};document.querySelectorAll('.filtros button.on').forEach(x=>f[x.dataset.g]=x.dataset.v);
document.querySelectorAll('.post').forEach(p=>{p.hidden=!Object.entries(f).every(([k,v])=>v=='*'||p.dataset[k]==v)})});
"""


def semana_de(d):
    ini = d - timedelta(days=d.weekday())
    fim = ini + timedelta(days=6)
    return f"Semana de {ini.day:02d}/{ini.month:02d} a {fim.day:02d}/{fim.month:02d}", ini


def imgs(p):
    d = post_dir(p)
    feed = sorted([f for f in d.glob("[0-9]*.jpg")], key=lambda f: int(f.stem))
    st = sorted(d.glob("story-*.jpg"))
    return [f"{d.name}/{f.name}" for f in feed], [f"{d.name}/{f.name}" for f in st]


def post_html(p, nome_mes):
    feed, st = imgs(p)
    allimg = feed + st
    vert = {i for i, s in enumerate(p["slides"]) if s["tipo"] == "reels"} | set(range(len(feed), len(allimg)))
    track = "".join(f'<img loading="lazy" class="{"v" if i in vert else ""}" src="{x}" alt="Slide {i+1}">' for i, x in enumerate(allimg))
    thumbs = "".join(f'<img src="{x}" class="{"on" if i == 0 else ""}">' for i, x in enumerate(allimg))
    pend = ""
    if p["pendencias"]:
        lbl = "Rascunho com pendência" if p["status"] == "pendencia" else "Observação"
        pend = f'<div class="alert"><b>{lbl}</b><ul>' + "".join(f"<li>{e(x)}</li>" for x in p["pendencias"]) + "</ul></div>"
    extra = ""
    if p.get("roteiro"):
        extra += '<div class="info"><b>Roteiro</b><ol>' + "".join(f"<li>{e(x)}</li>" for x in p["roteiro"]) + "</ol></div>"
    if p.get("stories"):
        extra += '<div class="info"><b>Stories do dia</b> (últimas imagens do carrossel)<ul>' + "".join(f'<li>{e(s["quando"])}: {e(s["titulo"])}. {e(s["corpo"])}</li>' for s in p["stories"]) + "</ul></div>"
    ig = p["legenda_ig"] + "\n\n" + HASHTAGS_BASE
    status = '<span class="pill ok">Pronto</span>' if p["status"] == "pronto" else '<span class="pill pend">Pendência</span>'
    ok_msg = f'Olá! Revisei o post {p["id"]} da Net do Bem ({p["data"]}, "{p["titulo"]}") e está APROVADO.'
    pre = f'Olá! Ajuste no post {p["id"]} da Net do Bem ({p["data"]}, "{p["titulo"]}"): '
    return f"""
<article class="post" id="post-{p['id']}" data-fase="{p['fase']}" data-status="{p['status']}">
 <div class="ph"><div class="n">Post {p['id']} · {e(p['dia_semana'])}, {p['data']} · {e(p['horario'])}</div>
  <h3>{e(p['titulo'])}</h3>
  <div class="sub"><span class="pill f{p['fase']}">{e(p['fase_nome'])}</span>{status} {e(p['formato'])} · {len(feed)} {'imagem' if len(feed)==1 else 'imagens'}</div></div>
 <div class="slider"><div class="track">{track}</div><button class="arr l" aria-label="Anterior">‹</button><button class="arr r" aria-label="Próximo">›</button><span class="cnt">1/{len(allimg)}</span></div>
 <div class="thumbs">{thumbs}</div>
 <div class="pb">
  {pend}
  <div class="meta"><div><span>Pauta</span>{e(p['pauta'])}</div><div><span>CTA único</span>{e(p['cta'])}</div>
   <div><span>Público</span>{e(p['publico'])}</div><div><span>Objetivo</span>{e(p['objetivo'])}</div></div>
  {extra}
  <div class="tabs"><button class="on" data-r="ig">Instagram</button><button data-r="fb">Facebook</button></div>
  <div class="leg" data-r="ig">{e(ig)}</div><div class="leg" data-r="fb" hidden>{e(p['legenda_fb'])}</div>
  <div class="row"><button class="btn b-copy">Copiar legenda</button><a class="btn b-ok" target="_blank" href="{wa(ok_msg)}">Aprovar no WhatsApp</a><button class="btn b-adj">Pedir ajuste</button></div>
  <div class="adj"><textarea placeholder="Descreva o ajuste (texto, imagem, data)"></textarea><div class="row"><button class="btn b-ok b-send" data-pre="{e(pre)}">Enviar ajuste no WhatsApp</button></div></div>
  <p class="sec-p" style="margin:12px 0 0;font-size:13px">Aprovação: Barros (gestor) · Patrícia e Agda (validadoras)</p>
  <details><summary>Texto alternativo e checklist de segurança</summary><p style="margin:8px 0">{e(p['alt'])}</p>
   <p>1 ideia · 1 CTA · gancho até 6 palavras · sem criança identificável · sem endereço ou rotina · sem cópia de perfil de referência · sem Imposto de Renda · rosto de adulto só com autorização · aprovado por Barros, Patrícia e Agda.</p></details>
 </div>
</article>"""


def month_page(mes):
    nome, _ = MESES[mes]
    ps = sorted([p for p in POSTS if p["mes"] == mes], key=lambda p: p["data_ordem"])
    prontos = sum(p["status"] == "pronto" for p in ps)
    semanas = {}
    for p in ps:
        d = date.fromisoformat(p["data_ordem"])
        lbl, ini = semana_de(d)
        semanas.setdefault((ini, lbl), []).append(p)
    cal = ""
    for (ini, lbl), lst in sorted(semanas.items()):
        cal += f'<div class="semana"><span>{lbl}</span><span>{len(lst)} {"post" if len(lst)==1 else "posts"}</span></div>'
        for p in lst:
            feed, _ = imgs(p)
            st = '<span class="pill ok">Pronto</span>' if p["status"] == "pronto" else '<span class="pill pend">Pendência</span>'
            cal += f'''<a class="tl" href="#post-{p['id']}"><div class="dbox"><b>{p['data'][:2]}</b><span>{p['dia_semana'][:3]}</span></div>
<img src="{feed[0]}" alt=""><div class="inf"><div><span class="pill f{p['fase']}">{e(p['fase_nome'].split(' · ')[1])}</span>{st}</div>
<div class="tt">{e(p['titulo'])}</div><div class="mt">{e(p['formato'])} · CTA: {e(p['cta'])}</div></div></a>'''
    fases = sorted({p["fase"] for p in ps})
    filt = '<div class="filtros"><button class="on" data-g="fase" data-v="*">Todas as etapas</button>' + \
        "".join(f'<button data-g="fase" data-v="{f}">{e(next(p["fase_nome"] for p in ps if p["fase"]==f).split(" · ")[1])}</button>' for f in fases) + \
        '<button class="on" data-g="status" data-v="*">Todos</button><button data-g="status" data-v="pronto">Prontos</button><button data-g="status" data-v="pendencia">Com pendência</button></div>'
    reserva = ""
    if mes == "novembro-dezembro":
        reserva = '<section><h2 class="sec-t">Posts de reserva</h2><div class="box res"><ul>' + "".join(
            f'<li><b>{e(r["titulo"])}</b> ({e(r["fase"])}). {e(r["quando"])}. {e(r["motivo"])}</li>' for r in RESERVA) + "</ul></div></section>"
    aprov = wa(f"Olá! Revisei o calendário de {nome} da Fundação Net do Bem ({len(ps)} posts) e está APROVADO.")
    ajuste = wa(f"Olá! Sobre o calendário de {nome} da Fundação Net do Bem, sugiro o seguinte ajuste: ")
    posts = "".join(post_html(p, nome) for p in ps)
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{nome} 2026 · Instagram e Facebook · Fundação Net do Bem</title><meta name="robots" content="noindex">
<link rel="icon" href="../ferramentas/brand/icon_green.svg"><style>{CSS}</style></head><body>
<header class="hero"><div class="in"><img class="lg" src="../ferramentas/brand/NET-DO-BEM-WHITE-HORIZONTAL.svg" alt="Fundação Net do Bem">
<div><span class="tag"><i></i>Fundação Net do Bem · {nome} 2026</span></div>
<h1>{nome} · Calendário de posts</h1><p>{e(INTRO[mes])}</p>
<div class="badges"><span class="badge">{len(ps)} posts</span><span class="badge">{prontos} prontos</span><span class="badge">{len(ps)-prontos} com pendência</span><span class="badge">Instagram + Facebook</span></div></div></header>
<nav class="nav"><a href="../index.html">← Todos os meses</a><a href="#calendario">Calendário</a><a href="#posts">Posts ({len(ps)})</a><a class="wa" target="_blank" href="{aprov}">Aprovar mês no WhatsApp</a></nav>
<main class="wrap">
<section id="calendario"><h2 class="sec-t">Calendário sugerido</h2><p class="sec-p">Inauguração: um post por dia de 25 a 30/11. Dezembro: 2 a 3 posts por semana, com as datas especiais (Dia de Doar, Voluntário, Direitos Humanos, FIA, Natal e Ano Novo).</p>
<div class="box"><b>Aprovação do calendário</b><p class="sec-p" style="margin:4px 0 0">Quem aprova: Barros (gestor), Patrícia Galheigo e Agda Ximenes (validadoras). Cada post vai ao ar com o ok dos três.</p><div class="row"><a class="btn b-ok" target="_blank" href="{aprov}">Aprovar calendário completo</a><a class="btn b-adj" target="_blank" href="{ajuste}">Sugerir mudança de data</a></div></div>
{cal}</section>
<section id="posts"><h2 class="sec-t">Posts para revisão</h2><p class="sec-p">Arraste as imagens, copie a legenda de cada rede e aprove ou peça ajuste. Post com pendência só vai ao ar depois que ela for resolvida.</p>
{filt}{posts}</section>{reserva}
<section><h2 class="sec-t">Roteiros e captação</h2><p class="sec-p">Rascunhos com pendência para a equipe revisar.</p>{"".join(f'<a class="tl" href="../doc.html?f={f}"><div class="inf"><div class="tt">{e(t)}</div><div class="mt">{f}</div></div></a>' for f, t in DOCS if f.startswith("roteiros/"))}</section>
<p class="foot">Fundação Net do Bem · @fundacao.netdobem · Conteúdo preparado pela Substrato Digital</p></main>
<div class="toast"></div><script>{JS}</script></body></html>"""


DOCS = [("estrategia/07-estrategia-v1.md", "Estratégia V.1 e calendário (atual)"),
        ("estrategia/06-pesquisa-v1-perfil-e-datas.md", "Pesquisa V.1: auditoria do perfil e datas de dezembro"),
        ("estrategia/01-estrategia.md", "Estratégia V.0 (histórico)"),
        ("estrategia/02-pesquisa-tendencias.md", "Pesquisa: tendências e oportunidades"),
        ("estrategia/03-sistema-visual.md", "Sistema visual"),
        ("estrategia/04-guia-copy.md", "Guia de copy e revisão no-ai-slop"),
        ("estrategia/05-fluxo-orquestrado.md", "Fluxo dos 5 papéis e aprovação"),
        ("roteiros/01-captacao-inauguracao.md", "Lista de captação da inauguração (26/11)"),
        ("roteiros/02-fala-abertura-andre.md", "Fala de abertura do André"),
        ("roteiros/03-reels-andre.md", "Roteiro do Reels do André"),
        ("roteiros/04-faq-provisorio.md", "Respostas provisórias para comentários e Direct"),
        ("roteiros/05-entrevista-cuidador.md", "Roteiro de entrevista com cuidador"),
        ("briefing/briefing-net-do-bem-v2.md", "Briefing V2 (fonte de verdade)")]


def hub():
    cards = ""
    for mes, (nome, _) in MESES.items():
        ps = [p for p in POSTS if p["mes"] == mes]
        capa = imgs(sorted(ps, key=lambda p: p["data_ordem"])[0])[0][0]
        cards += f'''<a class="tl" href="{mes}/index.html" style="padding:14px"><img src="{mes}/{capa}" style="width:72px;height:90px">
<div class="inf"><div class="tt" style="font-size:19px">{nome} 2026</div><div class="mt">{e(INTRO[mes])}</div>
<div style="margin-top:6px"><span class="pill ok">{sum(p["status"]=="pronto" for p in ps)} prontos</span><span class="pill pend">{sum(p["status"]!="pronto" for p in ps)} com pendência</span></div></div></a>'''
    for nome, txt in [("Janeiro 2027", "Natal e continuidade em 2027. Pautas definidas depois dos primeiros resultados da pesquisa de mapeamento."),
                      ("Fevereiro 2027", "Transparência e primeiros apoios. Pautas a definir com Barros, Patrícia e Agda.")]:
        cards += f'<div class="tl" style="padding:14px;opacity:.7"><div class="inf"><div class="tt" style="font-size:19px">{nome}</div><div class="mt">{txt}</div></div></div>'
    docs = "".join(f'<a class="tl" href="doc.html?f={f}"><div class="inf"><div class="tt">{e(t)}</div><div class="mt">{f}</div></div></a>' for f, t in DOCS)
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fundação Net do Bem · Instagram e Facebook</title><meta name="robots" content="noindex"><link rel="icon" href="ferramentas/brand/icon_green.svg">
<style>{CSS.replace('../ferramentas', 'ferramentas')}</style></head><body>
<header class="hero"><div class="in"><img class="lg" src="ferramentas/brand/NET-DO-BEM-WHITE-HORIZONTAL.svg" alt="Fundação Net do Bem">
<div><span class="tag"><i></i>Instagram e Facebook · Revisão do time</span></div><h1>Fortalecer quem cuida também é proteger a infância.</h1>
<p>Calendário de posts da Fundação Net do Bem, organizado por mês. Cada página traz as artes, as legendas das duas redes e o botão de aprovação.</p></div></header>
<main class="wrap"><section><h2 class="sec-t">Meses</h2>{cards}</section>
<section><h2 class="sec-t">Estratégia e documentação</h2>{docs}</section>
<p class="foot">Substrato Digital para Fundação Net do Bem</p></main></body></html>"""


DOC_VIEWER = """<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Documento · Fundação Net do Bem</title><meta name="robots" content="noindex"><link rel="icon" href="ferramentas/brand/icon_green.svg">
<style>body{font-family:Montserrat,system-ui,sans-serif;background:#FAF6EF;color:#1F2330;line-height:1.65;margin:0}
header{background:#2F6F4C;padding:16px 20px}header a{color:#fff;font-weight:600;text-decoration:none}
main{max-width:860px;margin:0 auto;padding:24px 18px 80px}h1,h2,h3{color:#2F6F4C;line-height:1.2}
table{border-collapse:collapse;width:100%;font-size:14px;display:block;overflow-x:auto;margin:12px 0}td,th{border:1px solid #E6E0D3;padding:8px;text-align:left;vertical-align:top;background:#fff}th{background:#F1F7F3}
code,pre{background:#fff;border:1px solid #E6E0D3;border-radius:8px}pre{padding:12px;overflow-x:auto}code{padding:1px 5px}blockquote{border-left:4px solid #5BDEA8;margin:0;padding-left:14px}</style>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script></head><body>
<header><a href="index.html">← Fundação Net do Bem · Instagram e Facebook</a></header><main id="c">Carregando…</main>
<script>const f=new URLSearchParams(location.search).get('f')||'';
if(!/^(estrategia|briefing|roteiros)\\/[\\w.-]+\\.md$/.test(f)){document.getElementById('c').textContent='Documento não encontrado.'}
else fetch(f).then(r=>r.text()).then(t=>{document.getElementById('c').innerHTML=marked.parse(t);document.title=(t.match(/^# (.*)/m)||[,'Documento'])[1]})</script></body></html>"""


if __name__ == "__main__":
    for mes in MESES:
        (ROOT / mes / "index.html").write_text(month_page(mes), encoding="utf-8")
        print("ok", mes)
    (ROOT / "index.html").write_text(hub(), encoding="utf-8")
    (ROOT / "doc.html").write_text(DOC_VIEWER, encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("ok index, doc")
