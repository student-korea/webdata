f= open("w0509/a1.txt","a",encoding="utf-8")
txt = "번호,제목,작성자,작성일,조회수\n"
f.write(txt)

txt = "1,이벤트신청1,홍길동,2025-04-20,1\n"
f.write(txt)
txt = "2,강의신청2,유관순,2025-04-21,2\n"
f.write(txt)

f.close()

print("프로그램 종료")