/* danielhunt.dev: shared chrome (web components) + page behaviors.
   Loaded with `defer` on every page. No framework, no build step. */

const SITE = {
  name: 'Daniel Hunt',
  location: 'Simi Valley, California',
  email: 'contact@danielhunt.dev',
  socials: {
    linkedin: 'https://www.linkedin.com/in/danielhuntdev',
    x: 'https://x.com/danielhunt_dev',
  },
};

/* A URL-scoped preview keeps light-mode QA and brand production reproducible
   without changing the dark default or persisting a visitor preference. */
const previewTheme = new URLSearchParams(window.location.search).get('theme');
if (previewTheme === 'light' || previewTheme === 'dark') {
  document.documentElement.dataset.theme = previewTheme;
  document
    .querySelector('meta[name="theme-color"]')
    ?.setAttribute('content', previewTheme === 'light' ? '#F5F7FA' : '#0A0C10');
}

const NAV_LINKS = [
  { label: 'Index', href: '/#top' },
  { label: 'About', href: '/#about' },
  { label: 'Services', href: '/services/' },
  { label: 'Contact', href: '/#contact' },
];

/* ── <site-nav> ─────────────────────────────────────────────── */

class SiteNav extends HTMLElement {
  connectedCallback() {
    const onHome = window.location.pathname === '/' || window.location.pathname === '/index.html';
    const resolveHref = (href) => onHome ? href.replace('/#', '#') : href;
    const links = NAV_LINKS.map(
      (link) => `<a href="${resolveHref(link.href)}" class="link-cinema">${link.label}</a>`
    ).join('');
    const mobileLinks = NAV_LINKS.map(
      (link) => `<a href="${resolveHref(link.href)}" class="mobile-menu__link">${link.label}</a>`
    ).join('');

    this.innerHTML = `
      <header class="site-header">
        <div class="container-page">
          <div class="site-header__bar">
            <a href="/" class="site-header__brand" aria-label="Daniel Hunt home">
              <span class="monogram-mark site-header__monogram">DH</span>
              <span class="site-header__name">Daniel Hunt</span>
            </a>

            <nav class="site-header__nav" aria-label="Primary">${links}</nav>

            <div class="site-header__meta">
              <span class="status-dot" aria-hidden="true"></span>
              <span class="mono-label">Public log / active</span>
            </div>

            <button
              id="mobile-menu-btn"
              class="mono-label site-header__menu-btn"
              aria-label="Open menu"
              aria-expanded="false"
              aria-controls="mobile-menu"
            >Menu</button>
          </div>
        </div>
      </header>

      <nav id="mobile-menu" class="mobile-menu hidden" aria-label="Mobile">
        <div class="container-page mobile-menu__inner">
          ${mobileLinks}
          <p class="mono-label"><span class="status-dot" aria-hidden="true"></span>Public log / active</p>
        </div>
      </nav>
    `;

    const btn = this.querySelector('#mobile-menu-btn');
    const menu = this.querySelector('#mobile-menu');

    const closeMenu = () => {
      menu.classList.add('hidden');
      btn.setAttribute('aria-expanded', 'false');
      btn.setAttribute('aria-label', 'Open menu');
      btn.textContent = 'Menu';
    };

    btn.addEventListener('click', () => {
      const expanded = btn.getAttribute('aria-expanded') !== 'true';
      menu.classList.toggle('hidden', !expanded);
      btn.setAttribute('aria-expanded', String(expanded));
      btn.setAttribute('aria-label', expanded ? 'Close menu' : 'Open menu');
      btn.textContent = expanded ? 'Close' : 'Menu';
    });

    menu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeMenu);
    });
  }
}

customElements.define('site-nav', SiteNav);

/* ── <site-footer> ──────────────────────────────────────────── */

class SiteFooter extends HTMLElement {
  connectedCallback() {
    const year = new Date().getFullYear();

    this.innerHTML = `
      <footer class="site-footer" aria-labelledby="footer-heading">
        <h2 id="footer-heading" class="sr-only">Site footer</h2>
        <div class="container-page">
          <div class="site-footer__row">
            <a href="/" class="monogram-mark site-footer__monogram" aria-label="Daniel Hunt home">DH</a>
            <div class="site-footer__meta">
              <p class="mono-value">&copy; ${year} &middot; ${SITE.name.toUpperCase()}</p>
              <div class="site-footer__links">
                <a href="/#about" class="mono-value link-cinema">About</a>
                <a href="/services/" class="mono-value link-cinema">Services</a>
                <a href="/#contact" class="mono-value link-cinema">Contact</a>
                <a href="/brand" class="mono-value link-cinema">design.md</a>
              </div>
            </div>
          </div>
        </div>
      </footer>
    `;
  }
}

customElements.define('site-footer', SiteFooter);

/* ── Scroll reveal ──────────────────────────────────────────── */
/* Runs after the components above are defined (and, with `defer`,
   after the document is parsed), so .reveal nodes inside custom
   elements are already in the DOM. */

const els = document.querySelectorAll('.reveal');
if (!('IntersectionObserver' in window) ||
    window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  els.forEach((el) => el.classList.add('is-visible'));
} else {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    },
    { rootMargin: '0px 0px -15% 0px', threshold: 0.08 }
  );
  els.forEach((el) => io.observe(el));
}

/* ── Vexoo-derived home composition ────────────────────────── */

