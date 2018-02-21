openssl genrsa -out /certs/rsa_private_key.pem 1024
echo -e "\n================= private key =================\n"
cat rsa_private_key.pem
rsa -in rsa_private_key.pem -pubout -out /certs/rsa_public_key.pem
echo -e "\n================== public key =================\n"
cat rsa_public_key.pem