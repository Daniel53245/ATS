FROM node:20-slim

# Set working directory
WORKDIR /app

# Install dependencies separately to optimize cache
COPY package*.json /app
RUN npm install --silent

# Copy all other files
COPY . /app

# Expose dev server port
EXPOSE 3000

# Start Vite dev server (listen on all interfaces so it's accessible from host)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
