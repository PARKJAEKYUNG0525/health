class GymManager:

    def __init__(self):
        self.users = {
            "admin": {"pw": "abc", "locker": None, "review": []},
            "홍길동": {"pw": "a", "locker": None, "review": []},
            "김철수": {"pw": "b", "locker": None, "review": []},
            "춘향이": {"pw": "c", "locker": None, "review": []}
        }

    # 로그인
    def login(self, name, pw):
        print("\n" + "="*40)
        if name in self.users and self.users[name]["pw"] == pw:
            print(f"✅ {name}님 로그인 성공!")
            print("="*40)
            return True
        else:
            print("❌ 로그인 실패")
            print("="*40)
            return False

    # 🔹 라커룸 사용 여부 확인 (중복 체크)
    def is_locker_used(self, locker):
        for user in self.users.values():
            if user["locker"] == locker:
                return True
        return False

    # C - 회원 추가
    def create_user(self):
        print("\n[ 회원 추가 ]")
        name = input("➤ 추가할 회원 이름: ")
        pw = input("➤ 비밀번호: ")

        if name in self.users:
            print("⚠ 이미 존재하는 회원입니다.")
        else:
            self.users[name] = {"pw": pw, "locker": None, "review": []}
            print("✅ 회원 추가 완료")

    # R - 회원 조회
    def read_users(self):
        print("\n[ 회원 목록 ]")
        print("-"*30)
        for name in self.users:
            print(f"👤 {name}")
        print("-"*30)

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

    # 라커룸 선택 (중복 체크)
    def select_locker(self):
        print("\n[ 라커룸 선택 ]")
        name = input("➤ 회원 이름: ")

        if name not in self.users:
            print("❌ 존재하지 않는 회원")
            return

        locker = input("➤ 라커룸 번호: ")

        if self.is_locker_used(locker):
            print("❌ 이미 사용 중인 라커룸입니다.")
        else:
            self.users[name]["locker"] = locker
            print("✅ 라커룸 배정 완료")

    # 라커룸 변경 (중복 체크)
    def change_locker(self):
        print("\n[ 라커룸 변경 ]")
        name = input("➤ 회원 이름: ")

        if name not in self.users or self.users[name]["locker"] is None:
            print("❌ 변경할 라커룸이 없습니다.")
            return

        locker = input("➤ 새 라커룸 번호: ")

        if self.is_locker_used(locker):
            print("❌ 이미 사용 중인 라커룸입니다.")
        else:
            self.users[name]["locker"] = locker
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

    # 라커룸 조회
    def read_lockers(self):
        print("\n[ 라커룸 사용 현황 ]")
        print("-"*40)
        for name, info in self.users.items():
            if info["locker"]:
                print(f"👤 {name} → 라커룸 {info['locker']}")
        print("-"*40)

    # 리뷰 조회
    def read_reviews(self):
        print("\n[ 리뷰 조회 ]")
        print("-"*40)
        for name in self.users:
            if self.users[name]["review"]:
                print(f"{name} 리뷰: {self.users[name]['review']}")
        print("-"*40)


# ================= 실행부 =================

manager = GymManager()

print("="*40)
print("🏋️  헬스장 회원 관리 시스템  🏋️")
print("="*40)

name = input("이름 입력: ")
pw = input("비밀번호 입력: ")

if manager.login(name, pw):

    # 관리자 메뉴
    if name == "admin":
        while True:
            print("\n" + "="*40)
            print("🔧 관리자 메뉴")
            print("="*40)
            print("1️⃣  회원 추가")
            print("2️⃣  회원 조회")
            print("3️⃣  회원 수정")
            print("4️⃣  회원 삭제")
            print("5️⃣  라커룸 선택")
            print("6️⃣  라커룸 변경")
            print("7️⃣  라커룸 취소")
            print("8️⃣  리뷰 조회")
            print("9️⃣  라커룸 조회")
            print("0️⃣  종료")
            print("=" * 40)

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
                manager.read_lockers()
            elif choice == "0":
                print("👋 프로그램 종료")
                break
            else:
                print("⚠ 잘못된 선택입니다.")

    # 일반 사용자 메뉴
    else:
        while True:
            print("\n" + "="*40)
            print(f"🙋 {name}님 메뉴")
            print("="*40)
            print("1️⃣  운동일지 작성")
            print("2️⃣  리뷰 작성")
            print("0️⃣  종료")
            print("="*40)

            choice = input("번호 선택 ➤ ")

            if choice == "1":
                diary = input("운동 내용 작성 ➤ ")
                print("✅ 운동일지 저장 완료")

            elif choice == "2":
                review = input("리뷰 작성 ➤ ")
                manager.users[name]["review"].append(review)
                print("✅ 리뷰 저장 완료")

            elif choice == "0":
                print("👋 로그아웃")
                break
            else:
                print("⚠ 잘못된 선택입니다.")