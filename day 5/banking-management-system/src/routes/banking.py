from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.account import Account
from ..models.transaction import Transaction
from ..models.user import User

banking_bp = Blueprint('banking', __name__)

@banking_bp.route('/account/<int:user_id>')
def account_details(user_id):
    account = Account.get_account_by_user_id(user_id)
    transactions = Transaction.get_transactions_by_account_id(account.id)
    return render_template('dashboard.html', account=account, transactions=transactions)

@banking_bp.route('/deposit', methods=['POST'])
def deposit():
    user_id = request.form.get('user_id')
    amount = float(request.form.get('amount'))
    account = Account.get_account_by_user_id(user_id)
    if amount > 0:
        account.deposit(amount)
        flash('Deposit successful!', 'success')
    else:
        flash('Invalid deposit amount.', 'danger')
    return redirect(url_for('banking.account_details', user_id=user_id))

@banking_bp.route('/withdraw', methods=['POST'])
def withdraw():
    user_id = request.form.get('user_id')
    amount = float(request.form.get('amount'))
    account = Account.get_account_by_user_id(user_id)
    if 0 < amount <= account.balance:
        account.withdraw(amount)
        flash('Withdrawal successful!', 'success')
    else:
        flash('Invalid withdrawal amount.', 'danger')
    return redirect(url_for('banking.account_details', user_id=user_id))