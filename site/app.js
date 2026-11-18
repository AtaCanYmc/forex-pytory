/**
 * Forex-Pytory Premium Documentation & Interactive Explorer
 * Vanilla Modern JS (ES2022) - Zero Bloat
 */

// --- 1. Theme Management (Modern Web Guidance Compliant) ---
function initTheme() {
  const metaColorScheme = document.querySelector('meta[name="color-scheme"]');
  const themeToggle = document.getElementById('theme-toggle');

  function getSystemPreference() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function getEffectiveTheme() {
    const stored = localStorage.getItem('color-scheme');
    if (stored === 'dark' || stored === 'light') return stored;
    return getSystemPreference();
  }

  function updateThemeUI() {
    const current = getEffectiveTheme();
    if (themeToggle) {
      themeToggle.setAttribute('aria-label', `Switch to ${current === 'dark' ? 'light' : 'dark'} mode`);
      themeToggle.innerHTML = current === 'dark'
        ? `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>`
        : `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>`;
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = getEffectiveTheme();
      const target = current === 'dark' ? 'light' : 'dark';
      const system = getSystemPreference();

      if (target === system) {
        localStorage.removeItem('color-scheme');
        if (metaColorScheme) metaColorScheme.content = 'light dark';
      } else {
        localStorage.setItem('color-scheme', target);
        if (metaColorScheme) metaColorScheme.content = target;
      }
      updateThemeUI();
    });
  }

  window.addEventListener('storage', (e) => {
    if (e.key === 'color-scheme') {
      if (metaColorScheme) metaColorScheme.content = e.newValue ?? 'light dark';
      updateThemeUI();
    }
  });

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    if (!localStorage.getItem('color-scheme')) {
      updateThemeUI();
    }
  });

  updateThemeUI();
}

// --- 2. Generic Tab Controller with Keyboard Navigation ---
function initTabs(containerSelector, tabSelector, panelSelector) {
  const containers = document.querySelectorAll(containerSelector);

  containers.forEach(container => {
    const tabs = Array.from(container.querySelectorAll(tabSelector));
    const panels = Array.from(container.querySelectorAll(panelSelector));

    function selectTab(selectedTab) {
      const targetId = selectedTab.getAttribute('aria-controls') || selectedTab.dataset.target;

      tabs.forEach(tab => {
        const isSelected = tab === selectedTab;
        tab.setAttribute('aria-selected', isSelected ? 'true' : 'false');
        tab.classList.toggle('active', isSelected);
      });

      panels.forEach(panel => {
        const isMatch = panel.id === targetId || panel.dataset.id === targetId;
        panel.classList.toggle('active', isMatch);
        if (isMatch) {
          panel.removeAttribute('hidden');
          panel.tabIndex = 0;
        } else {
          panel.setAttribute('hidden', '');
        }
      });
    }

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', () => selectTab(tab));

      tab.addEventListener('keydown', (e) => {
        let nextIndex = index;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
          nextIndex = (index + 1) % tabs.length;
        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
          nextIndex = (index - 1 + tabs.length) % tabs.length;
        } else if (e.key === 'Home') {
          nextIndex = 0;
        } else if (e.key === 'End') {
          nextIndex = tabs.length - 1;
        } else {
          return;
        }
        e.preventDefault();
        tabs[nextIndex].focus();
        selectTab(tabs[nextIndex]);
      });
    });
  });
}

