import calendar
import json

class GymManager:

    def __init__(self):
        """
        헬스장 회원 관리를 위한 객체.
        생성 시 저장된 사용자 데이터를 불러온다. 없으면 더미데이터로 설정한다.
        """
        user_data = self.load_user_data()
        if user_data:
            self.users = user_data
        else:
            self.users = {
                "admin": {"pw": "abc", "locker": None, "review": [], "diary": []},
                "홍길동": {"pw": "a", "locker": None, "review": [], "diary": []},
                "김철수": {"pw": "b", "locker": None, "review": [], "diary": []},
                "춘향이": {"pw": "c", "locker": None, "review": [], "diary": []}
            }

    # 로그인
    def login(self, name, pw):
        """
        로그인 유효성을 확인한다.
        
        :param name: 회원 이름
        :param pw: 회원 비밀번호
        :return: 로그인 성공 여부(True/False)
        """
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
        """
        회원 추가 UI를 출력한다. 새로운 회원의 이름과 비밀번호를 받아 회원 데이터에 추가한다.
        """
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
        """
        모든 회원의 라커룸 번호를 출력한다.
        """
        print("\n[ 회원 목록 ]")
        print("-"*40)
        for name, info in self.users.items():
            locker = info["locker"] if info["locker"] is not None else "X"
            print(f"👤 {name} | 라커룸 : {locker}")
        print("-"*40)

    # U - 회원 수정
    def update_user(self):
        """
        회원 비밀번호 수정 UI를 출력한다. 회원 이름과 새 비밀번호를 입력받아 회원 비밀번호를 변경한다.
        """
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
        """
        회원 삭제 UI를 출력한다. 회원 이름을 입력받아 회원 데이터에서 제거한다.
        """
        print("\n[ 회원 삭제 ]")
        name = input("➤ 삭제할 회원 이름: ")
        if name in self.users and name != "admin":
            del self.users[name]
            print("✅ 회원 삭제 완료")
        else:
            print("❌ 삭제할 수 없습니다.")

    # 라커룸 선택
    def select_locker(self):
        """
        라커룸 선택 UI를 출력한다. 회원 이름과 라커룸 번호를 입력받아 해당 회원 데이터에 라커룸 번호를 배정한다.
        """
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
        """
        라커룸 변경 UI를 출력한다. 회원 이름과 라커룸 번호를 입력받아 해당 회원 데이터에 새로운 라커룸 번호를 배정한다.
        """
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
        """
        라커룸 취소 UI를 출력한다. 회원 이름을 입력으로 받아 해당 회원 데이터의 라커룸 번호를 None으로 바꾼다.
        """
        print("\n[ 라커룸 취소 ]")
        name = input("➤ 회원 이름: ")
        if name in self.users and self.users[name]["locker"] is not None:
            self.users[name]["locker"] = None
            print("✅ 라커룸 취소 완료")
        else:
            print("❌ 취소할 라커룸이 없습니다.")

    # 리뷰 조회
    def read_reviews(self):
        """
        모든 회원의 바라는 점 목록을 출력한다.
        """
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
        """
        회원 이름과 연월을 받아 해당 회원의 당월 출석횟수와 출석률을 출력한다.

        :param name: 회원 이름
        :param year_month: 조회할 연월(yyyy.mm)
        """
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
        """
        현재 회원 데이터에서 회원별 요약 정보를 텍스트 파일로 저장한다.
        """
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

            print("✅ gym_members.txt 저장 완료!")

        except Exception as e:
            print("❌ 파일 저장 중 오류:", e)
    
    def save_user_data(self):
        """
        회원 데이터를 JSON 파일로 저장한다.

        :return: 파일 저장 성공 여부 (True/False)
        """
        filename = "users.json"

        try:
            with open(filename, "w", encoding='UTF-8') as f:
                json.dump(self.users, f, indent=2, ensure_ascii=False)
                return True
        except Exception as e:
            print("❌ 파일 저장 중 오류:", e)
            return False

    def load_user_data(self):
        """
        JSON 파일로부터 회원 데이터를 불러온다.

        :return: 회원 데이터(dict) / None(파일이 없을 경우)
        """
        filename = "users.json"

        try:
            with open(filename, "r", encoding='UTF-8') as f:
                return json.load(f)
        except Exception as e:
            return None

        # 1 운동일지 작성
    def write_diary(self,name):
        """
        회원 이름을 받고 운동일지 작성 UI를 출력한다. 운동 날짜, 운동 내용을 입력받아 해당 회원 데이터의 운동 일지 목록에 딕셔너리로 추가한다.

        :param name: 운동일지를 작성할 회원 이름
        """
        date = input("날짜 입력 (YYYY.MM.DD) ➤ ")
        content = input("운동 내용 작성 ➤ ")

        self.users[name]["diary"].append({
                "date": date,
                "content": content
        })

        print("✅ 운동일지 저장 완료")
    
        # 2 리뷰작성
    def write_review(self,name):
        """
        회원 이름을 받고 리뷰 작성 UI를 출력한다. 리뷰 내용을 입력받아 해당 회원 데이터의 리뷰 목록에 추가한다.
        """
        review = input("리뷰 작성 ➤ ")
        self.users[name]["review"].append(review)
        print("리뷰작성완료") # 요구사항 반영
    
        #3 조회
    def lookup_review(self,name):
        """
        회원 이름을 입력받아 출석 통계 UI를 출력한다. 조회할 연월을 입력받아 해당 월의 출석 통계를 출력한다.
        """
        ym = input("조회할 연월 입력 (YYYY.MM) ➤ ")
        self.monthly_attendance(name, ym)