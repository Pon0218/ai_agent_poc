# CLAUDE.md — /web

## Tech Stack

| Tool         | Version                                           |
| ------------ | ------------------------------------------------- |
| SvelteKit    | ^2.50                                             |
| Svelte       | ^5.51 (runes mode)                                |
| Vite         | ^7                                                |
| TailwindCSS  | ^4.1 (via `@tailwindcss/vite`)                    |
| TypeScript   | ^5.9                                              |
| Adapter      | `@sveltejs/adapter-cloudflare` (Cloudflare Pages) |
| Validation   | `zod` ^3                                          |
| Icons        | `@material-symbols/svg-400` ^0.42                 |
| SVG loader   | `@poppanator/sveltekit-svg` ^6                    |
| UI Primitive | `bits-ui` ^2                                      |
| Variant      | `class-variance-authority` (cva)                  |
| Class Merge  | `clsx` + `tailwind-merge` (`cn()`)                |
| Storybook    | ^10 (`@storybook/sveltekit`)                      |

---

## TailwindCSS v4

This project uses **Tailwind v4**. Key differences from v3:

- Config is in `src/routes/layout.css` via `@theme {}` — **no `tailwind.config.js`**.
- Custom tokens are defined as CSS variables under `@theme`:

```css
/* src/routes/layout.css */
@import 'tailwindcss';
@plugin '@tailwindcss/typography';

@theme {
	--color-s-background: #fbf7ef;
	--color-s-card-background: #e1e5e6;
	--color-s-headline: #24252d;
	--color-s-card-heading: #24252d;
	--color-s-sub-headline: #7c746f;
	--color-s-card-paragraph: #7c746f;
	--color-s-stroke: #bdc4c6;
	--color-s-secondary: #fbf7ef;
	--color-s-main: #ffffff;
	--color-s-button: #838b8e;
	--color-s-placeholder: #838b8e;
}
```

- Use these tokens as Tailwind classes: `text-s-background`, `bg-s-card-background`, `fill-s-background`, etc.
- Arbitrary variants work as normal: `border-s-background/18` (18% opacity).
- Do **not** add a `tailwind.config.js` or `tailwind.config.ts`.

---

## Material Symbols (`@material-symbols/svg-400`)

Uses `@poppanator/sveltekit-svg` to import SVGs as Svelte components via the `?component` suffix.
Register the plugin in `vite.config.ts` and add the type declaration in `src/app.d.ts`.

<!-- Style directly with Tailwind classes on the component -->
<KeyboardArrowDown class="fill-s-background size-4" />
```
---

## Svelte 5 Runes

Use runes syntax — no `$:` reactive statements, no `export let`.

```svelte
let value = $state(''); let derived = $derived(value.length); let {children} = $props();
```

---

## UI Component System

```
src/components/ui/<component>/      ← Primitive (bits-ui wrapper + cva styles)
src/features/<feature>/components/  ← Feature components (compose Primitives)
```

- **bits-ui** — headless accessible primitives. Wrap thinly, add Tailwind styles, export.
- **cva** — manage style variants per primitive. Variant names follow color tokens (e.g. `card` for `s-card-background`); semantic names (`primary / ghost / secondary`) for components with visual hierarchy like Button.
- **`cn()`** — `src/utils/cn.ts`, combines `clsx` + `tailwind-merge`. Use for all class merging.
- **Storybook** — place `*.stories.svelte` next to each primitive. Use `@storybook/addon-svelte-csf` v5 with args-based stories.

---

## Commands

```bash
npm run dev              # dev server
npm run build            # production build
npm run check            # svelte-check + tsc
npm run format           # prettier
npm run lint             # prettier + eslint
npm run storybook        # storybook dev (port 6006)
npm run build-storybook  # storybook static build
```

---

## ProductLens Design System

### Color tokens (`pl-*`)

Defined in `src/routes/layout.css` under `@theme {}`. Use as Tailwind utilities (`bg-pl-bg`, `text-pl-ink`, `border-pl-rule`, etc.).

| Token         | Value     | Role                             |
| ------------- | --------- | -------------------------------- |
| `pl-bg`       | `#F5F1EB` | Page background — warm cream     |
| `pl-bg-2`     | `#EFEAE0` | Slightly deeper background layer |
| `pl-card`     | `#E8E3DA` | Card / field surface             |
| `pl-card-2`   | `#DED7CB` | Deeper card surface              |
| `pl-ink`      | `#1A1A18` | Primary text & fills             |
| `pl-ink-2`    | `#888780` | Secondary / muted text           |
| `pl-ink-3`    | `#B5B1A8` | Placeholder / subtle text        |
| `pl-rule`     | `#D9D2C5` | Dividers & borders               |
| `pl-accent`   | `#2C2C2A` | Button & accent fills            |
| `pl-accent-h` | `#45433F` | Button hover state               |
| `pl-pos`      | `#3D5A3A` | Positive / strength indicator    |
| `pl-neg`      | `#8A3A2E` | Negative / weakness indicator    |
| `pl-warn`     | `#8A6E2E` | Warning / opportunity indicator  |

### Typography

| Token class           | Font            | Usage                                        |
| --------------------- | --------------- | -------------------------------------------- |
| `font-display`        | Lora 600        | Hero h1, section titles, card headings       |
| `font-display italic` | Lora 400 italic | Subheadings, pull quotes, lede text          |
| `font-ui`             | DM Sans         | All body copy and UI labels (body default)   |
| `font-mono`           | JetBrains Mono  | Eyebrows (`UPPERCASE · TRACKED`), code, meta |

Google Fonts link is pre-loaded in `src/app.html`.

### Spacing & layout

- **Section vertical padding**: `py-[clamp(72px,9vw,128px)]` (use on each `<section>`)
- **Wrap / max-width**: `max-w-[1280px] mx-auto px-5 md:px-12 lg:px-20`
- **Border radius**: `rounded-pl-sm` (8px) · `rounded-pl-md` (14px) · `rounded-pl-lg` (20px)

### Route & component map

| URL        | Route file                   | Key components                                                                                        |
| ---------- | ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| `/`        | `(app)/+page.svelte`         | Hero, SocialProof, FeatureGrid, Banner, BigPicture, CompareTable, Testimonial, Steps, CtaBanner       |
| `/analyze` | `(app)/analyze/+page.svelte` | ProductLensForm (calls `useCreateSession`, stores sessionId → sessionStorage, navigates to `/result`) |
| `/result`  | `(app)/result/+page.svelte`  | ProductLensLoading → ProductLensReport (reads sessionId from sessionStorage)                          |

All feature components live in `src/features/ProductLens/components/`.

Result sub-components (used inside `ProductLensReport`):

- `SwotGrid` — 4-quadrant SWOT display, accepts `strengths/weaknesses/opportunities/threats` string arrays
- `MarketOverview` — accepts optional `body` string (raw API markdown shown here)
- `CompetitorGrid` — accepts `competitors` array `{ name, score, description, percent }`
- `Recommendations` — accepts `items` array `{ timeframe, text }`

### Asset

`src/lib/assets/coffee.png` — hero photo used in `Testimonial.svelte` (import via `$lib/assets/coffee.png?url`).
