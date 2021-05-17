from bnhcoin.forms import *
from bnhcoin.db_user import User
from flask import Flask, jsonify, request, render_template, url_for, flash, redirect
from bnhcoin import app, db, bcrypt, blockchain_obj
from flask_login import login_user, current_user, logout_user, login_required
from Crypto.PublicKey import RSA
import requests


@app.route("/")
@app.route("/home")
def home():
    blockchain_obj.resolveConflicts()
    return render_template('blockchain.html', title="Blockchain", blockchain=blockchain_obj)


@app.route("/blockchain")
def blockchain():
    blockchain_obj.resolveConflicts()
    return render_template('blockchain.html', title="Blockchain", blockchain=blockchain_obj)


@app.route("/transaction", methods=['GET', 'POST'])
def transaction():
    form = TransactionForm()
    formNL = TransactionFormNotLoggedIn()
    if form.validate_on_submit():
        feedback = blockchain_obj.addTransaction(
            form.sender.data, form.reciever.data, form.amount.data, form.key.data, form.key.data)
        if feedback:
            flash(f'Transaction Made!', 'success')
        else:
            flash(f'Error!', 'danger')
        return render_template('transaction.html', title="Transaction", blockchain=blockchain_obj, form=form, formNL=formNL)

    if formNL.validate_on_submit():
        return redirect(url_for('login'))

    return render_template('transaction.html', title="Transaction", blockchain=blockchain_obj, form=form, formNL=formNL)


@app.route("/minerPage")
def minerPage():
    return render_template('minerPage.html', title="Mine", blockchain=blockchain_obj)


@app.route("/node")
def node():
    return render_template('node.html', title="Node")


@app.route("/purchase")
def purchase():
    return render_template('purchase.html', title="Purchase")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Password hashing
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        keyGen = blockchain_obj.generateKeys()
        user = User(name=form.name.data, username=form.username.data,
                    password=hashed_password, key=keyGen)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        nextPage = request.args.get('next')
        flash(
            f'Account created for @{form.username.data}! You are now logged in as well.', 'success')
        return redirect(nextPage) if nextPage else redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            nextPage = request.args.get('next')
            flash(f'Welcome! You are now logged in', 'success')
            return redirect(nextPage) if nextPage else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account', blockchain=blockchain_obj)


# BLOCKCHAIN BACKEND REQUESTS
@app.route('/mine', methods=['GET'])
def mine():
    print("madeit")
    miner = request.args.get('miner', None)
    lastBlock = blockchain_obj.getLastBlock()

    if len(blockchain_obj.pendingTransactions) <= 1:
        flash(f'Not enough pending transactions to mine! (Must be > 1)', 'danger')
    else:
        feedback = blockchain_obj.minePendingTransactions(miner)
        if feedback:
            flash(
                f'Block Mined! Your mining reward has now been added to the pending transactions!', 'success')
        else:
            flash(f'Error!', 'danger')
    return render_template('minerPage.html', title="Mine", blockchain=blockchain_obj)


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'reciever', 'amt']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain_obj.addTransaction(
        values['sender'], values['reciever'], values['amt'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain_obj.chainJSONencode(),
        'length': len(blockchain_obj.chain),
    }
    return jsonify(response), 200

# blockchain_obj DECENTRALIZED NODES


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain_obj.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain_obj.nodes),
    }
    return jsonify(response), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain_obj.resolveConflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain_obj.chainJSONencode()
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain_obj.chainJSONencode()
        }

    return jsonify(response), 200
