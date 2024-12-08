from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
a = 1
browser = webdriver.Chrome()
browser.get("https://auth.truckstop.com/as/authorize?client_id=7a99fb37-0cbd-4526-a557-bd283b9e9cf4&redirect_uri=https%3A%2F%2Fapp.truckstop.com%2FLanding%2FPingExternalLoginCallback&response_type=code%20id_token%20token&state=OpenIdConnect.AuthenticationProperties%3DkeO0mHKkZBNImEVpomOQfyWqtekWMJjSIIpiInYcQXoyA6yO62z_6_sbz5rdW25p6Dr_m7p_O-jVzlGjFx4OlK-aejvnPV0MAnZ6hrSTEYDpUB1pLhg6Ipmemqsosrq5Y8GXawpSDcEUtnU4g2qYH-m_pUPX3f3G0EiDanuaaxasvDS117Hn6ndeBwcMCmPlJxNIdbiqPInkKfjh_1HX48YdibwPHRueA45_zPlURe95KnjgtPtEL1t2TajDkFlmKafotA&response_mode=form_post&nonce=638669676049990409.YzE1MzhkMDMtY2Y1My00OTM1LWFiNGEtODA1ZmQ3NTZhZjJjNDMyZGEyYzktMGU2MS00N2JkLWE1MzctMmJhNjVjYWRkNTQ0&x-client-SKU=ID_NET461&x-client-ver=7.0.1.0")
#class="ag-center-cols-container"
while True:
    if a == 1:
        a = 1
        # find_element_by_id


