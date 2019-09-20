I=[1,2,3]
try:
    print(1[2])
    print(1[3])    #IndexError
except IndexError:
    print("리스트에 요송[ 접근하지 못댂습니다.")