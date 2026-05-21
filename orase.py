from flask import Flask
from app.lib.biblioteca_orase import populatie_barcelona, descriere_barcelona

app = Flask(__name__)

_ARR  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>'
_BCK  = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="m12 5-7 7 7 7"/></svg>'
_PIN  = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 13-8 13S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
_DWN  = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m5 12 7 7 7-7"/></svg>'
_GLB  = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'
_CITY = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
_LEAF = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>'
_ART  = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r=".5" fill="currentColor"/><circle cx="17.5" cy="10.5" r=".5" fill="currentColor"/><circle cx="8.5" cy="7.5" r=".5" fill="currentColor"/><circle cx="6.5" cy="12.5" r=".5" fill="currentColor"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.554C21.965 6.012 17.461 2 12 2z"/></svg>'
_STAD = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="11" rx="10" ry="5"/><path d="M2 11v4c0 2.76 4.48 5 10 5s10-2.24 10-5v-4"/><path d="M12 6v10"/><path d="M2 11h20"/></svg>'
_MAP  = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg>'
_USERS= '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
_STAR = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
_GH   = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>'
_LI   = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'

STYLE = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

  :root {
    --bg:     #070d1a;
    --surf:   #0f1829;
    --surf-h: #162035;
    --bd:     rgba(255,255,255,0.1);
    --bd-h:   rgba(56,189,248,0.5);
    --pri:    #38bdf8;
    --pri-d:  #0ea5e9;
    --acc:    #f97316;
    --acc-d:  #ea580c;
    --gold:   #fbbf24;
    --text:   #eef4ff;
    --muted:  rgba(238,244,255,0.56);
    --dim:    rgba(238,244,255,0.3);
    --glow-b: rgba(56,189,248,0.22);
    --glow-o: rgba(249,115,22,0.38);
  }

  *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    font-family: 'Inter', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
  }

  nav {
    position: fixed;
    top: 0; left: 0; right: 0;
    z-index: 200;
    height: 58px;
    display: flex;
    align-items: center;
    gap: 1.75rem;
    padding: 0 2.5rem;
    background: rgba(7, 13, 26, 0.96);
    border-bottom: 1px solid var(--bd);
  }
  .nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text);
    text-decoration: none;
    margin-right: auto;
    letter-spacing: .04em;
    display: flex;
    align-items: center;
    gap: .45rem;
  }
  .nav-logo svg { color: var(--pri); flex-shrink: 0; }
  nav a:not(.nav-logo) {
    color: var(--muted);
    text-decoration: none;
    font-size: .84rem;
    font-weight: 500;
    letter-spacing: .03em;
    padding: .3rem 0;
    position: relative;
    transition: color 150ms ease, text-shadow 250ms ease;
  }
  nav a:not(.nav-logo)::after {
    content: '';
    position: absolute;
    bottom: -1px; left: 0;
    width: 0; height: 1.5px;
    background: var(--pri);
    border-radius: 999px;
    transition: width 250ms cubic-bezier(0.16,1,0.3,1);
  }
  nav a:not(.nav-logo):hover {
    color: var(--text);
    text-shadow: 0 0 14px rgba(56,189,248,0.5);
  }
  nav a:not(.nav-logo):hover::after { width: 100%; }

  .hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 8rem 2rem 5rem;
    overflow: hidden;
    background:
      linear-gradient(175deg, rgba(7,13,26,.75) 0%, rgba(10,45,80,.6) 45%, rgba(234,88,12,.22) 100%),
      url('https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=1600&q=80') center/cover no-repeat;
  }
  #heroCanvas {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    z-index: 1;
    pointer-events: none;
  }
  .hero > *:not(#heroCanvas) { position: relative; z-index: 2; }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    font-size: .68rem;
    font-weight: 600;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: var(--pri);
    padding: .38rem 1rem;
    background: rgba(56,189,248,.12);
    border: 1px solid rgba(56,189,248,.3);
    border-radius: 999px;
    margin-bottom: 1.5rem;
    animation: si 600ms cubic-bezier(0.16,1,0.3,1) 0ms both;
  }
  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3.25rem, 9vw, 6.75rem);
    font-weight: 700;
    line-height: 1.04;
    letter-spacing: -.025em;
    color: var(--text);
    margin-bottom: .75rem;
    animation: si 600ms cubic-bezier(0.16,1,0.3,1) 80ms both;
  }
  .hero h1 em {
    font-style: italic;
    color: var(--pri);
    background: linear-gradient(130deg, var(--pri) 0%, var(--gold) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .hero-sub {
    font-size: .95rem;
    font-weight: 400;
    color: var(--muted);
    letter-spacing: .1em;
    text-transform: uppercase;
    margin-bottom: 2.75rem;
    animation: si 600ms cubic-bezier(0.16,1,0.3,1) 160ms both;
  }
  .hero-tags {
    display: flex;
    gap: .55rem;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 3rem;
    animation: si 600ms cubic-bezier(0.16,1,0.3,1) 240ms both;
  }
  .hero-tag {
    background: rgba(255,255,255,.09);
    border: 1px solid rgba(255,255,255,.14);
    color: rgba(255,255,255,.82);
    padding: .28rem .85rem;
    border-radius: 999px;
    font-size: .76rem;
    font-weight: 500;
    letter-spacing: .04em;
  }
  .hero-cta {
    display: inline-flex;
    align-items: center;
    gap: .5rem;
    background: var(--acc);
    color: #fff;
    padding: .875rem 2.25rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: .9rem;
    text-decoration: none;
    letter-spacing: .02em;
    min-height: 48px;
    box-shadow: 0 4px 28px var(--glow-o);
    touch-action: manipulation;
    animation: si 600ms cubic-bezier(0.16,1,0.3,1) 320ms both;
    transition: background 150ms ease, box-shadow 250ms ease, transform 150ms cubic-bezier(0.16,1,0.3,1);
  }
  .hero-cta:hover { background: var(--acc-d); box-shadow: 0 8px 40px var(--glow-o); transform: translateY(-2px); }
  .hero-cta:active { transform: scale(.97); transition-duration: 80ms; }

  .hero-scroll {
    position: absolute;
    bottom: 2.25rem; left: 50%;
    transform: translateX(-50%);
    z-index: 3;
    color: var(--dim);
    font-size: .68rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: .35rem;
    animation: bounce-y 2.6s ease-in-out infinite;
  }

  .hero--bcn::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: radial-gradient(rgba(56,189,248,.06) 1px, transparent 1px);
    background-size: 28px 28px;
    z-index: 0;
    pointer-events: none;
  }
  .hero--bcn .hero-deco {
    position: absolute;
    right: -4%; top: 50%;
    transform: translateY(-50%);
    width: 480px;
    max-width: 75vw;
    height: 480px;
    max-height: 75vw;
    z-index: 1;
    pointer-events: none;
    opacity: .4;
  }

  .container { max-width: 920px; margin: 0 auto; padding: 5rem 1.5rem; }

  .sec-label {
    font-size: .67rem;
    font-weight: 600;
    letter-spacing: .22em;
    text-transform: uppercase;
    color: var(--pri);
    margin-bottom: .5rem;
  }
  .sec-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 2rem;
    line-height: 1.2;
  }
  .divider {
    width: 48px; height: 2px;
    background: linear-gradient(90deg, var(--pri), transparent);
    margin: 0 0 2rem;
    border-radius: 999px;
  }

  .card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    transition: border-color 250ms ease, background 250ms ease, box-shadow 250ms ease, transform 250ms cubic-bezier(0.16,1,0.3,1);
  }
  .card:hover {
    border-color: var(--bd-h);
    background: var(--surf-h);
    box-shadow: 0 8px 40px rgba(0,0,0,.5);
    transform: translateY(-3px);
  }
  .card h2 { font-family: 'Playfair Display', serif; font-size: 1.15rem; color: var(--text); margin-bottom: .75rem; font-weight: 700; }
  .card p { line-height: 1.82; color: var(--muted); font-size: .93rem; }
  .card strong { color: var(--text); font-weight: 600; }

  .stat-card {
    background: linear-gradient(135deg, rgba(14,165,233,.18) 0%, rgba(15,24,41,.95) 100%);
    border: 1px solid rgba(56,189,248,.28);
    border-radius: 16px;
    padding: 2.75rem 2rem;
    text-align: center;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(ellipse at 65% -5%, rgba(56,189,248,.14) 0%, transparent 55%);
    pointer-events: none;
  }
  .s-label { font-size: .67rem; font-weight: 600; letter-spacing: .22em; text-transform: uppercase; color: var(--pri); margin-bottom: 1rem; }
  .s-value { font-family: 'Playfair Display', serif; font-size: 1.65rem; font-weight: 700; color: var(--text); line-height: 1.3; position: relative; }

  .stat-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 1.5rem; }
  .stat-mini {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 1.75rem 1.25rem;
    text-align: center;
    transition: border-color 250ms ease, transform 250ms cubic-bezier(0.16,1,0.3,1), box-shadow 250ms ease;
  }
  .stat-mini:hover { border-color: var(--bd-h); transform: translateY(-3px); box-shadow: 0 8px 32px rgba(0,0,0,.4); }
  .sm-icon { width: 44px; height: 44px; border-radius: 12px; background: rgba(56,189,248,.12); display: flex; align-items: center; justify-content: center; margin: 0 auto .9rem; color: var(--pri); }
  .sm-value { font-family: 'Playfair Display', serif; font-size: 1.75rem; font-weight: 700; color: var(--text); margin-bottom: .25rem; }
  .sm-label { font-size: .73rem; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }

  .geo-card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 2rem 2.25rem;
    margin-bottom: 1.5rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.75rem 2.5rem;
  }
  .gi-label { font-size: .64rem; font-weight: 600; letter-spacing: .2em; text-transform: uppercase; color: var(--dim); margin-bottom: .3rem; }
  .gi-value { font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 700; color: var(--pri); }

  .ms-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 1.5rem; }
  .ms-card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 1.75rem 1.5rem;
    transition: border-color 250ms ease, transform 250ms cubic-bezier(0.16,1,0.3,1), box-shadow 250ms ease;
  }
  .ms-card:hover { border-color: var(--bd-h); transform: translateY(-3px); box-shadow: 0 10px 36px rgba(0,0,0,.45); }
  .ms-icon { width: 48px; height: 48px; background: rgba(56,189,248,.12); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: var(--pri); margin-bottom: 1rem; }
  .ms-name { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: var(--text); margin-bottom: .35rem; }
  .ms-desc { font-size: .78rem; color: var(--muted); line-height: 1.55; }

  .city-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(185px, 1fr)); gap: 1rem; margin-top: 1.5rem; }
  .city-card {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 1.75rem 1.25rem;
    text-align: center;
    text-decoration: none;
    color: var(--text);
    font-weight: 600;
    font-size: .9rem;
    touch-action: manipulation;
    transition: border-color 250ms ease, background 250ms ease, transform 250ms cubic-bezier(0.16,1,0.3,1), box-shadow 250ms ease;
  }
  .city-card:hover { border-color: var(--bd-h); background: var(--surf-h); transform: translateY(-4px); box-shadow: 0 10px 36px rgba(0,0,0,.4); }
  .city-card:active { transform: scale(.97); transition-duration: 80ms; }
  .city-flag { font-size: 2.5rem; margin-bottom: .65rem; display: block; }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: .75rem 1.75rem;
    background: var(--pri-d);
    color: #fff;
    text-decoration: none;
    border-radius: 10px;
    font-weight: 600;
    font-size: .875rem;
    min-height: 44px;
    touch-action: manipulation;
    box-shadow: 0 2px 16px var(--glow-b);
    transition: background 150ms ease, box-shadow 250ms ease, transform 150ms cubic-bezier(0.16,1,0.3,1);
  }
  .btn:hover { background: var(--pri); box-shadow: 0 6px 24px var(--glow-b); transform: translateY(-1px); }
  .btn:active { transform: scale(.97); transition-duration: 80ms; }

  .btn-ghost {
    display: inline-flex;
    align-items: center;
    gap: .45rem;
    padding: .7rem 1.5rem;
    border: 1px solid var(--bd);
    color: var(--muted);
    background: var(--surf);
    text-decoration: none;
    border-radius: 10px;
    font-weight: 500;
    font-size: .85rem;
    min-height: 44px;
    touch-action: manipulation;
    transition: border-color 150ms ease, color 150ms ease, transform 150ms cubic-bezier(0.16,1,0.3,1);
  }
  .btn-ghost:hover { border-color: var(--bd-h); color: var(--text); transform: translateY(-1px); }
  .btn-ghost:active { transform: scale(.97); transition-duration: 80ms; }
  .btn-row { display: flex; gap: .75rem; flex-wrap: wrap; margin-top: 1.5rem; }
  .back { margin-bottom: 2.25rem; }

  .info-banner {
    background: linear-gradient(135deg, rgba(249,115,22,.1) 0%, rgba(15,24,41,.95) 100%);
    border: 1px solid rgba(249,115,22,.25);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
  }
  .info-banner p { line-height: 1.85; color: var(--muted); font-size: .93rem; }
  .info-banner strong { color: var(--text); }

  .chart-wrap {
    background: var(--surf);
    border: 1px solid var(--bd);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 1.5rem;
  }
  .chart-legend { font-size: .67rem; font-weight: 600; letter-spacing: .22em; text-transform: uppercase; color: var(--pri); margin-bottom: 1.5rem; }
  .chart-vals { display: flex; gap: 1rem; margin-bottom: .5rem; }
  .chart-vals span { flex: 1; text-align: center; font-family: 'Playfair Display', serif; font-size: .88rem; font-weight: 700; color: var(--text); opacity: 0; transition: opacity 400ms ease 900ms; }
  .sr.in .chart-vals span { opacity: 1; }
  .chart-bars { display: flex; gap: 1rem; height: 160px; align-items: flex-end; border-bottom: 1px solid var(--bd); padding-bottom: 1px; margin-bottom: .75rem; }
  .c-col { flex: 1; display: flex; align-items: flex-end; height: 100%; }
  .c-bar {
    width: 100%;
    height: 0;
    border-radius: 6px 6px 0 0;
    position: relative;
    overflow: hidden;
    transition: height 900ms cubic-bezier(0.16,1,0.3,1);
    transition-delay: calc(var(--j, 0) * 110ms);
  }
  .c-bar::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 40%; background: linear-gradient(180deg, rgba(255,255,255,.15), transparent); pointer-events: none; }
  .c-bar.pri { background: var(--pri); }
  .c-bar.acc { background: var(--acc); }
  .c-bar.dim { background: rgba(56,189,248,.35); }
  .sr.in .c-bar { height: calc(var(--pct, 50) * 1.4px); }
  .chart-names { display: flex; gap: 1rem; }
  .chart-names span { flex: 1; text-align: center; font-size: .76rem; font-weight: 500; color: var(--muted); }

  .tl { position: relative; margin: 2rem 0; }
  .tl-line {
    position: absolute;
    left: 2%; right: 2%; top: 110px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(56,189,248,.35) 12%, rgba(56,189,248,.35) 88%, transparent);
    pointer-events: none;
  }
  .tl-items { display: flex; height: 220px; }
  .tl-item { flex: 1; display: flex; flex-direction: column; align-items: center; }
  .tl-up { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding: 0 .4rem .75rem; text-align: center; }
  .tl-down { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: flex-start; padding: .75rem .4rem 0; text-align: center; }
  .tl-gap { flex: 1; }
  .tl-dot { width: 10px; height: 10px; background: var(--pri); border-radius: 50%; flex-shrink: 0; box-shadow: 0 0 0 3px rgba(56,189,248,.2), 0 0 10px rgba(56,189,248,.3); z-index: 1; }
  .tl-year { font-family: 'Playfair Display', serif; font-size: .95rem; font-weight: 700; color: var(--pri); margin-bottom: .2rem; }
  .tl-label { font-size: .72rem; color: var(--muted); line-height: 1.45; }

  footer { border-top: 1px solid var(--bd); }
  .ft-inner { max-width: 920px; margin: 0 auto; padding: 3rem 1.5rem 2rem; display: flex; justify-content: space-between; align-items: flex-start; gap: 3rem; flex-wrap: wrap; }
  .ft-brand { flex: 1; min-width: 180px; }
  .ft-logo { font-family: 'Playfair Display', serif; font-size: 1.15rem; font-weight: 700; color: var(--text); margin-bottom: .5rem; }
  .ft-tagline { font-size: .78rem; color: var(--muted); line-height: 1.6; max-width: 220px; }
  .ft-nav { display: flex; gap: 3rem; }
  .ft-col { display: flex; flex-direction: column; gap: .6rem; }
  .ft-col-label { font-size: .65rem; font-weight: 600; letter-spacing: .18em; text-transform: uppercase; color: var(--dim); margin-bottom: .2rem; }
  .ft-col a { font-size: .82rem; color: var(--muted); text-decoration: none; transition: color 150ms ease; }
  .ft-col a:hover { color: var(--text); }
  .ft-bottom { max-width: 920px; margin: 0 auto; padding: 1.25rem 1.5rem 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; font-size: .76rem; color: var(--dim); border-top: 1px solid var(--bd); }
  .ft-social { display: flex; gap: .75rem; }
  .ft-soc { width: 34px; height: 34px; border: 1px solid var(--bd); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: var(--muted); text-decoration: none; transition: border-color 150ms ease, color 150ms ease, transform 150ms cubic-bezier(0.16,1,0.3,1); }
  .ft-soc:hover { border-color: var(--bd-h); color: var(--text); transform: translateY(-2px); }

  #cursor { display: none; }
  @media (hover: hover) and (pointer: fine) {
    #cursor {
      display: block;
      position: fixed;
      width: 28px; height: 28px;
      border: 1.5px solid var(--pri);
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      left: -100px; top: -100px;
      transform: translate(-50%, -50%);
      transition: width 180ms ease, height 180ms ease, border-color 180ms ease;
    }
  }

  @media (prefers-reduced-motion: no-preference) {
    .sr {
      opacity: 0;
      transform: translateY(20px);
      transition: opacity 600ms cubic-bezier(0.16,1,0.3,1), transform 600ms cubic-bezier(0.16,1,0.3,1);
      transition-delay: calc(var(--i, 0) * 50ms);
    }
    .sr.in { opacity: 1; transform: none; }
  }

  @keyframes si {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: none; }
  }
  @keyframes bounce-y {
    0%, 100% { transform: translateX(-50%) translateY(0); }
    50%       { transform: translateX(-50%) translateY(8px); }
  }

  @media (max-width: 768px) {
    .stat-grid { grid-template-columns: 1fr 1fr; gap: .75rem; }
    .stat-grid .stat-mini:last-child { grid-column: 1 / -1; }
    .ms-grid { grid-template-columns: 1fr 1fr; }
    .ft-inner { flex-direction: column; gap: 2rem; }
    .ft-nav { gap: 2rem; }
  }
  @media (max-width: 640px) {
    nav { padding: 0 1.25rem; gap: 1.25rem; }
    .hero h1 { font-size: 2.75rem; }
    .geo-card { gap: 1.25rem 1.5rem; padding: 1.5rem; }
    .container { padding: 4rem 1.25rem; }
    .stat-card { padding: 2rem 1.5rem; }
    .ms-grid { grid-template-columns: 1fr; }
    .tl-items { height: auto; flex-direction: column; }
    .tl-line { top: 0; bottom: 0; left: 9px; right: auto; width: 1px; height: auto; background: linear-gradient(180deg, transparent, rgba(56,189,248,.35) 8%, rgba(56,189,248,.35) 92%, transparent); }
    .tl-item { flex-direction: row; align-items: center; gap: 1.25rem; height: auto; min-height: 80px; flex: none; padding-left: 4px; }
    .tl-up, .tl-down { flex: 1; align-items: flex-start; justify-content: center; padding: .5rem 0; text-align: left; }
    .tl-gap { display: none; }
    .tl-label { text-align: left; }
    .chart-bars { height: 120px; }
    .sr.in .c-bar { height: calc(var(--pct, 50) * 1.05px); }
  }
