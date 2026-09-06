#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64, io, os
from PIL import Image, ImageOps
import qrcode

BASE = os.path.expanduser("~/Desktop/StartUpSpace_VGTU")
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
QR_DIR = os.path.join(BASE, "qr")
OUT = os.path.join(BASE, "StartUpSpace_web_prezentatsiya.html")

def b64_img(path, resize=None, quality=84):
    im = Image.open(path)
    im = ImageOps.exif_transpose(im)
    if resize and max(im.size) > resize:
        im.thumbnail((resize, resize), Image.LANCZOS)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality)
    return "url(data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode() + ")"

def b64_font(path):
    with open(path, "rb") as f:
        return "url(data:font/ttf;base64," + base64.b64encode(f.read()).decode() + ")"

def b64_plain(path, mime="image/svg+xml"):
    with open(path, "rb") as f:
        return "url(data:" + mime + ";base64," + base64.b64encode(f.read()).decode() + ")"

def qr(url, name):
    os.makedirs(QR_DIR, exist_ok=True)
    p = os.path.join(QR_DIR, name + ".png")
    qrcode.make(url, box_size=12, border=2).save(p)
    buf = io.BytesIO()
    Image.open(p).save(buf, "PNG")
    return "url(data:image/png;base64," + base64.b64encode(buf.getvalue()).decode() + ")"

PH1 = b64_img(os.path.join(IMG, "IMG_6111.JPG"), 1600)
PH2 = b64_img(os.path.join(IMG, "IMG_6112.JPG"), 1600)
PH3 = b64_img(os.path.join(IMG, "IMG_6116.JPG"), 1600)
PH4 = b64_img(os.path.join(IMG, "IMG_5583.PNG"), 1400)
PH5 = b64_img(os.path.join(IMG, "IMG_5582.jpeg"), 1200)
PH6 = b64_img(os.path.join(IMG, "IMG_7852.jpeg"), 1600)
PH7 = b64_img(os.path.join(IMG, "IMG_5082.jpeg"), 1600)
PH8 = b64_img(os.path.join(IMG, "IMG_6117.JPG"), 1600)
PH9 = b64_img(os.path.join(IMG, "IMG_7735.jpeg"), 1600)
PH10 = b64_img(os.path.join(IMG, "IMG_7853 2.jpeg"), 1600)
PH11 = b64_img(os.path.join(IMG, "gemini-3-pro-image-preview-2k (nano-banana-pro)_a_сделай_здание_в_стил.PNG"), 1600)
FONT_INTER = b64_font(os.path.join(BASE, "fonts", "Inter.ttf"))
SULOGO = b64_plain(os.path.join(BASE, "su_mark_light.png"), "image/png")

QR_TG = qr("https://t.me/startupspacevstu", "tg")
QR_IG = qr("https://www.instagram.com/space_vstu/", "ig")
QR_GB = qr("https://t.me/glebentired", "gb")

CSS_VARS = (
    "--ph1:" + PH1 + ";\n"
    "--ph2:" + PH2 + ";\n"
    "--ph3:" + PH3 + ";\n"
    "--ph4:" + PH4 + ";\n"
    "--ph5:" + PH5 + ";\n"
    "--ph6:" + PH6 + ";\n"
    "--ph7:" + PH7 + ";\n"
    "--ph8:" + PH8 + ";\n"
    "--ph9:" + PH9 + ";\n"
    "--ph10:" + PH10 + ";\n"
    "--ph11:" + PH11 + ";\n"
    "--font-inter:" + FONT_INTER + ";\n"
    "--sulogo:" + SULOGO + ";\n"
    "--qrtg:" + QR_TG + ";\n"
    "--qrig:" + QR_IG + ";\n"
    "--qrgb:" + QR_GB + ";\n"
)

html = r"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>StartUp Space VSTU</title>
<style>
@font-face{font-family:'Inter';src:var(--font-inter) format('truetype');font-weight:100 900;}
:root{
""" + CSS_VARS + r"""
  --bg:#071022;--ink:#F4F7FC;--mut:#9FB0C8;--mut2:#6C7E99;
  --hair:#1C2944;--accent:#6E9BE0;--brand:#243C65;--flare:#FB9A24;
  --side:clamp(26px,6vw,88px);
  --pad:clamp(20px,4vh,44px);
}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%}
body{font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--ink);
  overflow:hidden;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- система слайдов ---------- */
