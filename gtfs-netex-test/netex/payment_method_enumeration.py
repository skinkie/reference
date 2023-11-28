from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PaymentMethodEnumeration(Enum):
    """
    Allowed values for Payment method.

    :cvar CASH: Payment in coins or notes accepted.
    :cvar CASH_EXACT_CHANGE_ONLY: Payment in coins or notes accepted,
        must be exact amount.
    :cvar CASH_AND_CARD: Payment with either cash or debit / credit card
        accepted.
    :cvar COIN: Payment in specie (coins) only.
    :cvar BANKNOTE: Payment in cash with banknotes (but no coins).
    :cvar CHEQUE: Payment with personal Bankers' cheque.
    :cvar TRAVELLERS_CHEQUE: Payment with Traveller's cheque.
    :cvar POSTAL_ORDER: Payment by Postal order.
    :cvar COMPANY_CHEQUE: Payment with Company cheque.
    :cvar CREDIT_CARD: Payment by credit card  (E.g. Visa, MasterCard,
        etc).
    :cvar DEBIT_CARD: Payment by Bank debit  card.
    :cvar CARDS_ONLY: Paymentonly with debit or credit card (no cash).
    :cvar TRAVEL_CARD: Payment with stored value travel card or
        smartcard.
    :cvar CONTACTLESS_PAYMENT_CARD: NFC Payment by contactless credit or
        debit card
    :cvar CONTACTLESS_TRAVEL_CARD: NFC Payment with stored value travel
        card or smartcard .
    :cvar DIRECT_DEBIT: Electronic payment by direct debit at retailers
        request from customer's bank account .
    :cvar BANK_TRANSFER: Electronic payment from customer account to
        retailers account.
    :cvar EPAY_DEVICE: Electronic payment with on device  application
        (e.g. ApplePay, GooglePay etc).
    :cvar EPAY_ACCOUNT: Electronic payment direct from account (e.g.
        PayPal etc).
    :cvar SMS: Payment by SMS charge to mobile account.
    :cvar MOBILE_PHONE: Payment with mobile device  / mobile app. [Use
        more specific MOBILE app]
    :cvar MOBILE_APP: Payment with mobile device  / mobile app. +v1.2.2
    :cvar VOUCHER: Payment with coupons or vouchers.
    :cvar TOKEN: Payment with physical tokens.
    :cvar WARRANT: Payment with warrant issued by an organisation (e.g.
        Army, government).
    :cvar MILEAGE_POINTS: Payment in mileage points.
    :cvar OTHER: Other means of payment .
    """
    CASH = "cash"
    CASH_EXACT_CHANGE_ONLY = "cashExactChangeOnly"
    CASH_AND_CARD = "cashAndCard"
    COIN = "coin"
    BANKNOTE = "banknote"
    CHEQUE = "cheque"
    TRAVELLERS_CHEQUE = "travellersCheque"
    POSTAL_ORDER = "postalOrder"
    COMPANY_CHEQUE = "companyCheque"
    CREDIT_CARD = "creditCard"
    DEBIT_CARD = "debitCard"
    CARDS_ONLY = "cardsOnly"
    TRAVEL_CARD = "travelCard"
    CONTACTLESS_PAYMENT_CARD = "contactlessPaymentCard"
    CONTACTLESS_TRAVEL_CARD = "contactlessTravelCard"
    DIRECT_DEBIT = "directDebit"
    BANK_TRANSFER = "bankTransfer"
    EPAY_DEVICE = "epayDevice"
    EPAY_ACCOUNT = "epayAccount"
    SMS = "sms"
    MOBILE_PHONE = "mobilePhone"
    MOBILE_APP = "mobileApp"
    VOUCHER = "voucher"
    TOKEN = "token"
    WARRANT = "warrant"
    MILEAGE_POINTS = "mileagePoints"
    OTHER = "other"
