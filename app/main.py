from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import io
from PIL import Image

# 하위 모듈에서 모델 불러오기
from .models.classifier import predict_spam, load_model

app = FastAPI(
    title="스팸 이미지 분류기 API",
    description="가벼운 이미지 모델을 활용하여 스팸 메시지(이미지)를 분류하는 MLOps 평가용 API입니다.",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    # 서버가 시작될 때 모델을 메모리에 로드합니다.
    load_model()

@app.get("/")
def read_root():
    return {"message": "Spam Image Classifier API에 오신 것을 환영합니다! POST /predict/ 엔드포인트를 사용하세요."}

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    # 파일 확장자/타입 검증
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="업로드한 파일이 이미지가 아닙니다.")
    
    try:
        # 파일 내용을 바이트로 읽기
        contents = await file.read()
        # PIL을 통해 이미지 객체로 변환 (RGB 형태로 보정)
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        
        # 모델을 이용한 예측 수행
        is_spam, confidence = predict_spam(image)
        
        return {
            "filename": file.filename,
            "is_spam": is_spam,
            "confidence": confidence,
            "message": "스팸입니다!" if is_spam else "정상 메시지입니다."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"이미지 처리 중 오류 발생: {str(e)}")
