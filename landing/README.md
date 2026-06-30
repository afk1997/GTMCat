# GTMCat — site & store content

Content drafts for the gtmcat.xyz landing site **and** the Chrome Web Store listing.
One `.md` per page. Copy into your landing project (Next route, Framer, etc.).

> ⚠️ `privacy.md` and `terms.md` are solid drafts grounded in how GTMCat actually
> works — but have a lawyer review them before you rely on them. Replace the
> bracketed placeholders (`[support email]`, `[mailing address]`, entity name).

## Pages to create

| Page | URL | Why you need it |
|---|---|---|
| **Home** | `gtmcat.xyz/` | `home.md` — marketing + "Add to Chrome" / "Start free" CTA. |
| **Privacy Policy** | `gtmcat.xyz/privacy` | `privacy.md` — **REQUIRED**: the Chrome Web Store needs a privacy-policy URL because the extension handles user data; also linked from the app + emails. |
| **Support** | `gtmcat.xyz/support` | `support.md` — **REQUIRED**: the store's "Support URL" must resolve (that's the "Support URL is not reachable" error). Also your help/contact page. |
| **Terms of Service** | `gtmcat.xyz/terms` | `terms.md` — paid SaaS + acceptable-use (the Reddit/ethics line). Strongly recommended; link at signup. |
| **Pricing** | `gtmcat.xyz/pricing` | `pricing.md` — the three plans + trial. (Can live on Home instead.) |
| **Refund / Cancellation** | `gtmcat.xyz/refunds` | `refunds.md` — billing trust; Dodo (merchant of record) expects a clear refund/cancel policy. |

`chrome-web-store-listing.md` is **not a web page** — it's the paste-ready text for the
store's "Privacy practices" tab (single purpose, permission justifications, data-use
certifications) plus the icon/screenshot checklist that clears every red item in your dialog.

## Mapping to the store errors you saw
- *Justification for alarms / host permission / remote code / sidePanel / storage / tabs* → `chrome-web-store-listing.md` → **Permission justifications**.
- *Single purpose description required* → `chrome-web-store-listing.md` → **Single purpose**.
- *Certify data usage complies…* → `chrome-web-store-listing.md` → **Data use & certifications**.
- *Support URL not reachable* → publish `support.md` at `gtmcat.xyz/support`.
- *Icon image is missing* → upload `apps/extension/public/icon/128.png` (the cat) as the store icon.
- *At least one screenshot* → see `chrome-web-store-listing.md` → **Screenshots**.
- Privacy-policy URL field → publish `privacy.md` at `gtmcat.xyz/privacy`.