.slide{position:fixed;inset:0;display:none;overflow:hidden;z-index:1}
.slide.active{display:block}
.slide.enter{display:block;animation:slideIn .68s cubic-bezier(.22,.8,.36,1) both}
.slide.leave{display:block;animation:slideOut .32s ease both}
@keyframes slideIn{from{opacity:0;transform:translateX(5vw) scale(.982)}to{opacity:1;transform:none}}
@keyframes slideOut{from{opacity:1;transform:none}to{opacity:0;transform:translateX(-4vw) scale(.99)}}
.inner{position:relative;z-index:3;height:100%;padding:var(--pad) var(--side)}
.rv{animation:rise .8s cubic-bezier(.22,.8,.36,1) both;animation-delay:var(--d,0s)}
@keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}

/* типографика */
.eyebrow{display:flex;align-items:center;gap:10px;font-size:12.5px;font-weight:600;
  text-transform:uppercase;letter-spacing:.22em;color:var(--mut)}
.eyebrow i{width:7px;height:7px;border-radius:2px;background:var(--flare);display:inline-block}
.eyebrow b{color:var(--ink);font-weight:600}
h1{font-size:clamp(2.7rem,5.8vw,5rem);font-weight:700;letter-spacing:-.03em;line-height:1.02;margin-top:18px}
h1 em{font-style:normal;color:var(--accent)}
h2{font-size:clamp(1.9rem,3.6vw,3rem);font-weight:700;letter-spacing:-.02em;line-height:1.05;margin-top:12px}
.lead{color:var(--mut);font-size:clamp(1.05rem,1.5vw,1.3rem);font-weight:400;line-height:1.55;margin-top:22px;max-width:560px}
.hair{height:1px;background:var(--hair);border:0}

/* число-статистика */
.stats-row{display:flex;flex-wrap:wrap;gap:clamp(24px,5vw,72px);margin-top:44px}
.stat .n{font-size:clamp(3rem,7vw,6.2rem);font-weight:700;letter-spacing:-.045em;line-height:.95;display:flex;align-items:baseline}
.stat .n u{text-decoration:none;color:var(--accent)}
.stat .l{color:var(--mut);font-size:clamp(.85rem,1.1vw,1rem);margin-top:10px;max-width:200px}
.stat.big{min-width:min(46vw,380px)}
.stat.big .n{font-size:clamp(4rem,11vw,9.5rem)}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:46px}
.k{background:rgba(8,16,34,.62);border:1px solid var(--hair);border-radius:20px;padding:26px 22px}
.k .n{font-size:clamp(2.6rem,5vw,4.4rem);font-weight:700;letter-spacing:-.04em;line-height:.95;display:flex;align-items:baseline}
.k .n u{text-decoration:none;color:var(--accent)}
.k .t{font-size:clamp(1rem,1.4vw,1.2rem);font-weight:650;margin-top:12px}
.k .l{color:var(--mut);font-size:.85rem;margin-top:5px;line-height:1.45}
.pfx{padding-left:min(56vw,800px);padding-right:5vw}
.pfx h1{font-size:clamp(2.2rem,4vw,3.6rem);margin-top:12px}
.pfx .row-item{grid-template-columns:52px minmax(170px,280px) 1fr;gap:14px;padding:15px 0}
.pfx .row-item .i{font-size:clamp(1.1rem,1.8vw,1.5rem)}
.pfx .row-item h4{font-size:clamp(.96rem,1.35vw,1.15rem)}
.pfx .row-item p{font-size:clamp(.76rem,1vw,.9rem);line-height:1.4}

/* фото */
.photo{position:absolute;inset:0;background-size:cover;background-position:center;z-index:0}
.photo-left{position:absolute;top:0;bottom:0;z-index:1;background-size:cover;background-position:center;
  left:0;width:min(52vw,740px)}
.photo-right{position:absolute;top:0;bottom:0;z-index:1;background-size:cover;background-position:center;
  right:0;width:min(52vw,740px)}
