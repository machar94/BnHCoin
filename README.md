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

### Create or reset database

Run in the top level repo, run the script `reset_db.py`. You should notice that a site.db file has been created in the bnhcoin folder.

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