</style>
"""

SHADER_JS = """
<script>
(function(){
  var c=document.getElementById('heroCanvas');
  if(!c)return;
  var gl=c.getContext('webgl')||c.getContext('experimental-webgl');
  if(!gl)return;
  var vs='attribute vec2 a;void main(){gl_Position=vec4(a,0.,1.);}';
  var fs=[
    'precision highp float;',
    'uniform float T;uniform vec2 R;',
    'float h(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}',
    'float n(vec2 p){vec2 i=floor(p),f=fract(p),u=f*f*(3.-2.*f);',
    'return mix(mix(h(i),h(i+vec2(1,0)),u.x),mix(h(i+vec2(0,1)),h(i+vec2(1,1)),u.x),u.y);}',
    'float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<4;i++){v+=a*n(p);p=p*2.1+vec2(1.3*float(i)+.7,1.7*float(i)+.3);a*=.5;}return v;}',
    'void main(){',
    'vec2 uv=gl_FragCoord.xy/R;float t=T*.1;',
    'vec2 q=vec2(fbm(uv*3.+t),fbm(uv*3.+vec2(1.)));',
    'vec2 r=vec2(fbm(uv*3.+2.*q+vec2(1.7,9.2)+.15*t),fbm(uv*3.+2.*q+vec2(8.3,2.8)+.126*t));',
    'float f=fbm(uv*3.+2.*r);',
    'vec3 c1=vec3(.047,.29,.431),c2=vec3(.055,.647,.914),c3=vec3(.918,.345,.047);',
    'vec3 col=mix(c1,c2,clamp(f*2.+.2,0.,1.));',
    'col=mix(col,c3,clamp(f*f*3.-.5,0.,1.));',
    'col+=vec3(.04,.1,.18)*clamp(f*f*f*2.,0.,1.);',
    'col*=smoothstep(0.,1.,1.-length((uv-.5)*1.8))*.55+.45;',
    'gl_FragColor=vec4(col,.5);}'
  ].join('');
  function sh(t,s){var x=gl.createShader(t);gl.shaderSource(x,s);gl.compileShader(x);return x;}
  var p=gl.createProgram();
  gl.attachShader(p,sh(gl.VERTEX_SHADER,vs));
  gl.attachShader(p,sh(gl.FRAGMENT_SHADER,fs));
  gl.linkProgram(p);gl.useProgram(p);
  var b=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,b);
  gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,1,-1,-1,1,1,1]),gl.STATIC_DRAW);
  var al=gl.getAttribLocation(p,'a');gl.enableVertexAttribArray(al);
  gl.vertexAttribPointer(al,2,gl.FLOAT,false,0,0);
  gl.enable(gl.BLEND);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);
  var uT=gl.getUniformLocation(p,'T'),uR=gl.getUniformLocation(p,'R'),t0=performance.now();
  function resize(){c.width=Math.floor(c.offsetWidth*.6);c.height=Math.floor(c.offsetHeight*.6);gl.viewport(0,0,c.width,c.height);}
  window.addEventListener('resize',resize);resize();
  (function loop(){gl.uniform1f(uT,(performance.now()-t0)*.001);gl.uniform2f(uR,c.width,c.height);gl.clear(gl.COLOR_BUFFER_BIT);gl.drawArrays(gl.TRIANGLE_STRIP,0,4);requestAnimationFrame(loop);})();
})();
</script>
"""

MOTION_JS = """
<script>
(function(){
  var yr=document.getElementById('ft-yr');
  if(yr)yr.textContent=new Date().getFullYear();
  var els=document.querySelectorAll('.sr');
  if(!els.length)return;
  if(window.matchMedia('(prefers-reduced-motion:reduce)').matches){
    els.forEach(function(el){el.classList.add('in');});
    return;
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}
    });
  },{threshold:.08,rootMargin:'0px 0px -28px 0px'});
  var seen=new Map();
  els.forEach(function(el){
    var par=el.parentElement;
    var idx=seen.get(par)||0;
    el.style.setProperty('--i',idx);
    seen.set(par,idx+1);
    io.observe(el);
  });
})();
</script>
"""

CURSOR_JS = """
<script>
(function(){
  var cur=document.getElementById('cursor');
  if(!cur)return;
  if(!window.matchMedia('(hover:hover) and (pointer:fine)').matches)return;
  var x=window.innerWidth/2,y=window.innerHeight/2,tx=x,ty=y;
  document.addEventListener('mousemove',function(e){tx=e.clientX;ty=e.clientY;});
  (function tick(){
    x+=(tx-x)*.14;y+=(ty-y)*.14;
    cur.style.left=x+'px';cur.style.top=y+'px';
    requestAnimationFrame(tick);
  })();
  document.addEventListener('mousedown',function(){cur.style.width='18px';cur.style.height='18px';cur.style.background='rgba(56,189,248,.12)';});
  document.addEventListener('mouseup',function(){cur.style.width='28px';cur.style.height='28px';cur.style.background='transparent';});
  document.querySelectorAll('a,button').forEach(function(el){
    el.addEventListener('mouseenter',function(){cur.style.width='42px';cur.style.height='42px';cur.style.borderColor='var(--acc)';});
    el.addEventListener('mouseleave',function(){cur.style.width='28px';cur.style.height='28px';cur.style.borderColor='var(--pri)';});
  });
})();
</script>
"""


def page(title, body, nav_links="", shader=False, motion=False):
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Orase SCC</title>
  {STYLE}
</head>
<body>
  <div id="cursor"></div>
  <nav>
    <a class="nav-logo" href="/">{_GLB} Orase</a>
    <a href="/">Acasa</a>
    <a href="/orase">Orase</a>
    {nav_links}
  </nav>
  {body}
  <footer>
    <div class="ft-inner">
      <div class="ft-brand">
        <div class="ft-logo">Orase SCC</div>
        <p class="ft-tagline">Proiect realizat in cadrul cursului Servicii Cloud si Containerizare, grupa 445D.</p>
      </div>
      <nav class="ft-nav">
        <div class="ft-col">
          <div class="ft-col-label">Navigare</div>
          <a href="/">Acasa</a>
          <a href="/orase">Orase</a>
          <a href="/barcelona">Barcelona</a>
        </div>
        <div class="ft-col">
          <div class="ft-col-label">Informatii</div>
          <a href="/barcelona/populatie">Populatie</a>
          <a href="/barcelona/descriere">Descriere</a>
        </div>
      </nav>
    </div>
    <div class="ft-bottom">
      <span>&copy; <span id="ft-yr"></span> Vlasceanu Mihnea-Stefan &middot; Grupa 445D</span>
      <div class="ft-social">
        <a href="#" aria-label="GitHub" class="ft-soc">{_GH}</a>
        <a href="#" aria-label="LinkedIn" class="ft-soc">{_LI}</a>
      </div>
    </div>
  </footer>
  {SHADER_JS if shader else ""}
  {MOTION_JS}
  {CURSOR_JS}
</body>
</html>"""


