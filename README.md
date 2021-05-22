# Overview

A webserver to interact with a blockchain.

![Home Page](imgs/homepage.png)

## Installation instructions

Use pip to install pipenv.

``` zsh
pip install pipenv
```

Create a pip environment in the root of the repository. This will install the necessary packages.

``` zsh
pipenv install
```

Activate the pipenv.

``` zsh
pipenv shell
```

### Create database

In the bnhcoin folder open a python interpreter and run the following:

``` python
>>> from app import db
>>> db.create_all()
```

You should notice that a site.db file has been created in the folder.

### Web Server

Create a Heroku account and install the [CLI](https://devcenter.heroku.com/articles/heroku-cli) tools.

Login in and follow the instructions.

``` zsh
heroku login
```

Create a web app. Heroku looks at the Procfile to see what to run once the repository is pushed.

``` zsh
heroku create [web-app-name]
```

Check to see that heroku is listed as a remote.

``` zsh
git remote -v
```

Push the app. Open the link displayed in the terminal in a browser.

``` zsh
git push heroku master
```

## Updating the web app

If you want to add a new package to the pipenv environment run the following command and it will be added to the Pipfile.

``` zsh
pipenv install [package]
```

Then update the web app.

``` zsh
git add .
git commit -m "commit message"
git push heroku master
```

## Security

Digital signatures are used in the application to verify that transactions being sent are not tampered, authenticate who sent a transaction, and prevent users from retracting transactions (once a transaction has been signed and broadcast, it is final). Signature algorithms include RSA, ECDSA (Elliptic Curve Digital Signature Algorithm) and EdDSA (Edwards-curve Digital Signature Algorithm). ECDSA is preferred over RSA because of shorter key lengths, shorter signature lengths, and higher security levels for the same key length. As an example a 3072-bit RSA signature has the same security strenght as a 256-bit ECDSA signature.

See blockchain.generateKeys for details on how RSA is used to generate public and private keys.

An example private key.

```text
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAnl3pGVH9wEb3WPWjcHUt7V6NK2AXycLdGFhai/2UqF8nOnLp
TLCPBpoOqqhTwTuVji/+4SCx8AUGLM5K1onhX/LZ0f2dI439l7XidsC3cvrKR55h
o+gj7/NwSsCuizyVJLknPR7LPYbfMCGf4K9RHQLthEAnpWBaJ2/H5tQF8OZTttxL
4MJhpIZdC5Mo8aKXRamWQLMfHyVxrwdvKoJSCyI5GoE8tD8ESumiuUC+setoRavU
H+y6YVmlqOpH9aqXw68IcMgiWonLfWfHc0fHzFh7Ln28HMqg9NGdQVM78fAioJ/f
ja4O05me6F2ze+Rbvh1AoGRMcilZvBIlsW+2zwIDAQABAoIBADRQT10G4azvhGvF
kPzoKIi98CJA9vq2PTT6ksaluMK51AqRxRGJTWXf5DJpsmkllqzGnAqgM0dXUYfh
iYU/PMzmOyAMCCmjkP7ZnXqfBLqdr85iulxbpetw3kpDRiVGmPntk9Gz521mrTmI
Efk10LSlr/I9Axu1LXLTkRRmO6Qs3LX6rkaww9AB6HcmtZKTe05PDM6dReOtEGXU
5SOA7tH1PJfqcy0wPfjJXxPyzhR/LlC5YVwt1IjIaCUZILZMq3dcB4hXxJyoJ2ma
uV4TlhpK7ffC7Niif3k8f/7bO2p6DJVsX/u3Uv788cqx09FiclHKYdnKwV1HHHmm
wW+P+DECgYEAxmzB/Q3j3htg0VWVq1HSRcXH41wQgdGG7egBa0xlWi4J0LEmHIjL
3ENm2YK/TeLaZ9sbnsGwbngTZxSTcVNdg5ku5S/hCC9gM7lAvxeKqqeKtf9EYq9z
uGG7404VS7rETbWdc3tc8+NCKLAKI8L0+LWj5MSVIBPZPy2Ydie7NckCgYEAzFGY
Xxo1hzpTB/GlOFyZgsDVEXxHRaIP8IWIdRNiUXOLY00kFD4Xy1gtWg3LHz+B68hf
9hwDXMc+Hxtpy9IkAFvXK9KAMIZTCeqC4MI6DhF7N3cWAksvSxqTirqGw/U3sQYB
qRl0m3wpVcC1fX9eJL91QoDzTwn7pv5NSBzKs9cCgYEAi4rmrdj73DIy12Sx2gaz
sr/RwBH5xeIdWugjP1s9l7ryyiIa5ExL2b5I8USi1tpnsEwF05LxSe8F7iMpQbRX
+nla4nDWd9Qhep6YawraSQOEaFN5u1EaN5v773H1Rgm1jdTgQtuJ1jaHS2fp6ZZs
gw/yj6q0GRf8WxLsuoNchAkCgYAHpCmRrPZBh3Hhgy0NrZDkLfgJ/l7gAM6dzTCs
SDxOFYcqAJGP3D6hkTuo+YkWMxbVzZmhJ60MhDsTiL/tKn/EL6sdbXLz3aIvZcDd
TQZEzmyQR3jgPxWWtni8IHu3ymz5xuK7A0O0KPGWzm07M08/CpYFFbODyjjKJwqW
3tTJ4wKBgG7GCZlHimNDhocL03exeyaIMY9gZHY5F7TtM72BdKMoTOLJEoG8PWCV
xHtspYrGnpby0mwMnCeW0NWAbWwgpdcmLBWdZvhtJExXXssKs+UOgdb2hT2+n13N
IHOpduDgpmT6kvBL5jg+3LISTmtBnw3B+EB893HWcZzxGjYYNIQ/
-----END RSA PRIVATE KEY-----
```

An example public key.

```text
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1KXx2UXNnJFn2iUjCmYg
mS1nxr1pqVtvbi78r93vt6Oe/lCO5SKk0A+Ly92zIZWgx5CDOND7/qEZwKHKkHRC
RY5i4fBem+AImHSefzdjLmbzsmv8auXdhYjk8lSePavDqaTFoAAFhjeFzaTPMDij
S8mdIsrLwfQY0Cm4BVR5KW53BTsxsRg1TcROLxxWDHN/pvhcxobZsP6Syj9Rk5LF
OHhgfMOTMDBm7QLQfyetle+R+HkKIwld8oYGbr0NlrXHiiRpJCcP/ztZXuG8FCe+
Mr1HFu+iJrysHhtH+bBwWznFViWrjHYMrTcuqNubHfVox8oVpd4o8xXNB/kuLB/1
YQIDAQAB
-----END PUBLIC KEY-----
```
