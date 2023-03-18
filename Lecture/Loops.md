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
