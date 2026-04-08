# Use an official Python runtime as a parent image
FROM python:3.11-slim

# 비루트 사용자 생성 (보안 모범 사례)
RUN useradd -m -s /bin/bash appuser

# 작업 디렉토리 설정
WORKDIR /app

# 환경 변수 설정
# PYTHONDONTWRITEBYTECODE: 파이썬이 .pyc 파일을 쓰지 않도록 설정
# PYTHONUNBUFFERED: 파이썬 출력이 버퍼링되지 않고 즉시 터미널에 출력되도록 설정
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 의존성 파일만 먼저 복사 (의존성이 변경될 때만 캐시를 무효화하여 빌드 속도 향상)
COPY requirements.txt .

# 시스템 패키지 업데이트, 필요한 빌드 도구 설치, 파이썬 라이브러리 설치, 불필요한 파일 삭제를 한 번에 진행하여 이미지 크기 최소화
RUN apt-get update && apt-get install -y --no-install-recommends gcc \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove gcc \
    && rm -rf /var/lib/apt/lists/*

# 애플리케이션 소스 코드 복사
COPY ./app ./app

# 디렉토리 권한을 비루트 사용자로 변경
RUN chown -R appuser:appuser /app

# 비루트 사용자로 전환
USER appuser

# 컨테이너가 8000번 포트를 수신할 것임을 명시
EXPOSE 8000

# 애플리케이션 실행 명령
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
