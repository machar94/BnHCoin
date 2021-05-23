from ecdsa import SigningKey, VerifyingKey, SECP256k1
from ecdsa.keys import BadSignatureError
import hashlib

# Resource: https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-examples
 

# ECDSA sign message (using the curve secp256k1 + SHA3-256)
msg = 'Message for ECDSA signing'.encode('utf8')
signing_key = SigningKey.generate(curve = SECP256k1)
signature = signing_key.sign_deterministic(msg, hashfunc=hashlib.sha3_256)
print('Message: ', msg)
print('Private key: ', signing_key.to_string().hex())
print('Private key size (bits): ', len(signing_key.to_string() * 8))
print('Signature: ', signature.hex())
print('Signature size (bits): ', len(signature) * 8)


# ECDSA verify signature (using the curve secp256k1 + SHA3-256)
verifying_key = signing_key.verifying_key
print('\nMessage: ', msg)
print('Public Key: ', verifying_key.to_string().hex())
try:
    valid = verifying_key.verify(signature, msg, hashfunc=hashlib.sha3_256)
    print('Signature valid: ', valid)
except BadSignatureError:
    print('Signature verification failed!')


# ECDSA verify tampered signature (using the curve secp256k1 + SHA3-256)
msg = 'Tampered ECDSA Message'.encode('utf8')
print('\nMessage: ', msg)
try:
    valid = verifying_key.verify(signature, msg, hashfunc=hashlib.sha3_256)
    print('Signature valid: ', valid)
except BadSignatureError:
    print('Signature verification failed!')

# Identify possible public keys from signature and hash
msg = 'Message for ECDSA signing'.encode('utf8')
keys = VerifyingKey.from_public_key_recovery(signature, msg, SECP256k1, hashfunc=hashlib.sha3_256)
print('Possible public keys:')
for key in keys:
    print(key.to_string().hex())

# Write keys to file
pem = signing_key.to_pem()
with open('private.pem', 'wb') as file:
    file.write(pem)

pem = verifying_key.to_pem()
with open('public.pem', 'wb') as file:
    file.write(pem)