@app.route('/')
def index():
    body = f"""
    <div class="hero">
      <canvas id="heroCanvas"></canvas>
      <div class="hero-badge">
        {_PIN}&nbsp; 41.3851° N &nbsp;·&nbsp; 2.1734° E
      </div>
      <h1>Explore <em>Orase</em></h1>
      <p class="hero-sub">Informatii despre orase din lume</p>
      <div class="hero-tags">
        <span class="hero-tag">Geografie</span>
        <span class="hero-tag">Populatie</span>
        <span class="hero-tag">Cultura</span>
        <span class="hero-tag">Arhitectura</span>
      </div>
      <a href="/orase" class="hero-cta">
        Exploreaza orasele {_ARR}
      </a>
      <div class="hero-scroll">
        {_DWN}
        scroll
      </div>
    </div>
    <div class="container">
      <div class="sec-label sr">Date rapide</div>
      <div class="sec-title sr">Proiectul in cifre</div>
      <div class="stat-grid">
        <div class="stat-mini sr">
          <div class="sm-icon">{_MAP}</div>
          <div class="sm-value">1</div>
          <div class="sm-label">Oras explorat</div>
        </div>
        <div class="stat-mini sr">
          <div class="sm-icon">{_GLB}</div>
          <div class="sm-value">1</div>
          <div class="sm-label">Tara acoperita</div>
        </div>
        <div class="stat-mini sr">
          <div class="sm-icon">{_USERS}</div>
          <div class="sm-value">12M+</div>
          <div class="sm-label">Turisti anual</div>
        </div>
      </div>
      <div class="sec-label sr">Despre proiect</div>
      <div class="sec-title sr">Servicii Cloud si Containerizare</div>
      <div class="card sr">
        <p>Aplicatie web dezvoltata in cadrul cursului <strong>SCC</strong>, grupa 445D.
        Prezinta informatii geografice, demografice si culturale despre orase din intreaga lume.
        Containerizata cu Docker si integrata intr-un pipeline CI/CD Jenkins.</p>
        <div class="btn-row">
          <a href="/orase" class="btn">{_PIN}&nbsp; Vezi orasele</a>
        </div>
      </div>
    </div>
    """
    return page("Acasa", body, shader=True)


