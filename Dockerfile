# use Debian image with uv, no need for system Python
FROM ghcr.io/astral-sh/uv:debian as build

# explicit work dir is important
WORKDIR /src

# copy all files
COPY . .

# install Python with uv
RUN uv python install 3.13

# run build process
RUN uv run --no-sync python build.py

# serve with Caddy
FROM caddy:alpine

# copy Caddy config
COPY Caddyfile /etc/caddy/Caddyfile

# copy generated static site
COPY --from=build /src/output /srv/

