# web

## 目錄

- [開始開發](#開始開發)
- [常用指令](#常用指令)
- [Docker 啟動](#docker-啟動)
- [專案設定](#專案設定)
- [詳細設定](#詳細設定)
- [UI 元件系統](#ui-元件系統)

---

## 開始開發

### 1. 安裝依賴

```bash
npm ci
```

### 2. 產生 Cloudflare Workers 型別

```bash
npm run gen
```

> 執行 `wrangler types`，產生 `worker-configuration.d.ts`，讓 TypeScript 能辨識 Cloudflare 環境變數與 Bindings。

### 3. 啟動開發伺服器（含 Mock Server）

```bash
npm run dev
```

> 預設模式會啟動 [MSW（Mock Service Worker）](https://mswjs.io/) 攔截 API 請求，不需要後端服務即可開發。

- Node.js `>=22.0.0`

---

## 常用指令

| 指令                      | 說明                                                    |
| ------------------------- | ------------------------------------------------------- |
| `npm run dev:local`       | 本地整合模式（關閉 Mock，連接真實後端，開放 host）      |
| `npm run build`           | 生產環境建置                                            |
| `npm run preview`         | 用 Wrangler 預覽 Cloudflare Pages 建置結果（port 4173） |
| `npm run check`           | `svelte-check` + TypeScript 型別檢查                    |
| `npm run lint`            | Prettier 格式檢查 + ESLint                              |
| `npm run format`          | Prettier 自動格式化                                     |
| `npm run storybook`       | 啟動 Storybook dev server（port 6006）                  |
| `npm run build-storybook` | 建置 Storybook 靜態檔案                                 |

---

## Docker 啟動

```bash
docker compose up --build
```

開啟：`http://localhost:5173/`

---

## 專案設定

### Tech Stack

| Tool         | Version                                            |
| ------------ | -------------------------------------------------- |
| SvelteKit    | ^2.50                                              |
| Svelte       | ^5（Runes 模式）                                   |
| TailwindCSS  | ^4（via `@tailwindcss/vite`）                      |
| TypeScript   | ^5                                                 |
| Vite         | ^7                                                 |
| Adapter      | `@sveltejs/adapter-cloudflare`（Cloudflare Pages） |
| Validation   | `zod` ^3                                           |
| HTTP Client  | `axios`                                            |
| Server State | `@tanstack/svelte-query`                           |
| Icons        | `@material-symbols/svg-400`                        |
| Mock         | MSW（Mock Service Worker）                         |
| UI Primitive | `bits-ui` ^2                                       |
| Variant      | `class-variance-authority`（cva）                  |
| Class Merge  | `clsx` + `tailwind-merge`（`cn()`）                |
| Storybook    | ^10（`@storybook/sveltekit`）                      |

### Commit 前自動檢查（lint-staged + husky）

每次 `git commit` 前會觸發 `.husky/pre-commit`，對 staged 檔案執行：

| 檔案類型                                                | 檢查項目                                     |
| ------------------------------------------------------- | -------------------------------------------- |
| `*.ts`, `*.js`, `*.svelte`                              | **ESLint**                                   |
| `*.ts`, `*.js`, `*.svelte`, `*.css`, `*.html`, `*.json` | **Prettier**（`--check` 只驗證，不自動修改） |

> 請先執行 `npm run format` 再 commit。

---

## 詳細設定

### ESLint 規則

- **Svelte**：`eslint-plugin-svelte`（Svelte 5 Runes 語法）
- **TypeScript**：`typescript-eslint` 嚴格模式
- **TanStack Query**：`@tanstack/eslint-plugin-query`（`flat/recommended-strict`）— 防止常見的 Query 使用錯誤，例如 `queryKey` 不穩定、Hook 在條件式內使用等
- **Import 路徑限制**：單向資料流，`features` 不能引入 `routes`；`components`/`hooks`/`lib`/`types`/`utils` 不能引入 `features` 或 `routes`

詳見 `eslint.config.js`。

---

## UI 元件系統

```
src/components/ui/<component>/      ← Primitive（bits-ui 包裝 + cva 樣式）
src/features/<feature>/components/  ← Feature 元件（組合 Primitive）
```

- **bits-ui** — headless UI primitive，負責無障礙行為
- **cva** — 管理樣式變體；`cn()` (`src/utils/cn.ts`) 合併 class
- **Storybook** — 每個 Primitive 旁放 `*.stories.svelte`，`npm run storybook` 啟動

### Axios Client

詳見 `src/lib/api-client.ts`。

### TanStack Query Client

詳見 `src/lib/query-client.ts`，掛載於 `src/routes/+layout.svelte` 的 `<QueryClientProvider>`。

開發環境會顯示 **SvelteQueryDevtools**（production build 自動移除）。

### API Module 慣例（`api/<>.ts`）

每個 API 模組按以下四段結構組織：

```
1. Zod Schema & TypeScript Types
2. Fetcher Function          — 呼叫 axios，回傳 parse 後的資料
3. Query/Mutation Options    — 若有共用設定才填寫
4. Hook                      — export 供頁面元件使用的 createMutation / createQuery
```

頁面元件只需引入 `useXxx()` hook，不直接操作 axios 或 fetch。
