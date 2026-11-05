FROM nginx:alpine

# Update Alpine packages to patched versions
RUN apk upgrade --no-cache

COPY index.html /usr/share/nginx/html/index.html
