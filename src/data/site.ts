export const NAV_LINKS = [
  { label: 'Services', href: '#services' },
  { label: 'About', href: '#about' },
  { label: 'FAQ', href: '#faq' },
  { label: 'Contact', href: '#contact' },
] as const;

export const SITE = {
  name: 'Daniel Hunt',
  jobTitle: 'AI Engineer & Consultant',
  url: 'https://danielhunt.dev',
  email: 'contact@danielhunt.dev',
  description:
    'Daniel Hunt is an independent AI engineer and consultant offering AI audits and implementation for small businesses — reviewing the AI tools your team already uses, flagging risks and quick wins, and building only what is worth building.',
  shortDescription:
    'AI audits and implementation for small businesses — honest advice from an independent engineer.',
  socials: {
    linkedin: 'https://www.linkedin.com/in/danielhunt16/',
    x: 'https://x.com/_danielhunt',
  },
  keywords: [
    'AI audit',
    'AI audit for small business',
    'AI for small business',
    'small business AI consultant',
    'AI readiness assessment',
    'AI strategy',
    'AI implementation',
    'workflow automation',
    'AI consultant',
    'AI engineer',
    'Daniel Hunt',
  ],
};

export const SERVICES = [
  {
    title: 'AI Starter Audit',
    slug: 'ai-starter-audit',
    blurb:
      'A fixed-scope, one-week review for small teams. I look at the AI tools your staff are already using (ChatGPT, Copilot, and whatever else), where your data is going, and the three or four quick wins worth acting on. You get a short written report and a call to walk through it.',
    tag: 'I',
  },
  {
    title: 'AI Deep Audit',
    slug: 'ai-deep-audit',
    blurb:
      'Two to four weeks. Everything in the Starter, plus a workflow-by-workflow map of where AI could save real hours, a vendor and cost review, and a prioritised roadmap with rough effort and impact for each opportunity — including an honest build-or-buy call on each one.',
    tag: 'II',
  },
  {
    title: 'AI Implementation',
    slug: 'ai-implementation',
    blurb:
      'Follow-on work to actually ship the items from the audit roadmap: automations that plug AI into the tools you already use (email, spreadsheets, CRMs, docs), and small custom apps when an off-the-shelf tool will not do. Boring, maintainable tech on purpose.',
    tag: 'III',
  },
];

export const FAQS = [
  {
    q: 'What is an AI audit, and do I need one?',
    a: 'An AI audit is a structured review of how AI is already being used in your business — the tools your team types into, the data going with it, the risks, and the opportunities to save real time. You probably need one if staff are using AI tools ad-hoc, if you are being pitched AI features by vendors, or if you want a plan before spending money on anything new.',
  },
  {
    q: "We're a small team — is this overkill for us?",
    a: 'No. The Starter Audit is built for teams of roughly 5 to 50 people who do not have an in-house AI specialist. The point is to give a small business the same calm, independent review a larger company would pay a big firm for, without the jargon or the price tag.',
  },
  {
    q: 'How much does an audit cost, and how long does it take?',
    a: 'The Starter Audit is a fixed scope, roughly one week from kick-off to written report. The Deep Audit runs two to four weeks depending on the size of the team and the number of workflows in scope. Exact pricing is shared on the scoping call so it can reflect what you actually need.',
  },
  {
    q: 'What happens after the audit?',
    a: 'You get a written report and a walk-through call. From there you decide what to do: take the report and run with it internally, hand it to another vendor, or engage me for the AI Implementation work to ship the recommendations. There is no obligation to continue past the audit.',
  },
  {
    q: 'Is my business data safe during the audit?',
    a: 'Yes. I sign an NDA before any engagement, I do not train any model on your data, and I review rather than export the tools your team is using. Where we touch real systems, it is read-only until you explicitly agree otherwise.',
  },
  {
    q: 'Which tools and platforms do you work with?',
    a: 'Whatever your team already uses — Google Workspace, Microsoft 365, common CRMs (HubSpot, Pipedrive, Salesforce), helpdesks, and the usual glue tools like Zapier or Make. On the engineering side I build with Python, TypeScript, Next.js, Supabase, and the major model providers (Anthropic, OpenAI) when custom work is warranted.',
  },
  {
    q: 'How do I hire Daniel Hunt?',
    a: 'Email contact@danielhunt.dev or use the contact form on danielhunt.dev. Daniel typically replies within two working days and offers a free 30-minute scoping call to see whether an audit is the right starting point.',
  },
];
