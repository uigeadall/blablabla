FROM library/debian:bookworm-slim
USER root

# Install necessary system packages (including Python)
RUN mkdir -p /opt/project/upload
WORKDIR /opt/project

# Install system dependencies and Python
COPY debian_packages.txt /opt/project/debian_packages.txt
RUN apt-get update --allow-insecure-repositories && \
    DEBIAN_FRONTEND=noninteractive xargs -a /opt/project/debian_packages.txt \
    apt-get install -y --allow-unauthenticated python3 python3-pip && \
    apt-get clean && \
    rm -rf /opt/project/debian_packages.txt

# Install Python dependencies (requests, pytest, etc.)
COPY requirements.txt /opt/project/requirements.txt
RUN pip3 install --no-cache-dir -r /opt/project/requirements.txt

# Unset because of https://github.com/psf/requests/issues/3829
ENV REQUESTS_CA_BUNDLE=

# Ignore warnings during requests calls
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

# Set the mock hostname
ENV MOCK_HOSTNAME=api-mock-server

# Copy the certificate generation scripts
COPY rsa-cert-generation/create_certs.sh /root/ca/rsa/create_certs.sh
COPY rsa-cert-generation/root-openssl.conf /root/ca/rsa/openssl.cnf
COPY rsa-cert-generation/intermediate-openssl.conf /root/ca/rsa/intermediate/openssl.cnf

# Copy the application and bin directories
COPY app /opt/project/
COPY bin /opt/project/

# Generate the SSL certificates
RUN /root/ca/rsa/create_certs.sh

# Copy the test scripts (optional, depending on where you store them)
COPY tests /opt/project/tests

# Entry point to run your server or start script
ENTRYPOINT ["/opt/project/start.sh"]