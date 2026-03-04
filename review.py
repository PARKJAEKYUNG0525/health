import calendar
import json
from datetime import datetime  # 날짜 검증 및 출석률 계산을 위해 추가

class GymManager:
    def __init__(self):
        userData = self.user_load()
        if userData:
            self.users = userData
        else:
            self.users = {
                "admin": {"pw": "abc", "locker": None, "review": [], "diary": []},
                "홍길동": {"pw": "a", "locker": None, "review": [], "diary": []},
                "김철수": {"pw": "b", "locker": None, "review": [], "diary": []},
                "춘향이": {"pw": "c", "locker": None, "review": [], "diary": []}
            }

    # [공통] 로그인
    def login(self, name, pw):
        print("\n" + "="*50)
        if name in self.users and self.users[name]["pw"] == pw:
            print(f"               ✅ {name}님 로그인 성공!")
            return True
        else:
            print("❌ 로그인 실패")
            print("="*40)
            return False

    # [관리자] 1. 회원 추가
    def create_user(self):
        print("\n[ 회원 추가 ]")
        name = input("➤ 추가할 회원 이름: ")
        pw = input("➤ 비밀번호: ")
        if name in self.users:
            print("⚠ 이미 존재하는 회원입니다.") 
        else:
            self.users[name] = {"pw": pw, "locker": None, "review": [], "diary": []}
            print("✅ 회원 추가 완료")

    # [관리자] 2. 회원 조회 (실시간 출석률 삽입)
    def read_users(self):
        print("\n" + "="*55)
        print("               👥 전체 회원 목록 및 출석률")
        print("="*55)
        
        # 현재 시스템 날짜 기준 이번 달 정보 가져오기
        now = datetime.now()
        curr_ym = now.strftime("%Y.%m")
        _, total_days = calendar.monthrange(now.year, now.month)

        for name, info in self.users.items():
            if name == "admin": continue
            locker = info["locker"] if info["locker"] is not None else "X"
            
            # 이번 달(YYYY.MM)에 해당하는 일지 개수 계산
            count = sum(1 for d in info["diary"] if d["date"][:7] == curr_ym)
            percent = (count / total_days) * 100
            
            print(f"👤 {name:^5} | 라커: {locker:^3} | 이번 달 출석률: {percent:>6.2f}% ({count}/{total_days})")
        print("-" * 55)

    # 3. 회원 수정 / 4. 회원 삭제 (기존 유지)
    def update_user(self):
        print("\n[ 회원 수정 ]")
        name = input("➤ 수정할 회원 이름: ")
        if name in self.users:
            new_pw = input("➤ 새 비밀번호: ")
            self.users[name]["pw"] = new_pw
            print("✅ 비밀번호 변경 완료")
        else: print("❌ 존재하지 않는 회원")

    def delete_user(self):
        print("\n[ 회원 삭제 ]")
        name = input("➤ 삭제할 회원 이름: ")
        if name in self.users and name != "admin":
            del self.users[name]
            print("✅ 회원 삭제 완료")
        else: print("❌ 삭제할 수 없습니다.")

    # 5. 라커룸 선택 / 6. 라커룸 변경 / 7. 라커룸 취소 (기존 유지)
    def select_locker(self):
        print("\n[ 라커룸 선택 ]")
        name = input("➤ 회원 이름: ")
        if name not in self.users: print("❌ 존재하지 않는 회원"); return
        locker = input("➤ 라커룸 번호: ")
        for user, info in self.users.items():
            if info["locker"] == locker:
                print(f"❌ {locker}번 라커는 이미 {user}님이 사용 중입니다."); return
        self.users[name]["locker"] = locker
        print("✅ 라커룸 배정 완료")

    def change_locker(self):
        print("\n[ 라커룸 변경 ]")
        name = input("➤ 회원 이름: ")
        if name not in self.users or self.users[name]["locker"] is None:
            print("❌ 변경할 라커룸이 없습니다."); return
        new_locker = input("➤ 새 라커룸 번호: ")
        for user, info in self.users.items():
            if info["locker"] == new_locker:
                print(f"❌ {new_locker}번 라커는 이미 {user}님이 사용 중입니다."); return
        self.users[name]["locker"] = new_locker
        print("✅ 라커룸 변경 완료")

    def cancel_locker(self):
        print("\n[ 라커룸 취소 ]")
        name = input("➤ 회원 이름: ")
        if name in self.users and self.users[name]["locker"] is not None:
            self.users[name]["locker"] = None
            print("✅ 라커룸 취소 완료")
        else: print("❌ 취소할 라커룸 정보가 없습니다.")

    # 8. 리뷰 조회
    def read_reviews(self):
        print("\n" + "="*40)
        print("📋 [ 전 회원 바라는 점(리뷰) 조회 ]")
        print("-" * 40)
        has_review = False
        for name, info in self.users.items():
            if info["review"]:
                has_review = True
                print(f"👤 아이디: {name}")
                for idx, content in enumerate(info["review"], 1):
                    print(f"   {idx}. {content}")
                print("-" * 40)
        if not has_review: print("현재 등록된 바라는 점이 없습니다.")
        print("="*40)

    # 9. 월별 통계 / 10. TXT 출력 / JSON 저장 및 로드
    def monthly_attendance(self, name, year_month):
        try:
            year, month = map(int, year_month.split("."))
            total_days = calendar.monthrange(year, month)[1]
            count = sum(1 for record in self.users[name]["diary"] if record["date"][:7] == year_month)
            percent = (count / total_days) * 100
            print(f"\n📊 {name}님 출석 통계\n{year_month} 출석 : {count}번 / 출석률 : {percent:.2f}%")
        except: print("❌ 형식 오류 (YYYY.MM 로 입력하세요)")

    def txt_print(self):
        try:
            with open("gym_members.txt", "w", encoding="utf-8") as f:
                f.write("🏋️ 헬스장 회원 정보\n" + "="*50 + "\n")
                for name, info in self.users.items():
                    locker = info["locker"] if info["locker"] else "없음"
                    f.write(f"이름 : {name} | 라커 : {locker} | 리뷰: {len(info['review'])}개 | 기록: {len(info['diary'])}개\n")
            print("✅ gym_members.txt 저장 완료!")
        except Exception as e: print("❌ 파일 저장 중 오류:", e)

    def user_save(self):
        try:
            with open("users.json", "w", encoding='UTF-8') as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
            return True
        except: return False

    def user_load(self):
        try:
            with open("users.json", "r", encoding='UTF-8') as f:
                return json.load(f)
        except: return None


