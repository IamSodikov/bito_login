Feature: Login funksiyasi

  Scenario: Foydalanuvchi to‘g‘ri login ma’lumotlari bilan tizimga kiradi
    Given Foydalanuvchi login sahifasida
    When U to‘g‘ri email va parolni kiritadi
    And U "Kirish" tugmasini bosadi
    Then U bosh sahifaga muvaffaqiyatli yo‘naltiriladi
