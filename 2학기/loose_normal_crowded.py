while True:

    in0 = input("탑승객 수는?(-1:끝)")
    if in0=="-1":
        break
    in0 = int(in0)
    out = int(input("하차객 수는?"))

    sum += in0-out

print("버스에 있는 사람수는", sum)

if 0 < sum <10:
    print("여유")
elif 10 <= sum <20:
    print("보통")
else:
    print("혼잡")