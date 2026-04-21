# --- Dev ---
FROM node:22

WORKDIR /app

COPY package.json package-lock.json* pnpm-lock.yaml* ./
RUN npm ci

COPY . .
RUN npx svelte-kit sync

EXPOSE 5173

CMD ["npm", "run", "dev:local"]