# ================= 실행부 =================
manager = GymManager()

print("="*40)
print("🏋️  헬스장 회원 관리 시스템  🏋️")
print("="*40)

while True:
    print("(종료시 exit 입력)")
    name = input("이름 입력: ")
    if name == "exit":
        manager.user_save()
        print("💾 데이터 저장 후 종료합니다."); break
    
    pw = input("비밀번호 입력: ")

    if manager.login(name, pw):
        # 1. 관리자 메뉴
        if name == "admin":
            while True:
                print("\n" + "="*50)
                print("                🔧 관리자 메뉴")
                print("="*50)
                print("1️⃣  회원 추가  |  5️⃣  라커룸 선택  |  8️⃣  리뷰 조회")
                print("2️⃣  회원 조회  |  6️⃣  라커룸 변경  |  9️⃣  TXT 출력")
                print("3️⃣  회원 수정  |  7️⃣  라커룸 취소  |  0️⃣  로그 아웃")
                print("="*50)
                choice = input("번호 선택 ➤ ")
                if choice == "1": manager.create_user()
                elif choice == "2": manager.read_users()
                elif choice == "3": manager.update_user()
                elif choice == "4": manager.delete_user()
                elif choice == "5": manager.select_locker()
                elif choice == "6": manager.change_locker()
                elif choice == "7": manager.cancel_locker()
                elif choice == "8": manager.read_reviews()
                elif choice == "9": manager.txt_print()
                elif choice == "0": break
        
        # 2. 일반 사용자 메뉴
        else:
            while True:
                print("\n" + "="*50)
                print(f"                🙋 {name}님 메뉴")
                print("="*50)
                print("                1️⃣  운동일지 작성")
                print("                2️⃣  리뷰 작성")
                print("                3️⃣  월별 출석 통계")
                print("                0️⃣  로그아웃")
                print("="*50)
                choice = input("번호 선택 ➤ ")

                if choice == "1":
                    # [추가] 관리자 메뉴 스타일의 UI 박스
                    print("\n" + "="*50)
                    print("                🗓️  운동일지 작성 모드")
                    print("="*50)
                    
                    date = input("➤ 날짜 입력 (YYYY.MM.DD) ➤ ")
                    
                    # [에러 체크 1] 잘못된 날짜 형식 및 존재하지 않는 날짜 검증
                    try:
                        datetime.strptime(date, "%Y.%m.%d")
                    except ValueError:
                        print("\n" + "!"*50)
                        print("❌ 에러: 날짜 형식이 틀리거나 존재하지 않는 날짜입니다.")
                        print("        (입력 예시: 2026.03.04)")
                        print("!"*50)
                        continue 
                    
                    # [에러 체크 2] 중복 날짜 검증