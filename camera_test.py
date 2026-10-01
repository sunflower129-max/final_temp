import cv2

# 카메라 연결
cap = cv2.VideoCapture(0)

print("카메라 테스트 시작!")
print("종료하려면 q 키를 누르세요")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("카메라를 찾을 수 없어요!")
        break
    
    # 화면에 보여주기
    cv2.imshow("카메라 테스트", frame)
    
    # q 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("테스트 종료!")