if (document.body.classList.contains('site-vexoo')) {
  const body = document.body;
  const homeView = document.querySelector('[data-view="home"]');
  const detailViews = [...document.querySelectorAll('.detail-view[data-view]')];
  const viewTriggers = [...document.querySelectorAll('[data-view-target]')];
  const homeTriggers = [...document.querySelectorAll('[data-home]')];
  const homeLabel = document.querySelector('[data-home-label]');
  const wordmark = document.querySelector('#home-wordmark');
  const themeSwitch = document.querySelector('#theme-switch');
  const themeMeta = document.querySelector('meta[name="theme-color"]');
  const timeNode = document.querySelector('#local-time');
  const defaultWordmark = 'DANIEL HUNT';
  const validViews = new Set(detailViews.map((view) => view.dataset.view));
  let wordmarkTimer;

  const currentTheme = () => document.documentElement.dataset.theme === 'light' ? 'light' : 'dark';

  const syncThemeControl = () => {
    const light = currentTheme() === 'light';
    themeSwitch?.setAttribute('aria-pressed', String(light));
    themeSwitch?.setAttribute('aria-label', light ? 'Switch to dark mode' : 'Switch to light mode');
    themeMeta?.setAttribute('content', light ? '#F5F7FA' : '#0A0C10');
  };

  const setTheme = (theme) => {
    document.documentElement.dataset.theme = theme;
    const url = new URL(window.location.href);
    url.searchParams.set('theme', theme);
    window.history.replaceState(window.history.state, '', url);
    syncThemeControl();
    syncInternalThemeLinks();
  };

  const syncInternalThemeLinks = () => {
    document.querySelectorAll('a[href^="/"]').forEach((link) => {
      const originalHref = link.dataset.themeHref || link.getAttribute('href');
      if (!originalHref) return;
      link.dataset.themeHref = originalHref;
      const destination = new URL(originalHref, window.location.origin);
      destination.searchParams.set('theme', currentTheme());
      link.setAttribute('href', `${destination.pathname}${destination.search}${destination.hash}`);
    });
  };

  themeSwitch?.addEventListener('click', () => {
    setTheme(currentTheme() === 'dark' ? 'light' : 'dark');
  });

  const setWordmark = (label) => {
    if (!wordmark || wordmark.textContent === label) return;
    window.clearTimeout(wordmarkTimer);
    wordmark.classList.add('is-changing');
    wordmarkTimer = window.setTimeout(() => {
      wordmark.textContent = label;
      wordmark.classList.remove('is-changing');
    }, 110);
  };

  const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)');

  document.querySelectorAll('[data-title]').forEach((card) => {
    card.addEventListener('pointerenter', () => {
      if (finePointer.matches) setWordmark(card.dataset.title);
    });
    card.addEventListener('pointerleave', () => {
      if (finePointer.matches) setWordmark(defaultWordmark);
    });
    card.addEventListener('focusin', () => setWordmark(card.dataset.title));
    card.addEventListener('focusout', () => setWordmark(defaultWordmark));
  });

  const updateLocalTime = () => {
    if (!timeNode) return;
    timeNode.textContent = new Intl.DateTimeFormat('en-US', {
      timeZone: 'America/Los_Angeles',
      hour: 'numeric',
      minute: '2-digit',
    }).format(new Date());
  };

  syncThemeControl();
  syncInternalThemeLinks();
  updateLocalTime();
  window.setInterval(updateLocalTime, 30_000);

  if (homeView) {
    const redirectLegacyServices = () => {
      if (window.location.hash !== '#services') return false;
      const destination = new URL('/services/', window.location.origin);
      const theme = new URLSearchParams(window.location.search).get('theme');
      if (theme === 'light' || theme === 'dark') destination.searchParams.set('theme', theme);
      window.location.replace(destination);
      return true;
    };

    const showView = (name, options = {}) => {
      const detailName = validViews.has(name) ? name : null;
      const isHome = detailName === null;

      homeView.hidden = !isHome;
      detailViews.forEach((view) => {
        view.hidden = view.dataset.view !== detailName;
      });
      body.classList.toggle('detail-open', !isHome);
      if (homeLabel) homeLabel.textContent = isHome ? 'Daniel Hunt' : 'Home';

      if (options.updateHistory !== false) {
        const url = new URL(window.location.href);
        url.hash = isHome ? '' : detailName;
        window.history.pushState({ view: detailName || 'home' }, '', url);
      }

      window.scrollTo({ top: 0, behavior: 'instant' });
      if (!isHome && options.focus !== false) {
        const title = document.querySelector(`[data-view="${detailName}"] h2`);
        title?.setAttribute('tabindex', '-1');
        title?.focus({ preventScroll: true });
      }
    };

    viewTriggers.forEach((trigger) => {
      trigger.addEventListener('click', (event) => {
        event.preventDefault();
        showView(trigger.dataset.viewTarget);
      });
    });

    homeTriggers.forEach((trigger) => {
      trigger.addEventListener('click', () => {
        if (body.classList.contains('detail-open')) showView(null);
      });
    });

    window.addEventListener('popstate', () => {
      if (!redirectLegacyServices()) {
        showView(window.location.hash.slice(1), { updateHistory: false, focus: false });
      }
    });

    if (!redirectLegacyServices()) {
      showView(window.location.hash.slice(1), { updateHistory: false, focus: false });
    }
  }
}
