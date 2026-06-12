/* danielhunt.dev — shared chrome (web components) + page behaviors.
   Loaded with `defer` on every page. No framework, no build step. */

const SITE = {
  name: 'Daniel Hunt',
  location: 'Simi Valley, California',
  email: 'contact@danielhunt.dev',
  socials: {
    linkedin: 'https://www.linkedin.com/in/danielhunt16/',
    x: 'https://x.com/danielhunt_dev',
  },
};

const NAV_LINKS = [
  { label: 'About', href: '/#about' },
  { label: 'Contact', href: '/#contact' },
];

/* ── <site-nav> ─────────────────────────────────────────────── */

class SiteNav extends HTMLElement {
  connectedCallback() {
    const links = NAV_LINKS.map(
      (link) => `<a href="${link.href}" class="link-cinema">${link.label}</a>`
    ).join('');
    const mobileLinks = NAV_LINKS.map(
      (link) => `<a href="${link.href}" class="mobile-menu__link">${link.label}</a>`
    ).join('');

    this.innerHTML = `
      <header class="site-header">
        <div class="container-page">
          <div class="site-header__bar">
            <a href="#top" class="site-header__brand" aria-label="Daniel Hunt — home">
              <span class="monogram-mark site-header__monogram">DH</span>
              <span class="site-header__name">Daniel Hunt</span>
            </a>

            <nav class="site-header__nav" aria-label="Primary">${links}</nav>

            <div class="site-header__meta">
              <span class="mono-label">${SITE.location.split(',')[0]}</span>
              <span id="la-time" class="mono-label">Loading time</span>
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
          <p class="mono-label">${SITE.location}</p>
          <p id="la-time-mobile" class="mono-label">Loading time</p>
        </div>
      </nav>
    `;

    const btn = this.querySelector('#mobile-menu-btn');
    const menu = this.querySelector('#mobile-menu');
    const laTime = this.querySelector('#la-time');
    const laTimeMobile = this.querySelector('#la-time-mobile');

    const updateTime = () => {
      const formatted = new Intl.DateTimeFormat('en-US', {
        timeZone: 'America/Los_Angeles',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true,
      }).format(new Date());

      laTime.textContent = formatted;
      laTimeMobile.textContent = formatted;
    };

    updateTime();
    window.setInterval(updateTime, 60000);

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
            <a href="#top" class="monogram-mark site-footer__monogram" aria-label="Daniel Hunt — home">DH</a>
            <div class="site-footer__meta">
              <p class="mono-value">&copy; ${year} &middot; ${SITE.name.toUpperCase()}</p>
              <div class="site-footer__links">
                <a href="/#about" class="mono-value link-cinema">About</a>
                <a href="/#contact" class="mono-value link-cinema">Contact</a>
                <a href="/brand" class="mono-value link-cinema">Brand</a>
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
