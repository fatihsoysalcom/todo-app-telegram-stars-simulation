import sys

# --- In-memory storage for todos and premium status ---
# In a real Telegram bot, this would be per-user and persisted (e.g., in a database).
# For this simulation, we'll use a single global state.
todos = []
is_premium = False
STARS_COST_FOR_PREMIUM = 100 # Example cost in Telegram Stars

def display_menu():
    print("\n--- Todo Uygulaması (Telegram Stars Simülasyonu) ---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Premium Özellikleri Görüntüle")
    print("4. Çıkış")
    print("--------------------------------------------------")

def add_task():
    global todos, is_premium
    task = input("Eklemek istediğiniz görevi girin: ").strip()
    if not task:
        print("Görev boş olamaz.")
        return

    # Illustrates a premium feature: free users have a task limit
    if not is_premium and len(todos) >= 3:
        print("Üzgünüm, ücretsiz hesaplar en fazla 3 görev ekleyebilir.")
        print("Daha fazla görev eklemek için premium hesaba geçin!")
    else:
        todos.append(task)
        print(f"'{task}' görevi eklendi!")

def list_tasks():
    global todos
    if not todos:
        print("Yapılacaklar listenizde henüz bir görev yok.")
    else:
        print("\n--- Yapılacaklar Listeniz ---")
        for i, task in enumerate(todos):
            print(f"{i+1}. {task}")
        print("----------------------------")

def show_premium_features():
    global is_premium
    if is_premium:
        print("\n🎉 Zaten premium hesapsınız! Sınırsız görev ekleyebilirsiniz.")
    else:
        print("\n🌟 Premium Özellikler! 🌟")
        print("Bu özellik, sınırsız sayıda görev eklemenizi sağlar.")
        print(f"Maliyet: {STARS_COST_FOR_PREMIUM} Telegram Stars ⭐️")
        print("\n*Bu bir simülasyondur.* Gerçek bir Telegram botunda, burada bir 'Stars ile Satın Al' düğmesi olurdu.")
        print("Bu düğme, sizi Telegram'ın kendi Stars ödeme akışına yönlendirir.")
        print("Ödeme başarılı olduğunda, botunuz bu özelliği sizin için otomatik olarak açardı.")
        
        choice = input(f"Premium hesabı {STARS_COST_FOR_PREMIUM} Stars ile satın almak ister misiniz? (e/h): ").lower()
        if choice == 'e':
            # Simulate successful payment via Telegram Stars
            is_premium = True
            print("🎉 Tebrikler! Premium hesabınız aktif edildi. Artık sınırsız görev ekleyebilirsiniz.")
        else:
            print("Premium satın alma işlemi iptal edildi.")

def main():
    while True:
        display_menu()
        choice = input("Seçiminizi yapın (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            show_premium_features()
        elif choice == '4':
            print("Uygulamadan çıkılıyor. Hoşça kalın!")
            sys.exit()
        else:
            print("Geçersiz seçim. Lütfen 1 ile 4 arasında bir sayı girin.")

if __name__ == '__main__':
    main()
