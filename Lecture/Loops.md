> Vòng lặp for trong Python <

# 1. Cú pháp:

    - Vòng lặp for trong Python sử dụng điều kiện lặp lại là việc xét các phần tử trong một tập hợp các phần tử.

        -> Cú pháp:

            for i in collection:
                <Đoạn mã lặp>

        => Trong đó:

            . i: là biến nhận giá trị của các phần tử bên trong của tập hợp trong mỗi lần lặp.

> Vòng lặp thực thi việc lặp qua tất cả các phần tử của tập hợp collection cho đến khi chúng ta duyệt hết phần tử cuôi cùng trong tập hợp.

> Phần thân của vòng lặp for được phân tách khởi phần còn lại của đoạn mã bằng thụt đầu dòng (indentation) tương tự như khối if...else.

> Mỗi câu lệnh for đánh dấu bắt đầu bằng một khối mới và tất cả các đoạn mã muốn thực hiện lặp đi lặp lại cần đặt trong khối này (thụt dòng).

        -> VD1:

            sinh_vien = ["Sinh viên a", "Sinh viên b", "Sinh viên c"]
            for sv in sinh_vien:
                print(sv)

> Trong vd trên, biến lặp sv lặp qua tất cả các phần tử của tập hợp sinh_vien. Mỗi phần tử thuộc tập này tương ứng với một vòng lặp, và tại mỗi vòng lặp thì chương trình sẽ lặp đi lặp lại đoạn mã print(sv).

> Ở đây lưu ý rằng tại mỗi vòng lặp thì giá trị đang xét của sv là một phần tử khác nhau của tập sinh_vien. Do đó, kết quả in cũng sẽ có giá trị tương ứng của các phần tử này.

# Note:

    - Từ "tập hợp" ở đây chính là collection: tức là các tập nói chung chứa nhiều phần tử (chúng có thể là kiểu tập hợp set, danh sách list, kiểu dict, v.v hoặc cũng có thể là một chuỗi ký tự gồm nhiều ký tự khác nhau).

---

# 2. Lặp qua các giá trị số nguyên với hàm range():

    - Python hỗ trợ việc tạo ra một dãy số bằng cách sử dụng hàm range(). Nó cho phép chúng ta tạo ra các dãy số với giá trị nằm trong khoảng nhất định.


        -> Cú pháp:

            range(start, stop, step_size)

            => Trong đó:

                . start: là giá trị bắt đầu của phần tử. Khi tham số này được bỏ trống nó sẽ có giá trị mặc định là 0.
                . stop: là giá trị kết thúc của phần tử. Tuy nhiên, cũng giống như phép cắt danh sách hay cắt chuôi, ta sẽ không bao hàm phần tử stop trong kết quả được sinh ra (giữ đầu bỏ cuối).
                . step_size: mặc định là 1 nếu không được truyền giá trị. Đây là bước nhảy hay khoảng cách giữa các giá trị liên tiếp, ví dụ nếu stepsize = 1 (mặc định) thì ta sẽ có các giá trị 0,1,2,3,4, nếu stepsize = 2 thì là 0,2,4,6.


        -> VD2 :

            for x in range(4):
                print(x)

> Chú ý rằng: range(4) không phải cá giá trị 0 đén 4 mà là các giá trị từ 0 đến 3 (quy tấc: Giữ đầu bỏ cuối).

        -> VD3. Thêm tham số start vào hàm range():

            for x in range(1,4):
                print(x)

            # 1
            # 2
            # 3

        -> VD4. Khi chúng ta chỉ định step_size, các giá trị sẽ được lặp theo khoảng cách bằng khoảng giá trị:

            for x in range(2, 20, 3):
                print(x)

            # 2
            # 5
            # 8
            # 11
            # 14
            # 17

# 3. Vòng lặp for sử dụng câu lệnh else.

    - Vòng lặp for cũng có thể có một khối else tuỳ chọn. Đoạn mã trong khối else sẽ được thực thi nếu các phần tử trong chuỗi được sử dụng trong vòng lặp for không còn.

        -> VD5 :

            for i in rang(0, 5):
                print(i)
            else:
                print("Không còn phần tử")

            => Trong đó: Vòng lặp for sẽ in ra các giá trị từ 0 -> 4 cho đến khi vòng lặp kết thúc. Khi vòng lặp for kết thúc, nó thực thi đoạn mã câu lệnh else.

# 4. Vòng lặp for lồng nhau:

    - Ta có thể thực hiện vòng lặp for lồng nhau, tức là đặt một vòng lặp for bên trong một vòng lặp for khác.

        -> VD6:

            for i in range(3):
                for j in range(2):
                    print(i,j)

            # Kết quả:
                0 0
                0 1
                1 0
                1 1
                2 0
                2 1

> Tuy nhiên, việc sử dụng nhiều vòng lặp for lồng nhau sẽ có thể gây ra sự phức tạp cho chương trình. Do đó, ta có thể tranh sử dụng nhiều vòng lăp lồng nhau để giảm bớt sự phức tạp nếu không cần thiết, trừ trường hợp bắt buộc
