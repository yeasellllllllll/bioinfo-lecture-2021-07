#! /usr/bin/env python

class Account:
    account_count = 0

    def __init__(self, balance, password):
        self.__balance = balance
        self.__password = password
        self.bank = 'SC은행'

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount): #입금
        if amount >= 1:
            self.showBalance.append(amount)
            self.__balance += amount
    def whithdraw(self, amount): #출금
        if self.__balance > amount:
            self.showBalance.append(amount)
            self.__balance -= amount
    def transfer(self, accountTo, amount): #받는 계좌 추가 필요!
        if amount >= 1:
            accountFrom.showBalance.append(amount)
            self.__balance -= amount
            accountTo.__balance += amount
    def showBalance(self):
        for amount in self.showBalance:
            print(amount)


