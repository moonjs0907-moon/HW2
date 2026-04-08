import random
from PIL import Image

def load_model():
    """
    실제 MLOps 환경에서는 이 곳에서 MLFlow, S3 등에서 모델 가중치를 로드하거나
    ONNX, PyTorch, TensorFlow 기반의 모델을 초기화합니다.
    """
    print("Dummy Model loaded.")
    pass

def predict_spam(image: Image.Image) -> tuple[bool, float, str]:
    """
    이미지를 입력받아 스팸 여부, 모델의 확신도, 그리고 스팸 유형을 반환합니다.
    """
    # 더미 추론 로직: 랜덤하게 1차 스팸 여부 결과 반환
    is_spam = random.choice([True, False])
    confidence = round(random.uniform(0.7, 0.99), 4)
    
    # 모델 업데이트: 스팸인 경우 스팸 세부 유형(Class)을 판별하는 기능 추가
    spam_classification_categories = ["불법도박", "보이스피싱", "성인물", "주식/투자 사기", "일반 광고"]
    spam_type = random.choice(spam_classification_categories) if is_spam else "정상(유형 없음)"
    
    return is_spam, confidence, spam_type
