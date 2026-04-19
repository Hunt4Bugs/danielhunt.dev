export const NAV_LINKS = [
  { label: 'Work', href: '#services' },
  { label: 'About', href: '#about' },
  { label: 'FAQ', href: '#faq' },
  { label: 'Contact', href: '#contact' },
] as const;

export const SITE = {
  name: 'Daniel Hunt',
  jobTitle: 'AI & Data Engineer',
  location: 'Simi Valley, California',
  url: 'https://danielhunt.dev',
  email: 'contact@danielhunt.dev',
  ogTitle: 'Daniel Hunt — AI & Data Engineer',
  description:
    'Daniel Hunt is an independent AI and data engineer offering AI audits, data and AI infrastructure, autonomous agents and workflow automation, and custom application development.',
  ogDescription:
    'Independent AI & data engineer. Audits, infrastructure, pipelines, agents, and custom systems designed to survive production use.',
  shortDescription:
    'Independent AI and data engineer — audits, infrastructure, agents, data systems, custom apps.',
  socials: {
    linkedin: 'https://www.linkedin.com/in/danielhunt16/',
    x: 'https://x.com/_danielhunt',
  },
  keywords: [
    'AI consultant',
    'AI engineer',
    'data engineer',
    'data engineering',
    'AI audit',
    'AI infrastructure',
    'data infrastructure',
    'data platforms',
    'RAG',
    'LLM evaluations',
    'AI agents',
    'autonomous agents',
    'MCP servers',
    'workflow automation',
    'agentic systems',
    'custom AI application development',
    'Daniel Hunt',
  ],
};

export const SERVICES = [
  {
    title: 'AI Audit',
    slug: 'ai-audit',
    blurb:
      'A clear-eyed review of your existing AI usage — accuracy, cost, security, and risk. You leave with a prioritised action list and an honest answer to "is this actually working?"',
    tag: 'I',
  },
  {
    title: 'AI & Data Infrastructure',
    slug: 'ai-infrastructure',
    blurb:
      'Production-grade foundations: RAG, vector databases, pipelines, warehouses, model gateways, evals, observability and CI. The unglamorous pieces that turn a demo into a dependable product.',
    tag: 'II',
  },
  {
    title: 'Agent & Workflow Automation',
    slug: 'agent-workflow-automation',
    blurb:
      'Autonomous agents, multi-step workflows, and tool integrations that plug into your real systems — Slack, Notion, Linear, internal APIs — and quietly remove hours of repetitive work each week.',
    tag: 'III',
  },
  {
    title: 'Custom App Development',
    slug: 'custom-app-development',
    blurb:
      'Full-stack AI-powered applications built on a modern, boring-by-choice stack (FastAPI, Next.js, Supabase). From first prototype to a product your team actually uses.',
    tag: 'IV',
  },
];

export const FAQS = [
  {
    q: 'What does Daniel Hunt do?',
    a: 'Daniel Hunt is an independent AI and data engineer. He helps companies design, build, and operate AI products and data systems — including audits of existing systems, production infrastructure for pipelines and models, autonomous agents and workflow automation, and full-stack applications.',
  },
  {
    q: 'How do I hire Daniel Hunt?',
    a: 'Email contact@danielhunt.dev or use the contact form on danielhunt.dev. Daniel typically replies within two working days and offers free 30-minute scoping calls.',
  },
  {
    q: 'What is an AI audit?',
    a: 'An AI audit is a structured review of an organisation\u2019s existing AI usage covering accuracy, cost, latency, security, governance, and risk. The deliverable is a prioritised action list and a candid assessment of whether each AI feature is actually delivering value.',
  },
  {
    q: 'Which technologies does Daniel work with?',
    a: 'Python, TypeScript, SQL, orchestration and data pipeline tooling, warehouses and Postgres systems, Supabase, Vercel and Render for deployment, and the major model providers (Anthropic, OpenAI, Google). For agent work he builds autonomous agents, multi-step workflows, and MCP servers that integrate with tools like Slack, Notion, and Linear.',
  },
  {
    q: 'Does Daniel work with startups or enterprises?',
    a: 'Both. Engagements range from one-week audits for early-stage startups to multi-month builds and ongoing fractional engineering for established companies.',
  },
  {
    q: 'Where is Daniel based?',
    a: 'Daniel is based in Simi Valley, California and works remotely with clients globally. He is comfortable collaborating across time zones and is fluent in English.',
  },
];
