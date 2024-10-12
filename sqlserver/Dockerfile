# First stage: Install required packages
FROM ubuntu:22.04 AS builder

# Install tools needed for installation
RUN apt-get update && apt-get install -y \
    curl apt-transport-https \
    gnupg2

# Add Microsoft GPG key and repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools unixodbc-dev && \
    rm -rf /var/lib/apt/lists/*

# Second stage: Use SQL Server image and copy the installed tools
FROM mcr.microsoft.com/mssql/server:2022-latest

# Copy tools from the builder stage
COPY --from=builder /opt/mssql-tools /opt/mssql-tools
# COPY --from=builder /usr/lib/x86_64-linux-gnu/odbc/* /usr/lib/x86_64-linux-gnu/odbc/

# Set environment variables
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourPassword123!

# Expose SQL Server port
EXPOSE 1433

# Set the default user to 'mssql'
USER mssql
