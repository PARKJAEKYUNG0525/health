import calendar
import json

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

    # 로그인
    def login(self, name, pw):
        print("\n" + "="*50)
        if name in self.users and self.users[name]["pw"] == pw:
            print(f"              ✅ {name}님 로그인 성공!")
            return True
        else:
            print("❌ 로그인 실패")
            print("="*40)
            return False

    # C - 회원 추가
    def create_user(self):
        print("\n[ 회원 추가 ]")
        name = input("➤ 추가할 회원 이름: ")
        pw = input("➤ 비밀번호: ")

        if name in self.users:
            print("⚠ 이미 존재하는 회원입니다.") 
        else:
            self.users[name] = {"pw": pw, "locker": None, "review": [], "diary": []}
            print("✅ 회원 추가 완료")

    # R - 회원 조회
    def read_users(self):
        print("\n[ 회원 목록 ]")
        print("-"*40)
        for name, info in self.users.items():
            locker = info["locker"] if info["locker"] is not None else "X"
            print(f"👤 {name} | 라커룸 : {locker}")
        print("-"*40)

    # U - 회원 수정
    def update_user(self):
        print("\n[ 회원 수정 ]")
        name = input("➤ 수정할 회원 이름: ")
        if name in self.users:
            new_pw = input("➤ 새 비밀번호: ")
            self.users[name]["pw"] = new_pw
            print("✅ 비밀번호 변경 완료")
        else:
            print("❌ 존재하지 않는 회원")

    # D - 회원 삭제
    def delete_user(self):
        print("\n[ 회원 삭제 ]")
        name = input("➤ 삭제할 회원 이름: ")
        if name in self.users and name != "admin":
            del self.users[name]
            print("✅ 회원 삭제 완료")
        else:
            print("❌ 삭제할 수 없습니다.")

    # 라커룸 선택
    def select_locker(self):
        print("\n[ 라커룸 선택 ]")
        name = input("➤ 회원 이름: ")
        if name not in self.users:
            print("❌ 존재하지 않는 회원")
            return
        locker = input("➤ 라커룸 번호: ")
        for user, info in self.users.items():
            if info["locker"] == locker:
                print(f"❌ {locker}번 라커는 이미 {user}님이 사용 중입니다.")
                return
        self.users[name]["locker"] = locker
        print("✅ 라커룸 배정 완료")

    # 라커룸 변경
    def change_locker(self):
        print("\n[ 라커룸 변경 ]")
        name = input("➤ 회원 이름: ")

        # 회원 존재 + 현재 라커 있음 확인
        if name not in self.users or self.users[name]["locker"] is None:
            print("❌ 변경할 라커룸이 없습니다.")
            return

        new_locker = input("➤ 새 라커룸 번호: ")

        # 🔥 이미 사용중인지 검사
        for user, info in self.users.items():
            if info["locker"] == new_locker:
                print(f"❌ {new_locker}번 라커는 이미 {user}님이 사용 중입니다.")
                return

        self.users[name]["locker"] = new_locker
        print("✅ 라커룸 변경 완료")

    # 라커룸 취소
    def cancel_locker(self):
        print("\n[ 라커룸 취소 ]")
        name = input("➤ 회원 이름: ")
        if name in self.users and self.users[name]["locker"] is not None:
            self.users[name]["locker"] = None
            print("✅ 라커룸 취소 완료")
        else:
            print("❌ 취소할 라커룸이 없습니다.")

    # 리뷰 조회
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
        
        if not has_review:
            print("현재 등록된 바라는 점이 없습니다.")
        print("="*40)

    # 월별 통계
    def monthly_attendance(self, name, year_month):
        try:
            year, month = map(int, year_month.split("."))

            # (그 달의 시작 요일 [0], 그 달의 총 일수[1])
            total_days = calendar.monthrange(year, month)[1]

            count = 0
            for record in self.users[name]["diary"]:
                if record["date"][:7] == year_month:
                    count += 1

            percent = (count / total_days) * 100

            print(f"\n📊 {name}님 출석 통계")
            print(f"{year_month} 출석 횟수 : {count}번")
            print(f"총 일수 : {total_days}일")
            print(f"출석률 : {percent:.2f}%")

        except:
            print("❌ 형식 오류 (YYYY.MM 로 입력하세요)")
    
    def txt_print(self):
        filename = "gym_members.txt" #경로 설정

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("🏋️ 헬스장 회원 정보\n")
                f.write("="*50 + "\n")

                for name, info in self.users.items():
                    locker = info["locker"] if info["locker"] else "없음"

                    f.write(f"이름 : {name}\n")
                    f.write(f"라커룸 : {locker}\n")
                    f.write(f"리뷰 개수 : {len(info['review'])}\n")
                    f.write(f"운동 기록 수 : {len(info['diary'])}\n")
                    f.write("-"*50 + "\n")

            print("✅ C 드라이브에 gym_members.txt 저장 완료!")

        except Exception as e:
            print("❌ 파일 저장 중 오류:", e)
    
    def user_save(self):
        filename = "users.json"

        try:
            with open(filename, "w", encoding='UTF-8') as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
                return True
        except Exception as e:
            print("❌ 파일 저장 중 오류:", e)
            return False

    def user_load(self):
        filename = "users.json"

        try:
            with open(filename, "r", encoding='UTF-8') as f:
                return json.load(f)
        except Exception as e:
            return None

    def write_diary(self,name):
        date = input("날짜 입력 (YYYY.MM.DD) ➤ ")
        content = input("운동 내용 작성 ➤ ")

        manager.users[name]["diary"].append({
                "date": date,
                "content": content
        })

        print("✅ 운동일지 저장 완료")
    
    def write_review(self,name):
        review = input("리뷰 작성 ➤ ")
        manager.users[name]["review"].append(review)
        print("리뷰작성완료") # 요구사항 반영
    
    def lookup_review(self,name):
        ym = input("조회할 연월 입력 (YYYY.MM) ➤ ")
        manager.monthly_attendance(name, ym)
        
