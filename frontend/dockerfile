FROM node:20-alpine
WORKDIR /app
RUN corepack enable
COPY package.json package-lock.json* ./
RUN pnpm install
COPY . .
EXPOSE 3000