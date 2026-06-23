# -*- coding: utf-8 -*-
"""Article bodies for the Xagent docs site.

Each entry maps a root-relative path to (title, article_html, toc_items).
toc_items is a list of (level, anchor, text) for the "On this page" rail.
"""

def c(body):
    """Code block matching the site's highlight markup."""
    return f'<div class="highlight"><pre><span></span><code>{body}</code></pre></div>'

def adm(kind, heading, body_html):
    return (f'<div class="admonition admonition-{kind}">'
            f'<p class="admonition-heading">{heading}</p>{body_html}</div>')


PAGES = {}

# ===========================================================================
# Overview
# ===========================================================================
PAGES["overview.html"] = ("Overview", '''<h1 id="xagent-documentation">Xagent Documentation</h1>
<p>Xagent is an enterprise agent platform built on a simple idea: <strong>describe tasks, not workflows</strong>. Instead of wiring up flowcharts and brittle automation chains, you tell an agent what outcome you want — and Xagent plans the task, decomposes it into steps, selects the right tools, and executes.</p>
<h2 id="what-is-xagent">What is Xagent?</h2>
<p>Xagent pairs an LLM-driven planning engine with multi-agent orchestration and a secure execution sandbox. When you give an agent a goal, the platform:</p>
<ol>
<li><strong>Plans</strong> the task dynamically at runtime instead of following a fixed graph</li>
<li><strong>Decomposes</strong> it into executable steps</li>
<li><strong>Selects</strong> the tools, skills, and knowledge bases each step needs</li>
<li><strong>Executes</strong> inside a VM-level sandbox, then evaluates and iterates</li>
<li><strong>Delivers</strong> results — reports, decks, posters, structured data, or chat responses</li>
</ol>
<p>The same runtime powers everything from one-shot chat assistants to long-running multi-agent <a href="agents/workforces.html">workforces</a>.</p>
<h2 id="core-concepts">Core Concepts</h2>
<table>
<thead><tr><th>Concept</th><th>Description</th></tr></thead>
<tbody>
<tr><td><strong>Agent</strong></td><td>A configured assistant with instructions, an execution mode, models, knowledge bases, skills, and a set of allowed tools.</td></tr>
<tr><td><strong>Task</strong></td><td>A single run of an agent against a goal. Tracked through a lifecycle with steps, files, and an output.</td></tr>
<tr><td><strong>Workforce</strong></td><td>A team of agents that collaborate on a shared objective, orchestrated automatically.</td></tr>
<tr><td><strong>Knowledge Base</strong></td><td>A collection of ingested documents, indexed for retrieval-augmented generation (RAG).</td></tr>
<tr><td><strong>Skill</strong></td><td>A reusable, packaged capability (e.g. presentation generation, evidence-based RAG) an agent can recall.</td></tr>
<tr><td><strong>Team</strong></td><td>A workspace that groups users, shares a plan and billing account, and scopes available tools.</td></tr>
</tbody>
</table>
<h2 id="key-features">Key Features</h2>
<ul>
<li><strong>Dynamic planning engine</strong> — Plan → Execute → Reflect loops with conditional branching, not static flows</li>
<li><strong>Multi-agent orchestration</strong> — compose specialised agents into a workforce</li>
<li><strong>Tool &amp; model orchestration</strong> — OpenAI, Anthropic, self-hosted models via Xinference, MCP servers, and custom APIs</li>
<li><strong>Knowledge bases (RAG)</strong> — ingest documents and ground agents in your own data</li>
<li><strong>VM-level sandbox</strong> — safe agent execution, isolated from the host</li>
<li><strong>Multi-tenant teams</strong> — invite members, assign roles, and share a billing account</li>
<li><strong>SSO support</strong> — sign in with Google</li>
<li><strong>Flexible deployment</strong> — local, private/on-prem, or cloud via Docker</li>
</ul>
<h2 id="quick-links">Quick Links</h2>
<div class="card-grid">
  <a class="card" href="./getting-started/quickstart.html">
    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 14c-1.5 1.5-2 5-2 5s3.5-.5 5-2"/><path d="M12 15l-3-3c1-4 4-7 9-9 0 5-3 8-6 9z"/><circle cx="14.5" cy="9.5" r="1.2"/></svg></span>
    <span class="card__title">Quickstart <span class="card__arrow">→</span></span>
    <p class="card__desc">Run Xagent with Docker and create your first agent in minutes.</p>
  </a>
  <a class="card" href="./agents/overview.html">
    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-1 5 3 3 0 0 0 2 4 3 3 0 0 0 5 1V5a3 3 0 0 0-3-1Z"/><path d="M15 4a3 3 0 0 1 3 3 3 3 0 0 1 1 5 3 3 0 0 1-2 4 3 3 0 0 1-5 1"/></svg></span>
    <span class="card__title">Agents <span class="card__arrow">→</span></span>
    <p class="card__desc">Understand how agents plan, choose tools, and execute tasks.</p>
  </a>
  <a class="card" href="./workspace-api/overview.html">
    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m9 8-4 4 4 4"/><path d="m15 8 4 4-4 4"/></svg></span>
    <span class="card__title">Workspace API <span class="card__arrow">→</span></span>
    <p class="card__desc">Create agents and run tasks programmatically with the v1 SDK API.</p>
  </a>
  <a class="card" href="./self-hosting/overview.html">
    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5 12 3l9 6.5"/><path d="M5 9v11h14V9"/></svg></span>
    <span class="card__title">Self-Hosting <span class="card__arrow">→</span></span>
    <p class="card__desc">Deploy Xagent on your own infrastructure with Docker.</p>
  </a>
</div>''', [
 (2, "what-is-xagent", "What is Xagent?"),
 (2, "core-concepts", "Core Concepts"),
 (2, "key-features", "Key Features"),
 (2, "quick-links", "Quick Links"),
])

# ===========================================================================
# Getting Started
# ===========================================================================
PAGES["getting-started/quickstart.html"] = ("Quickstart", '''<h1 id="quickstart">Quickstart</h1>
<p>Get Xagent running and create your first agent in a few minutes.</p>
<h2 id="1-run-xagent">1. Run Xagent</h2>
<p>The fastest way to start is with Docker. Clone the repository, copy the example environment file, and bring the stack up:</p>
''' + c('''git clone https://github.com/xorbitsai/xagent.git
cd xagent
cp example.env .env
docker compose up -d''') + '''
<p>Then open the app in your browser:</p>
''' + c("http://localhost:80") + '''
<p>For the SaaS layer (teams, billing, workspace API) use the <code>xagent-saas</code> stack instead — see <a href="../self-hosting/docker.html">Docker</a>.</p>
<h2 id="2-create-the-admin-account">2. Create the Admin Account</h2>
<p>On first startup Xagent redirects to <code>/setup</code>. Create the first administrator account there to complete initialisation. If you ever lose the admin password, reset it from the CLI:</p>
''' + c("python -m xagent.web.reset_admin_password --username &lt;admin_username&gt;") + '''
<h2 id="3-connect-a-model">3. Connect a Model</h2>
<p>Agents need at least one model. Under <strong>Models</strong>, add a provider — OpenAI, Anthropic, or a self-hosted model served by <a href="https://xinference.co">Xinference</a> — and supply the API key or endpoint. Test the connection before saving.</p>
''' + adm("tip", "Tip", "<p>Xagent integrates deeply with Xinference for open-source model serving, so you can mix hosted API models and your own GPU-backed models in the same agent.</p>") + '''
<h2 id="4-create-an-agent">4. Create an Agent</h2>
<p>Go to <strong>Agents → New Agent</strong>. Give it a name and instructions describing the outcome you want, pick an execution mode, and optionally attach <a href="../knowledge-bases/overview.html">knowledge bases</a>, <a href="../tools/overview.html">tools</a>, and skills. Or start from a <a href="../agents/templates.html">template</a> for common marketing, sales, and support use cases.</p>
<h2 id="5-run-a-task">5. Run a Task</h2>
<p>Open the agent and describe a task in the chat box. Xagent plans, executes, and streams progress step by step. When it finishes, the result — a report, deck, file, or answer — appears in the task output.</p>
''' + adm("info", "Note", '<p>You can also create agents and run tasks programmatically. See the <a href="../workspace-api/overview.html">Workspace API</a>.</p>') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./authentication.html">Authentication →</a> — sign-in, SSO, and API keys</li>
<li><a href="../agents/building-agents.html">Building Agents →</a> — instructions, modes, and tools</li>
<li><a href="../billing/overview.html">Billing →</a> — plans and usage</li>
</ul>''', [
 (2, "1-run-xagent", "1. Run Xagent"),
 (2, "2-create-the-admin-account", "2. Create the Admin Account"),
 (2, "3-connect-a-model", "3. Connect a Model"),
 (2, "4-create-an-agent", "4. Create an Agent"),
 (2, "5-run-a-task", "5. Run a Task"),
 (2, "next-steps", "Next Steps"),
])

PAGES["getting-started/authentication.html"] = ("Authentication", '''<h1 id="authentication">Authentication</h1>
<p>Xagent supports interactive sign-in for the web app and API keys for programmatic access.</p>
<h2 id="sign-in">Sign In</h2>
<p>Users authenticate with email and password, or via Google single sign-on (OIDC). The first time the instance starts, an administrator account is created at <code>/setup</code>; afterwards, whether open registration is allowed is controlled by the deployment.</p>
<p><strong>Log in:</strong></p>
''' + c('''POST /api/auth/login
GET  /api/auth/me
POST /api/auth/refresh
POST /api/auth/change-password''') + '''
<p>A successful login returns a JWT access token plus a refresh token. Send the access token as a bearer header on subsequent requests:</p>
''' + c('Authorization: Bearer &lt;access_token&gt;') + '''
<h2 id="google-sso">Google SSO</h2>
<p>If Google OIDC is configured, users can sign in without a password:</p>
''' + c('''GET /api/auth/google/login
GET /api/auth/google/callback''') + '''
<h2 id="personal-api-keys">Personal API Keys</h2>
<p>For scripting against your own account, mint a personal API key. The full key is shown once at creation — store it securely.</p>
''' + c('''POST   /api/me/personal-keys      # create a key
GET    /api/me/personal-keys      # list key metadata
DELETE /api/me/personal-keys/{key_id}''') + '''
<h2 id="workspace-and-runtime-keys">Workspace &amp; Runtime Keys</h2>
<p>Programmatic access to the <a href="../workspace-api/overview.html">Workspace API</a> uses two key types:</p>
<table>
<thead><tr><th>Key</th><th>Scope</th></tr></thead>
<tbody>
<tr><td><strong>Workspace key</strong></td><td>Team-scoped. Manages agents and templates across a workspace.</td></tr>
<tr><td><strong>Runtime key</strong></td><td>Agent-scoped. Runs tasks for a single agent. Generated when you create an agent or call its <code>api-key</code> endpoint.</td></tr>
</tbody>
</table>
''' + adm("warning", "Keep keys secret", "<p>API keys grant access to your agents and usage. Never commit them to source control or expose them in client-side code. Revoke and rotate any key you suspect is compromised.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./teams.html">Teams &amp; Workspaces →</a> — organise users and share access</li>
<li><a href="../workspace-api/overview.html">Workspace API →</a> — authenticate the SDK</li>
</ul>''', [
 (2, "sign-in", "Sign In"),
 (2, "google-sso", "Google SSO"),
 (2, "personal-api-keys", "Personal API Keys"),
 (2, "workspace-and-runtime-keys", "Workspace & Runtime Keys"),
 (2, "next-steps", "Next Steps"),
])

