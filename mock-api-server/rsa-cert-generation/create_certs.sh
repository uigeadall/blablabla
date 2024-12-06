#!/usr/bin/env bash

##################################################################################################
# ROOT CA
# Using home directory instead of /root
mkdir -p ~/ca/rsa/certs ~/ca/rsa/csr ~/ca/rsa/newcerts ~/ca/rsa/private ~/ca/rsa/volumed_dir
#Read and write to root in private folder
chmod 700 ~/ca/rsa/private
touch ~/ca/rsa/index.txt
#Echo the user id
echo 1000 > ~/ca/rsa/serial
echo 1000 > ~/ca/rsa/crlnumber
#Generating the root key for the Certificate Authority | For simplicity without passphrase for usage within docker
openssl genrsa -out ~/ca/rsa/private/ca.key.pem 4096
#Read-only rights to the running user
chmod 777 ~/ca/rsa/private/ca.key.pem
#Now let's create the certificate for the authority and pass along the subject as will be ran in non-interactive mode
openssl req -config ~/ca/rsa/openssl.cnf \
      -key ~/ca/rsa/private/ca.key.pem \
      -new -x509 -days 3650 -sha256 -extensions v3_ca \
      -out ~/ca/rsa/certs/ca.cert.pem \
      -subj "/C=UA/ST=Rivne/L=Rivne/O=SoftServerAcademy/OU=Engineering/CN=SoftServer Engineering Root CA"

#Grant everyone reading rights
chmod 777 ~/ca/rsa/certs/ca.cert.pem
##################################################################################################
# INTERMEDIATE CA
#Now that we created the root pair, we should use and intermediate one.
#This part is the same as above except for the folder
mkdir -p ~/ca/rsa/intermediate/certs ~/ca/rsa/intermediate/csr ~/ca/rsa/intermediate/newcerts ~/ca/rsa/intermediate/private
chmod 700 ~/ca/rsa/intermediate/private

#We must create a serial file to add serial numbers to our certificates - This will be useful when revoking as well
echo 2000 > ~/ca/rsa/intermediate/serial
echo 2000 > ~/ca/rsa/intermediate/crlnumber
touch ~/ca/rsa/intermediate/index.txt

openssl genrsa -out ~/ca/rsa/intermediate/private/intermediate.key.pem 4096
chmod 777 ~/ca/rsa/intermediate/private/intermediate.key.pem

#Creating the intermediate certificate signing request using the intermediate ca config
openssl req -config ~/ca/rsa/intermediate/openssl.cnf \
      -key ~/ca/rsa/intermediate/private/intermediate.key.pem \
      -new -sha256 \
      -out ~/ca/rsa/intermediate/csr/intermediate.csr.pem \
      -subj "/C=UA/ST=Rivne/L=Rivne/O=SoftServerAcademy/OU=Engineering/CN=SoftServer Engineering Intermediate CA"

#Creating an intermediate certificate, by signing the previous csr with the CA key based on root ca config with the directive v3_intermediate_ca extension to sign the intermediate CSR
echo -e "y\ny\n" | openssl ca -config ~/ca/rsa/openssl.cnf \
      -extensions v3_intermediate_ca \
      -days 3650 -notext -md sha256 \
      -in ~/ca/rsa/intermediate/csr/intermediate.csr.pem \
      -out ~/ca/rsa/intermediate/certs/intermediate.cert.pem

#Grant everyone reading rights
chmod 777 ~/ca/rsa/intermediate/certs/intermediate.cert.pem
##################################################################################################
# CN = MOCK HOSTNAME
##################################################################################################
sed -i '' "s+<mock-hostname>+$MOCK_HOSTNAME+g" ~/ca/rsa/intermediate/openssl.cnf

#First generate the key for the server
openssl genrsa \
      -out ~/ca/rsa/intermediate/private/mock.key.pem 4096
chmod 777 ~/ca/rsa/intermediate/private/mock.key.pem

#Then create the certificate signing request
openssl req -config ~/ca/rsa/intermediate/openssl.cnf \
      -key ~/ca/rsa/intermediate/private/mock.key.pem \
      -new -sha256 -out ~/ca/rsa/intermediate/csr/mock.csr.pem \
      -subj "/C=UA/ST=Rivne/L=Rivne/O=SoftServerAcademy/OU=Engineering/CN=$MOCK_HOSTNAME"

#Now sign it with the intermediate CA
echo -e "y\ny\n" | openssl ca -config ~/ca/rsa/intermediate/openssl.cnf \
      -extensions leaf_cert -days 365 -notext -md sha256 \
      -in ~/ca/rsa/intermediate/csr/mock.csr.pem \
      -out ~/ca/rsa/intermediate/certs/mock.cert.pem

chmod 777 ~/ca/rsa/intermediate/certs/mock.cert.pem
##################################################################################################
# Creating chains and copy certs to the volumed_dir
##################################################################################################
#Creating certificate chain with intermediate and root
cat ~/ca/rsa/intermediate/certs/intermediate.cert.pem \
      ~/ca/rsa/certs/ca.cert.pem > ~/ca/rsa/certs/ca-chain.cert.pem
chmod 777 ~/ca/rsa/certs/ca-chain.cert.pem

#Creating full certificate chain
cat ~/ca/rsa/intermediate/certs/mock.cert.pem \
      ~/ca/rsa/intermediate/certs/intermediate.cert.pem \
      ~/ca/rsa/certs/ca.cert.pem > ~/ca/rsa/certs/full-chain.cert.pem
chmod 777 ~/ca/rsa/certs/full-chain.cert.pem

# Copy single certs to volumed_dir
cp ~/ca/rsa/certs/ca-chain.cert.pem ~/ca/rsa/volumed_dir/ca-chain.cert.pem
cp ~/ca/rsa/certs/full-chain.cert.pem ~/ca/rsa/volumed_dir/full-chain.cert.pem
cp ~/ca/rsa/certs/ca.cert.pem ~/ca/rsa/volumed_dir/ca.cert.pem
cp ~/ca/rsa/intermediate/certs/intermediate.cert.pem ~/ca/rsa/volumed_dir/intermediate.cert.pem
cp ~/ca/rsa/intermediate/certs/mock.cert.pem ~/ca/rsa/volumed_dir/mock.cert.pem
cp ~/ca/rsa/intermediate/private/mock.key.pem ~/ca/rsa/volumed_dir/mock.key.pem
