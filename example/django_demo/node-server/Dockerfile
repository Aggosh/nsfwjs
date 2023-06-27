FROM --platform=linux/arm64/v8 node:buster-slim as builder
WORKDIR /usr/app
RUN npm install -g pnpm
ADD node-server/pnpm-lock.yaml .
ADD node-server/package.json .
RUN pnpm install
COPY node-server/ .
RUN pnpm build

FROM --platform=linux/arm64/v8 node:buster-slim
WORKDIR /app
RUN npm install -g pnpm
COPY --from=builder /usr/app /app/
EXPOSE 3333
