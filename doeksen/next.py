import requests
import json

# input = """{"bookingFlow":"ONEWAY","process":{"enteredSteps":["Route","SearchDateOutbound","SearchDateInbound","Passengers","Vehicles","DeparturesOutbound"],"created":false,"paid":false,"processStartedAtStep":"Route"},"productCode":"WEBENK","route":{"portCodeFrom":"H","portCodeTo":"T","isEmpty":false},"isReturnJourney":false,"searchDateOutbound":"2023-12-10T01:00:00+01:00","searchDateInbound":null,"passengers":{"groupType":"None","categories":[{"categoryCode":"V","quantity":1}],"quantity":1},"departureCodeOutbound":null,"departureCodeInbound":null,"luggage":[],"carbonNeutral":false,"extras":[],"offer":{"type":"None","productCode":null},"coupon":{"couponCode":null,"codeNotApplicable":false,"productCode":null,"containsCategoryCode":false,"couponRemoved":false,"couponRemovedMessage":null,"showCouponInput":false},"terms":{"agreeToTerms":false,"agreeToTermsCovid19":false},"promotionCode":null,"bookingCode":null,"customerLoggedOutDueToError":false,"session":{"sessionId":"c0dbe616-c44c-4afb-8fad-1e7702638720","expiry":"2023-12-06T21:48:47.293Z"},"metadata":null,"isCopy":false,"customer":{"agentCode":null,"agentName":null,"customerCode":null,"newCustomer":false,"isBookingAgent":false,"isAgent":false,"isDebiteur":false,"customerType":"Guest","hasLinkedCustomers":false,"bearerToken":null,"bearerTokenLifeTime":0,"websiteUser":null,"subscribedToNewsLetter":false,"carbonNeutralPreferenceAvailable":false,"carbonNeutralPreference":false,"customerInfo":null,"vehicleInfo":null,"session":{"sessionId":null,"expiry":"0001-01-01T00:00:00+01:00"},"subscriptionPeriod":null,"loggedInDuringBooking":false,"membershipExpiry":null,"validation":null,"guestType":null,"isAutoPas":false,"isEmployee":false,"isIslander":false,"isStudent":false,"isBusinessFrequentTraveler":false,"isFamilyFrequentTraveler":false,"isFrequentTraveler":false,"isForens":false,"isPassHolder":false,"hasSubscription":false,"hasMembership":false,"isLoggedIn":false,"isLinkedCustomer":false,"canEditCustomerInfo":true,"membershipPeriod":null},"payment":{"expiryTime":null,"loyaltyPoints":0,"type":null,"issuer":null,"extPayId":null,"paymentCompletedUrl":null,"eTicketPaymentFailed":false},"modify":{"isModifying":false,"loadedSteps":[],"originalShoppingBasket":null},"vehicles":[{"type":"None","subType":null,"quantity":0,"licensePlate":null,"licensePlateChecked":false,"licensePlateSkipped":false,"options":[]}]}"""

headers = {
    'User-Agent': 'openOV/1.0',
    'From': 'ndovloket+doeksen@opengeo.nl'  # This is another valid field
}

