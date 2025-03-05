import google.generativeai as genai
from google.colab import userdata

genai.configure(api_key=userdata.get('GOOGLE_API_KEY')) # for Google Colab

model = genai.GenerativeModel('gemini-1.5-flash-8b')

def complete_text(prompt):
    """
    Google AI'nın Gemini modelini kullanarak metin tamamlama işlemi yapar.

    Parametreler:
        prompt (str): Tamamlanacak giriş metni

    Dönüş:
        str: Yapay zeka tarafından oluşturulan metin
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def main():
    """
    Metin tamamlama arayüzünü yöneten ana fonksiyon.
    Kullanıcıların metin girişi yapmasını ve yapay zeka
    tarafından tamamlanan metinleri almalarını sağlar.
    """
    print("Metin tamamlama uygulamasına hoş geldiniz!")
    print("Çıkmak için 'çıkış' yazabilirsiniz.\n")

    while True:
        prompt = input("Lütfen bir metin girin: ")

        if prompt.lower() == "çıkış":
            print("Uygulamadan çıkılıyor...")
            break

        completed_text = complete_text(prompt)
        print("\nTamamlanan Metin:")
        print(f"{prompt} {completed_text}")
        print("-" * 50 + "\n")

if __name__ == "__main__":
    main()