PAGES["getting-started/teams.html"] = ("Teams & Workspaces", '''<h1 id="teams-and-workspaces">Teams &amp; Workspaces</h1>
<p>Xagent is tenant-aware. A <strong>team</strong> is a workspace that groups users, shares a subscription plan and billing account, and scopes which tools are available. Agents, knowledge bases, and tasks live inside a team.</p>
<h2 id="how-teams-work">How Teams Work</h2>
<ul>
<li>Every user belongs to a team. New sign-ups get a personal team by default.</li>
<li>A team shares one <a href="../billing/plans.html">plan</a> — Free, Starter, or Business — which sets quota limits.</li>
<li>Team owners and admins invite members and assign <a href="../teams/members.html">roles</a>.</li>
<li>Available <a href="../tools/overview.html">tools</a> can be enabled or disabled per team.</li>
</ul>
<h2 id="create-a-team">Create a Team</h2>
<p>From the web app, open <strong>Teams → New Team</strong>, or use the API:</p>
''' + c('''POST /api/teams            # create a team
GET  /api/teams            # list your teams
GET  /api/teams/my-team    # the current workspace''') + '''
<h2 id="invite-members">Invite Members</h2>
<p>Invite teammates by email; they receive an invitation they can accept to join the workspace. See <a href="../teams/invitations.html">Invitations</a> for the full flow.</p>
''' + c('''POST /api/teams/{team_id}/invitations
GET  /api/teams/{team_id}/members''') + '''
<h2 id="workspace-keys">Workspace Keys</h2>
<p>Each team can issue workspace API keys for the SDK, letting you manage agents programmatically across the whole workspace:</p>
''' + c('''POST   /api/teams/{team_id}/workspace-keys
GET    /api/teams/{team_id}/workspace-keys
DELETE /api/teams/{team_id}/workspace-keys/{key_id}''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../teams/members.html">Members &amp; Roles →</a></li>
<li><a href="../teams/invitations.html">Invitations →</a></li>
<li><a href="../billing/plans.html">Plans →</a></li>
</ul>''', [
 (2, "how-teams-work", "How Teams Work"),
 (2, "create-a-team", "Create a Team"),
 (2, "invite-members", "Invite Members"),
 (2, "workspace-keys", "Workspace Keys"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Agents
# ===========================================================================
PAGES["agents/overview.html"] = ("Agents Overview", '''<h1 id="agents-overview">Agents Overview</h1>
<p>An agent is a configured assistant that plans and executes tasks toward a goal. Unlike a workflow builder, an agent decides <em>how</em> to reach an outcome at runtime — it is not a fixed sequence of steps.</p>
<h2 id="the-execution-loop">The Execution Loop</h2>
<p>When an agent receives a task, the dynamic planning engine runs a <strong>Plan → Execute → Reflect</strong> loop:</p>
<ol>
<li><strong>Plan</strong> — decompose the goal into steps and decide what each needs</li>
<li><strong>Execute</strong> — call tools, query knowledge bases, and run skills inside the sandbox</li>
<li><strong>Reflect</strong> — evaluate results, branch on conditions, and re-plan if needed</li>
</ol>
<p>The loop continues until the goal is met or the agent reports it cannot proceed.</p>
<h2 id="what-makes-up-an-agent">What Makes Up an Agent</h2>
<table>
<thead><tr><th>Field</th><th>Description</th></tr></thead>
<tbody>
<tr><td><strong>name</strong></td><td>Display name of the agent.</td></tr>
<tr><td><strong>instructions</strong></td><td>System prompt describing the agent's role, constraints, and the outcomes it should produce.</td></tr>
<tr><td><strong>execution_mode</strong></td><td>How aggressively the agent plans and spends compute (e.g. <code>balanced</code>).</td></tr>
<tr><td><strong>models</strong></td><td>The model(s) backing planning and execution.</td></tr>
<tr><td><strong>knowledge_bases</strong></td><td>Knowledge bases the agent can retrieve from.</td></tr>
<tr><td><strong>skills</strong></td><td>Packaged capabilities the agent can recall.</td></tr>
<tr><td><strong>tool_categories</strong></td><td>Which categories of tools the agent may use.</td></tr>
<tr><td><strong>suggested_prompts</strong></td><td>Starter prompts shown to users.</td></tr>
</tbody>
</table>
<h2 id="instant-vs-planned-execution">Instant vs. Planned Execution</h2>
<p>For simple use cases — chat assistants or embedded AI features — an agent can run tool-enabled LLM calls instantly with no planning overhead. For complex goals, the full planning engine decomposes and orchestrates multiple steps. Start simple and scale up when needed.</p>
<h2 id="publishing-and-sharing">Publishing &amp; Sharing</h2>
<p>Agents can be <strong>published</strong> to make them available to others, embedded as a chat <strong>widget</strong> on allowed domains, or driven through the <a href="../workspace-api/overview.html">Workspace API</a> with a runtime key.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./building-agents.html">Building Agents →</a></li>
<li><a href="./templates.html">Templates →</a></li>
<li><a href="./workforces.html">Workforces →</a></li>
</ul>''', [
 (2, "the-execution-loop", "The Execution Loop"),
 (2, "what-makes-up-an-agent", "What Makes Up an Agent"),
 (2, "instant-vs-planned-execution", "Instant vs. Planned Execution"),
 (2, "publishing-and-sharing", "Publishing & Sharing"),
 (2, "next-steps", "Next Steps"),
])

PAGES["agents/building-agents.html"] = ("Building Agents", '''<h1 id="building-agents">Building Agents</h1>
<p>This page walks through configuring an agent for good results.</p>
<h2 id="write-clear-instructions">Write Clear Instructions</h2>
<p>Instructions are the agent's system prompt. Describe the role, the desired output format, and any constraints. Be explicit about what "done" looks like — the planner uses this to decide when the task is complete.</p>
''' + adm("tip", "Tip", "<p>Xagent can help refine a prompt. The <code>optimize-instructions</code> endpoint rewrites a draft into clearer, more actionable instructions.</p>") + '''
<h2 id="choose-an-execution-mode">Choose an Execution Mode</h2>
<p>The execution mode controls the trade-off between speed, cost, and thoroughness. A <code>balanced</code> mode suits most tasks; heavier modes plan more deeply and spend more compute on complex, multi-step goals.</p>
<h2 id="attach-knowledge-and-tools">Attach Knowledge &amp; Tools</h2>
<ul>
<li><strong>Knowledge bases</strong> ground the agent in your documents via RAG. See <a href="../knowledge-bases/overview.html">Knowledge Bases</a>.</li>
<li><strong>Tool categories</strong> determine which actions the agent can take — web access, file generation, MCP servers, and <a href="../tools/custom-apis.html">custom APIs</a>.</li>
<li><strong>Skills</strong> add packaged capabilities like presentation or report generation.</li>
</ul>
<h2 id="create-an-agent-via-api">Create an Agent via API</h2>
<p>You can create agents from the UI or programmatically:</p>
''' + c('''POST /api/agents
{
  "name": "Market Research Assistant",
  "instructions": "Produce concise competitor analysis reports.",
  "execution_mode": "balanced",
  "knowledge_bases": ["kb_market"],
  "skills": ["evidence-based-rag"],
  "tool_categories": ["web", "files"],
  "suggested_prompts": ["Summarize the top 3 competitors"]
}''') + '''
<h2 id="preview-publish-and-embed">Preview, Publish &amp; Embed</h2>
''' + c('''POST /api/agents/preview              # dry-run a configuration
POST /api/agents/{agent_id}/publish
POST /api/agents/{agent_id}/unpublish
POST /api/agents/{agent_id}/logo
POST /api/agents/{agent_id}/api-key   # mint a runtime key''') + '''
<p>Published agents can be embedded as a chat widget. Restrict where the widget runs with <code>allowed_domains</code>.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./templates.html">Templates →</a></li>
<li><a href="../workspace-api/agents.html">Managing Agents via API →</a></li>
</ul>''', [
 (2, "write-clear-instructions", "Write Clear Instructions"),
 (2, "choose-an-execution-mode", "Choose an Execution Mode"),
 (2, "attach-knowledge-and-tools", "Attach Knowledge & Tools"),
 (2, "create-an-agent-via-api", "Create an Agent via API"),
 (2, "preview-publish-and-embed", "Preview, Publish & Embed"),
 (2, "next-steps", "Next Steps"),
])

PAGES["agents/templates.html"] = ("Templates", '''<h1 id="templates">Templates</h1>
<p>Templates are pre-built agent configurations for common business use cases. Starting from a template gives you sensible instructions, tools, and skills that you can customise.</p>
<h2 id="built-in-templates">Built-in Templates</h2>
<p>Xagent ships with templates across marketing, sales, and support:</p>
<table>
<thead><tr><th>Template</th><th>Use case</th></tr></thead>
<tbody>
<tr><td><strong>Marketing Content Agent</strong></td><td>Generate on-brand marketing copy and content.</td></tr>
<tr><td><strong>Marketing Collateral Agent</strong></td><td>Produce posters, decks, and collateral assets.</td></tr>
<tr><td><strong>LinkedIn Content Manager</strong></td><td>Plan and draft LinkedIn posts and campaigns.</td></tr>
<tr><td><strong>Sales Email Agent</strong></td><td>Draft and personalise outbound sales emails.</td></tr>
<tr><td><strong>Sales Inbound Agent</strong></td><td>Qualify and respond to inbound leads.</td></tr>
<tr><td><strong>Support Email Agent</strong></td><td>Triage and answer support email.</td></tr>
<tr><td><strong>Support AI Chatbot Agent</strong></td><td>Power a customer-facing support chatbot.</td></tr>
</tbody>
</table>
<h2 id="browse-and-use-templates">Browse &amp; Use Templates</h2>
''' + c('''GET  /api/templates                  # list templates
GET  /api/templates/{template_id}    # template detail
POST /api/templates/{template_id}/use    # create an agent from it
POST /api/templates/{template_id}/like''') + '''
<p>Creating an agent from a template copies its configuration into your workspace, where you can edit instructions, models, knowledge bases, and tools.</p>
<h2 id="from-the-workspace-api">From the Workspace API</h2>
<p>Templates are also available through the SDK so you can provision agents programmatically:</p>
''' + c('''GET  /v1/templates
GET  /v1/templates/{template_id}
POST /v1/agents/from-template''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./workforces.html">Workforces →</a></li>
<li><a href="../workspace-api/agents.html">Managing Agents →</a></li>
</ul>''', [
 (2, "built-in-templates", "Built-in Templates"),
 (2, "browse-and-use-templates", "Browse & Use Templates"),
 (2, "from-the-workspace-api", "From the Workspace API"),
 (2, "next-steps", "Next Steps"),
])

PAGES["agents/workforces.html"] = ("Workforces", '''<h1 id="workforces">Workforces</h1>
<p>A workforce is a team of agents that collaborate on a shared objective. Where a single agent decomposes and executes a task itself, a workforce coordinates several specialised agents — each handling part of the problem — under automatic orchestration.</p>
<h2 id="when-to-use-a-workforce">When to Use a Workforce</h2>
<ul>
<li>The goal spans distinct specialisations (e.g. research, drafting, and review)</li>
<li>You want agents to hand off intermediate results to one another</li>
<li>A single agent's context or toolset is too broad for one configuration</li>
</ul>
<h2 id="building-a-workforce">Building a Workforce</h2>
<p>Create a workforce, add agent members, and configure how they collaborate. You can build one from scratch, generate it from a prompt, or shape it in the visual builder.</p>
''' + c('''GET  /api/workforces                         # list
POST /api/workforces                         # create
POST /api/workforces/from-prompt             # generate from a description
GET  /api/workforces/agent-options           # selectable agents
POST /api/workforces/{workforce_id}/agents   # add a member
GET  /api/workforces/{workforce_id}/canvas   # visual layout''') + '''
<h2 id="the-builder">The Builder</h2>
<p>The builder lets you describe changes in natural language; Xagent proposes an updated workforce, which you review and apply:</p>
''' + c('''GET  /api/workforces/{workforce_id}/builder/messages
POST /api/workforces/{workforce_id}/builder/propose
POST /api/workforces/{workforce_id}/builder/apply''') + '''
<h2 id="running-a-workforce">Running a Workforce</h2>
<p>Start a run and the orchestrator assigns work to member agents, coordinates hand-offs, and aggregates the result:</p>
''' + c('POST /api/workforces/{workforce_id}/runs') + '''
<p>Like agents, workforces can be published and unpublished for reuse across the workspace.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../knowledge-bases/overview.html">Knowledge Bases →</a></li>
<li><a href="../tools/overview.html">Tools &amp; Skills →</a></li>
</ul>''', [
 (2, "when-to-use-a-workforce", "When to Use a Workforce"),
 (2, "building-a-workforce", "Building a Workforce"),
 (2, "the-builder", "The Builder"),
 (2, "running-a-workforce", "Running a Workforce"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Knowledge Bases
# ===========================================================================
PAGES["knowledge-bases/overview.html"] = ("Knowledge Bases Overview", '''<h1 id="knowledge-bases">Knowledge Bases</h1>
<p>A knowledge base lets an agent ground its answers in your own documents. Xagent ingests, chunks, embeds, and indexes content so agents can retrieve the most relevant passages at runtime — retrieval-augmented generation (RAG).</p>
<h2 id="how-it-works">How It Works</h2>
<ol>
<li><strong>Ingest</strong> — upload files or point at a cloud source. PDFs and other documents are parsed and split into chunks.</li>
<li><strong>Embed</strong> — each chunk is embedded and stored in a vector store.</li>
<li><strong>Retrieve</strong> — at query time the agent searches for the chunks most relevant to the task.</li>
<li><strong>Ground</strong> — retrieved passages are fed to the model, with citations back to the source.</li>
</ol>
<h2 id="ingesting-documents">Ingesting Documents</h2>
<p>Add content from local uploads or a cloud bucket:</p>
''' + c('''POST /api/kb/ingest          # ingest uploaded documents
POST /api/kb/ingest-cloud    # ingest from a cloud source''') + '''
<p>Ingestion returns a result per document so you can track which succeeded and which need attention.</p>
<h2 id="evidence-based-rag">Evidence-Based RAG</h2>
<p>The built-in <strong>evidence-based-rag</strong> skill makes agents cite the passages they relied on, so answers stay traceable to the source material. Attach it to an agent alongside one or more knowledge bases.</p>
''' + adm("tip", "Grounding agents", '<p>Attach a knowledge base to an agent in its configuration (<code>knowledge_bases</code>). The agent will automatically retrieve from it during planning and execution.</p>') + '''
<h2 id="managing-knowledge-bases">Managing Knowledge Bases</h2>
<p>Knowledge bases support search, updates, and deletion of documents through the <code>/api/kb</code> endpoints. Content is scoped to your <a href="../getting-started/teams.html">team</a>.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../agents/building-agents.html">Building Agents →</a></li>
<li><a href="../tools/overview.html">Tools &amp; Skills →</a></li>
</ul>''', [
 (2, "how-it-works", "How It Works"),
 (2, "ingesting-documents", "Ingesting Documents"),
 (2, "evidence-based-rag", "Evidence-Based RAG"),
 (2, "managing-knowledge-bases", "Managing Knowledge Bases"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Tools & Skills
# ===========================================================================
PAGES["tools/overview.html"] = ("Tools & Skills Overview", '''<h1 id="tools-and-skills">Tools &amp; Skills</h1>
<p>Tools and skills are how agents <em>act</em>. Tools give an agent the ability to take actions — search the web, generate files, call external services. Skills package higher-level capabilities the agent can recall when relevant.</p>
<h2 id="tools">Tools</h2>
<p>Tools are grouped into categories. When you build an agent you grant it specific <code>tool_categories</code>, and the planner chooses which tool to invoke at each step. Tools can be enabled or disabled per <a href="../getting-started/teams.html">team</a>.</p>
''' + c('''GET /api/tools                                 # list tools
GET /api/teams/{team_id}/tools                 # team tool config
GET /api/teams/{team_id}/tools/available
PUT /api/teams/{team_id}/tools/{tool_name}/enabled''') + '''
<h2 id="skills">Skills</h2>
<p>Skills are reusable, packaged capabilities. Xagent ships with a library of built-in skills:</p>
<table>
<thead><tr><th>Skill</th><th>What it does</th></tr></thead>
<tbody>
<tr><td><strong>agent-builder</strong></td><td>Helps design and configure new agents.</td></tr>
<tr><td><strong>evidence-based-rag</strong></td><td>Retrieval with citations back to source documents.</td></tr>
<tr><td><strong>presentation-generator</strong></td><td>Builds slide presentations.</td></tr>
<tr><td><strong>pptx-editorial</strong> / <strong>html-deck-editorial</strong></td><td>Editorial-quality decks in PPTX or HTML.</td></tr>
<tr><td><strong>pdf-report-editorial</strong></td><td>Long-form, formatted PDF reports.</td></tr>
<tr><td><strong>xlsx-financial-report</strong></td><td>Structured financial spreadsheets.</td></tr>
<tr><td><strong>poster-design</strong></td><td>Marketing posters and visual assets.</td></tr>
</tbody>
</table>
''' + c('''GET  /api/skills                 # list skills
GET  /api/skills/{skill_name}    # skill detail
POST /api/skills/recall          # recall a skill for a task
POST /api/skills/reload''') + '''
<h2 id="extending-the-toolset">Extending the Toolset</h2>
<p>Beyond the built-ins you can connect external capabilities:</p>
<ul>
<li><a href="./mcp.html">MCP Servers →</a> — connect Model Context Protocol servers</li>
<li><a href="./custom-apis.html">Custom APIs →</a> — register your own HTTP APIs as tools</li>
</ul>''', [
 (2, "tools", "Tools"),
 (2, "skills", "Skills"),
 (2, "extending-the-toolset", "Extending the Toolset"),
])

PAGES["tools/mcp.html"] = ("MCP Servers", '''<h1 id="mcp-servers">MCP Servers</h1>
<p>Xagent supports the <strong>Model Context Protocol (MCP)</strong>, an open standard for exposing tools and data to AI agents. Connecting an MCP server gives your agents a whole set of new actions without writing custom integration code.</p>
<h2 id="what-is-mcp">What is MCP?</h2>
<p>An MCP server advertises a set of tools (and optionally resources) over a standard protocol. Xagent acts as an MCP client: once a server is registered, its tools become available to agents just like built-in tools.</p>
<h2 id="registering-a-server">Registering a Server</h2>
<p>Register and manage MCP servers through the MCP management API:</p>
''' + c('GET /api/mcp    # manage MCP server connections') + '''
<p>Xagent also maintains a registry of built-in MCP integrations that can be enabled per workspace. Administrators can curate which servers are available.</p>
''' + adm("info", "Per-team availability", '<p>Like other tools, MCP-provided tools respect <a href="../getting-started/teams.html">team</a> configuration, so you can control which workspaces may use a given server.</p>') + '''
<h2 id="using-mcp-tools-in-agents">Using MCP Tools in Agents</h2>
<p>Once a server is connected, grant the relevant tool category to an agent. The planner will select MCP tools when they fit the task, the same way it selects native tools.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./custom-apis.html">Custom APIs →</a></li>
<li><a href="../agents/building-agents.html">Building Agents →</a></li>
</ul>''', [
 (2, "what-is-mcp", "What is MCP?"),
 (2, "registering-a-server", "Registering a Server"),
 (2, "using-mcp-tools-in-agents", "Using MCP Tools in Agents"),
 (2, "next-steps", "Next Steps"),
])

PAGES["tools/custom-apis.html"] = ("Custom APIs", '''<h1 id="custom-apis">Custom APIs</h1>
<p>Custom APIs let you turn any HTTP endpoint into a tool an agent can call. This is the bridge between Xagent and your internal systems — CRMs, databases behind a service, internal automation, or third-party APIs.</p>
<h2 id="registering-a-custom-api">Registering a Custom API</h2>
<p>Describe the endpoint — its URL, method, parameters, and authentication — and Xagent exposes it as a callable tool:</p>
''' + c('GET /api/custom-apis    # manage custom API tools') + '''
<p>Each registered API becomes available to agents that are granted the matching tool category. The planner decides when to call it and supplies the arguments based on the task.</p>
<h2 id="authentication">Authentication</h2>
<p>Custom APIs can carry their own credentials (such as a bearer token or API key header) so the agent authenticates to your service without exposing secrets in prompts.</p>
''' + adm("warning", "Trust boundary", "<p>A custom API gives agents the ability to call your services. Scope each registration to the minimum it needs, and prefer read-only endpoints unless write access is required.</p>") + '''
<h2 id="when-to-use-custom-apis-vs-mcp">Custom APIs vs. MCP</h2>
<ul>
<li>Use a <strong>custom API</strong> for a single endpoint you control and want to expose quickly.</li>
<li>Use an <a href="./mcp.html"><strong>MCP server</strong></a> when a richer set of tools and resources is already packaged behind the protocol.</li>
</ul>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../agents/building-agents.html">Building Agents →</a></li>
<li><a href="../workspace-api/overview.html">Workspace API →</a></li>
</ul>''', [
 (2, "registering-a-custom-api", "Registering a Custom API"),
 (2, "authentication", "Authentication"),
 (2, "when-to-use-custom-apis-vs-mcp", "Custom APIs vs. MCP"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Workspace API
# ===========================================================================
PAGES["workspace-api/overview.html"] = ("Workspace API Overview", '''<h1 id="workspace-api">Workspace API</h1>
<p>The Workspace API is the programmatic SDK surface for Xagent. Use it to create and manage agents, provision them from templates, and run tasks — all without the web UI. It lives under the <code>/v1</code> prefix and is designed for stable, versioned integration.</p>
<h2 id="authentication">Authentication</h2>
<p>Requests authenticate with one of two keys (see <a href="../getting-started/authentication.html">Authentication</a>):</p>
<table>
<thead><tr><th>Key</th><th>Use it to</th></tr></thead>
<tbody>
<tr><td><strong>Workspace key</strong></td><td>Manage agents and templates across a team workspace.</td></tr>
<tr><td><strong>Runtime key</strong></td><td>Run tasks for a single agent.</td></tr>
</tbody>
</table>
<p>Send the key as a bearer token:</p>
''' + c('Authorization: Bearer &lt;workspace_or_runtime_key&gt;') + '''
<h2 id="endpoints-at-a-glance">Endpoints at a Glance</h2>
''' + c('''GET  /v1/me                       # identity behind the key
GET  /v1/agents                   # list agents
POST /v1/agents                   # create an agent
POST /v1/agents/from-template     # create from a template
POST /v1/agents/{agent_id}/api-key    # mint a runtime key
GET  /v1/templates                # list templates
POST /v1/chat/tasks               # run a task''') + '''
<h2 id="typical-flow">Typical Flow</h2>
<ol>
<li>Create an agent with a <strong>workspace key</strong> (or from a template), requesting a runtime key.</li>
<li>Use the returned <strong>runtime key</strong> to create tasks for that agent.</li>
<li>Poll the task for status, steps, files, and output.</li>
</ol>
''' + adm("info", "Versioning", "<p>The Workspace API is versioned under <code>/v1</code>. Breaking changes ship under a new version prefix so existing integrations keep working.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./agents.html">Managing Agents →</a></li>
<li><a href="./tasks.html">Running Tasks →</a></li>
<li><a href="../api-reference/workspace.html">Workspace SDK Reference →</a></li>
</ul>''', [
 (2, "authentication", "Authentication"),
 (2, "endpoints-at-a-glance", "Endpoints at a Glance"),
 (2, "typical-flow", "Typical Flow"),
 (2, "next-steps", "Next Steps"),
])

PAGES["workspace-api/agents.html"] = ("Managing Agents", '''<h1 id="managing-agents">Managing Agents</h1>
<p>Create, list, and provision agents programmatically with a workspace key.</p>
<h2 id="list-agents">List Agents</h2>
''' + c('GET /v1/agents') + '''
<p>Returns a summary for each agent: id, name, status, widget settings, and allowed domains.</p>
<h2 id="create-an-agent">Create an Agent</h2>
<p>Provide instructions and configuration. Set <code>generate_runtime_key</code> to receive a runtime key in the response so you can immediately run tasks.</p>
<p><strong>Request:</strong></p>
''' + c('''POST /v1/agents
{
  "name": "Research Assistant",
  "description": "Competitor analysis on demand",
  "instructions": "Produce concise, sourced competitor reports.",
  "execution_mode": "balanced",
  "knowledge_bases": [],
  "skills": ["evidence-based-rag"],
  "tool_categories": ["web", "files"],
  "suggested_prompts": ["Summarize the market"],
  "generate_runtime_key": true
}''') + '''
<p><strong>Response:</strong></p>
''' + c('''{
  "agent": {
    "id": 42,
    "name": "Research Assistant",
    "status": "active",
    "execution_mode": "balanced",
    "knowledge_bases": [],
    "skills": ["evidence-based-rag"],
    "tool_categories": ["web", "files"],
    "widget_enabled": false,
    "allowed_domains": []
  },
  "api_key": {
    "full_key": "rt-...",
    "key_prefix": "rt",
    "created_at": "2026-06-23T12:00:00Z"
  }
}''') + '''
''' + adm("warning", "Save the runtime key", "<p>The <code>full_key</code> is returned only once. Store it securely — you cannot retrieve it again later, only rotate it.</p>") + '''
<h2 id="create-from-a-template">Create from a Template</h2>
''' + c('''POST /v1/agents/from-template
{
  "template_id": "marketing-content-agent",
  "name": "My Marketing Agent",
  "generate_runtime_key": true
}''') + '''
<h2 id="rotate-a-runtime-key">Rotate a Runtime Key</h2>
''' + c('POST /v1/agents/{agent_id}/api-key') + '''
<p>Issues a fresh runtime key for the agent, invalidating the previous one.</p>
''' + adm("info", "Model ids", "<p>When you set the <code>models</code> field, known model slots must use integer model ids from your workspace's configured models.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./tasks.html">Running Tasks →</a></li>
</ul>''', [
 (2, "list-agents", "List Agents"),
 (2, "create-an-agent", "Create an Agent"),
 (2, "create-from-a-template", "Create from a Template"),
 (2, "rotate-a-runtime-key", "Rotate a Runtime Key"),
 (2, "next-steps", "Next Steps"),
])

PAGES["workspace-api/tasks.html"] = ("Running Tasks", '''<h1 id="running-tasks">Running Tasks</h1>
<p>A task is one run of an agent against a goal. Use a <strong>runtime key</strong> (scoped to a single agent) to create and track tasks.</p>
<h2 id="create-a-task">Create a Task</h2>
<p>Send the agent id and the first user message. The server validates that the message's <code>agent_id</code> matches the key.</p>
<p><strong>Request:</strong></p>
''' + c('''POST /v1/chat/tasks
{
  "agent_id": 42,
  "message": { "role": "user", "content": "Summarize the EV battery market." },
  "metadata": { "source": "sdk" }
}''') + '''
<p><strong>Response:</strong></p>
''' + c('''{
  "task_id": "task_abc123",
  "status": "running"
}''') + '''
<h2 id="track-progress">Track Progress</h2>
<p>Fetch task details and the step-by-step plan as the agent works:</p>
''' + c('''GET /v1/chat/tasks/{task_id}          # task info & status
GET /v1/chat/tasks/{task_id}/steps    # planned/executed steps''') + '''
<p>A task moves through its lifecycle from <code>running</code> to a terminal state (completed or failed). Steps reflect the Plan → Execute → Reflect loop.</p>
<h2 id="retrieve-output-and-files">Retrieve Output &amp; Files</h2>
<p>When a task finishes, collect its output and any generated files. In the full app these are available via the chat task endpoints:</p>
''' + c('''GET /api/chat/task/{task_id}
GET /api/chat/task/{task_id}/status
GET /api/chat/workspace/{task_id}/files
GET /api/chat/workspace/{task_id}/output''') + '''
''' + adm("tip", "Tip", "<p>Pass <code>metadata</code> on task creation to correlate runs with your own systems — request ids, user references, or campaign tags.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../api-reference/workspace.html">Workspace SDK Reference →</a></li>
<li><a href="../api-reference/overview.html">API Reference →</a></li>
</ul>''', [
 (2, "create-a-task", "Create a Task"),
 (2, "track-progress", "Track Progress"),
 (2, "retrieve-output-and-files", "Retrieve Output & Files"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Billing
# ===========================================================================
PAGES["billing/overview.html"] = ("Billing Overview", '''<h1 id="billing">Billing</h1>
<p>Billing in Xagent is subscription-based and powered by Stripe. Each <a href="../getting-started/teams.html">team</a> is on a plan that sets monthly quota limits. Usage is metered against those limits.</p>
<h2 id="how-billing-works">How Billing Works</h2>
<ul>
<li>A team subscribes to a <a href="./plans.html">plan</a> — Free, Starter, or Business.</li>
<li>Paid plans are billed through Stripe Checkout; manage payment methods and invoices in the Stripe customer portal.</li>
<li>Each plan caps agents, monthly executions, and API calls. See <a href="./usage.html">Usage &amp; Quotas</a>.</li>
</ul>
<h2 id="subscribing-and-upgrading">Subscribing &amp; Upgrading</h2>
<p>Start a checkout session to subscribe, open the customer portal to manage an existing subscription, or upgrade between plans:</p>
''' + c('''POST /api/billing/create-checkout-session
POST /api/billing/portal-session
POST /api/billing/upgrade-plan
GET  /api/billing/subscription''') + '''
<h2 id="webhooks">Webhooks</h2>
<p>Stripe notifies Xagent of subscription events (payments, cancellations, plan changes) via a signed webhook so the team's plan stays in sync:</p>
''' + c('POST /api/webhooks    # Stripe webhook receiver') + '''
''' + adm("info", "Self-hosting billing", '<p>Billing requires Stripe credentials. Set <code>STRIPE_SECRET_KEY</code>, <code>STRIPE_WEBHOOK_SECRET</code>, and the plan price ids — see <a href="../self-hosting/environment-variables.html">Environment Variables</a>.</p>') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./plans.html">Plans →</a></li>
<li><a href="./usage.html">Usage &amp; Quotas →</a></li>
</ul>''', [
 (2, "how-billing-works", "How Billing Works"),
 (2, "subscribing-and-upgrading", "Subscribing & Upgrading"),
 (2, "webhooks", "Webhooks"),
 (2, "next-steps", "Next Steps"),
])

PAGES["billing/plans.html"] = ("Plans", '''<h1 id="plans">Plans</h1>
<p>Xagent offers three plans. Each sets per-team limits on agents, monthly agent executions, and monthly API calls. A limit of <strong>unlimited</strong> means there is no cap on that plan.</p>
<h2 id="plan-comparison">Plan Comparison</h2>
<table>
<thead><tr><th>Plan</th><th>Max agents</th><th>Executions / month</th><th>API calls / month</th></tr></thead>
<tbody>
<tr><td><strong>Free</strong></td><td>1</td><td>10</td><td>1,000</td></tr>
<tr><td><strong>Starter</strong></td><td>5</td><td>100</td><td>10,000</td></tr>
<tr><td><strong>Business</strong></td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td></tr>
</tbody>
</table>
<h2 id="billing-periods">Billing Periods</h2>
<p>Paid plans (Starter and Business) can be billed monthly or yearly. The price ids for each interval are configured per deployment and passed to Stripe Checkout.</p>
<h2 id="choosing-a-plan">Choosing a Plan</h2>
<ul>
<li><strong>Free</strong> — evaluate Xagent with a single agent and light usage.</li>
<li><strong>Starter</strong> — small teams running several agents in production.</li>
<li><strong>Business</strong> — organisations that need unlimited agents and volume.</li>
</ul>
''' + adm("tip", "Upgrades take effect immediately", '<p>Upgrading raises your limits right away via <code>POST /api/billing/upgrade-plan</code>. Downgrades apply at the end of the current billing period.</p>') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./usage.html">Usage &amp; Quotas →</a></li>
<li><a href="./overview.html">Billing Overview →</a></li>
</ul>''', [
 (2, "plan-comparison", "Plan Comparison"),
 (2, "billing-periods", "Billing Periods"),
 (2, "choosing-a-plan", "Choosing a Plan"),
 (2, "next-steps", "Next Steps"),
])

PAGES["billing/usage.html"] = ("Usage & Quotas", '''<h1 id="usage-and-quotas">Usage &amp; Quotas</h1>
<p>Every team has quota limits set by its <a href="./plans.html">plan</a>. Xagent meters usage against those limits and enforces them as you create agents and run tasks.</p>
<h2 id="what-is-metered">What Is Metered</h2>
<table>
<thead><tr><th>Metric</th><th>Counts</th></tr></thead>
<tbody>
<tr><td><strong>Agents</strong></td><td>Number of agents in the workspace, capped by <code>max_agents</code>.</td></tr>
<tr><td><strong>Agent executions</strong></td><td>Task runs per calendar month, capped by <code>max_agent_executions_per_month</code>.</td></tr>
<tr><td><strong>API calls</strong></td><td>Workspace API requests per month, capped by <code>max_api_calls_per_month</code>.</td></tr>
</tbody>
</table>
<h2 id="checking-usage">Checking Usage</h2>
<p>Read current usage and remaining quota for your team:</p>
''' + c('GET /api/billing/usage') + '''
<h2 id="when-you-hit-a-limit">When You Hit a Limit</h2>
<p>Once a quota is reached, further actions of that type are blocked until the next monthly reset or until you upgrade. Execution and API-call counters reset at the start of each calendar month; the agent count is a standing limit.</p>
''' + adm("warning", "Plan downgrades", "<p>If you downgrade below your current agent count, existing agents keep running but you cannot create new ones until you are under the new limit.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./plans.html">Plans →</a></li>
<li><a href="../api-reference/overview.html">API Reference →</a></li>
</ul>''', [
 (2, "what-is-metered", "What Is Metered"),
 (2, "checking-usage", "Checking Usage"),
 (2, "when-you-hit-a-limit", "When You Hit a Limit"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Teams
# ===========================================================================
PAGES["teams/members.html"] = ("Members & Roles", '''<h1 id="members-and-roles">Members &amp; Roles</h1>
<p>A team is a shared workspace. Members collaborate on the same agents, knowledge bases, and tasks, and roles determine what each member can do.</p>
<h2 id="roles">Roles</h2>
<table>
<thead><tr><th>Role</th><th>Capabilities</th></tr></thead>
<tbody>
<tr><td><strong>Owner</strong></td><td>Full control: manage billing, members, tools, and delete the team.</td></tr>
<tr><td><strong>Admin</strong></td><td>Manage members and tool configuration; invite and remove users.</td></tr>
<tr><td><strong>Member</strong></td><td>Create and run agents within the workspace.</td></tr>
</tbody>
</table>
<h2 id="managing-members">Managing Members</h2>
''' + c('''GET    /api/teams/{team_id}/members
DELETE /api/teams/{team_id}/members/{user_id}''') + '''
<p>Admins and owners can list members and remove them from the workspace. Removing a member revokes their access to the team's resources.</p>
<h2 id="team-tool-configuration">Team Tool Configuration</h2>
<p>Owners and admins decide which tools are available to everyone in the team:</p>
''' + c('''GET /api/teams/{team_id}/tools
GET /api/teams/{team_id}/tools/available
PUT /api/teams/{team_id}/tools/{tool_name}/enabled''') + '''
''' + adm("info", "One workspace, shared quota", '<p>All members draw from the same <a href="../billing/plans.html">plan</a> limits. Monitor consumption on the <a href="../billing/usage.html">usage</a> page.</p>') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./invitations.html">Invitations →</a></li>
<li><a href="../billing/overview.html">Billing →</a></li>
</ul>''', [
 (2, "roles", "Roles"),
 (2, "managing-members", "Managing Members"),
 (2, "team-tool-configuration", "Team Tool Configuration"),
 (2, "next-steps", "Next Steps"),
])

PAGES["teams/invitations.html"] = ("Invitations", '''<h1 id="invitations">Invitations</h1>
<p>Invitations bring new users into a team. An owner or admin invites someone by email; the recipient accepts to join the workspace.</p>
<h2 id="sending-an-invitation">Sending an Invitation</h2>
''' + c('''POST /api/teams/{team_id}/invitations
GET  /api/teams/{team_id}/invitations''') + '''
<p>Provide the invitee's email and the role they should receive. Pending invitations are listed so you can track who has yet to accept.</p>
<h2 id="accepting-an-invitation">Accepting an Invitation</h2>
<p>The invitee sees and acts on their pending invitations through the invitations endpoint. Accepting adds them to the team with the assigned role.</p>
''' + c('GET /api/invitations    # invitations for the current user') + '''
''' + adm("tip", "Tip", "<p>Invite users at the role they need from the start. You can change a member's effective access later by removing and re-inviting, or through team administration.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./members.html">Members &amp; Roles →</a></li>
<li><a href="../getting-started/teams.html">Teams &amp; Workspaces →</a></li>
</ul>''', [
 (2, "sending-an-invitation", "Sending an Invitation"),
 (2, "accepting-an-invitation", "Accepting an Invitation"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# API Reference
# ===========================================================================
PAGES["api-reference/overview.html"] = ("API Reference Overview", '''<h1 id="api-reference">API Reference</h1>
<p>Xagent exposes two API surfaces: the <strong>application API</strong> under <code>/api</code> that powers the web app, and the versioned <strong>Workspace SDK</strong> under <code>/v1</code> for stable programmatic integration.</p>
<h2 id="base-url">Base URL</h2>
<p>All endpoints are served from your Xagent deployment. For a local install:</p>
''' + c('http://localhost:80') + '''
<h2 id="authentication">Authentication</h2>
<p>Send a bearer token — a JWT from sign-in, a personal API key, or a workspace/runtime key, depending on the surface:</p>
''' + c('Authorization: Bearer &lt;token&gt;') + '''
<h2 id="api-groups">API Groups</h2>
<table>
<thead><tr><th>Group</th><th>Prefix</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>Authentication</td><td><code>/api/auth</code></td><td>Login, SSO, refresh, password management.</td></tr>
<tr><td>Agents</td><td><code>/api/agents</code></td><td>Create, configure, publish, and key agents.</td></tr>
<tr><td>Workforces</td><td><code>/api/workforces</code></td><td>Multi-agent teams and runs.</td></tr>
<tr><td>Knowledge Bases</td><td><code>/api/kb</code></td><td>Ingest and search documents.</td></tr>
<tr><td>Tools / Skills</td><td><code>/api/tools</code>, <code>/api/skills</code></td><td>Tooling and packaged capabilities.</td></tr>
<tr><td>MCP / Custom APIs</td><td><code>/api/mcp</code>, <code>/api/custom-apis</code></td><td>External tool integrations.</td></tr>
<tr><td>Chat / Tasks</td><td><code>/api/chat</code></td><td>Create and track task runs.</td></tr>
<tr><td>Teams</td><td><code>/api/teams</code>, <code>/api/invitations</code></td><td>Workspaces, members, invitations.</td></tr>
<tr><td>Billing</td><td><code>/api/billing</code>, <code>/api/webhooks</code></td><td>Subscriptions and usage.</td></tr>
<tr><td>Workspace SDK</td><td><code>/v1</code></td><td>Versioned agent &amp; task SDK.</td></tr>
</tbody>
</table>
<h2 id="reference-pages">Reference Pages</h2>
<ul>
<li><a href="./agents.html">Agents API →</a></li>
<li><a href="./workspace.html">Workspace SDK →</a></li>
</ul>''', [
 (2, "base-url", "Base URL"),
 (2, "authentication", "Authentication"),
 (2, "api-groups", "API Groups"),
 (2, "reference-pages", "Reference Pages"),
])

PAGES["api-reference/agents.html"] = ("Agents API", '''<h1 id="agents-api">Agents API</h1>
<p>The <code>/api/agents</code> endpoints manage agents in the current workspace. Authenticate with a session token or personal API key.</p>
<h2 id="endpoints">Endpoints</h2>
''' + c('''POST   /api/agents                       # create an agent
GET    /api/agents                       # list agents
GET    /api/agents/{agent_id}            # get an agent
PUT    /api/agents/{agent_id}            # update an agent
DELETE /api/agents/{agent_id}            # delete an agent
POST   /api/agents/preview               # dry-run a configuration
POST   /api/agents/optimize-instructions # refine instructions
POST   /api/agents/{agent_id}/publish
POST   /api/agents/{agent_id}/unpublish
POST   /api/agents/{agent_id}/logo
POST   /api/agents/{agent_id}/api-key    # mint runtime key
GET    /api/agents/{agent_id}/api-key    # key metadata
DELETE /api/agents/{agent_id}/api-key    # revoke runtime key''') + '''
<h2 id="create-agent-body">Create Agent Body</h2>
<table>
<thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr></thead>
<tbody>
<tr><td>name</td><td>string</td><td>Yes</td><td>Display name.</td></tr>
<tr><td>instructions</td><td>string</td><td>No</td><td>System prompt for the agent.</td></tr>
<tr><td>execution_mode</td><td>string</td><td>No</td><td>Planning/compute mode (default <code>balanced</code>).</td></tr>
<tr><td>models</td><td>object</td><td>No</td><td>Model assignments by slot.</td></tr>
<tr><td>knowledge_bases</td><td>array</td><td>No</td><td>Knowledge bases to retrieve from.</td></tr>
<tr><td>skills</td><td>array</td><td>No</td><td>Skills the agent can recall.</td></tr>
<tr><td>tool_categories</td><td>array</td><td>No</td><td>Tool categories the agent may use.</td></tr>
<tr><td>suggested_prompts</td><td>array</td><td>No</td><td>Starter prompts shown to users.</td></tr>
</tbody>
</table>
<h2 id="example">Example</h2>
''' + c('''curl -X POST http://localhost:80/api/agents \\
  -H "Authorization: Bearer &lt;token&gt;" \\
  -H "Content-Type: application/json" \\
  -d '{"name":"Research Assistant","execution_mode":"balanced"}'
''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./workspace.html">Workspace SDK →</a></li>
</ul>''', [
 (2, "endpoints", "Endpoints"),
 (2, "create-agent-body", "Create Agent Body"),
 (2, "example", "Example"),
 (2, "next-steps", "Next Steps"),
])

PAGES["api-reference/workspace.html"] = ("Workspace SDK", '''<h1 id="workspace-sdk">Workspace SDK</h1>
<p>The versioned SDK under <code>/v1</code> is the stable surface for programmatic integration. Authenticate with a <strong>workspace key</strong> (manage agents) or a <strong>runtime key</strong> (run tasks).</p>
<h2 id="identity">Identity</h2>
''' + c('GET /v1/me    # the principal behind the key') + '''
<h2 id="agents">Agents</h2>
''' + c('''GET  /v1/agents
POST /v1/agents
POST /v1/agents/from-template
POST /v1/agents/{agent_id}/api-key''') + '''
<h2 id="templates">Templates</h2>
''' + c('''GET /v1/templates
GET /v1/templates/{template_id}''') + '''
<h2 id="tasks">Tasks</h2>
''' + c('''POST /v1/chat/tasks
GET  /v1/chat/tasks/{task_id}
GET  /v1/chat/tasks/{task_id}/steps''') + '''
<h2 id="create-task-body">Create Task Body</h2>
<table>
<thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr></thead>
<tbody>
<tr><td>agent_id</td><td>integer</td><td>Yes</td><td>Agent to run. Must match the runtime key.</td></tr>
<tr><td>message</td><td>object</td><td>Yes</td><td>First user message: <code>{ "role": "user", "content": "..." }</code>.</td></tr>
<tr><td>metadata</td><td>object</td><td>No</td><td>Arbitrary key/value pairs for correlation.</td></tr>
</tbody>
</table>
<h2 id="errors">Errors</h2>
<p>The SDK returns structured errors with a code and HTTP status — for example <code>INVALID_INPUT</code> (400) for a bad configuration or <code>INTERNAL_ERROR</code> (500) for server failures.</p>
''' + c('''{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Agent with this name already exists."
  }
}''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../workspace-api/overview.html">Workspace API Guide →</a></li>
</ul>''', [
 (2, "identity", "Identity"),
 (2, "agents", "Agents"),
 (2, "templates", "Templates"),
 (2, "tasks", "Tasks"),
 (2, "create-task-body", "Create Task Body"),
 (2, "errors", "Errors"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Self-Hosting
# ===========================================================================
PAGES["self-hosting/overview.html"] = ("Self-Hosting Overview", '''<h1 id="self-hosting">Self-Hosting</h1>
<p>Xagent is built to run on your own infrastructure. You control the models, the data, and where everything runs — local, private cloud, or on-premise.</p>
<h2 id="deployment-options">Deployment Options</h2>
<ul>
<li><strong>Local</strong> — Docker Compose on a single machine for development or small teams.</li>
<li><strong>Private cloud</strong> — your VPC, behind your own networking and identity.</li>
<li><strong>On-premise</strong> — fully air-gapped enterprise infrastructure.</li>
</ul>
<h2 id="architecture">Architecture</h2>
<p>A deployment is composed of the application backend, a frontend, a database, the agent execution sandbox, and (optionally) the SaaS layer for teams and billing. A reverse proxy (Caddy) fronts the services.</p>
<table>
<thead><tr><th>Layer</th><th>Responsibility</th></tr></thead>
<tbody>
<tr><td>Agent definition</td><td>Intent &amp; constraints</td></tr>
<tr><td>Planning engine</td><td>Dynamic decomposition</td></tr>
<tr><td>Execution runtime</td><td>Orchestration &amp; sandboxing</td></tr>
<tr><td>Tool layer</td><td>Integrations &amp; actions</td></tr>
<tr><td>Model layer</td><td>LLM &amp; inference backend</td></tr>
</tbody>
</table>
<h2 id="security">Security</h2>
<p>Agent code executes inside a VM-level sandbox isolated from the host, so untrusted, model-generated actions cannot reach your infrastructure directly.</p>
''' + adm("info", "Models", '<p>Bring your own model providers — OpenAI, Anthropic — or serve open-source models with <a href="https://xinference.co">Xinference</a> for full control over inference.</p>') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./docker.html">Docker →</a></li>
<li><a href="./environment-variables.html">Environment Variables →</a></li>
</ul>''', [
 (2, "deployment-options", "Deployment Options"),
 (2, "architecture", "Architecture"),
 (2, "security", "Security"),
 (2, "next-steps", "Next Steps"),
])

PAGES["self-hosting/docker.html"] = ("Docker", '''<h1 id="docker">Docker</h1>
<p>Docker Compose is the recommended way to run Xagent. The stack bundles the backend, frontend, database, sandbox, and reverse proxy.</p>
<h2 id="prerequisites">Prerequisites</h2>
<ul>
<li>Docker and Docker Compose</li>
<li>At least one model provider key or a reachable Xinference endpoint</li>
</ul>
<h2 id="start-the-stack">Start the Stack</h2>
''' + c('''git clone https://github.com/xorbitsai/xagent.git
cd xagent
cp example.env .env
docker compose up -d''') + '''
<p>Then open <code>http://localhost:80</code>. On first run you are redirected to <code>/setup</code> to create the administrator account.</p>
<h2 id="the-saas-stack">The SaaS Stack</h2>
<p>To run the multi-tenant layer (teams, billing, the Workspace API), use the <code>xagent-saas</code> compose file, which wraps the core <code>xagent</code> service and adds the SaaS backend and frontend overlay:</p>
''' + c('''cp .env.example .env   # add your Stripe keys
docker compose up -d''') + '''
<h2 id="reset-the-admin-password">Reset the Admin Password</h2>
''' + c('python -m xagent.web.reset_admin_password --username &lt;admin_username&gt;') + '''
<h2 id="reverse-proxy">Reverse Proxy</h2>
<p>A Caddy reverse proxy routes traffic to the backend and frontend and can terminate TLS. Point your domain at the host and configure Caddy for automatic HTTPS in production.</p>
''' + adm("warning", "Production checklist", "<p>Before exposing Xagent publicly: set strong secrets, enable HTTPS, restrict registration, and configure backups for the database volume.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./environment-variables.html">Environment Variables →</a></li>
</ul>''', [
 (2, "prerequisites", "Prerequisites"),
 (2, "start-the-stack", "Start the Stack"),
 (2, "the-saas-stack", "The SaaS Stack"),
 (2, "reset-the-admin-password", "Reset the Admin Password"),
 (2, "reverse-proxy", "Reverse Proxy"),
 (2, "next-steps", "Next Steps"),
])

PAGES["self-hosting/environment-variables.html"] = ("Environment Variables", '''<h1 id="environment-variables">Environment Variables</h1>
<p>Xagent is configured through environment variables, typically in a <code>.env</code> file. The SaaS layer inherits all core <code>xagent</code> variables and adds billing configuration on top.</p>
<h2 id="core-configuration">Core Configuration</h2>
<p>Copy the example and adjust values for your environment:</p>
''' + c('''cp example.env .env''') + '''
<p>Core variables cover the database connection, model provider credentials, authentication secrets, and the sandbox. See <code>example.env</code> in the <code>xagent</code> repository for the full list.</p>
<h2 id="billing-configuration">Billing (SaaS)</h2>
<p>The SaaS layer needs Stripe credentials and the price ids for each paid plan and interval:</p>
''' + c('''STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxxxxxxxxx
STRIPE_PRICE_STARTER_MONTHLY=
STRIPE_PRICE_STARTER_YEARLY=
STRIPE_PRICE_BUSINESS_MONTHLY=
STRIPE_PRICE_BUSINESS_YEARLY=''') + '''
<p>Plan price ids are referenced from <code>plans.yaml</code> using <code>${ENV_VAR}</code> syntax, so the same configuration works across staging and production by swapping the environment.</p>
''' + adm("tip", "Secrets management", "<p>Keep <code>.env</code> out of source control. In production, inject secrets through your orchestrator's secret store rather than a file on disk.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./docker.html">Docker →</a></li>
<li><a href="../billing/overview.html">Billing →</a></li>
</ul>''', [
 (2, "core-configuration", "Core Configuration"),
 (2, "billing-configuration", "Billing (SaaS)"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Models
# ===========================================================================
PAGES["models/overview.html"] = ("Models Overview", '''<h1 id="models-overview">Models Overview</h1>
<p>Xagent supports multiple types of AI models, each serving a different purpose in task execution. You connect providers under <strong>Models</strong>, then assign models to roles and set defaults.</p>
<h2 id="model-types">Model Types</h2>
<p>Internally each model is bound to a configuration role (<code>config_type</code>): <code>general</code>, <code>small_fast</code>, <code>compact</code>, <code>visual</code>, or <code>embedding</code>.</p>
<table>
<thead><tr><th>Role</th><th>config_type</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td><strong>Main Model</strong></td><td><code>general</code></td><td>Required. Powers planning, reasoning, and decision-making for all task execution.</td></tr>
<tr><td><strong>Fast Model</strong></td><td><code>small_fast</code></td><td>Optional. Used for steps the planner marks as simple — lowers cost and improves speed.</td></tr>
<tr><td><strong>Long Context Model</strong></td><td><code>compact</code></td><td>Optional. Compresses conversation history when it exceeds the token threshold (default 32,000).</td></tr>
<tr><td><strong>Vision Model</strong></td><td><code>visual</code></td><td>Optional. Required for image-understanding tools (<code>understand_images</code>, <code>describe_images</code>, <code>detect_objects</code>).</td></tr>
<tr><td><strong>Embedding Model</strong></td><td><code>embedding</code></td><td>Converts text to vectors for knowledge base search and RAG.</td></tr>
</tbody>
</table>
<h2 id="model-sharing">Model Sharing</h2>
<p>Admins can configure which models are available to other users, set permissions, and monitor usage. Regular users access the shared models directly without managing their own API keys.</p>
''' + adm("info", "Admin configured", "<p>Model sharing is set up by admin users in the Models settings. Regular users can only access shared models.</p>") + '''
<h2 id="configuration">Configuration</h2>
<ol>
<li><strong>Add a provider</strong> — OpenAI &amp; OpenAI-compatible, Anthropic, Google, Xinference, or a custom endpoint.</li>
<li><strong>Configure models</strong> — select the model, enter credentials, set parameters, and test the connection.</li>
<li><strong>Set defaults</strong> — choose default models globally, per task, or per agent.</li>
</ol>
<h2 id="requirements">Requirements</h2>
<ul>
<li><strong>Required:</strong> at least one LLM as the Main model (Claude 4.6 Sonnet or higher recommended).</li>
<li><strong>Knowledge Base:</strong> an embedding model.</li>
<li><strong>Image analysis:</strong> a vision model.</li>
<li><strong>Cost optimization:</strong> a fast model.</li>
<li><strong>Long conversations:</strong> a long-context model.</li>
</ul>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./llm.html">LLM Models →</a></li>
<li><a href="./embedding.html">Embedding Models →</a></li>
<li><a href="./image-generation.html">Image Generation Models →</a></li>
</ul>''', [
 (2, "model-types", "Model Types"),
 (2, "model-sharing", "Model Sharing"),
 (2, "configuration", "Configuration"),
 (2, "requirements", "Requirements"),
 (2, "next-steps", "Next Steps"),
])

PAGES["models/llm.html"] = ("LLM Models", '''<h1 id="llm-models">LLM Models</h1>
<p>Large Language Models are the core intelligence behind Xagent, handling reasoning, planning, and text generation. Different LLM roles can be filled by different models.</p>
<h2 id="llm-roles">LLM Roles</h2>
<h3 id="main-model">Main Model</h3>
<p>The primary LLM used for all task execution by default — planning, decomposition, tool selection, and decision-making. Required.</p>
<p>Recommended: Claude 4.6 Sonnet (balanced), Claude 4.6 Opus (complex tasks), GPT 5.2, Gemini 3 Pro.</p>
<h3 id="fast-model">Fast Model (Optional)</h3>
<p>A lightweight LLM used for steps the planner identifies as simple. If not configured, the main model handles every step. Automatic routing requires no manual intervention and reduces cost and latency for routine operations.</p>
<h3 id="long-context-model">Long Context Model (Compact)</h3>
<p>Compresses conversation history when it exceeds the compact threshold, preserving the original goal, key information, and critical context so long-running tasks do not hit context limits.</p>
<table>
<thead><tr><th>Option</th><th>Description</th></tr></thead>
<tbody>
<tr><td><strong>Threshold</strong></td><td>Token limit that triggers compaction (default 32,000). Adjustable per task or agent.</td></tr>
<tr><td><strong>Fallback</strong></td><td>If compaction fails, Xagent truncates to recent messages while keeping system messages.</td></tr>
</tbody>
</table>
<h3 id="vision-optional">Vision Model (Optional)</h3>
<p>A multimodal LLM that analyses images alongside text. Enables the image tools <code>understand_images</code>, <code>describe_images</code>, and <code>detect_objects</code> for screenshot interpretation, OCR, and chart analysis.</p>
<h2 id="model-parameters">Model Parameters</h2>
<table>
<thead><tr><th>Parameter</th><th>Range</th><th>Guidance</th></tr></thead>
<tbody>
<tr><td><strong>Temperature</strong></td><td>0.0 – 2.0</td><td>0.0–0.3 deterministic; 0.4–0.7 balanced; 0.8+ creative. Main model 0.3–0.5.</td></tr>
<tr><td><strong>Max Tokens</strong></td><td>—</td><td>Maximum response length. Balance detail against token cost.</td></tr>
<tr><td><strong>Top P</strong></td><td>0.0 – 1.0</td><td>Alternative to temperature; lower is more focused.</td></tr>
</tbody>
</table>
<h2 id="supported-providers">Supported Providers</h2>
<table>
<thead><tr><th>Provider</th><th>Models</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><strong>OpenAI</strong> &amp; compatible</td><td>GPT 5.x</td><td>General-purpose, wide ecosystem.</td></tr>
<tr><td><strong>Anthropic</strong></td><td>Claude 4.6 (Opus, Sonnet, Haiku)</td><td>Complex reasoning, long context.</td></tr>
<tr><td><strong>Google</strong></td><td>Gemini 3 Pro</td><td>Large context windows, multimodal.</td></tr>
<tr><td><strong>Xinference</strong></td><td>Open-source LLMs (Llama, Mistral, Qwen)</td><td>Privacy, cost control, self-hosting.</td></tr>
</tbody>
</table>
''' + adm("info", "Credentials", "<p>For OpenAI, Anthropic, and Google, just enter the API key. A Base URL is only needed for OpenAI-compatible services or self-hosted models (e.g. Xinference).</p>") + '''
<h2 id="adding-an-llm">Adding an LLM</h2>
<ol>
<li>Go to <strong>Models</strong> in the sidebar and add a provider.</li>
<li>Enter the API key (and Base URL for compatible/self-hosted endpoints).</li>
<li>Xagent fetches available models — pick one and assign its role.</li>
<li>Configure parameters, test the connection, and set as default.</li>
</ol>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./embedding.html">Embedding Models →</a></li>
<li><a href="./image-generation.html">Image Generation Models →</a></li>
<li><a href="../agents/building-agents.html">Building Agents →</a></li>
</ul>''', [
 (2, "llm-roles", "LLM Roles"),
 (2, "model-parameters", "Model Parameters"),
 (2, "supported-providers", "Supported Providers"),
 (2, "adding-an-llm", "Adding an LLM"),
 (2, "next-steps", "Next Steps"),
])

PAGES["models/embedding.html"] = ("Embedding Models", '''<h1 id="embedding-models">Embedding Models</h1>
<p>Embedding models convert text into vector representations, enabling semantic search and knowledge base operations. Similar concepts produce similar vectors, which is what powers retrieval-augmented generation (RAG).</p>
<h2 id="how-embeddings-work">How Embeddings Work</h2>
<ol>
<li>Documents are chunked and converted to embeddings.</li>
<li>Embeddings are stored in a vector database.</li>
<li>When a task queries the knowledge base, Xagent searches for similar embeddings.</li>
<li>Retrieved content is provided as context to the LLM.</li>
</ol>
<h2 id="when-to-configure">When to Configure</h2>
<p>An embedding model is <strong>required</strong> for knowledge base functionality — uploading and searching documents, building RAG systems, and semantic retrieval.</p>
<h2 id="supported-providers">Supported Providers</h2>
<table>
<thead><tr><th>Provider</th><th>Models</th><th>Best for</th></tr></thead>
<tbody>
<tr><td><strong>OpenAI</strong> &amp; compatible</td><td>text-embedding-3-small / -large, text-embedding-ada-002</td><td>General-purpose embeddings.</td></tr>
<tr><td><strong>DashScope</strong> (Alibaba Cloud)</td><td>text-embedding-v4 / v3 / v2</td><td>Chinese / Asian-language optimization.</td></tr>
<tr><td><strong>Xinference</strong></td><td>bge-large-en-v1.5, bge-base-en, all-MiniLM-L6-v2, other HuggingFace models</td><td>Privacy and self-hosting.</td></tr>
</tbody>
</table>
''' + adm("info", "HuggingFace models", "<p>To use HuggingFace embedding models, deploy them via Xinference and point Xagent at the Xinference Base URL.</p>") + '''
<h2 id="parameters">Parameters</h2>
<table>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td><strong>Dimensions</strong></td><td>Vector size. Lower (384–768) is faster and cheaper; higher (3072+) improves accuracy at more storage cost.</td></tr>
<tr><td><strong>Chunk size</strong></td><td>Tokens per chunk when indexing (typically 512–1000). Smaller chunks are more precise; larger chunks carry more context.</td></tr>
</tbody>
</table>
<h2 id="best-practices">Best Practices</h2>
<ul>
<li>General use: OpenAI <code>text-embedding-3-small</code> — good cost/performance.</li>
<li>Highest quality: <code>text-embedding-3-large</code> or <code>bge-large-en-v1.5</code>.</li>
<li>Match chunk size to typical query length and use overlap to preserve context.</li>
</ul>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="../knowledge-bases/overview.html">Knowledge Bases →</a></li>
<li><a href="./llm.html">LLM Models →</a></li>
</ul>''', [
 (2, "how-embeddings-work", "How Embeddings Work"),
 (2, "when-to-configure", "When to Configure"),
 (2, "supported-providers", "Supported Providers"),
 (2, "parameters", "Parameters"),
 (2, "best-practices", "Best Practices"),
 (2, "next-steps", "Next Steps"),
])

PAGES["models/image-generation.html"] = ("Image Generation Models", '''<h1 id="image-generation-models">Image Generation Models</h1>
<p>Image generation models let Xagent create and modify images from text prompts. They power the <code>generate_image</code> and <code>edit_image</code> tools.</p>
<h2 id="generation-vs-understanding">Generation vs. Understanding</h2>
<p>Image generation models <em>create</em> images. Analysing or reading existing images (OCR, chart analysis) is handled by <a href="./llm.html#vision-optional">Vision LLMs</a>, not image generation models.</p>
<h2 id="supported-providers">Supported Providers</h2>
<table>
<thead><tr><th>Provider</th><th>Models</th><th>Abilities</th></tr></thead>
<tbody>
<tr><td><strong>OpenAI</strong> &amp; compatible</td><td>gpt-image-1 and compatible</td><td>generate + edit</td></tr>
<tr><td><strong>DashScope</strong> (Alibaba Cloud)</td><td>qwen-image</td><td>generate (can support edit)</td></tr>
<tr><td><strong>Gemini</strong> (Google)</td><td>gemini-3-pro-preview-image</td><td>generate only</td></tr>
<tr><td><strong>Xinference</strong></td><td>Stable Diffusion variants</td><td>configurable (default generate, supports edit)</td></tr>
</tbody>
</table>
''' + adm("info", "Editing support", "<p>Not every model supports editing. Gemini image models support generation only — use <code>generate_image</code>. DashScope editing accepts JPG/PNG/BMP/TIFF/WEBP up to 10MB.</p>") + '''
<h2 id="configuration">Configuration</h2>
<ol>
<li>Add an image generation provider under <strong>Models</strong> and enter credentials.</li>
<li>Configure parameters: image size (e.g. 1024×1024), response format (<code>url</code> or <code>b64_json</code>), and number of images.</li>
<li>Set the model's abilities — <strong>generate</strong>, <strong>edit</strong>, or both.</li>
</ol>
<h2 id="usage-examples">Usage Examples</h2>
''' + c('''User: "Create a promotional poster for a coffee shop"
Xagent: [uses generate_image] -> saves image to workspace

User: "Change the color scheme to warm tones"
Xagent: [uses edit_image] -> modifies existing image''') + '''
<h2 id="security-and-privacy">Security &amp; Privacy</h2>
<p>Generated images are saved to the task workspace. Review your provider's content policy and data-retention terms, and confirm you have rights to the generated content.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./llm.html">LLM &amp; Vision Models →</a></li>
<li><a href="../tools/built-in.html">Built-in Tools →</a></li>
</ul>''', [
 (2, "generation-vs-understanding", "Generation vs. Understanding"),
 (2, "supported-providers", "Supported Providers"),
 (2, "configuration", "Configuration"),
 (2, "usage-examples", "Usage Examples"),
 (2, "security-and-privacy", "Security & Privacy"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Agents (additions)
# ===========================================================================
PAGES["agents/sharing.html"] = ("Sharing Agents", '''<h1 id="sharing-agents">Sharing Agents</h1>
<p>Xagent offers two distinct ways to expose an agent beyond its owner. They solve different problems and can be used together.</p>
<h2 id="publishing-vs-share-links">Publishing vs. Share Links</h2>
<p><strong>Publishing</strong> makes an agent visible as a reusable asset to authenticated internal users. <strong>Share links</strong> create a public, token-based guest entry point for a published agent.</p>
<table>
<thead><tr><th>Capability</th><th>Published agent</th><th>Share link</th></tr></thead>
<tbody>
<tr><td>Internal reuse</td><td>Yes</td><td>No</td></tr>
<tr><td>Guest access</td><td>No</td><td>Yes</td></tr>
<tr><td>Appears in agents list</td><td>Yes</td><td>No</td></tr>
<tr><td>Public token-based entry</td><td>No</td><td>Yes</td></tr>
</tbody>
</table>
<h2 id="share-link-lifecycle">Share Link Lifecycle</h2>
<p>Owners manage share links through dedicated endpoints — get current state, enable/create, rotate the token, and disable:</p>
''' + c('''GET  /api/agents/{agent_id}/share-link
POST /api/agents/{agent_id}/share-link/enable
POST /api/agents/{agent_id}/share-link/rotate
POST /api/agents/{agent_id}/share-link/disable''') + '''
''' + adm("warning", "Treat the token like a secret", "<p>The share token is owner-only state. Anyone with the link can reach the agent as a guest — rotate it if it leaks.</p>") + '''
<h2 id="preparing-an-agent-for-sharing">Preparing an Agent for Sharing</h2>
<p>Share links are meant for agents that are ready for outside use. Before enabling one:</p>
<ul>
<li>Finalise instructions and prompts</li>
<li>Test the suggested prompts</li>
<li>Review file-handling behaviour</li>
<li>Confirm the agent should be publicly reachable</li>
</ul>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./widget-embed.html">Widget Embed →</a></li>
<li><a href="./building-agents.html">Building Agents →</a></li>
</ul>''', [
 (2, "publishing-vs-share-links", "Publishing vs. Share Links"),
 (2, "share-link-lifecycle", "Share Link Lifecycle"),
 (2, "preparing-an-agent-for-sharing", "Preparing an Agent for Sharing"),
 (2, "next-steps", "Next Steps"),
])

PAGES["agents/widget-embed.html"] = ("Widget Embed", '''<h1 id="widget-embed">Embedding Agents as Widgets</h1>
<p>Xagent can expose an agent through an embeddable chat widget for website or product integration. The widget flow is guest-oriented and runs on the public chat runtime.</p>
<h2 id="how-widgets-work">How Widgets Work</h2>
<ol>
<li>The client authenticates a guest against a specific agent.</li>
<li>It receives a guest chat token.</li>
<li>It uploads files if needed.</li>
<li>It creates a widget chat task.</li>
<li>The session continues over the public chat runtime.</li>
</ol>
''' + c('''POST /api/widget/authenticate    # issue a guest token
POST /api/widget/tasks           # create a widget chat task
POST /api/widget/files           # upload a file for the guest session''') + '''
<h2 id="agent-level-controls">Agent-Level Controls</h2>
<p>Widget access is controlled per agent, not globally, through two settings:</p>
<table>
<thead><tr><th>Field</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>widget_enabled</code></td><td>Whether the agent can be embedded as a widget.</td></tr>
<tr><td><code>allowed_domains</code></td><td>Origins permitted to load the widget.</td></tr>
</tbody>
</table>
<h2 id="domain-allowlist">Domain Allowlist</h2>
<p>The widget authentication flow validates the request origin against the agent's allowed domains. You can allow exact domains, subdomains, or <code>*</code> for unrestricted access.</p>
''' + adm("warning", "Prefer a strict allowlist", "<p>Use <code>*</code> only if you deliberately want the widget embeddable anywhere. For production, list the exact domains where the widget should run.</p>") + '''
<h2 id="recommended-setup">Recommended Setup</h2>
<ul>
<li>Use a focused prompt and keep tools narrow and predictable.</li>
<li>Add safe suggested prompts.</li>
<li>Restrict <code>allowed_domains</code>.</li>
<li>Test guest file uploads and session continuity.</li>
</ul>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./sharing.html">Sharing Agents →</a></li>
<li><a href="../workspace-api/overview.html">Workspace API →</a></li>
</ul>''', [
 (2, "how-widgets-work", "How Widgets Work"),
 (2, "agent-level-controls", "Agent-Level Controls"),
 (2, "domain-allowlist", "Domain Allowlist"),
 (2, "recommended-setup", "Recommended Setup"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Tasks
# ===========================================================================
PAGES["tasks/overview.html"] = ("Tasks Overview", '''<h1 id="tasks-overview">Tasks Overview</h1>
<p>Tasks are the fundamental unit of work in Xagent. You describe a goal in natural language and Xagent plans, executes, and delivers the result — no predefined workflow required.</p>
<h2 id="what-is-a-task">What is a Task?</h2>
<p>A task is a plain-language description of an outcome. Xagent interprets your intent and breaks it into executable steps.</p>
''' + c('''"Research the latest AI developments and write a summary"
"Create a 10-slide presentation about renewable energy"
"Design a promotional poster for a coffee shop"''') + '''
<h2 id="task-configuration">Task Configuration</h2>
<p>Before running a task you can choose the models it uses:</p>
<ul>
<li><strong>Main Model</strong> — used for all execution by default.</li>
<li><strong>Fast Model</strong> — used automatically for steps identified as simple.</li>
<li><strong>Long Context / Vision</strong> — for context compression and image tools.</li>
</ul>
<p>You can also adjust temperature, max tokens, and other parameters per task. See <a href="../models/llm.html">LLM Models</a>.</p>
<h2 id="key-features">Key Features</h2>
<ul>
<li><strong>Natural-language input</strong> — describe the goal in plain language.</li>
<li><strong>File attachments</strong> — upload documents, spreadsheets, images, or code for context. See <a href="../files/upload.html">File Upload</a>.</li>
<li><strong>Real-time execution</strong> — watch each step get planned and executed, view intermediate results, and iterate.</li>
</ul>
<h2 id="creating-a-task-via-api">Creating a Task via API</h2>
''' + c('''POST /api/chat/task/create
{
  "description": "Summarize the EV battery market",
  "files": []
}''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./execution.html">Task Execution →</a></li>
<li><a href="../workspace-api/tasks.html">Running Tasks via API →</a></li>
</ul>''', [
 (2, "what-is-a-task", "What is a Task?"),
 (2, "task-configuration", "Task Configuration"),
 (2, "key-features", "Key Features"),
 (2, "creating-a-task-via-api", "Creating a Task via API"),
 (2, "next-steps", "Next Steps"),
])

PAGES["tasks/execution.html"] = ("Task Execution", '''<h1 id="task-execution">Task Execution</h1>
<p>This page explains how Xagent plans, executes, and completes a task from start to finish.</p>
<h2 id="execution-phases">Execution Phases</h2>
<h3 id="1-planning">1. Planning Phase</h3>
<p>Xagent analyses your request, breaks the task into steps, identifies the tools needed, and generates a <strong>DAG</strong> (Directed Acyclic Graph) of the workflow.</p>
<ul>
<li><strong>Nodes</strong> — individual execution steps.</li>
<li><strong>Edges</strong> — dependencies between steps.</li>
<li><strong>Flow</strong> — execution order from start to finish.</li>
</ul>
<h3 id="2-execution">2. Execution Phase</h3>
<p>Steps run in dependency order. Tools are called automatically, results pass between steps, and progress updates in real time with step-by-step logging, error handling, retries, and dynamic adaptation.</p>
<h3 id="3-completion">3. Completion Phase</h3>
<p>Results from all steps are aggregated into a final output, an execution summary is shown, and the task is saved for reference.</p>
<h2 id="the-execution-interface">The Execution Interface</h2>
<p>While a task runs you see the agent interface with a vertical step layout:</p>
<ul>
<li><strong>Chat area</strong> — your request, real-time status, the final result, and follow-up conversation.</li>
<li><strong>Execution steps</strong> — each step shows its number and title, the agent's reasoning, inline tool calls and responses, and status indicators. Steps are expandable for detail.</li>
</ul>
<h2 id="tracking-a-task">Tracking a Task</h2>
''' + c('''GET /api/chat/task/{task_id}
GET /api/chat/task/{task_id}/status
GET /api/chat/workspace/{task_id}/files
GET /api/chat/workspace/{task_id}/output''') + '''
''' + adm("tip", "Real-time updates", "<p>Task progress is streamed over a WebSocket connection, so the interface reflects each planning and execution event as it happens.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./overview.html">Tasks Overview →</a></li>
<li><a href="../files/management.html">File Management →</a></li>
</ul>''', [
 (2, "execution-phases", "Execution Phases"),
 (2, "the-execution-interface", "The Execution Interface"),
 (2, "tracking-a-task", "Tracking a Task"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Memory
# ===========================================================================
PAGES["memory/overview.html"] = ("Memory Overview", '''<h1 id="memory-overview">Memory Overview</h1>
<p>Memory enables agents to learn from past experiences and improve over time. Instead of treating each task as isolated, agents remember what worked, what didn't, and apply those lessons to future tasks.</p>
<h2 id="what-is-memory">What is Memory?</h2>
<p>Memory stores execution results, insights, and experiences from tasks:</p>
<ul>
<li><strong>Task patterns</strong> — approaches that worked for similar tasks.</li>
<li><strong>User preferences</strong> — communication style and format preferences.</li>
<li><strong>Execution insights</strong> — successes, failures, and lessons learned.</li>
<li><strong>Best practices</strong> — effective tool combinations and strategies.</li>
</ul>
<h2 id="how-memory-works">How Memory Works</h2>
<p><strong>Storage</strong> — after a task completes, Xagent analyses the result, extracts insights, stores structured notes, and indexes them for search.</p>
<p><strong>Retrieval</strong> — when a new task starts, Xagent searches memory, selects relevant matches by similarity, enhances its understanding of the goal, and avoids past mistakes while reusing what worked.</p>
<h2 id="managing-memory">Managing Memory</h2>
''' + c('''POST   /api/memory          # create a memory
GET    /api/memory          # list memories
GET    /api/memory/{id}     # get a memory
PUT    /api/memory/{id}     # update a memory
DELETE /api/memory/{id}     # delete a memory
GET    /api/memory/stats    # memory statistics''') + '''
''' + adm("info", "Continuous learning", "<p>Memory turns isolated runs into a learning loop: pattern recognition across similar tasks, richer context for new goals, and fewer repeated mistakes.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./types.html">Memory Types →</a></li>
<li><a href="./configuration.html">Memory Configuration →</a></li>
</ul>''', [
 (2, "what-is-memory", "What is Memory?"),
 (2, "how-memory-works", "How Memory Works"),
 (2, "managing-memory", "Managing Memory"),
 (2, "next-steps", "Next Steps"),
])

PAGES["memory/types.html"] = ("Memory Types", '''<h1 id="memory-types">Memory Types</h1>
<p>Xagent organises memories into categories to make them more useful and searchable. Each category is retrieved in different situations.</p>
<h2 id="plan-execution-memory">Plan Execution Memory</h2>
<p>Insights from task planning and DAG generation — planning strategies that worked, step-decomposition approaches, tool-selection insights, and task-complexity analysis. Retrieved when starting similar tasks or planning multi-step workflows.</p>
''' + c('''"For data analysis tasks with multiple steps, generate a DAG
with parallel processing for independent calculations. Use the
Python executor for transformations."''') + '''
<h2 id="execution-memory">Execution Memory</h2>
<p>Results and learnings from task execution — outcomes (success/failure), user feedback and corrections, tool effectiveness, performance bottlenecks, and error patterns with solutions. Retrieved when encountering similar challenges or optimising performance.</p>
''' + c('''"When processing CSV files larger than 100MB, use chunked
reading with pandas. Web search API times out after 30
seconds for complex queries."''') + '''
<h2 id="react-memory">ReAct Memory</h2>
<p>Insights from the ReAct (Reasoning–Action) loop — reasoning patterns, tool-usage effectiveness, step-by-step execution insights, and iteration strategies. Retrieved when using ReAct execution mode or choosing reasoning strategies.</p>
''' + c('''"For research tasks requiring multiple sources, start with web
search to identify key sources, then use file tools to process
and synthesize findings."''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./configuration.html">Memory Configuration →</a></li>
<li><a href="./overview.html">Memory Overview →</a></li>
</ul>''', [
 (2, "plan-execution-memory", "Plan Execution Memory"),
 (2, "execution-memory", "Execution Memory"),
 (2, "react-memory", "ReAct Memory"),
 (2, "next-steps", "Next Steps"),
])

PAGES["memory/configuration.html"] = ("Memory Configuration", '''<h1 id="memory-configuration">Memory Configuration</h1>
<p>Configure how memory is stored and retrieved to balance performance, persistence, and search quality.</p>
<h2 id="in-memory-storage">In-Memory Storage</h2>
<p>Best for development, testing, and short-term tasks. Enabled by default, fast, and requires no configuration — but data is lost on restart.</p>
''' + c('''memory:
  type: "in_memory"''') + '''
<h2 id="vector-database-storage">Vector Database Storage (LanceDB)</h2>
<p>Best for production, long-term learning, and semantic search. Persists across restarts.</p>
''' + c('''memory:
  type: "lancedb"
  db_dir: "/path/to/memory/database"
  collection_name: "memories"
  embedding_model: "text-embedding-v4"   # optional
  similarity_threshold: 0.8''') + '''
<table>
<thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>db_dir</code></td><td>Required. Directory for LanceDB storage; created if missing.</td></tr>
<tr><td><code>collection_name</code></td><td>Optional (default <code>memories</code>). Agents can share or separate collections.</td></tr>
<tr><td><code>embedding_model</code></td><td>Optional. Embedding model for semantic search; falls back to configured embedding models.</td></tr>
<tr><td><code>similarity_threshold</code></td><td>Optional (default 1.0). 0.0–1.0; higher is stricter, lower retrieves more memories.</td></tr>
</tbody>
</table>
''' + adm("info", "Text fallback", "<p>If <code>embedding_model</code> is not configured, the LanceDB memory store falls back to text-based search instead of semantic similarity.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./types.html">Memory Types →</a></li>
<li><a href="../models/embedding.html">Embedding Models →</a></li>
</ul>''', [
 (2, "in-memory-storage", "In-Memory Storage"),
 (2, "vector-database-storage", "Vector Database Storage (LanceDB)"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Tools (additions)
# ===========================================================================
PAGES["tools/built-in.html"] = ("Built-in Tools", '''<h1 id="built-in-tools">Built-in Tools</h1>
<p>Xagent ships with a library of built-in tools, organised by category. The planner selects from them automatically based on the task and the categories granted to an agent.</p>
<h2 id="basic-tools">Basic Tools</h2>
<h3 id="web-search">web_search</h3>
<p>Search the internet for current information — recent news, research, current data, and fact-checking.</p>
<table>
<thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead>
<tbody>
<tr><td>query</td><td>string</td><td>Yes</td><td>The search query.</td></tr>
<tr><td>num_results</td><td>integer</td><td>No</td><td>Number of results (default 10).</td></tr>
<tr><td>include_content</td><td>boolean</td><td>No</td><td>Whether to include full page content.</td></tr>
</tbody>
</table>
<h3 id="python-executor">python_executor</h3>
<p>Execute Python safely for data analysis and computation — pandas transformations, matplotlib visualisation, and mathematical work.</p>
<table>
<thead><tr><th>Parameter</th><th>Type</th><th>Required</th><th>Description</th></tr></thead>
<tbody>
<tr><td>code</td><td>string</td><td>Yes</td><td>Python code to execute.</td></tr>
<tr><td>libraries</td><td>array</td><td>No</td><td>Available libraries (pandas, numpy, matplotlib, …).</td></tr>
</tbody>
</table>
<h2 id="file-and-image-tools">File &amp; Image Tools</h2>
<p>File tools (<code>read_file</code>, write/edit) let agents work with the task workspace — see <a href="../files/management.html">File Management</a>. Image tools depend on configured models:</p>
<ul>
<li><strong>Vision (understanding)</strong> — <code>understand_images</code>, <code>describe_images</code>, <code>detect_objects</code> require a <a href="../models/llm.html#vision-optional">vision model</a>.</li>
<li><strong>Image generation</strong> — <code>generate_image</code>, <code>edit_image</code> require an <a href="../models/image-generation.html">image generation model</a>.</li>
</ul>
<h2 id="discovering-tools">Discovering Tools</h2>
<p>List the tools available to your account, including MCP-provided tools:</p>
''' + c('''GET /api/tools/available     # all available tools, incl. MCP
GET /api/tools/configurable
GET /api/tools/usage         # tool usage statistics''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./mcp.html">MCP Servers →</a></li>
<li><a href="./custom-apis.html">Custom APIs →</a></li>
</ul>''', [
 (2, "basic-tools", "Basic Tools"),
 (2, "file-and-image-tools", "File & Image Tools"),
 (2, "discovering-tools", "Discovering Tools"),
 (2, "next-steps", "Next Steps"),
])

PAGES["tools/mcp-providers.html"] = ("MCP Providers", '''<h1 id="mcp-providers">MCP Providers Configuration</h1>
<p>Some built-in MCP tools require OAuth authentication — Google, LinkedIn, and Microsoft services. For these you configure a <strong>Client ID</strong> and <strong>Client Secret</strong> per provider.</p>
<h2 id="general-setup">General Setup</h2>
<p>For every provider you register an OAuth application and set an authorized redirect URI. The Xagent format is:</p>
''' + c('https://&lt;YOUR_XAGENT_DOMAIN&gt;/api/auth/&lt;provider&gt;/callback') + '''
<p>Replace <code>&lt;YOUR_XAGENT_DOMAIN&gt;</code> with your deployment domain and <code>&lt;provider&gt;</code> with <code>google</code>, <code>linkedin</code>, or <code>microsoft</code>. Locally it may be <code>http://localhost:8000/api/auth/&lt;provider&gt;/callback</code>.</p>
<h2 id="google">Google (Drive, Gmail, …)</h2>
<ol>
<li>In the <strong>Google Cloud Console</strong>, create a project and enable the APIs you need (Google Drive API, Gmail API).</li>
<li>Configure the <strong>OAuth consent screen</strong> and add the required scopes (e.g. <code>https://www.googleapis.com/auth/drive</code>).</li>
<li>Create an <strong>OAuth client ID</strong> of type <em>Web application</em>, and add the Xagent callback URL as an authorized redirect URI.</li>
<li>Copy the generated Client ID and Client Secret into your Xagent configuration.</li>
</ol>
''' + adm("info", "LinkedIn &amp; Microsoft", "<p>LinkedIn and Microsoft follow the same pattern — register an OAuth app on the provider, set the matching <code>/api/auth/&lt;provider&gt;/callback</code> redirect URI, and copy the Client ID/Secret into Xagent.</p>") + '''
''' + adm("warning", "Keep secrets safe", "<p>Client secrets grant access to the connected accounts. Store them through your deployment's secret management, not in source control.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./mcp.html">MCP Servers →</a></li>
<li><a href="../channels/overview.html">Channels →</a></li>
</ul>''', [
 (2, "general-setup", "General Setup"),
 (2, "google", "Google (Drive, Gmail, …)"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Files
# ===========================================================================
PAGES["files/overview.html"] = ("Files Overview", '''<h1 id="files-overview">Files Overview</h1>
<p>Files let agents work with real documents and data during task execution — upload reference materials, data files, or any document an agent needs to analyse, process, or reference.</p>
<h2 id="what-you-can-do">What You Can Do</h2>
<ul>
<li><strong>Analyze</strong> — process documents and extract information.</li>
<li><strong>Reference</strong> — consult files during execution.</li>
<li><strong>Transform</strong> — convert between formats.</li>
<li><strong>Generate</strong> — create new files as output.</li>
</ul>
<h2 id="how-files-work">How Files Work</h2>
<ol>
<li><strong>Upload</strong> — the file is stored in your workspace.</li>
<li><strong>Available</strong> — it becomes accessible to agents.</li>
<li><strong>Read</strong> — the agent reads it when needed.</li>
<li><strong>Process</strong> — the agent analyses the content.</li>
<li><strong>Generate</strong> — the agent can produce new files.</li>
</ol>
<h2 id="managing-files-via-api">Managing Files via API</h2>
''' + c('''POST   /api/files            # upload a file
GET    /api/files            # list files
GET    /api/files/{id}/preview
GET    /api/files/{id}/download
DELETE /api/files/{id}''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./upload.html">File Upload →</a></li>
<li><a href="./management.html">File Management →</a></li>
</ul>''', [
 (2, "what-you-can-do", "What You Can Do"),
 (2, "how-files-work", "How Files Work"),
 (2, "managing-files-via-api", "Managing Files via API"),
 (2, "next-steps", "Next Steps"),
])

PAGES["files/upload.html"] = ("File Upload", '''<h1 id="file-upload">File Upload</h1>
<p>Upload files to a task workspace so agents can access and process them during execution.</p>
<h2 id="upload-methods">Upload Methods</h2>
<ul>
<li><strong>From the Task page</strong> — click the attachment icon, select files, and they are attached to your task request. Multiple files at once are supported.</li>
<li><strong>Drag and drop</strong> — drag files from your file manager onto the task input area to attach them automatically.</li>
</ul>
<h2 id="supported-content">Supported Content</h2>
<ul>
<li>Documents — PDF, DOCX, TXT</li>
<li>Spreadsheets — CSV, XLSX</li>
<li>Images — PNG, JPG</li>
<li>Code files and more</li>
</ul>
<h2 id="file-size-limits">File Size Limits</h2>
<p>Maximum file size is typically 10–100MB per file, and total upload size varies by configuration and plan. For large files, compress to ZIP, split into smaller chunks, or reduce image resolution.</p>
''' + adm("info", "Limits vary", "<p>Upload limits depend on your Xagent configuration and plan. Contact your administrator for the exact limits in your deployment.</p>") + '''
<h2 id="upload-via-api">Upload via API</h2>
''' + c('''POST /api/files            # multipart/form-data file upload''') + '''
<p>An uploaded file's id can then be passed when <a href="../tasks/overview.html#creating-a-task-via-api">creating a task</a>.</p>
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./management.html">File Management →</a></li>
<li><a href="../tasks/overview.html">Tasks Overview →</a></li>
</ul>''', [
 (2, "upload-methods", "Upload Methods"),
 (2, "supported-content", "Supported Content"),
 (2, "file-size-limits", "File Size Limits"),
 (2, "upload-via-api", "Upload via API"),
 (2, "next-steps", "Next Steps"),
])

PAGES["files/management.html"] = ("File Management", '''<h1 id="file-management">File Management</h1>
<p>Agents manage files in the task workspace during execution — reading, writing, listing, and editing as needed.</p>
<h2 id="task-workspace">Task Workspace</h2>
<p>Each task has an isolated workspace:</p>
<ul>
<li><strong>Automatic creation</strong> — created when the task starts.</li>
<li><strong>Isolated storage</strong> — only the current task can access it.</li>
<li><strong>Temporary</strong> — exists during execution.</li>
<li><strong>Auto-cleanup</strong> — removed after the task completes.</li>
</ul>
''' + adm("warning", "Download before completion", "<p>Files are automatically cleaned up after a task ends. Download any generated files you want to keep before the task completes.</p>") + '''
<h2 id="file-lifecycle">File Lifecycle</h2>
''' + c('''1. Upload   -> file stored in task workspace
2. Access   -> agent reads file when needed
3. Process  -> agent analyzes and processes content
4. Output   -> agent creates new files
5. Download -> you download files before task ends
6. Cleanup  -> workspace deleted after task''') + '''
<h2 id="agent-file-operations">Agent File Operations</h2>
<p>Agents read content with the <code>read_file</code> tool, which handles plain text directly and parses documents such as PDF and DOCX:</p>
''' + c('''read_file(file_path="data.txt")
read_file(file_path="report.pdf")
read_file(file_path="document.docx")''') + '''
<p>Workspace files for a task are also retrievable through the API:</p>
''' + c('''GET /api/chat/workspace/{task_id}/files
GET /api/chat/workspace/{task_id}/output''') + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./overview.html">Files Overview →</a></li>
<li><a href="../tasks/execution.html">Task Execution →</a></li>
</ul>''', [
 (2, "task-workspace", "Task Workspace"),
 (2, "file-lifecycle", "File Lifecycle"),
 (2, "agent-file-operations", "Agent File Operations"),
 (2, "next-steps", "Next Steps"),
])

# ===========================================================================
# Channels
# ===========================================================================
PAGES["channels/overview.html"] = ("Channels Overview", '''<h1 id="channels-overview">Channels Overview</h1>
<p>Channels connect Xagent to external chat platforms so users can interact with agents and tasks outside the web app. In the current implementation, channels are user-owned integrations.</p>
<h2 id="how-channels-work">How Channels Work</h2>
<ol>
<li>Create a bot or app on the target platform.</li>
<li>Add the credentials in Xagent.</li>
<li>Activate the channel.</li>
<li>Send messages from the external platform.</li>
<li>Xagent creates or continues tasks for that conversation in the channel owner's workspace.</li>
</ol>
<p>Channels are managed from the <strong>Channels</strong> page and the <code>/api/channels</code> endpoints.</p>
''' + c('''GET    /api/channels          # list your channels
POST   /api/channels          # create a channel
PUT    /api/channels/{id}     # update a channel
DELETE /api/channels/{id}     # delete a channel''') + '''
<h2 id="supported-platforms">Supported Platforms</h2>
<ul>
<li><a href="./telegram.html">Telegram</a></li>
<li>Feishu</li>
</ul>
<p>Typical use cases include personal assistant bots, internal team bots, and lightweight task intake from chat.</p>
<h2 id="channel-concepts">Shared Channel Concepts</h2>
<table>
<thead><tr><th>Field</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>channel_type</code></td><td>Platform type, e.g. <code>telegram</code> or <code>feishu</code>.</td></tr>
<tr><td><code>channel_name</code></td><td>A readable display name.</td></tr>
<tr><td><code>config</code></td><td>Platform-specific configuration.</td></tr>
<tr><td><code>is_active</code></td><td>Whether the bot or app should currently be running.</td></tr>
</tbody>
</table>
''' + adm("info", "Protected secrets", "<p>Sensitive fields inside <code>config</code> (such as bot tokens) are stored as protected channel secrets.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./telegram.html">Telegram →</a></li>
</ul>''', [
 (2, "how-channels-work", "How Channels Work"),
 (2, "supported-platforms", "Supported Platforms"),
 (2, "channel-concepts", "Shared Channel Concepts"),
 (2, "next-steps", "Next Steps"),
])

PAGES["channels/telegram.html"] = ("Telegram", '''<h1 id="telegram">Telegram</h1>
<p>Connect a Telegram bot to your Xagent account so you can start and continue tasks directly from Telegram. The integration is user-owned: Xagent starts or reloads the bot automatically when the channel is saved and active.</p>
<h2 id="what-it-supports">What It Supports</h2>
<ul>
<li>Text conversations</li>
<li>Continuing an existing conversation in the same chat</li>
<li>Starting a fresh conversation with <code>/new</code></li>
<li>Stopping or pausing the current run with <code>/stop</code> or <code>/pause</code></li>
<li>Uploading documents, images, audio, or video into the task workspace</li>
</ul>
<h2 id="quick-setup">Quick Setup</h2>
<h3 id="1-create-a-bot">1. Create a bot in BotFather</h3>
<p>In Telegram, chat with <code>@BotFather</code>, run <code>/newbot</code>, follow the prompts, and save the bot token:</p>
''' + c('123456789:ABCdefGHIjklmNOPqrsTUVwxyz') + '''
<h3 id="2-add-the-channel">2. Add the channel in Xagent</h3>
<p>Open the <strong>Channels</strong> page and add a new <strong>Telegram Bot</strong> channel. The fields are:</p>
<table>
<thead><tr><th>Field</th><th>Required</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Bot token</td><td>Yes</td><td>The token from BotFather.</td></tr>
<tr><td>Allowed users</td><td>No</td><td>Comma-separated Telegram user IDs. If empty, any user who can reach the bot is allowed.</td></tr>
<tr><td>Active</td><td>—</td><td>Whether this bot should be running.</td></tr>
</tbody>
</table>
<h3 id="3-save-and-activate">3. Save and activate</h3>
<p>Saving an active channel starts the bot. Message the bot in Telegram to create a task; it runs in your Xagent workspace and streams the result back to the chat.</p>
''' + adm("warning", "Restrict access", "<p>Leaving <strong>Allowed users</strong> empty lets anyone who finds the bot use it — and run tasks in your workspace. Set the allowed Telegram user IDs for anything beyond personal testing.</p>") + '''
<h2 id="next-steps">Next Steps</h2>
<ul>
<li><a href="./overview.html">Channels Overview →</a></li>
<li><a href="../tasks/overview.html">Tasks Overview →</a></li>
</ul>''', [
 (2, "what-it-supports", "What It Supports"),
 (2, "quick-setup", "Quick Setup"),
 (2, "next-steps", "Next Steps"),
])
