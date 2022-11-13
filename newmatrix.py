test_matrix= [[0,4,-3,1],[1,1,2,9],[-3,6,-6,0],[3,-2,3,1]]
def func3(var,list1,list2):
    newlist2=[float("%.3f"%((var*list1[i1])+list2[i1])) for i1 in range(len(list1))]
    """
    ''func3()'' 는 기본행 연산 3개 중 한 행에 상수배를 하여 다른행에 더해주는 역할을 하는 함수이다.
    'list2': 변하는 행
    'list1': 기본행 연산에 사용되는 행
    알고리즘 : 'list1'에 상수배(var)를 하여 'list2'에 더해줌
    """
    return newlist2
def func2(var,list1):
    newlist1=[float("%.3f"%(var*list1[i])) for i in range(len(list1))]
    """
    ''func2()'' 는 기본행 연산 3개 중 한 행에 상수배를 하는 함수이다.
    'list1': 변하는 행
    알고리즘 : 'list1'에 상수배(var)를 함.
    """
    return newlist1
def front(two_di_list):
    front_matrix=two_di_list.copy()
    row_num=[]
    used_row=[]
    for col in range (len(front_matrix[0])):
        for row in range(len(front_matrix)):
            if row in used_row:
                continue
            else:
                if front_matrix[row][col]==0:
                    continue
                else:
                    row_num.append(row)
        if len(row_num) <=1:    
            row_num.clear()
            continue
        else:
            used_row.append(row_num[0])
            row_num.pop(0)
            for i in range(len(row_num)):
                front_matrix[row_num[i]]= func3(-1*(front_matrix[row_num[i]][col])/(front_matrix[used_row[col]][col]),front_matrix[used_row[col]],front_matrix[row_num[i]])
            row_num.clear()
    """
    ''front()'' 는 전방소거법을 실행하는 함수로 각 행의 0 이 아닌 처음 으로 나오는 수 아래의 수는 모두 0이 된다.
    'front_matrix' : input 값으로 받은 'two_di_list'를 copy 하여 최종적으로 전방소거법을 실행 한 후 output으로 나오는 함수
    'row_num' : 각 열에서 0으로 이루어지지 않은 요소가 있는 행의 행을 저장함.
    'used_row' : 'row_num' 에서 저장된 행들 중 전방 소거법을 시행하는데 이미 사용된 행을 저장하는 리스트
    알고리즘: 하나의 열을 정하여 행을 순차적으로 검사한다. 여기서 검사란 정해진 열에서의 행들의 요소가 0 이 아닐 시, 'row_num' 에 저장한다.
              만약 저장된 행의 숫자 중 가장 앞에 있는 행은 전방소거법을 시행하는데 사용된다. 한마디로 다른 행을 변환하는데 'func3()' 를 사용한다.
              이렇게 사용된 행은 'used_row'로 저장되고 다음 전방 소거법을 시행하는데의 'row_num' 에 사용되지 않는다. 또한, row_num에서 사용된 행의 수는
              다음 열로 넘어 갈 때 지워진다.
    """
    return front_matrix
def refm(fronted_two_di_list):
    num=0
    el_row_and_col=[]
    refm_list=fronted_two_di_list.copy()
    for el_row in range(len(fronted_two_di_list)):
        for el_col in range (len(fronted_two_di_list[0])):
            if fronted_two_di_list[el_row][el_col] == 0:
                continue
            else: 
                el_row_and_col.append([el_row,el_col])
                break
        else:
            el_row_and_col.append([el_row,'0 matrix'])
    
    zero_el_row_and_col=[el_row_and_col[i] for i in range(len(el_row_and_col)) if '0 matrix' in el_row_and_col[i]]
    nonzero_el_row_and_col=[el_row_and_col[i] for i in range(len(el_row_and_col)) if '0 matrix' not in el_row_and_col[i]]
    while True:
        if num == len(nonzero_el_row_and_col)-1:
            break
        else:
            num=0
            for i in range(1,len(nonzero_el_row_and_col)):        
                if nonzero_el_row_and_col[i-1][1] > nonzero_el_row_and_col[i][1]:
                    temp_save_list1=nonzero_el_row_and_col[i-1]
                    temp_save_list2=nonzero_el_row_and_col[i]
                    nonzero_el_row_and_col[i]=temp_save_list1
                    nonzero_el_row_and_col[i-1]= temp_save_list2
                else:
                    num= num+1
                    continue
    sorted_el_row_and_col= nonzero_el_row_and_col + zero_el_row_and_col
    for i in range(len(el_row_and_col)):
        refm_list[i]= fronted_two_di_list[sorted_el_row_and_col[i][0]]
    """
    ''refm'' 은 (계단행렬형) 행다사디꼴 행렬형으로 변환하는 함수 이다. 한 마디로 0으로만 이루어진 행은 가장 아래에 있어야 하고,
    각행에 저음 나타나는 수는 위의 행의 처음 나타나는 수의 오른쪽에 위치해야 한다.
    'el_row_and_col' : 각 행에 처음으로 나오는 0이 아닌 수의 열과 행을 저장하는 리스트이다. 
    'refm_list' : 전방소거법을 시행한 행렬을 input 받아 복사하고 output으로 행사다리꼴 행렬을 반환한다.
    알고리즘: 'el_row_and_col'에 각 행에 처음으로 나오는 0이 아닌 수의 열과 행을 저장한다. 0 으로만 이루어진 행은 행만 숫자로 저장하고 열은 '0 matrix'로 저장한다.
              'zero_el_row_and_col' 에 'el_row_and_col' 에 속하는 리스트 중 0 으로만 이루어진 행의 행과 열의 숫자를 저장함. 반대로 nonzero_el_row_and_col에는
              'el_row_and_col' 에 속하는 리스트 중 0 으로만 이루어지지 않은 행의 행과 열의 숫자를 저장함.
              
                          
    """
    
    return refm_list

def reef(refm_list):
    el_row_and_col=[]
    pre_reef_list= refm_list.copy()
    for i in range(len(refm_list)):
        for j in range(len(refm_list[0])):
            if refm_list[i][j] == 0 :
                continue
            else :
                pre_reef_list[i] = func2((1/refm_list[i][j]),refm_list[i])
                break    
    for row in range(len(pre_reef_list)):
        for col in range(len(pre_reef_list[0])):
            if pre_reef_list[row][col]== 1:
                el_row_and_col.append([row,col])
                break
            else:
                continue
    post_reef_list= pre_reef_list.copy()
    print(el_row_and_col)
    for i in range(len(el_row_and_col)):
        print('i: %1d'%i)
        for j in range(el_row_and_col[i][0]):
            print('j: %1d'%j)
            post_reef_list[j] = func3((-1*(post_reef_list[j][el_row_and_col[i][1]])),post_reef_list[el_row_and_col[i][0]],post_reef_list[j])
        print(post_reef_list)
    return post_reef_list
print(reef(refm(front(test_matrix))))