// --- 3. Clipboard Copy Helper with Accessible Live Feedback ---
function initCopyButtons() {
  document.querySelectorAll('.btn-copy').forEach(btn => {
    btn.addEventListener('click', async () => {
      const textToCopy = btn.dataset.copy || btn.closest('.code-card, .install-box')?.querySelector('code, .install-code-text')?.innerText?.trim();
      if (!textToCopy) return;

      try {
        await navigator.clipboard.writeText(textToCopy);
        const originalText = btn.innerHTML;
        btn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg> Copied!`;
        btn.classList.add('copied');

        setTimeout(() => {
          btn.innerHTML = originalText;
          btn.classList.remove('copied');
        }, 2000);
      } catch (err) {
        console.error('Failed to copy text: ', err);
      }
    });
  });
}

// --- 4. Interactive Economic Event Explorer & Real Data Simulator ---
const SAMPLE_EVENTS = [
  {
    market: "forex",
    id: "ff_104812",
    time: "08:30am",
    currency: "USD",
    event: "Core CPI m/m",
    impact: "high",
    forecast: "0.3%",
    actual: "0.4%",
    previous: "0.3%"
  },
  {
    market: "forex",
    id: "ff_104813",
    time: "08:30am",
    currency: "USD",
    event: "CPI y/y",
    impact: "high",
    forecast: "3.2%",
    actual: "3.5%",
    previous: "3.2%"
  },
  {
    market: "forex",
    id: "ff_104814",
    time: "10:00am",
    currency: "USD",
    event: "Prelim UoM Consumer Sentiment",
    impact: "medium",
    forecast: "79.0",
    actual: "77.9",
    previous: "79.4"
  },
  {
    market: "forex",
    id: "ff_104815",
    time: "02:00pm",
    currency: "EUR",
    event: "German Buba President Nagel Speaks",
    impact: "low",
    forecast: "—",
    actual: "—",
    previous: "—"
  },
  {
    market: "crypto",
    id: "cc_50124",
    time: "04:00am",
    currency: "BTC",
    event: "Bitcoin Difficulty Adjustment",
    impact: "high",
    forecast: "+1.2%",
    actual: "+3.9%",
    previous: "-0.4%"
  },
  {
    market: "crypto",
    id: "cc_50125",
    time: "12:00pm",
    currency: "ETH",
    event: "Ethereum All Core Devs Execution Call",
    impact: "medium",
    forecast: "—",
    actual: "—",
    previous: "—"
  },
  {
    market: "crypto",
    id: "cc_50126",
    time: "03:30pm",
    currency: "SOL",
    event: "Network Upgrade Epoch Transition",
    impact: "low",
    forecast: "—",
    actual: "—",
    previous: "—"
  },
  {
    market: "energy",
    id: "ee_9201",
    time: "10:30am",
    currency: "USD",
    event: "EIA Crude Oil Inventories",
    impact: "high",
    forecast: "-1.4M",
    actual: "+3.2M",
    previous: "-2.1M"
  },
  {
    market: "energy",
    id: "ee_9202",
    time: "10:30am",
    currency: "USD",
    event: "EIA Natural Gas Storage",
    impact: "medium",
    forecast: "+52B",
    actual: "+50B",
    previous: "+24B"
  },
  {
    market: "metals",
    id: "mm_4102",
    time: "09:00am",
    currency: "USD",
    event: "COMEX Gold Vault Registered Stocks Update",
    impact: "high",
    forecast: "—",
    actual: "11.2M oz",
    previous: "11.1M oz"
  },
  {
    market: "metals",
    id: "mm_4103",
    time: "01:30pm",
    currency: "USD",
    event: "LBMA Silver Daily Clearing Volume",
    impact: "low",
    forecast: "—",
    actual: "214M oz",
    previous: "198M oz"
  }
];

function initExplorer() {
  const tableBody = document.getElementById('explorer-tbody');
  const jsonPre = document.getElementById('explorer-json-code');
  const marketChips = document.querySelectorAll('#market-chips .chip');
  const impactChips = document.querySelectorAll('#impact-chips .chip');
  const viewBtns = document.querySelectorAll('.view-btn');
  const tableView = document.getElementById('explorer-table-view');
  const jsonView = document.getElementById('explorer-json-view');

  let activeMarket = 'all';
  let activeImpact = 'all';

  function renderData() {
    const filtered = SAMPLE_EVENTS.filter(item => {
      const matchMarket = activeMarket === 'all' || item.market === activeMarket;
      const matchImpact = activeImpact === 'all' || item.impact === activeImpact;
      return matchMarket && matchImpact;
    });

    // Render Table
    if (tableBody) {
      if (filtered.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="7" style="text-align: center; padding: 2rem; color: var(--text-muted);">No calendar events match the selected filters.</td></tr>`;
      } else {
        tableBody.innerHTML = filtered.map(item => `
          <tr>
            <td><strong>${item.time}</strong></td>
            <td><span class="version-pill">${item.currency}</span></td>
            <td>${item.event}</td>
            <td><span class="impact-badge impact-${item.impact}">${item.impact}</span></td>
            <td>${item.forecast}</td>
            <td><strong>${item.actual}</strong></td>
            <td>${item.previous}</td>
          </tr>
        `).join('');
      }
    }

    // Render JSON Output matching Pydantic EconomicEvent model
    if (jsonPre) {
      const pydanticList = filtered.map(item => ({
        ID: item.id,
        Time: item.time,
        Currency: item.currency,
        Event: item.event,
        Impact: item.impact,
        Forecast: item.forecast,
        Actual: item.actual,
        Previous: item.previous
      }));
      jsonPre.textContent = JSON.stringify(pydanticList, null, 2);
    }
  }

  marketChips.forEach(chip => {
    chip.addEventListener('click', () => {
      marketChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeMarket = chip.dataset.market;
      renderData();
    });
  });

  impactChips.forEach(chip => {
    chip.addEventListener('click', () => {
      impactChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeImpact = chip.dataset.impact;
      renderData();
    });
  });

  viewBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      viewBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const view = btn.dataset.view;
      if (view === 'table') {
        tableView.style.display = 'block';
        jsonView.style.display = 'none';
      } else {
        tableView.style.display = 'none';
        jsonView.style.display = 'block';
      }
    });
  });

  renderData();
}

