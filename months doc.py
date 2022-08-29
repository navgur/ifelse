months=input("enter the number=")
if months == "january" or months=="march" or months=="may" or months=="july" or months=="december":
    print("31")
elif months=="feb":
    print("28")
elif months=="april" or months=="june" or months=="august" or months=="auctober":
    print("30 days")
else:
    print("wrong")

