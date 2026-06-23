#!/usr/bin/env python3
"""Generate the Xagent documentation site.

Holds the shared chrome (navbar + sidebar + footer + scripts) and the
per-page article content, then writes every standalone HTML file. Mirrors
the structure/formatting of the Xinference docs site.

Run:  python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Sidebar icons (re-used from the shared design system)
# ---------------------------------------------------------------------------
ICONS = {
 "home":'<path d="M3 9.5 12 3l9 6.5"/><path d="M5 9v11h14V9"/>',
 "rocket":'<path d="M5 14c-1.5 1.5-2 5-2 5s3.5-.5 5-2"/><path d="M12 15l-3-3c1-4 4-7 9-9 0 5-3 8-6 9z"/><circle cx="14.5" cy="9.5" r="1.2"/>',
 "lock":'<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
 "users":'<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5 6-5s6 1.7 6 5"/><path d="M16 5.5a3 3 0 0 1 0 5.8"/><path d="M21 20c0-2.4-1.3-3.9-3.5-4.6"/>',
 "box":'<path d="M21 8 12 3 3 8v8l9 5 9-5z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/>',
 "grid":'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
 "layers":'<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
 "server":'<rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><circle cx="7" cy="7.5" r="1"/><circle cx="7" cy="16.5" r="1"/>',
 "plus":'<circle cx="12" cy="12" r="9"/><path d="M12 8v8M8 12h8"/>',
 "activity":'<path d="M3 12h4l3 8 4-16 3 8h4"/>',
 "settings":'<circle cx="12" cy="12" r="3.2"/><path d="M19 12a7 7 0 0 0-.1-1.3l2-1.5-2-3.4-2.3 1a7 7 0 0 0-2.2-1.3L14 3h-4l-.4 2.2a7 7 0 0 0-2.2 1.3l-2.3-1-2 3.4 2 1.5A7 7 0 0 0 5 12c0 .4 0 .9.1 1.3l-2 1.5 2 3.4 2.3-1c.7.5 1.4 1 2.2 1.3L10 21h4l.4-2.2c.8-.3 1.5-.8 2.2-1.3l2.3 1 2-3.4-2-1.5c.1-.4.1-.9.1-1.3Z"/>',
 "code":'<path d="m9 8-4 4 4 4"/><path d="m15 8 4 4-4 4"/>',
 "chat":'<path d="M21 12a8 8 0 0 1-11.5 7.2L4 21l1.8-5.5A8 8 0 1 1 21 12Z"/>',
 "hash":'<path d="M5 9h14M5 15h14M10 4 8 20M16 4l-2 16"/>',
 "plug":'<path d="M9 3v6M15 3v6"/><path d="M7 9h10v3a5 5 0 0 1-10 0z"/><path d="M12 17v4"/>',
 "card":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 10h18"/>',
 "gauge":'<path d="M12 13l4-4"/><path d="M4 18a9 9 0 1 1 16 0"/>',
 "tag":'<path d="M3 11V4h7l11 11-7 7z"/><circle cx="7.5" cy="7.5" r="1.3"/>',
 "building":'<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
 "mail":'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "book":'<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 0-3 3z"/><path d="M5 4v16"/>',
 "terminal":'<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M13 15h4"/>',
 "cloud":'<path d="M7 18a4 4 0 0 1 0-8 5 5 0 0 1 9.6-1.3A3.5 3.5 0 0 1 18 18z"/>',
 "docker":'<rect x="4" y="11" width="16" height="6" rx="1"/><path d="M7 11V8h3v3M11 11V8h3v3M7 11V6h0"/>',
 "brain":'<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1 5 3 3 0 0 0 2 4 3 3 0 0 0 5 1V5a3 3 0 0 0-3-1Z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 1 5 3 3 0 0 1-2 4 3 3 0 0 1-5 1"/>',
 "cpu":'<rect x="5" y="5" width="14" height="14" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "image":'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/>',
 "share":'<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
 "file":'<path d="M14 3v5h5"/><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>',
 "upload":'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M7 9l5-5 5 5"/><path d="M12 4v12"/>',
}

def icon(key):
    p = ICONS.get(key, ICONS["box"])
    return ('<span class="menu__icon"><svg viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            'stroke-linejoin="round">' + p + '</svg></span>')

# ---------------------------------------------------------------------------
# Information architecture (label, root-relative href, icon key)
# ---------------------------------------------------------------------------
TOP = ("Overview", "overview.html", "home")
SECTIONS = [
 ("Getting Started", [
    ("Quickstart", "getting-started/quickstart.html", "rocket"),
    ("Authentication", "getting-started/authentication.html", "lock"),
    ("Teams &amp; Workspaces", "getting-started/teams.html", "users"),
 ]),
 ("Models", [
    ("Overview", "models/overview.html", "cpu"),
    ("LLM Models", "models/llm.html", "brain"),
    ("Embedding Models", "models/embedding.html", "hash"),
    ("Image Generation", "models/image-generation.html", "image"),
 ]),
 ("Agents", [
    ("Overview", "agents/overview.html", "brain"),
    ("Building Agents", "agents/building-agents.html", "plus"),
    ("Templates", "agents/templates.html", "grid"),
    ("Workforces", "agents/workforces.html", "layers"),
    ("Sharing Agents", "agents/sharing.html", "share"),
    ("Widget Embed", "agents/widget-embed.html", "code"),
 ]),
 ("Tasks", [
    ("Overview", "tasks/overview.html", "activity"),
    ("Execution", "tasks/execution.html", "layers"),
 ]),
 ("Knowledge Bases", [
    ("Overview", "knowledge-bases/overview.html", "book"),
 ]),
 ("Memory", [
    ("Overview", "memory/overview.html", "brain"),
    ("Memory Types", "memory/types.html", "grid"),
    ("Configuration", "memory/configuration.html", "settings"),
 ]),
 ("Tools &amp; Skills", [
    ("Overview", "tools/overview.html", "plug"),
    ("Built-in Tools", "tools/built-in.html", "grid"),
    ("MCP Servers", "tools/mcp.html", "server"),
    ("MCP Providers", "tools/mcp-providers.html", "lock"),
    ("Custom APIs", "tools/custom-apis.html", "code"),
 ]),
 ("Files", [
    ("Overview", "files/overview.html", "file"),
    ("Upload", "files/upload.html", "upload"),
    ("Management", "files/management.html", "settings"),
 ]),
 ("Channels", [
    ("Overview", "channels/overview.html", "chat"),
    ("Telegram", "channels/telegram.html", "chat"),
 ]),
 ("Workspace API", [
    ("Overview", "workspace-api/overview.html", "code"),
    ("Managing Agents", "workspace-api/agents.html", "box"),
    ("Running Tasks", "workspace-api/tasks.html", "chat"),
 ]),
 ("Billing", [
    ("Overview", "billing/overview.html", "card"),
    ("Plans", "billing/plans.html", "tag"),
    ("Usage &amp; Quotas", "billing/usage.html", "gauge"),
 ]),
 ("Teams", [
    ("Members &amp; Roles", "teams/members.html", "users"),
    ("Invitations", "teams/invitations.html", "mail"),
 ]),
 ("API Reference", [
    ("Overview", "api-reference/overview.html", "book"),
    ("Agents", "api-reference/agents.html", "box"),
    ("Workspace SDK", "api-reference/workspace.html", "code"),
 ]),
 ("Self-Hosting", [
    ("Overview", "self-hosting/overview.html", "home"),
    ("Docker", "self-hosting/docker.html", "docker"),
    ("Environment Variables", "self-hosting/environment-variables.html", "terminal"),
 ]),
]

CHEVRON = ('<svg class="menu__chevron" viewBox="0 0 24 24" fill="none" '
           'stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>')
SEARCH_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/>'
              '<path d="m21 21-4-4"/></svg>')
SUN_SVG = ('<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"/>'
           '<path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5 5l1.5 1.5M17.5 17.5 19 19M19 5l-1.5 1.5M6.5 17.5 5 19"/></svg>')
MOON_SVG = ('<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M21 12.5A8.5 8.5 0 1 1 11.5 3 6.5 6.5 0 0 0 21 12.5Z"/></svg>')
BOLT_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>')

WIDGET = ('<script\n'
          '  src="https://sg.cloud.xagent.co/widget.js"\n'
          '  data-agent-id="76"\n'
          '  data-button-size="60px"\n'
          '  data-button-color="#000"\n'
          '  data-icon-color="#fff"\n'
          '  data-panel-bg-color="#fff">\n'
          '</script>')

def link(label, root_href, ikey, prefix, current):
    active = " menu__link--active" if root_href == current else ""
    return (f'<li class="menu__list-item"><a class="menu__link{active}" '
            f'href="{prefix}{root_href}">{icon(ikey)}<span>{label}</span></a></li>')

def build_navbar(prefix):
    return f'''<header class="navbar">
  <div class="navbar__inner">
    <a class="navbar__brand" href="{prefix}overview.html">
      <img class="navbar__logo" src="{prefix}img/logo.svg" alt="Xagent Logo" />
      <span class="navbar__title">Xagent <span class="navbar__title-light">Docs</span></span>
    </a>
    <div class="navbar__items--right">
      <button class="navbar__search" type="button" aria-label="Search documentation">
        {SEARCH_SVG}<span>Search documentation...</span><kbd class="navbar__kbd">⌘K</kbd>
      </button>
      <button class="navbar__theme" type="button" aria-label="Toggle theme">{SUN_SVG}{MOON_SVG}</button>
      <a class="navbar__cta" href="{prefix}getting-started/quickstart.html">Get started</a>
    </div>
  </div>
</header>'''

def build_sidebar(prefix, current):
    parts = ['<aside class="sidebar-container"><nav class="sidebar"><ul class="menu">']
    parts.append(link(TOP[0], TOP[1], TOP[2], prefix, current))
    for title, items in SECTIONS:
        parts.append(f'<li class="menu__list-item menu__category" data-collapsed="false">'
                     f'<button class="menu__category-label" type="button">{title}{CHEVRON}</button>'
                     f'<ul class="menu menu__sub">')
        for label, href, ikey in items:
            parts.append(link(label, href, ikey, prefix, current))
        parts.append('</ul></li>')
    parts.append('</ul></nav>')
    parts.append(f'<div class="sidebar__footer">{BOLT_SVG}<span>Powered by '
                 f'<a href="https://xagent.run">Xagent</a></span></div>')
    parts.append('</aside>')
    return "".join(parts)

def build_footer(prefix):
    return f'''<footer class="footer">
  <div class="footer__inner">
    <div class="footer__col">
      <div class="footer__title">Documentation</div>
      <a class="footer__link" href="{prefix}overview.html">Overview</a>
      <a class="footer__link" href="{prefix}getting-started/quickstart.html">Getting Started</a>
      <a class="footer__link" href="{prefix}api-reference/overview.html">API Reference</a>
    </div>
    <div class="footer__col">
      <div class="footer__title">Product</div>
      <a class="footer__link" href="{prefix}agents/overview.html">Agents</a>
      <a class="footer__link" href="{prefix}knowledge-bases/overview.html">Knowledge Bases</a>
      <a class="footer__link" href="{prefix}billing/overview.html">Billing</a>
    </div>
    <div class="footer__col">
      <div class="footer__title">Company</div>
      <a class="footer__link" href="https://xagent.run">Website</a>
      <a class="footer__link" href="https://docs.xagent.run">Docs</a>
      <a class="footer__link" href="https://github.com/xorbitsai/xagent">GitHub</a>
    </div>
  </div>
  <div class="footer__copyright">Copyright © 2026 Xagent. All Rights Reserved.</div>
</footer>'''

def toc(items):
    """items: list of (level, anchor, text); level in (2,3)."""
    lis = "".join(
        f'<li class="toc__item toc__item--h{lv}"><a href="#{anc}">{txt}</a></li>'
        for lv, anc, txt in items)
    return f'<aside class="toc"><div class="toc__title">On this page</div><ul class="toc__list">{lis}</ul></aside>'

def page(rel, title, article, toc_items):
    depth = rel.count("/")
    prefix = "../" * depth
    return f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} | Xagent Docs</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{prefix}assets/styles.css" />
</head>
<body>
{build_navbar(prefix)}
<div class="layout">
  {build_sidebar(prefix, rel)}
  <main class="main">
    <article class="doc-content markdown">
{article}
    </article>
    {toc(toc_items)}
  </main>
</div>
{build_footer(prefix)}
<script src="{prefix}assets/app.js"></script>
{WIDGET}
</body>
</html>
'''

# ---------------------------------------------------------------------------
# Small content helpers
# ---------------------------------------------------------------------------
def code(body):
    return f'<div class="highlight"><pre><span></span><code>{body}</code></pre></div>'

def adm(kind, heading, body_html):
    return (f'<div class="admonition admonition-{kind}">'
            f'<p class="admonition-heading">{heading}</p>{body_html}</div>')

# Import the page bodies from a sibling module to keep this file readable.
from content import PAGES  # noqa: E402

# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------
INDEX = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
         '<meta http-equiv="refresh" content="0; url=overview.html">'
         '<title>Xagent Docs</title></head><body>'
         '<p>Redirecting to <a href="overview.html">documentation</a>…</p>'
         + WIDGET + '</body></html>\n')

def main():
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX)
    count = 0
    for rel, (title, article, toc_items) in PAGES.items():
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(rel, title, article, toc_items))
        count += 1
        print("wrote:", rel)
    print(f"\nDone. {count} pages + index.html")

if __name__ == "__main__":
    main()
