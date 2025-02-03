from app import app, db, Question
import random

# Flask uygulama bağlamını başlat
with app.app_context():
    # Veritabanını oluştur
    db.drop_all()

    db.create_all()

    # Örnek sorular ve seçenekler
    questions = [
        {
            "question": "Python'da AI geliştirme ile ilgili doğru seçeneği belirleyin:",
            "options": ["Derin Öğrenme", "Makine Öğrenimi", "Nöral Ağlar", "Doğal Dil İşleme"],
            "correct_option": "Makine Öğrenimi"
        },
        {
            "question": "Bilgisayar görüşü ile ilgili doğru seçeneği belirleyin:",
            "options": ["Yüz Tanıma", "Sahne Analizi", "Özellik Çıkartma", "Ses Tanıma"],
            "correct_option": "Yüz Tanıma"
        },
        {
            "question": "NLP ile ilgili doğru seçeneği belirleyin:",
            "options": ["Metin Sınıflandırma", "Görüntü Tanıma", "Ses Analizi", "Öneri Sistemleri"],
            "correct_option": "Metin Sınıflandırma"
        },
        {
            "question": "Python uygulamalarında AI modelleri ile ilgili doğru seçeneği belirleyin:",
            "options": ["İnteraktif AI", "AI Teknolojisi", "Makine Öğrenimi", "Derin Öğrenme"],
            "correct_option": "Makine Öğrenimi"
        },
        {
            "question": "Derin öğrenme ile ilgili doğru seçeneği belirleyin:",
            "options": ["Destek Vektör Makineleri", "K-En Yakın Komşu", "Konvolüsyonel Sinir Ağları", "Karar Ağaçları"],
            "correct_option": "Konvolüsyonel Sinir Ağları"
        },
        {
            "question": "Doğal dil işleme (NLP) uygulamalarında kullanılan tekniklerden biri aşağıdakilerden hangisidir?",
            "options": ["LSTM", "AdaBoost", "Kümeleme", "Anlamlı Cümleler"],
            "correct_option": "LSTM"
        },
        {
            "question": "Bilgisayar görüşü projelerinde kullanılan bir yöntem aşağıdakilerden hangisidir?",
            "options": ["Yapay Sinir Ağları", "Kümeleme", "Regresyon", "Öznitelik Seçimi"],
            "correct_option": "Yapay Sinir Ağları"
        },
        {
            "question": "Python'da veri analizi için hangi kütüphane kullanılır?",
            "options": ["NumPy", "Matplotlib", "Scikit-learn", "TensorFlow"],
            "correct_option": "NumPy"
        },
        {
            "question": "Makine öğrenimi modelinin performansını değerlendirmek için kullanılan bir metrik aşağıdakilerden hangisidir?",
            "options": ["Kayıp Fonksiyonu", "Doğruluk", "Özellik Çıkartma", "Ağır Öğrenme"],
            "correct_option": "Doğruluk"
        },
        {
            "question": "Python'da makine öğrenimi modelleri için hangi kütüphane yaygın olarak kullanılır?",
            "options": ["Scikit-learn", "Pandas", "Numpy", "Requests"],
            "correct_option": "Scikit-learn"
        }
    ]

    for q in questions:
        # Seçenekleri karıştır
        options = q["options"].copy()
        random.shuffle(options)

        # Doğru cevabın karıştırılmış seçenekler içinde hangi sırada olduğunu bulun
        correct_option = q["correct_option"]
        correct_index = options.index(correct_option)

        # Veritabanına soruları ekle
        question = Question(
            question=q["question"],
            option1=options[0],
            option2=options[1],
            option3=options[2],
            option4=options[3],
            correct_option=options[correct_index]
        )
        db.session.add(question)

    db.session.commit()