.shade{position:absolute;inset:0;z-index:2;background:linear-gradient(100deg,rgba(4,9,22,.97) 8%,rgba(7,16,34,.55) 52%,rgba(7,16,34,.06) 82%)}
.shade-c{position:absolute;inset:0;z-index:2;background:linear-gradient(180deg,rgba(7,16,34,.15),rgba(4,9,22,.78) 88%)}
.shade-b{position:absolute;inset:0;z-index:2;background:linear-gradient(0deg,rgba(4,9,22,.96) 2%,rgba(7,16,34,.3) 55%,rgba(7,16,34,.02) 90%)}
.tile{position:relative;border-radius:22px;overflow:hidden;border:1px solid rgba(255,255,255,.09);background:#0E1A33}
.tile .back{position:absolute;inset:0;background-size:cover;background-position:center;transition:transform 1.2s cubic-bezier(.22,.8,.36,1)}
.tile:hover .back{transform:scale(1.045)}
.tile .cap{position:absolute;left:22px;right:22px;bottom:20px;color:#fff;z-index:3}
.tile .cap .n{font-size:clamp(1.6rem,3vw,2.6rem);font-weight:700;letter-spacing:-.03em;line-height:1}
.tile .cap .t{font-size:clamp(.95rem,1.3vw,1.15rem);font-weight:600;margin-top:6px}
.tile .cap .d{font-size:clamp(.75rem,.95vw,.85rem);color:#d6d6db;margin-top:4px}
.tile::after{content:'';position:absolute;inset:0;z-index:2;background:linear-gradient(180deg,transparent 45%,rgba(0,0,0,.62))}

/* списки */
.row-item{display:grid;grid-template-columns:70px minmax(180px,320px) 1fr;gap:20px;align-items:baseline;padding:22px 0;
  border-bottom:1px solid var(--hair)}
.row-item:last-child{border-bottom:0}
.row-item .i{font-size:clamp(1.4rem,2.4vw,2rem);font-weight:300;color:var(--mut2);letter-spacing:-.02em}
.row-item h4{font-size:clamp(1.1rem,1.8vw,1.45rem);font-weight:650;letter-spacing:-.01em}
.row-item p{color:var(--mut);font-size:clamp(.92rem,1.25vw,1.1rem);line-height:1.5}

/* roadmap */
.road{display:grid;grid-template-columns:repeat(5,1fr);gap:0;margin-top:56px;position:relative}
.road::before{content:'';position:absolute;left:9%;right:9%;top:9px;height:1px;background:var(--hair)}
.rd{position:relative;padding-top:30px}
.rd .dot{position:absolute;top:0;left:0;width:19px;height:19px;border-radius:50%;
  background:var(--bg);border:2px solid var(--accent);box-shadow:0 0 0 4px var(--bg)}
.rd .step{color:var(--mut2);font-size:11.5px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;margin-top:6px}
.rd h4{font-size:clamp(1rem,1.5vw,1.3rem);font-weight:700;letter-spacing:-.01em;margin-top:6px}
.rd p{color:var(--mut);font-size:clamp(.78rem,1vw,.95rem);margin-top:6px;line-height:1.45;max-width:180px}

/* QR */
.qs{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:52px}
.qcard{background:rgba(8,16,34,.62);border:1px solid var(--hair);border-radius:24px;padding:40px 30px 36px;
  text-align:center;backdrop-filter:blur(8px);transition:border-color .3s,transform .3s}
.qcard:hover{border-color:rgba(110,155,224,.5);transform:translateY(-4px)}
.qcard.hl{border-color:rgba(251,154,36,.55);background:linear-gradient(180deg,rgba(251,154,36,.12),rgba(8,16,34,.6))}
.qbox{width:158px;height:158px;background-color:#fff;background-size:cover;border-radius:18px;margin:0 auto}
.qcard .nw{font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);margin-top:18px}
.qcard .hd{font-size:clamp(1.05rem,1.5vw,1.3rem);font-weight:700;letter-spacing:-.01em;margin-top:6px}
.qcard .nt{font-size:13px;color:var(--mut);margin-top:8px;line-height:1.4}

/* кнопки, бейджи */
.btn{display:inline-flex;align-items:center;gap:10px;background:var(--brand);color:#fff;font-weight:700;
  border-radius:980px;padding:15px 26px;font-size:15px;text-decoration:none;transition:.25s}
.btn:hover{filter:brightness(1.12);transform:translateY(-1px)}
.chip{display:inline-flex;align-items:center;gap:10px;border:1px solid var(--hair);border-radius:999px;
  padding:10px 16px;font-size:13px;color:var(--mut);background:rgba(8,16,34,.5)}
.chip b{color:var(--ink);font-weight:600}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.tag{font-size:12.5px;color:var(--mut);border:1px solid var(--hair);border-radius:999px;padding:7px 14px;background:rgba(8,16,34,.4)}

/* навигация */
.dots{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);display:flex;gap:7px;z-index:50;align-items:center}
.dots span{width:7px;height:7px;border-radius:99px;background:#2A3A5C;cursor:pointer;transition:all .3s}
.dots span.on{width:26px;background:var(--accent)}
.nav{position:fixed;bottom:16px;right:22px;z-index:50;display:flex;gap:8px}
.nav button{width:42px;height:42px;border-radius:13px;background:transparent;border:1px solid var(--hair);
  color:var(--mut);font-size:17px;cursor:pointer;transition:.2s;backdrop-filter:blur(6px)}
.nav button:hover{border-color:var(--accent);color:var(--ink)}

/* спикер */
.spk{display:flex;align-items:center;gap:14px;border-top:1px solid var(--hair);padding-top:20px;margin-top:46px;max-width:560px}
.spk .av{width:38px;height:38px;border-radius:50%;background:rgba(110,155,224,.16);border:1px solid rgba(110,155,224,.45);
  display:grid;place-items:center;color:var(--accent);font-weight:700;font-size:15px}
.spk b{font-size:15px;font-weight:650;display:block}
.spk span{font-size:13px;color:var(--mut)}
.spks{margin-top:42px;display:grid;gap:16px;max-width:600px}
.spks .spk{margin-top:0}
.su-wrap{display:grid;grid-template-columns:1fr min(40vw,600px);gap:clamp(32px,5vw,80px);align-items:center;height:100%}
.su-left{display:flex;flex-direction:column;justify-content:center;min-width:0;padding-left:clamp(30px,6vw,110px)}
.su-side{height:min(66vh,600px);border-radius:30px;border:1px solid rgba(255,255,255,.1);
  background:linear-gradient(170deg,#1F3D72,#0D1830);display:grid;place-items:center;position:relative;overflow:hidden}
.su-side::after{content:'';position:absolute;inset:0;background:radial-gradient(120% 90% at 80% 10%,rgba(110,155,224,.25),transparent 60%)}
.su-mark{width:min(24vw,300px);height:min(24vw,300px);background-image:var(--sulogo);background-size:contain;background-repeat:no-repeat;background-position:center;position:relative;z-index:1;filter:drop-shadow(0 12px 28px rgba(0,0,0,.4))}
.meta{display:flex;justify-content:space-between;align-items:center;color:var(--mut2);font-size:11.5px;
  letter-spacing:.12em;text-transform:uppercase;margin-top:34px}

@media (max-width:960px){
  .photo-left,.photo-right{width:100%;opacity:.5}
  .pfx{padding-left:var(--side);padding-right:var(--side)}
  .kpi{grid-template-columns:repeat(2,1fr)}
  .su-wrap{grid-template-columns:1fr;gap:28px}
  .su-side{height:min(34vh,280px);order:-1}
  .row-item{grid-template-columns:44px 1fr}
  .row-item p{grid-column:1/-1;margin-top:6px}
  .qs{grid-template-columns:1fr}
  .road{grid-template-columns:1fr;gap:22px}
  .road::before{display:none}
  .dots{display:none}
}
@media (prefers-reduced-motion:reduce){.rv,.slide.active,.slide.enter,.slide.leave{animation:none}}
</style>
</head>
<body>
<!-- 01 · HERO -->
<section class="slide active">
  <div class="photo" style="background-image:var(--ph8);background-position:center 30%"></div>
  <div class="shade"></div>
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.08s">Хакатоны меняют<br><em>студенчество.</em></h1>
    <p class="lead rv" style="--d:.16s">Реальные задачи бизнеса, команда за 48 часов и бесплатный акселератор — путь от идеи до стартапа, который уже прошли 5000+ студентов.</p>
    <div class="tags rv" style="--d:.22s">
      <span class="tag">Хакатоны</span><span class="tag">Space University</span><span class="tag">Space Day</span><span class="tag">Парк высоких технологий</span>
    </div>
    <div class="spks rv" style="--d:.3s">
      <div class="spk">
        <div class="av">ГТ</div>
        <div><b>Глеб Токарь</b><span>руководитель StartUp Space VSTU</span></div>
      </div>
      <div class="spk">
        <div class="av">МГ</div>
        <div><b>Михаил Гунько</b><span>главный по PR-отделу StartUp Space VSTU</span></div>
      </div>
    </div>
  </div>
</section>

<!-- 02 · ЦИФРЫ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.08s">Сообщество <em>в цифрах</em></h1>
    <div class="kpi">
      <div class="k rv" style="--d:.16s"><div class="n">5000<u>+</u></div><div class="t">участников</div><div class="l">во всей стране</div></div>
      <div class="k rv" style="--d:.22s"><div class="n">150<u>+</u></div><div class="t">стартап-проектов</div><div class="l">запущенных с нуля</div></div>
      <div class="k rv" style="--d:.28s"><div class="n">20</div><div class="t">компаний-партнёров</div><div class="l">дают задачи и призы</div></div>
      <div class="k rv" style="--d:.34s"><div class="n">5</div><div class="t">лет сообществу</div><div class="l">которое продолжает расти</div></div>
    </div>
  </div>
</section>

<!-- 03 · ЧТО ДАЁТ -->
<section class="slide">
  <div class="photo-left" style="background-image:var(--ph1)"></div>
  <div class="shade" style="background:linear-gradient(100deg,rgba(4,9,22,.98) 6%,rgba(7,16,34,.6) 46%,rgba(7,16,34,.05) 78%)"></div>
  <div class="inner pfx" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.08s">Один хакатон —<br>четыре <em>результата.</em></h1>
    <div class="rv" style="--d:.22s;margin-top:18px">
      <div class="row-item"><span class="i">01</span><h4>Опыт и портфолио</h4><p>Реальный кейс и быстрый рост навыков — за дни, а не годы.</p></div>
      <div class="row-item"><span class="i">02</span><h4>Команда</h4><p>Единомышленники и будущие сооснователи.</p></div>
      <div class="row-item"><span class="i">03</span><h4>Экспертиза</h4><p>Менторы, спикеры и фидбек жюри из бизнеса.</p></div>
      <div class="row-item"><span class="i">04</span><h4>Призы и оффер</h4><p>Гранты до 5 000 BYN, стажировки и работа.</p></div>
    </div>
  </div>
</section>

<!-- 04 · ФОРМАТ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.06s">48 часов,<br>чтобы <em>построить команду</em></h1>
    <div class="tags rv" style="--d:.16s"><span class="tag">Реальная задача от компании</span><span class="tag">Команда 3–5 человек</span><span class="tag">Питч жюри</span></div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:30px">
      <div class="tile rv" style="--d:.24s;height:min(34vh,300px)">
        <div class="back" style="background-image:var(--ph2)"></div>
        <div class="cap"><div class="n">01</div><div class="t">Задача</div><div class="d">Кейс, который бизнесу нужно решить прямо сейчас.</div></div>
      </div>
      <div class="tile rv" style="--d:.32s;height:min(34vh,300px)">
        <div class="back" style="background-image:var(--ph3);background-position:center 20%"></div>
        <div class="cap"><div class="n">02</div><div class="t">Команда</div><div class="d">Находишь людей на площадке — сразу.</div></div>
      </div>
      <div class="tile rv" style="--d:.4s;height:min(34vh,300px)">
        <div class="back" style="background-image:var(--ph1);background-position:center 25%"></div>
        <div class="cap"><div class="n">03</div><div class="t">Питч</div><div class="d">Прототип, презентация и решение жюри.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- 05 · ПАРТНЁРЫ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.06s">Задачи решают <em>компании</em></h1>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:30px">
      <div class="tile rv" style="--d:.18s;height:min(44vh,380px)">
        <div class="back" style="background-image:var(--ph6)"></div>
        <div class="cap"><div class="n">MTS</div><div class="t">Space Hackathon with MTS</div><div class="d">48 часов · главный приз 5 000 BYN · Яндекс Станция и Redmi Watch.</div></div>
      </div>
      <div class="tile rv" style="--d:.26s;height:min(44vh,380px)">
        <div class="back" style="background-image:var(--ph7)"></div>
        <div class="cap"><div class="n">Great Stone</div><div class="t">Хакатон с «Великим Камнем» и МИРАН</div><div class="d">Кейсы индустриального парка и производства, кейсы B2B.</div></div>
      </div>
    </div>
  </div>
</section>

<!-- 07 · SPACE UNIVERSITY -->
<section class="slide">
  <div class="inner" style="padding:0">
    <div class="su-wrap">
      <div class="su-left">
        <div class="rv" style="--d:.08s;display:flex;align-items:baseline;gap:30px;margin-top:8px">
          <div style="font-size:clamp(5rem,14vw,10rem);font-weight:700;letter-spacing:-.05em;line-height:.9">8</div>
          <h2 style="margin-top:0">недель от идеи<br>до <em>продукта</em></h2>
        </div>
        <div class="rv" style="--d:.16s;display:grid;gap:10px;margin-top:22px;max-width:660px">
          <p class="lead" style="margin-top:0;max-width:none">Методология Lean Startup, спикеры — топ-менеджеры компаний и предприниматели.</p>
          <p class="lead" style="margin-top:0;max-width:none">Space University — открытая программа для студентов со всей страны: бесплатно, 8 недель, своя команда и реальные кейсы.</p>
        </div>
        <div class="stats-row rv" style="--d:.24s;margin-top:30px">
          <div class="stat"><div class="n">100<u>→</u>30<u>–40</u></div><div class="l" style="max-width:250px">проектов проходят отбор — лучшие, бесплатно</div></div>
          <div class="stat"><div class="n">2</div><div class="l" style="max-width:200px">лекции с экспертами в неделю</div></div>
          <div class="stat"><div class="n">7<u>–8</u></div><div class="l" style="max-width:200px">часов питч-практики по воскресеньям</div></div>
        </div>
      </div>
      <div class="su-side rv" style="--d:.18s">
        <div class="su-mark"></div>
      </div>
    </div>
  </div>
</section>

<!-- 08 · ПРОГРАММА -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.06s">Как устроен <em>акселератор</em></h1>
    <div class="rv" style="--d:.2s;margin-top:24px">
      <div class="row-item"><span class="i">01</span><h4>Погружение</h4><p>Проверяем идею и гипотезы: startup-разведка, Design Sprint и проблемные интервью с клиентами.</p></div>
      <div class="row-item"><span class="i">02</span><h4>Продукт</h4><p>MVP без разработки — лендинг, бот, форма; UX-тесты и Battle of MVP с экспертным голосованием.</p></div>
      <div class="row-item"><span class="i">03</span><h4>Бизнес-модель</h4><p>Юнит-экономика, инвест-симуляция и питчинг «попроси правильно» — деньги и партнёрства.</p></div>
      <div class="row-item"><span class="i">04</span><h4>Финал</h4><p>Питч-дек и сценическая подача: полуфинал 15 декабря, финальная питч-сессия 18 декабря.</p></div>
    </div>
  </div>
</section>

<!-- 09 · ВЫПУСКНИКИ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.06s">Они начали<br>с <em>нуля</em></h1>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:30px;margin-top:34px;border-top:1px solid var(--hair)">
      <div class="rv" style="--d:.16s;padding-top:22px">
        <h3 style="font-size:clamp(1.4rem,2.4vw,2rem);font-weight:700;letter-spacing:-.02em">EdMe</h3>
        <p style="color:var(--mut);font-size:.95rem;margin-top:8px;line-height:1.5">Онлайн-центр репетиторов с оборотом более $1 млн.</p>
      </div>
      <div class="rv" style="--d:.22s;padding-top:22px">
        <h3 style="font-size:clamp(1.4rem,2.4vw,2rem);font-weight:700;letter-spacing:-.02em">PSP Brand</h3>
        <p style="color:var(--mut);font-size:.95rem;margin-top:8px;line-height:1.5">Вырос из «Крама БДУ» — сегодня бренд-студия.</p>
      </div>
      <div class="rv" style="--d:.28s;padding-top:22px">
        <h3 style="font-size:clamp(1.4rem,2.4vw,2rem);font-weight:700;letter-spacing:-.02em">Mary</h3>
        <p style="color:var(--mut);font-size:.95rem;margin-top:8px;line-height:1.5">Стартап выпускника, получивший инвестиции.</p>
      </div>
      <div class="rv" style="--d:.34s;padding-top:22px">
        <h3 style="font-size:clamp(1.4rem,2.4vw,2rem);font-weight:700;letter-spacing:-.02em">MarketMate</h3>
        <p style="color:var(--mut);font-size:.95rem;margin-top:8px;line-height:1.5">Продвижение на маркетплейсах — выросло в компанию.</p>
      </div>
    </div>
    <p class="lead rv" style="--d:.44s;margin-top:26px">Без гарантий, опыта и команды — только идея и готовность попробовать. Следующая история — твоя.</p>
  </div>
</section>

<!-- 10 · ПУТЬ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.06s">Путь от идеи<br>до <em>стартапа</em></h1>
    <div class="road">
      <div class="rd rv" style="--d:.16s"><div class="dot"></div><div class="step">01</div><h4>Идея</h4><p>или просто интерес — этого достаточно</p></div>
      <div class="rd rv" style="--d:.22s"><div class="dot"></div><div class="step">02</div><h4>Хакатон</h4><p>команда и первый опыт за 48 часов</p></div>
      <div class="rd rv" style="--d:.28s"><div class="dot"></div><div class="step">03</div><h4>Space University</h4><p>акселерация и питчинг</p></div>
      <div class="rd rv" style="--d:.34s"><div class="dot"></div><div class="step">04</div><h4>Generation</h4><p>форум и демо-день</p></div>
      <div class="rd rv" style="--d:.4s"><div class="dot"></div><div class="step">05</div><h4>Резидент</h4><p>поддержка и рост проекта</p></div>
    </div>
    <p class="lead rv" style="--d:.5s;margin-top:40px;max-width:600px">Хакатон — лучший «первый шаг»: он не требует ни идеи, ни готовой команды.</p>
  </div>
</section>

<!-- 11 · VSTU -->
<section class="slide">
  <div class="photo-right" style="background-image:var(--ph4);background-position:center 12%"></div>
  <div class="shade" style="background:linear-gradient(270deg,rgba(4,9,22,.98) 4%,rgba(7,16,34,.58) 46%,rgba(7,16,34,.04) 78%)"></div>
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.08s">Мы уже в <em>ВГТУ</em></h1>
    <p class="lead rv" style="--d:.16s">27 мая 2026 филиал StartUp Space открылся в VSTU на семинаре-практикуме «Университет как платформа развития молодёжного инновационного предпринимательства».</p>
    <div class="spk rv" style="--d:.26s">
      <div class="av">ГТ</div>
      <div><b>Глеб Токарь</b><span>руководитель StartUp Space VSTU</span></div>
    </div>
    <div class="tags rv" style="--d:.34s"><span class="tag">Встречи</span><span class="tag">Хакатоны</span><span class="tag">Программы для студентов</span></div>
  </div>
</section>

<!-- 12 · КАК НАЧАТЬ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center">
    <h1 class="rv" style="--d:.06s">Три шага до<br>твоего <em>стартапа</em></h1>
    <div class="rv" style="--d:.2s;margin-top:26px">
      <div class="row-item"><span class="i">01</span><h4>Следи</h4><p>Подпишись на сообщество StartUp Space VSTU — там анонсы и открытая регистрация.</p></div>
      <div class="row-item"><span class="i">02</span><h4>Приходи</h4><p>Встречи филиала в VSTU — команда, идеи, наставники.</p></div>
      <div class="row-item"><span class="i">03</span><h4>Участвуй</h4><p>Регистрируйся на хакатон, Space University или Space Day.</p></div>
    </div>
    <div class="rv" style="--d:.34s;display:flex;align-items:center;gap:22px;flex-wrap:wrap;margin-top:34px">
      <span class="chip">Space Day · 15 сентября · <b>Falcon Club Arena</b> · вход свободный</span>
      <a class="btn" href="https://spaceday.by/" target="_blank">Зарегистрироваться →</a>
    </div>
  </div>
</section>

<!-- 13 · КОНТАКТЫ -->
<section class="slide">
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
    <h1 class="rv" style="--d:.06s">Присоединяйся</h1>
    <div class="qs">
      <div class="qcard rv" style="--d:.18s">
        <div class="qbox" style="background-image:var(--qrtg)"></div>
        <div class="nw">Telegram</div>
        <div class="hd">@startup_space_vstu</div>
        <div class="nt">канал сообщества VSTU</div>
      </div>
      <div class="qcard rv" style="--d:.26s">
        <div class="qbox" style="background-image:var(--qrig)"></div>
        <div class="nw">Instagram</div>
        <div class="hd">@space_vstu</div>
        <div class="nt">фото, видео, анонсы</div>
      </div>
      <div class="qcard hl rv" style="--d:.34s">
        <div class="qbox" style="background-image:var(--qrgb)"></div>
        <div class="nw">Глеб Токарь</div>
        <div class="hd">@glebentired</div>
        <div class="nt">руководитель филиала — пиши напрямую</div>
      </div>
    </div>
  </div>
</section>

<!-- 14 · ФИНАЛ -->
<section class="slide">
  <div class="photo" style="background-image:var(--ph11);background-position:center 35%"></div>
  <div class="shade-c"></div>
  <div class="inner" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
    <h1 class="rv" style="--d:.1s;max-width:900px">Идеи без действий<br><em>ничего не стоят.</em></h1>
    <p class="lead rv" style="--d:.2s;text-align:center">Приходи на хакатон — пусть твой первый стартап начнётся именно в VSTU.</p>
    <div class="rv" style="--d:.3s;margin-top:28px">
      <div style="font-size:clamp(1.2rem,1.9vw,1.5rem);font-weight:650;letter-spacing:.01em">Присоединяйтесь</div>
    </div>
  </div>
</section>

<div class="dots" id="dots"></div>
<div class="nav">
  <button id="prev">‹</button>
  <button id="next">›</button>
</div>

<script>
(function(){
  var slides=[].slice.call(document.querySelectorAll('.slide'));
  var dots=document.getElementById('dots');
  slides.forEach(function(s,i){var d=document.createElement('span');
    d.onclick=function(){go(i)};dots.appendChild(d);});
  var ds=[].slice.call(dots.children),cur=0,busy=false;
  function render(){
    slides.forEach(function(s,i){s.classList.toggle('active',i===cur)});
    ds.forEach(function(d,i){d.classList.toggle('on',i===cur)});
  }
  function go(n){
    if(busy)return;
    var nn=(n+slides.length)%slides.length;
    if(nn===cur)return;
    busy=true;
    slides[cur].classList.add('leave');
    setTimeout(function(){
      slides.forEach(function(s){s.classList.remove('active','enter')});
      slides[cur].classList.remove('leave');
      cur=nn;
      slides[cur].classList.add('active');
      void slides[cur].offsetWidth;
      slides[cur].classList.add('enter');
      render();
      busy=false;
    },340);
  }
  document.getElementById('next').onclick=function(){go(cur+1)};
  document.getElementById('prev').onclick=function(){go(cur-1)};
  document.addEventListener('keydown',function(e){
    if(['ArrowRight','PageDown',' ','Enter'].indexOf(e.key)>-1){e.preventDefault();go(cur+1)}
    if(['ArrowLeft','PageUp','Backspace'].indexOf(e.key)>-1){e.preventDefault();go(cur-1)}
    if(e.key==='Home'){go(0)}if(e.key==='End'){go(slides.length-1)}
  });
  var tx=null;
  document.addEventListener('touchstart',function(e){tx=e.changedTouches[0].clientX});
  document.addEventListener('touchend',function(e){var dx=e.changedTouches[0].clientX-tx;
    if(Math.abs(dx)>60){dx<0?go(cur+1):go(cur-1)}},{passive:true});
  render();
})();
</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("SAVED:", OUT)
print("SIZE: %.1f MB" % (os.path.getsize(OUT) / 1048576))