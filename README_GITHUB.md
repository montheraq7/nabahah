# 🛡️ نباهة - Nabahah
## نظام نقاط المخاطر للهوية الرقمية

[![Status](https://img.shields.io/badge/status-ready-success)]()
[![Python](https://img.shields.io/badge/python-3.11-blue)]()
[![Flask](https://img.shields.io/badge/flask-3.0-green)]()

نظام متكامل لحساب مؤشر المخاطر للهوية الرقمية باستخدام Machine Learning

---

## 🚀 Demo

[🌐 جرّب التطبيق مباشرة](https://your-app.up.railway.app)

---

## ✨ الميزات

- 🤖 Machine Learning Model (Decision Tree)
- 📊 حساب مؤشر المخاطر (0-100)
- 🎨 واجهة عربية احترافية
- ⚡ استجابة فورية
- 🔄 نظام احتياطي

---

## 📸 Screenshots

![Screenshot](screenshot.png)

---

## 🏗️ التقنيات المستخدمة

- **Backend**: Flask + scikit-learn
- **Frontend**: HTML/CSS/JavaScript
- **ML Model**: Decision Tree Regressor
- **Deployment**: Railway.app

---

## 🚀 التشغيل المحلي

```bash
# 1. استنساخ المشروع
git clone https://github.com/YOUR_USERNAME/nabahah.git
cd nabahah

# 2. تثبيت المكتبات
pip install -r requirements.txt

# 3. تشغيل السيرفر
python risk_api.py

# 4. فتح الموقع
افتح index.html في المتصفح
```

---

## 📡 API Usage

```bash
# Health Check
curl https://your-app.up.railway.app/api/health

# Calculate Risk Score
curl -X POST https://your-app.up.railway.app/api/calculate-risk \
  -H "Content-Type: application/json" \
  -d '{
    "device_type": 1,
    "location_match": 0,
    "time_anomaly": 0,
    "transaction_sensitivity": 1,
    "recent_failed_attempts": 2
  }'
```

**Response:**
```json
{
  "success": true,
  "risk_score": 45,
  "level": "medium",
  "level_ar": "متوسط",
  "recommendation": "يتطلب تحقق إضافي",
  "action": "verify"
}
```

---

## 📊 معايير التقييم

| المعيار | القيم | التأثير |
|---------|-------|---------|
| نوع الجهاز | معروف (1) / غير معروف (0) | عالي |
| تطابق الموقع | مطابق (1) / غير مطابق (0) | عالي |
| شذوذ الوقت | عادي (0) / غير عادي (1) | متوسط |
| حساسية المعاملة | منخفضة (0-2) | عالي |
| المحاولات الفاشلة | 0-10 | متوسط |

---

## 📈 مستويات المخاطر

- 🟢 **منخفض (0-39)**: تنفيذ مباشر
- 🟡 **متوسط (40-74)**: تحقق إضافي (OTP)
- 🔴 **مرتفع (75-100)**: إيقاف ومراجعة

---

## 📂 هيكل المشروع

```
nabahah/
├── risk_api.py              # Backend API
├── nabahah_integrated.html  # Frontend
├── index.html               # الصفحة الرئيسية
├── requirements.txt         # المكتبات
├── Procfile                 # Railway config
└── runtime.txt              # Python version
```

---

## 🌐 النشر على Railway

1. Fork المشروع
2. اذهب إلى [Railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. اختر المشروع
5. Generate Domain

**Done!** 🎉

---

## 📚 الوثائق

- [دليل النشر الكامل](DEPLOYMENT_GUIDE.md)
- [ملخص المشروع](PROJECT_SUMMARY.md)
- [دليل البدء السريع](quick_start_guide_AR.md)

---

## 🎓 المشروع

تم تطوير هذا المشروع لهاكاتون أبشر طويق 2024

---

## 📄 الترخيص

MIT License

---

## 👥 الفريق

- [اسم الفريق]
- [أعضاء الفريق]

---

## 🙏 شكر وتقدير

شكراً لأكاديمية طويق ومنصة أبشر على الفرصة

---

<div align="center">

**🎉 جرّب التطبيق الآن!**

[🌐 Live Demo](https://your-app.up.railway.app) • [📖 الوثائق](DEPLOYMENT_GUIDE.md) • [🐛 Report Bug](issues)

Made with ❤️ for Tuwaiq Absher Hackathon 2024

</div>
