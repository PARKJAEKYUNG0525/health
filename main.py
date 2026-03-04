from gym_manager_main import GymManager

# ================= 실행부 =================
if __name__=="__main__":
    manager = GymManager()

    print("="*40)
    print("🏋️  헬스장 회원 관리 시스템  🏋️")
    print("="*40)
    while True:
        print("(종료시 exit 입력)")
        name = input("이름 입력: ")

        if name == "exit":
            if manager.save_user_data():
                print("💾 데이터 저장 완료")
            else:
                print("❌ 데이터 저장 실패")
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
                    print("3️⃣  회원 수정  |  7️⃣  라커룸 취소  |  0️⃣  로그아웃")
                    print("4️⃣  회원 삭제  | ")
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
                        print("👋 로그아웃")
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

                        