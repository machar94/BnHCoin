# Resource: https://cryptobook.nakov.com/digital-signatures/rsa-sign-verify-examples


from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii


# Generate 1024-bit RSA key pair (private + public key)
key_pair = RSA.generate(bits=1024)
pub_key = key_pair.publickey()

# Sign the message using the PKCS#1 v1.5 signature scheme (RSASP1)
msg = 'Message for RSA signing'.encode()
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key_pair)
signature = signer.sign(hash) # output is bytes
# 1024-bit digital signature
print('Signature: ', binascii.hexlify(signature))

# Verify valid PKCS#1 v1.5 signature (RSAVP1)
msg = 'Message for RSA signing'.encode()
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pub_key)
try:
    verifier.verify(hash, signature)
    print('Signature is valid.')
except:
    print('Signature is invalid')

# Verify invalid PKCS#1 v1.5 signature (RSAVP1)
msg = 'A tampered message'.encode()
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pub_key)
try:
    verifier.verify(hash, signature)
    print('Signature is valid.')
except:
    print('Signature is invalid')
