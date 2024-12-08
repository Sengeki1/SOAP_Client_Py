from zeep import Client

client = Client("http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL")

capital = client.service.CapitalCity('CV')
coin = client.service.CountryCurrency('CV')

print(f"Capital: {capital} and Coin: {coin['sName']}")
