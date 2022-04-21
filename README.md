# API
B1: Tạo db bằng file sql 

B2: Nhập lại localhost, username, password ở file database

B3: Chạy file main

Task OOP_1:
- http://127.0.0.1:8686/account chạy trên post man phương thức thức GET
- http://127.0.0.1:8686/add_acc chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ name: String, not empty, dộ dài từ 1-45 ký tự
+ amount: float, not empty, min:1
+ number: String, not empty, dãy số có 3 ký tự

- http://127.0.0.1:8686/deposit chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ money: float, not empty, min:1
+ number: String, not empty, dãy số có 3 ký tự

- http://127.0.0.1:8686/withdrawal chạy trên post man phương thức thức POST nhập vào  kiểu dữ liệu input JSON:
+ money: float, not empty, min:1
+ number: String, not empty, dãy số có 3 ký tự


Task OOP_2:
- http://127.0.0.1:1111/show_cus, http://127.0.0.1:1111/show_pro chạy trên postman phương thức GET

- http://127.0.0.1:1111/add_cus chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ name: String, not empty, độ dài từ 1-45 ký tự
+ phone: String, not mepty, độ dài từ 10-11 ký tự

- http://127.0.0.1:1111/add_pro chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ name, brand_name, category: String, not empty, độ dài từ 1-45 ký tự
+ price: Float, not empty, min: 1

- http://127.0.0.1:1111/add_bill chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ cus_id: Integer, not empty

- http://127.0.0.1:1111/sell chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ pro_id, cus_id: Integer, not empty
+ count: integer, not empty, min: 1


Task OOP_4:
- http://127.0.0.1:1010/show_saving_acc, http://127.0.0.1:1010/show_current_acc chạy trên postman phương thức GET
- http://127.0.0.1:1010/add_acc chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ acc_number: String, not empty, dãy số có 3 ký tự
+ amount: Float, not empty, min: 1
+ category: String, not empty, gồm 2 trường hợp: "tktk"/"tkvl"
+ cus_id: Integer, not empty
+ link: Integer, can empty

- http://127.0.0.1:1010/add_cus chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ name: String, not empty, độ dài từ 1-45 ký tự


- http://127.0.0.1:1010/deposit, http://127.0.0.1:1010/withdrawal chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ acc_number: String, not empty, dãy số có 3 ký tự 
+ money: Float not empty, min: 1

- http://127.0.0.1:1010/update_link chạy trên post man phương thức thức POST nhập vào kiểu dữ liệu input JSON:
+ sa_acc_number, ca_acc_number: String, not empty, dãy số có 3 ký tự
+ link: int

