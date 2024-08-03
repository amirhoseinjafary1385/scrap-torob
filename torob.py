
#Light_Phoneixx
#Email:amirhoseinjafary85@gmail.com
#====================================
import requests
from bs4 import BeautifulSoup

# پیام خوش آمدید
print("خوش آمدید...")

# بررسی اتصال اینترنت
try:
    requests.get("https://www.torob.com", timeout = 5)
except (requests.ConnectionError, requests.Timeout):
    print("اینترنت شما تمام شده است...")
else:

    #پروتِنی
    urls = [
    #URL 1
        "https://torob.com/browse/506/%D9%BE%D8%B1%D9%88%D8%AA%DB%8C%D9%86%DB%8C/",
    #URL 2
        "https://torob.com/browse/2449/%D9%81%D8%B1%D9%87%D9%86%DA%AF%DB%8C-%D9%88-%D8%A7%D9%85%D9%88%D8%B2%D8%B4%DB%8C/"
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
for url in urls:
        
    fetch = requests.get(url, headers=headers)

    print(fetch.status_code, fetch.content)
    # بررسی وضعیت پاسخ و نمایش پیام مناسب
    if fetch.status_code == 200:
        print("Connected")
    else:
        print(f"Failed to connect: {fetch.status_code}")

    # بررسی وضعیت پاسخ و ثبت پیام موفقیت
    if fetch.status_code == 200:
        print(f"محتوا از {url} با موفقیت دریافت شد.")
    else:
        print(f"محتوا از {url} با موفقیت دریافت نشد.")

    soup = BeautifulSoup(fetch.text, 'html.parser')

    # بررسی وضعیت پاسخ
    # print(f"Status Code: {fetch.status_code}")

    # چاپ محتوای HTML برای بررسی

    print(soup.prettify())

    # فرض کنید که محصولات در تگ‌های خاصی قرار دارند

    products = soup.find_all('div', class_='product-item')

if not products: 
    print("هیچ محصولی یافت نشد...")

else:
    for product in products:
        # استفاده از get_text برای حذف فضاهای اضافی
        title = product.find('h2', class_='product-title').text.strip() 
        price = product.find('span', class_ = 'product-price').get_text(strip=True)
        print(f'product:{title}, Price:{price}')
        
    print("\n\n\n\n\n\n\n data data data ")