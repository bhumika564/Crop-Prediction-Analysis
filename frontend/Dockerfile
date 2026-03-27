# Stage 1: Build the React Application (Use Node for building)
FROM node:18-alpine as builder
WORKDIR /app
# Dependencies files copy karein
COPY package.json .
COPY package-lock.json .
RUN npm install
# Source code copy karein aur production build chalaayein
COPY . .
RUN npm run build

# Stage 2: Serve the Built Application using a lightweight Nginx server
FROM nginx:alpine
# Purani default Nginx config hataayein
RUN rm /etc/nginx/conf.d/default.conf
# Custom Nginx config copy karein (jo hum agle step mein banaayenge)
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf 
# Built React static files ko Nginx public folder mein copy karein
COPY --from=builder /app/dist /usr/share/nginx/html

# Port 80 exposed
EXPOSE 80 
CMD ["nginx", "-g", "daemon off;"]