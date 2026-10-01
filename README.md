# 💊 의약품 인식 AI 프로젝트

## 📋 프로젝트 개요
카메라(또는 이미지)로 의약품을 인식하고
AI가 약품 정보를 분석해주는 로컬 실행 프로그램

---

## ✅ 요구사항
- 로컬 환경에서 실행 (인터넷 불필요)
- 카메라 또는 이미지 파일 입력
- 실시간 화면 표시
- 완전 무료

---

## 🛠️ 기술 스택
| 역할 | 라이브러리 |
|------|-----------|
| 화면 UI | Tkinter |
| 카메라/이미지 처리 | OpenCV |
| 글자 인식 (OCR) | EasyOCR |
| AI 분석 | Ollama (llama3.2) |
| 이미지 처리 보조 | Pillow, NumPy |

---

## 💻 개발 환경
- OS: Windows
- Python: 설치 완료
- VS Code: 설치 완료

---

## 📦 설치 완료 목록

### Python 라이브러리
```bash
pip install opencv-python
pip install easyocr
pip install pillow
pip install numpy
pip install requests
```

### Ollama 설치
```bash
# Ollama 공식 사이트에서 설치
# https://ollama.ai

# llama3.2 모델 다운로드
ollama pull llama3.2
```

---

## 📁 프로젝트 구조
```
의약품AI/
│
├── README.md          # 프로젝트 설명서
├── camera_test.py     # 카메라 테스트 코드
├── main.py            # 메인 실행 파일 (예정)
├── ocr_module.py      # OCR 모듈 (예정)
├── ai_module.py       # AI 분석 모듈 (예정)
└── medicine.jpg       # 테스트용 이미지 (예정)
```

---

## 🚀 실행 방법
```bash
# 카메라 테스트
python camera_test.py

# 메인 프로그램 실행 (개발 예정)
python main.py
```

---

## ⚠️ 현재 이슈 및 해결방법
| 이슈 | 원인 | 해결방법 |
|------|------|---------|
| 카메라 인식 불가 | 내장 카메라 없음 | 이미지 파일로 대체 개발 후 카메라 연결 시 코드 1줄 수정 |

---

## 📅 개발 진행 현황
- [x] 요구사항 확정
- [x] 기술스택 선정
- [x] Python 설치
- [x] 라이브러리 설치
- [x] Ollama 설치
- [x] llama3.2 모델 다운로드
- [x] 카메라 테스트 코드 작성
- [ ] OCR 모듈 개발
- [ ] AI 분석 모듈 개발
- [ ] UI 개발
- [ ] 카메라 연동
- [ ] 최종 테스트

---

## 👨‍💻 개발자 메모
- 카메라 없이 이미지 파일로 먼저 개발
- 추후 외장 카메라 연결 시 VideoCapture(0) → 번호 변경만 하면 됨
- Ollama는 로컬에서 실행되므로 인터넷 불필요
