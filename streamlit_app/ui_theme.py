"""
ui_theme.py - presentation layer for the Real Estate app.
Only CSS and tiny HTML helpers. No data loading, no model, no calculations.
Call apply_theme() once per page, right after st.set_page_config().
"""

import streamlit as st

_CSS = """
:root {
  --ink: #12292C;
  --spruce: #0E2F33;
  --spruce-soft: #173F44;
  --mist: #EEF3F2;
  --paper: #FFFFFF;
  --line: #D3DFDC;
  --muted: #5A706E;
  --teal: #0B7A75;
  --teal-deep: #085F5B;
  --sand: #F1D9A6;
  --display: "Bricolage Grotesque", "Instrument Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
}

/* ---------- App shell ---------- */
[data-testid="stApp"] { background: var(--mist); }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stAppDeployButton"] { display: none; }

[data-testid="stMainBlockContainer"] {
  max-width: 1240px;
  margin: 0 auto;
  padding: 2.4rem 2.6rem 4rem;
}
@media (max-width: 640px) {
  [data-testid="stMainBlockContainer"] { padding: 1.4rem 1rem 3rem; }
}

/* The style block itself should not take up layout space */
[data-testid="stElementContainer"]:has(> [data-testid="stHtml"] > style:only-child),
[data-testid="stElementContainer"]:has(> style:only-child) { display: none; }

/* ---------- Typography ---------- */
[data-testid="stMainBlockContainer"] h1 {
  font-family: var(--display);
  font-weight: 700;
  font-size: 2.35rem;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--spruce);
  padding: 0 0 0.3rem;
}
[data-testid="stMainBlockContainer"] h2 {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.35rem;
  letter-spacing: -0.01em;
  color: var(--spruce);
  padding: 0.2rem 0 0.35rem;
}
[data-testid="stMainBlockContainer"] h3 {
  font-family: var(--display);
  font-weight: 500;
  font-size: 1.25rem;
  letter-spacing: -0.01em;
  color: var(--muted);
}
.lead {
  max-width: 72ch;
  margin: 0 0 1.4rem;
  font-size: 1.05rem;
  line-height: 1.55;
  color: var(--muted);
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] { background: var(--spruce); border-right: 0; }
[data-testid="stSidebarHeader"] { padding: 1.5rem 1.1rem 0.6rem 1.4rem; align-items: center; }
[data-testid="stLogoSpacer"] { display: none; }
[data-testid="stSidebarHeader"]::before {
  content: "Real Estate App";
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.2rem;
  letter-spacing: -0.01em;
  color: #FFFFFF;
  white-space: nowrap;
}
[data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"] { color: #8FB3AE; }

[data-testid="stSidebarNav"] { padding-top: 0.6rem; }
[data-testid="stSidebarNavLink"] {
  border-radius: 10px;
  padding: 0.55rem 0.85rem;
  color: #C9DCD9;
  transition: background 0.15s ease;
}
[data-testid="stSidebarNavLink"] p { color: inherit; font-weight: 500; }
[data-testid="stSidebarNavLink"]:hover { background: rgba(255, 255, 255, 0.07); }
[data-testid="stSidebarNavLink"][aria-current="page"] { background: rgba(255, 255, 255, 0.13); color: #FFFFFF; }
[data-testid="stSidebarNavLink"][aria-current="page"] p { font-weight: 600; }

/* ---------- Cards (containers created with key="card-..." etc.) ---------- */
[class*="st-key-card-"],
[class*="st-key-tile-"],
.st-key-estimate-panel,
.st-key-map-card {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 1.25rem 1.4rem 1.3rem;
  gap: 0.9rem;
}
.card-title {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.05rem;
  letter-spacing: -0.005em;
  color: var(--spruce);
  margin: 0;
}
.card-note { margin: -0.35rem 0 0; font-size: 0.9rem; line-height: 1.5; color: var(--muted); }
.tile-text { margin: 0; font-size: 0.97rem; line-height: 1.55; color: var(--muted); }

/* ---------- Inputs ----------
   Fill, border, radius and focus colour come from the native theme in
   .streamlit/config.toml, so they keep working across Streamlit versions. */
[data-testid="stWidgetLabel"] p { font-size: 0.86rem; font-weight: 600; color: var(--ink); }

/* ---------- Buttons ---------- */
[data-testid="stBaseButton-primary"] {
  background: var(--teal);
  border: 1px solid var(--teal);
  color: #FFFFFF;
  border-radius: 10px;
  min-height: 48px;
  padding: 0 1.6rem;
  font-weight: 600;
  letter-spacing: 0.005em;
  transition: background 0.15s ease, border-color 0.15s ease;
}
[data-testid="stBaseButton-primary"]:hover { background: var(--teal-deep); border-color: var(--teal-deep); color: #FFFFFF; }
[data-testid="stBaseButton-primary"]:focus-visible { outline: 3px solid rgba(11, 122, 117, 0.35); outline-offset: 2px; }
.st-key-estimate-panel [data-testid="stElementContainer"]:has([data-testid="stButton"]),
.st-key-estimate-panel [data-testid="stButton"],
.st-key-estimate-panel [data-testid="stButton"] button { width: 100% !important; }

/* ---------- Estimate (the one memorable element) ---------- */
@media (min-width: 1000px) {
  [data-testid="stLayoutWrapper"]:has(> .st-key-estimate-panel) {
    position: sticky;
    top: 4.5rem;
  }
}
.panel-hint { margin: -0.35rem 0 0; font-size: 0.93rem; line-height: 1.5; color: var(--muted); }
.est-card {
  background: var(--spruce);
  border-radius: 14px;
  padding: 1.35rem 1.4rem 1.25rem;
  color: #DCE9E7;
  container-type: inline-size;
}
.est-label { font-size: 0.9rem; font-weight: 500; color: #9FC2BD; }
.est-range {
  margin-top: 0.35rem;
  font-family: var(--display);
  font-weight: 700;
  font-size: clamp(1.3rem, 9.5cqw, 2.4rem);
  white-space: nowrap;
  line-height: 1.12;
  letter-spacing: -0.02em;
  color: var(--sand);
}
.est-unit { margin-left: 0.3rem; font-size: 0.55em; font-weight: 500; letter-spacing: 0; color: #C9B98F; }
.est-sentence {
  margin: 0.95rem 0 0;
  padding-top: 0.85rem;
  border-top: 1px solid rgba(255, 255, 255, 0.14);
  font-size: 0.93rem;
  line-height: 1.5;
  color: #DCE9E7;
  text-wrap: pretty;
}

/* ---------- Tables, alerts, charts ---------- */
[data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }
[data-testid="stAlert"] > div {
  background: #E1EFED;
  border: 1px solid #C3DCD8;
  border-radius: 12px;
  color: var(--ink);
}
.st-key-map-card { padding: 1.1rem 1.1rem 0.8rem; }
.st-key-map-card [data-testid="stPlotlyChart"] { border-radius: 12px; overflow: hidden; }

@media (prefers-reduced-motion: reduce) {
  * { transition: none !important; }
}
"""


def apply_theme():
    """Inject the shared CSS."""
    st.html(f"<style>{_CSS}</style>")


def lead(text):
    st.html(f'<p class="lead">{text}</p>')


def card_title(text, note=None):
    html = f'<div class="card-title">{text}</div>'
    if note:
        html += f'<p class="card-note">{note}</p>'
    st.html(html)


def panel_hint(text):
    st.html(f'<p class="panel-hint">{text}</p>')


def tile_text(text):
    st.html(f'<p class="tile-text">{text}</p>')


def estimate_card(low, high, sentence):
    """Result panel. `low`/`high` are the already-rounded numbers from the existing
    prediction code; `sentence` is your original result sentence, unchanged."""
    st.html(
        '<div class="est-card">'
        '<div class="est-label">Estimated price range</div>'
        f'<div class="est-range">&#8377;{low:.2f} &ndash; {high:.2f}<span class="est-unit">Cr</span></div>'
        f'<p class="est-sentence">{sentence}</p>'
        "</div>"
    )