@app.route('/orase')
def orase():
    body = f"""
    <div style="padding-top:58px"></div>
    <div class="container">
      <div class="back sr">
        <a href="/" class="btn-ghost">{_BCK}&nbsp; Acasa</a>
      </div>
      <div class="sec-label sr">Explorare</div>
      <div class="sec-title sr">Orase disponibile</div>
      <div class="divider sr"></div>
      <div class="card sr">
        <p>Selecteaza un oras pentru a vedea informatii detaliate despre localizare,
        populatie si cultura.</p>
        <div class="city-grid">
          <a href="/barcelona" class="city-card sr">
            <span class="city-flag">&#127466;&#127480;</span>
            Barcelona
          </a>
        </div>
      </div>
    </div>
    """
    return page("Orase", body, nav_links=f'<a href="/barcelona">Barcelona</a>')


@app.route('/barcelona')
def barcelona():
    deco_svg = """<svg class="hero-deco" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
      <circle cx="100" cy="100" r="95" stroke="rgba(56,189,248,0.12)" stroke-width="0.5"/>
      <circle cx="100" cy="100" r="75" stroke="rgba(56,189,248,0.1)" stroke-width="0.5"/>
      <circle cx="100" cy="100" r="55" stroke="rgba(56,189,248,0.08)" stroke-width="0.5"/>
      <circle cx="100" cy="100" r="35" stroke="rgba(56,189,248,0.06)" stroke-width="0.5"/>
      <line x1="5" y1="100" x2="195" y2="100" stroke="rgba(56,189,248,0.07)" stroke-width="0.5"/>
      <line x1="100" y1="5" x2="100" y2="195" stroke="rgba(56,189,248,0.07)" stroke-width="0.5"/>
      <line x1="33" y1="33" x2="167" y2="167" stroke="rgba(56,189,248,0.05)" stroke-width="0.5"/>
      <line x1="167" y1="33" x2="33" y2="167" stroke="rgba(56,189,248,0.05)" stroke-width="0.5"/>
      <circle cx="100" cy="5" r="2.5" fill="rgba(56,189,248,0.35)"/>
      <circle cx="100" cy="195" r="2.5" fill="rgba(56,189,248,0.35)"/>
      <circle cx="5" cy="100" r="2.5" fill="rgba(56,189,248,0.35)"/>
      <circle cx="195" cy="100" r="2.5" fill="rgba(56,189,248,0.35)"/>
    </svg>"""

    body = f"""
    <div class="hero hero--bcn" style="min-height:65vh;background-image:
      linear-gradient(175deg,rgba(7,13,26,.78) 0%,rgba(10,50,90,.62) 50%,rgba(234,88,12,.22) 100%),
      url('https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=1600&q=80')">
      <canvas id="heroCanvas"></canvas>
      {deco_svg}
      <div class="hero-badge">
        {_PIN}&nbsp; 41.3851° N &nbsp;·&nbsp; 2.1734° E
      </div>
      <h1><em>Barcelona</em></h1>
      <p class="hero-sub">Capitala Cataloniei &nbsp;·&nbsp; Spania</p>
      <div class="hero-tags">
        <span class="hero-tag">Costa Mediteraneana</span>
        <span class="hero-tag">Arhitectura Gaudi</span>
        <span class="hero-tag">JO 1992</span>
        <span class="hero-tag">FC Barcelona</span>
      </div>
    </div>
    <div class="container">
      <div class="back sr">
        <a href="/orase" class="btn-ghost">{_BCK}&nbsp; Orase</a>
      </div>
      <div class="geo-card sr">
        <div class="geo-item">
          <div class="gi-label">Latitudine</div>
          <div class="gi-value">41.3851° N</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Longitudine</div>
          <div class="gi-value">2.1734° E</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Altitudine</div>
          <div class="gi-value">12 m</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Tara</div>
          <div class="gi-value">Spania</div>
        </div>
      </div>
      <div class="sec-label sr">Atractii</div>
      <div class="sec-title sr">Must See</div>
      <div class="ms-grid">
        <div class="ms-card sr">
          <div class="ms-icon">{_CITY}</div>
          <div class="ms-name">Sagrada Familia</div>
          <div class="ms-desc">Capodopera lui Gaudí, bazilica în constructie din 1882</div>
        </div>
        <div class="ms-card sr">
          <div class="ms-icon">{_LEAF}</div>
          <div class="ms-name">Park Güell</div>
          <div class="ms-desc">Parc public cu mozaicuri ceramice si peisaje panoramice</div>
        </div>
        <div class="ms-card sr">
          <div class="ms-icon">{_ART}</div>
          <div class="ms-name">Casa Batlló</div>
          <div class="ms-desc">Bijuterie Art Nouveau pe Passeig de Gràcia</div>
        </div>
        <div class="ms-card sr">
          <div class="ms-icon">{_STAD}</div>
          <div class="ms-name">Camp Nou</div>
          <div class="ms-desc">Cel mai mare stadion din Europa, 99.354 locuri</div>
        </div>
      </div>
      <div class="card sr" style="margin-top:1.5rem">
        <h2>Informatii despre Barcelona</h2>
        <p>Alege o sectiune pentru a afla mai multe despre acest oras mediteranean unic.</p>
        <div class="btn-row">
          <a href="/barcelona/populatie" class="btn">{_ARR}&nbsp; Populatie</a>
          <a href="/barcelona/descriere" class="btn">{_ARR}&nbsp; Descriere</a>
        </div>
      </div>
    </div>
    """
    return page("Barcelona", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>',
                shader=True)


