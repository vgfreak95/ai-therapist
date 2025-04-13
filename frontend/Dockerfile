ARG NODE_VERSION=22

FROM node:${NODE_VERSION}-slim as base

ARG PORT=3000

WORKDIR /src

# Build
FROM base as build

COPY ./package.json ./

RUN npm install

COPY . .

RUN npm run build

# Run
FROM base

ENV PORT=$PORT
ENV NODE_ENV=production

COPY --from=build /src/.output /src/.output

CMD [ "node", ".output/server/index.mjs" ]