// --- 5. Interactive Command Builder & Code Snippet Generator ---
function initCommandBuilder() {
  const sourceSelect = document.getElementById('builder-source');
  const dateInput = document.getElementById('builder-date');
  const formatSelect = document.getElementById('builder-format');

  const cliCode = document.getElementById('builder-cli-code');
  const pythonCode = document.getElementById('builder-python-code');
  const mcpCode = document.getElementById('builder-mcp-code');

  function updateSnippets() {
    const source = sourceSelect ? sourceSelect.value : 'forex';
    const dateVal = dateInput && dateInput.value ? dateInput.value : '';
    const format = formatSelect ? formatSelect.value : 'table';

    // 1. CLI Snippet
    let cliStr = `forex-scraper --source ${source} --format ${format}`;
    if (dateVal) {
      cliStr += ` --date ${dateVal}`;
    }
    if (cliCode) cliCode.textContent = cliStr;

    // 2. Python SDK Snippet
    const scraperModuleMap = {
      forex: 'forex_factory_scraper',
      crypto: 'crypto_craft_scraper',
      energy: 'energy_exch_scraper',
      metals: 'metals_mine_scraper'
    };
    const mod = scraperModuleMap[source] || 'forex_factory_scraper';
    let pyStr = `from forex_pytory.core.scraper import ${mod}\n\n`;
    if (dateVal) {
      const [year, month, day] = dateVal.split('-').map(Number);
      pyStr += `# Scrape specific date ${dateVal}\n`;
      pyStr += `url = ${mod}.get_url(day=${day}, month=${month}, year=${year})\n`;
    } else {
      pyStr += `from datetime import datetime\n`;
      pyStr += `today = datetime.now()\n`;
      pyStr += `url = ${mod}.get_url(day=today.day, month=today.month, year=today.year)\n`;
    }
    pyStr += `events = ${mod}.get_records(url)\n\n`;
    pyStr += `for event in events:\n`;
    pyStr += `    print(f"[{event.time}] {event.currency} - {event.event} ({event.impact})")`;
    if (pythonCode) pythonCode.textContent = pyStr;

    // 3. MCP Tool Call Payload
    const mcpPayload = {
      name: "fetch_economic_events",
      arguments: {
        source: source,
        ...(dateVal ? { date: dateVal } : {})
      }
    };
    if (mcpCode) mcpCode.textContent = JSON.stringify(mcpPayload, null, 2);
  }

  if (sourceSelect) sourceSelect.addEventListener('change', updateSnippets);
  if (dateInput) dateInput.addEventListener('input', updateSnippets);
  if (formatSelect) formatSelect.addEventListener('change', updateSnippets);

  updateSnippets();
}

// --- 6. Mobile Navigation Controller ---
function initMobileNav() {
  const toggle = document.querySelector('.mobile-nav-toggle');
  const nav = document.querySelector('.nav-links');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('mobile-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    nav.querySelectorAll('.nav-link').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('mobile-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
}

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initTabs('.install-box', '.install-tab-btn', '.install-code-wrap');
  initTabs('.doc-tabs-wrap', '.doc-tab-btn', '.doc-panel');
  initCopyButtons();
  initExplorer();
  initCommandBuilder();
  initMobileNav();
});
