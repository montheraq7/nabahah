from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import pickle
import os

app = Flask(__name__, static_folder='.')
CORS(app)  # للسماح بالاتصال من الموقع

# تدريب مودل بسيط بناءً على البيانات
# Features: device_type, location_match, time_anomaly, transaction_sensitivity, recent_failed_attempts
X_train = np.array([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 2, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 2, 1],
    [1, 0, 1, 2, 2],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 2, 1],
    [0, 0, 1, 2, 2],
    [0, 0, 1, 1, 3],
    [0, 0, 1, 2, 4],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 2],
    [1, 1, 1, 2, 2],
    [1, 0, 1, 2, 3],
    [0, 1, 1, 2, 3],
    [0, 0, 0, 2, 5],
    [0, 0, 1, 2, 5],
])

y_train = np.array([5, 15, 25, 20, 35, 45, 60, 30, 40, 65, 80, 75, 90, 30, 45, 55, 70, 85, 95, 100])

# تدريب المودل
model = DecisionTreeRegressor(random_state=42, max_depth=5)
model.fit(X_train, y_train)

@app.route('/api/calculate-risk', methods=['POST'])
def calculate_risk():
    """
    حساب Risk Score بناءً على البيانات المرسلة
    Expected JSON format:
    {
        "device_type": 0 or 1,  # 0=غير معروف، 1=معروف
        "location_match": 0 or 1,  # 0=موقع غير مطابق، 1=موقع مطابق
        "time_anomaly": 0 or 1,  # 0=وقت عادي، 1=وقت غير عادي
        "transaction_sensitivity": 0-2,  # 0=منخفض، 1=متوسط، 2=مرتفع
        "recent_failed_attempts": 0-5  # عدد المحاولات الفاشلة
    }
    """
    try:
        data = request.get_json()
        
        # استخراج القيم
        device_type = int(data.get('device_type', 1))
        location_match = int(data.get('location_match', 1))
        time_anomaly = int(data.get('time_anomaly', 0))
        transaction_sensitivity = int(data.get('transaction_sensitivity', 0))
        recent_failed_attempts = int(data.get('recent_failed_attempts', 0))
        
        # إنشاء feature vector
        features = np.array([[device_type, location_match, time_anomaly, 
                            transaction_sensitivity, recent_failed_attempts]])
        
        # حساب Risk Score
        risk_score = model.predict(features)[0]
        risk_score = max(0, min(100, int(round(risk_score))))  # التأكد من أن القيمة بين 0-100
        
        # تحديد المستوى والتوصية
        if risk_score <= 39:
            level = "low"
            level_ar = "منخفض"
            recommendation = "تنفيذ مباشر - لا توجد مخاطر"
            action = "allow"
        elif risk_score <= 74:
            level = "medium"
            level_ar = "متوسط"
            recommendation = "يتطلب تحقق إضافي (OTP، بصمة)"
            action = "verify"
        else:
            level = "high"
            level_ar = "مرتفع"
            recommendation = "إيقاف العملية ومراجعة أمنية"
            action = "block"
        
        response = {
            'success': True,
            'risk_score': risk_score,
            'level': level,
            'level_ar': level_ar,
            'recommendation': recommendation,
            'action': action,
            'input_data': {
                'device_type': device_type,
                'location_match': location_match,
                'time_anomaly': time_anomaly,
                'transaction_sensitivity': transaction_sensitivity,
                'recent_failed_attempts': recent_failed_attempts
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/health', methods=['GET'])
def health_check():
    """فحص حالة الـ API"""
    return jsonify({
        'status': 'healthy',
        'message': 'Risk Score API is running'
    })

@app.route('/')
def home():
    """الصفحة الرئيسية"""
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """خدمة الملفات الثابتة"""
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("🚀 Starting Nabahah Risk Score API...")
    print("📊 Model trained and ready")
    port = int(os.environ.get('PORT', 5000))
    print(f"🌐 API will be available at: http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