"""
curl 'https://api-2021.rederij-doeksen.nl/bookingProcess/DeparturesOutbound/shoppingBasket' \
  -H 'authority: api-2021.rederij-doeksen.nl' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'accept-language: nl' \
  -H 'content-type: application/json' \
  -H 'origin: https://www.rederij-doeksen.nl' \
  -H 'referer: https://www.rederij-doeksen.nl/' \
  -H 'sec-ch-ua: "Chromium";v="115", "Not/A)Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'snkwr-siteid: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36' \
  -H 'website-sessionid: f1fe0c9f-1cac-4d1a-bede-6c5d688946d9' \
  --data-raw '{"bookingFlow":"ONEWAY","process":{"enteredSteps":["Route","SearchDateOutbound","SearchDateInbound","Passengers","Vehicles","DeparturesOutbound"],"created":false,"paid":false,"processStartedAtStep":"Route"},"productCode":"WEBENK","route":{"portCodeFrom":"H","portCodeTo":"T","isEmpty":false},"isReturnJourney":false,"searchDateOutbound":"2023-12-08T01:00:00+01:00","searchDateInbound":null,"passengers":{"groupType":"None","categories":[{"categoryCode":"V","quantity":1}],"quantity":1},"departureCodeOutbound":null,"departureCodeInbound":null,"luggage":[],"carbonNeutral":false,"extras":[],"offer":{"type":"None","productCode":null},"coupon":{"couponCode":null,"codeNotApplicable":false,"productCode":null,"containsCategoryCode":false,"couponRemoved":false,"couponRemovedMessage":null,"showCouponInput":false},"terms":{"agreeToTerms":false,"agreeToTermsCovid19":false},"promotionCode":null,"bookingCode":null,"customerLoggedOutDueToError":false,"session":{"sessionId":"c0dbe616-c44c-4afb-8fad-1e7702638720","expiry":"2023-12-06T21:36:20.171Z"},"metadata":null,"isCopy":false,"customer":{"agentCode":null,"agentName":null,"customerCode":null,"newCustomer":false,"isBookingAgent":false,"isAgent":false,"isDebiteur":false,"customerType":"Guest","hasLinkedCustomers":false,"bearerToken":null,"bearerTokenLifeTime":0,"websiteUser":null,"subscribedToNewsLetter":false,"carbonNeutralPreferenceAvailable":false,"carbonNeutralPreference":false,"customerInfo":null,"vehicleInfo":null,"session":{"sessionId":null,"expiry":"0001-01-01T00:00:00+01:00"},"subscriptionPeriod":null,"loggedInDuringBooking":false,"membershipExpiry":null,"validation":null,"guestType":null,"isAutoPas":false,"isEmployee":false,"isIslander":false,"isStudent":false,"isBusinessFrequentTraveler":false,"isFamilyFrequentTraveler":false,"isFrequentTraveler":false,"isForens":false,"isPassHolder":false,"hasSubscription":false,"hasMembership":false,"isLoggedIn":false,"isLinkedCustomer":false,"canEditCustomerInfo":true,"membershipPeriod":null},"payment":{"expiryTime":null,"loyaltyPoints":0,"type":null,"issuer":null,"extPayId":null,"paymentCompletedUrl":null,"eTicketPaymentFailed":false},"modify":{"isModifying":false,"loadedSteps":[],"originalShoppingBasket":null},"vehicles":[{"type":"None","subType":null,"quantity":0,"licensePlate":null,"licensePlateChecked":false,"licensePlateSkipped":false,"options":[]}]}' \
  --compressed
"""

def flatten(departure):
    return {'code': departure['code'], 'departure': departure['departureDateTime'], 'arrival': departure['arrivalDateTime'], 'duration': departure['duration'], 'vesselName': departure['vesselName'], 'vessel': departure['vessel'], 'from': departure['portFrom']['code'], 'to': departure['portTo']['code']}

import datetime
import csv
from_date = datetime.date.today()
session = requests.Session()


# input = """{"isOutbound":false,"isInbound":false,"portFrom":{"code":"H","name":"Harlingen","data":null},"portTo":{"code":"T","name":"Terschelling","data":null},"searchDate":"2023-12-08T01:00:00+01:00"}"""
# input = json.loads(input)

import time

with open('scrape-output/doeksen-{}.csv'.format(from_date.isoformat().replace('-', '')), 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['code','departure','arrival','duration','vesselName','vessel','from','to'])
    writer.writeheader()

    nomoredata = False
    for i in range(1, 60):
        today = from_date + datetime.timedelta(days=i)
        departure_date = datetime.datetime.combine(today, datetime.time.min).isoformat() + "Z"
        for f in ('H', 'V', 'T'):
            for t in ('H', 'V', 'T'):
                if f != t:
                    document = session.get(f"https://api-2021.rederij-doeksen.nl/departures/{f}/{t}/{departure_date}",
                                           headers=headers).json()

                    if 'departures' in document:
                        for departure in document['departures']:
                            flattened = flatten(departure)
                            if flattened['duration'] > 200:
                                print("..")
                            writer.writerow(flattened)
                        csvfile.flush()
                    else:
                        nomoredata = True
                    time.sleep(0.200)

        if nomoredata:
            break
"""
document = session.get("https://api-2021.rederij-doeksen.nl/departures/H/V/2023-12-10T00:00:00.000Z", headers=headers)
hv = document.json()

document = session.get("https://api-2021.rederij-doeksen.nl/departures/H/T/2023-12-10T00:00:00.000Z", headers=headers)
ht = document.json()

document = session.get("https://api-2021.rederij-doeksen.nl/departures/T/H/2023-12-10T00:00:00.000Z", headers=headers)
th = document.json()

document = session.get("https://api-2021.rederij-doeksen.nl/departures/T/V/2023-12-10T00:00:00.000Z", headers=headers)
tv = document.json()

document = session.get("https://api-2021.rederij-doeksen.nl/departures/V/H/2023-12-10T00:00:00.000Z", headers=headers)
vh = document.json()

document = session.get("https://api-2021.rederij-doeksen.nl/departures/V/T/2023-12-10T00:00:00.000Z", headers=headers)
vt = document.json()
"""

#  document = session.post("https://api-2021.rederij-doeksen.nl/departures/availability", json=input, headers=headers)
# document = document.json()



print("...")
