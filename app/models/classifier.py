import random
from PIL import Image

def load_model():
    """
    실제 MLOps 환경에서는 이 곳에서 MLFlow, S3 등에서 모델 가중치를 로드하거나
    ONNX, PyTorch, TensorFlow 기반의 모델을 초기화합니다.
    """
    print("Dummy Model loaded.")
    pass

def predict_spam(image: Image.Image) -> tuple[bool, float]:
    """
    이미지를 입력받아 스팸 여부와 모델의 확신도(confidence)를 반환합니다.
    (현재는 아키텍처 설계를 위한 더미 로직입니다)
    """
    # 실제 환경:
    # 1. 이미지 전처리 (예: transform(image))
    # 2. 모델 추론 (예: outputs = model(inputs))
    # 3. 결과 후처리
    
    # 더미 추론 로직: 랜덤하게 결과 반환
    is_spam = random.choice([True, False])
    confidence = round(random.uniform(0.7, 0.99), 4)
    
    return is_spam, confidence
