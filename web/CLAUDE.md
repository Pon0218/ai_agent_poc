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
	--color-s-background: #020826;
	--color-s-card-background: #eaddcf;
	--color-s-headline: #020826;
	--color-s-card-heading: #020826;
	--color-s-sub-headline: #716040;
	--color-s-card-paragraph: #716040;
	--color-s-stroke: #020826;
	--color-s-secondary: #eaddcf;
	--color-s-main: #fffffe;
	--color-s-tertiary: #f25042;
	--color-s-highlight: #8c7851;
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