# ================= 실행부 =================

manager = GymManager()

print("="*40)
print("🏋️  헬스장 회원 관리 시스템  🏋️")
print("="*40)
while True:
    print("(종료시 exit 입력)")
    name = input("이름 입력: ")

    if name == "exit":
        if manager.user_save():
            print("💾 데이터 저장 완료")
        else:
            print("⛔ 데이터 저장 실패")
        print("👋 프로그램 완전 종료")
        break
    pw = input("비밀번호 입력: ")

    if manager.login(name, pw):

        # 관리자 메뉴
        if name == "admin":
            while True:
                print("\n" + "="*50)
                print("                 🔧 관리자 메뉴")
                print("="*50)
                print("1️⃣  회원 추가  |  5️⃣  라커룸 선택  |  8️⃣  리뷰 조회")
                print("2️⃣  회원 조회  |  6️⃣  라커룸 변경  |  9️⃣  TXT 출력")
                print("3️⃣  회원 수정  |  7️⃣  라커룸 취소  |  0️⃣  로그 아웃")
                print("="*50)

                choice = input("번호 선택 ➤ ")

                if choice == "1":
                    manager.create_user()
                elif choice == "2":
                    manager.read_users()
                elif choice == "3":
                    manager.update_user()
                elif choice == "4":
                    manager.delete_user()
                elif choice == "5":
                    manager.select_locker()
                elif choice == "6":
                    manager.change_locker()
                elif choice == "7":
                    manager.cancel_locker()
                elif choice == "8":
                    manager.read_reviews()
                elif choice == "9":
                    manager.txt_print()
                elif choice == "0":
                    print("👋 프로그램 종료")
                    break
                else:
                    print("⚠ 잘못된 선택입니다.")

        # 일반 사용자 메뉴
        else:
            while True:
                print("\n" + "="*50)
                print(f"                🙋 {name}님 메뉴")
                print("="*50)
                print("                 1️⃣  운동일지 작성")
                print("                 2️⃣  리뷰 작성")
                print("                 3️⃣  월별 출석 통계")
                print("                 0️⃣  로그아웃")
                print("="*50)

                choice = input("번호 선택 ➤ ")

                if choice == "1":
                    manager.write_diary(name)

                elif choice == "2":
                    manager.write_review(name)

                elif choice == "3":
                    manager.lookup_review(name)

                elif choice == "0":
                    print("👋 로그아웃")
                    break

                else:
                    print("⚠ 잘못된 선택입니다.") 
