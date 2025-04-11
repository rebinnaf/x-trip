# Use Node.js LTS version as the base image
FROM node:20-alpine

# Install pnpm
RUN corepack enable && corepack prepare pnpm@9.15.1 --activate

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json pnpm-lock.yaml ./

# Install dependencies
RUN pnpm install --frozen-lockfile

# Copy the rest of the application
COPY . .

# Build the application
RUN pnpm build

# Install a simple http server to serve static content
RUN npm install -g http-server

# Expose port 8080
EXPOSE 8080

# Start the http server
CMD ["http-server", "dist", "-p", "8080"] 