@app.route('/barcelona/populatie')
def populatie():
    info = populatie_barcelona()
    body = f"""
    <div style="padding-top:58px"></div>
    <div class="container">
      <div class="back sr">
        <a href="/barcelona" class="btn-ghost">{_BCK}&nbsp; Barcelona</a>
      </div>
      <div class="sec-label sr">Date demografice</div>
      <div class="sec-title sr">Populatia Barcelonei</div>
      <div class="divider sr"></div>
      <div class="stat-card sr">
        <div class="s-label">Populatie &nbsp;&middot;&nbsp; Barcelona</div>
        <div class="s-value">{info}</div>
      </div>
      <div class="chart-wrap sr">
        <div class="chart-legend">Comparatie populatie &mdash; oras (milioane loc.)</div>
        <div class="chart-vals">
          <span>1.6M</span>
          <span>3.3M</span>
          <span>0.8M</span>
        </div>
        <div class="chart-bars">
          <div class="c-col">
            <div class="c-bar pri" style="--pct:49;--j:0"></div>
          </div>
          <div class="c-col">
            <div class="c-bar acc" style="--pct:100;--j:1"></div>
          </div>
          <div class="c-col">
            <div class="c-bar dim" style="--pct:24;--j:2"></div>
          </div>
        </div>
        <div class="chart-names">
          <span>Barcelona</span>
          <span>Madrid</span>
          <span>Valencia</span>
        </div>
      </div>
      <div class="info-banner sr">
        <p>Barcelona este al doilea cel mai populat oras din Spania, dupa Madrid.
        Zona metropolitana depaseste <strong>5.5 milioane</strong> de locuitori,
        facand-o unul dintre cele mai mari centre urbane din sudul Europei.
        Densitatea populatiei in centrul orasului este de aproximativ
        <strong>16.000 locuitori/km&sup2;</strong>.</p>
      </div>
    </div>
    """
    return page("Populatie Barcelona", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>')


@app.route('/barcelona/descriere')
def descriere():
    info = descriere_barcelona()
    body = f"""
    <div style="padding-top:58px"></div>
    <div class="container">
      <div class="back sr">
        <a href="/barcelona" class="btn-ghost">{_BCK}&nbsp; Barcelona</a>
      </div>
      <div class="sec-label sr">Despre oras</div>
      <div class="sec-title sr">Descriere</div>
      <div class="divider sr"></div>
      <div class="card sr">
        <h2>Prezentare generala</h2>
        <p>{info}</p>
      </div>
      <div class="card sr">
        <h2>Repere culturale</h2>
        <p>Barcelona este renumita la nivel mondial pentru operele arhitectului
        <strong>Antoni Gaudi</strong>: Sagrada Familia, Park Guell, Casa Batllo si Casa Mila.
        Orasul a gazduit <strong>Jocurile Olimpice din 1992</strong>, eveniment care a
        transformat infrastructura urbana. Bucataria catalana, viata de noapte, plajele
        mediteraneene si muzeele de arta atrag anual peste
        <strong>12 milioane de turisti</strong>.</p>
      </div>
      <div class="sec-label sr" style="margin-top:3rem">Istorie</div>
      <div class="sec-title sr">Momente cheie</div>
      <div class="tl sr">
        <div class="tl-line"></div>
        <div class="tl-items">
          <div class="tl-item">
            <div class="tl-up">
              <div class="tl-year">230 î.Hr.</div>
              <div class="tl-label">Fondare romană<br>Colonia Barcino</div>
            </div>
            <div class="tl-dot"></div>
            <div class="tl-gap"></div>
          </div>
          <div class="tl-item">
            <div class="tl-gap"></div>
            <div class="tl-dot"></div>
            <div class="tl-down">
              <div class="tl-year">985</div>
              <div class="tl-label">Cucerire maură<br>Al-Manzur</div>
            </div>
          </div>
          <div class="tl-item">
            <div class="tl-up">
              <div class="tl-year">1714</div>
              <div class="tl-label">Căderea Barcelonei<br>Razboiul Succesiunii</div>
            </div>
            <div class="tl-dot"></div>
            <div class="tl-gap"></div>
          </div>
          <div class="tl-item">
            <div class="tl-gap"></div>
            <div class="tl-dot"></div>
            <div class="tl-down">
              <div class="tl-year">1888</div>
              <div class="tl-label">Expozitia Universala<br>Parc de la Ciutadella</div>
            </div>
          </div>
          <div class="tl-item">
            <div class="tl-up">
              <div class="tl-year">1992</div>
              <div class="tl-label">Jocurile Olimpice<br>Transformare urbana</div>
            </div>
            <div class="tl-dot"></div>
            <div class="tl-gap"></div>
          </div>
        </div>
      </div>
      <div class="geo-card sr" style="margin-top:1.5rem">
        <div class="geo-item">
          <div class="gi-label">Fondare</div>
          <div class="gi-value">230 î.Hr.</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Suprafata</div>
          <div class="gi-value">101 km&sup2;</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Climat</div>
          <div class="gi-value">Mediteranean</div>
        </div>
        <div class="geo-item">
          <div class="gi-label">Temp. medie</div>
          <div class="gi-value">17.5° C</div>
        </div>
      </div>
    </div>
    """
    return page("Descriere Barcelona", body,
                nav_links=f'<a href="/barcelona">Barcelona</a>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)
